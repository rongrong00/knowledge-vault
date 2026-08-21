#!/usr/bin/env python3
"""
claude-session-log.py — write a Claude Code session summary into an Obsidian vault.

Wired to the SessionEnd hook. Reads the hook payload as JSON on stdin, parses the
session transcript, and writes ONE note per session into <vault>/Log/Sessions/.

Design notes
------------
* The vault is derived from this script's own location (<vault>/_bin/…), so the
  script is distributed to every machine by the same git sync that carries the notes.
  Nothing machine-specific is hard-coded.
* One file per session, with the machine name in the filename. Two machines can never
  write the same path, so git never sees a merge conflict on session notes.
* The transcript JSONL schema is NOT documented by Anthropic. Every field access here
  is defensive and falls back rather than raising. A parse failure degrades the note,
  it never breaks your session exit.
* Exits 0 unconditionally. A logging hook must never interfere with Claude Code.

Manual use:
    ./claude-session-log.py --dry-run < payload.json    # print the note, write nothing
    ./claude-session-log.py --self-test                 # run built-in checks
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SESSIONS = VAULT / "Log" / "Sessions"
CONFIG = VAULT / "_bin" / "config.json"

MAX_PROMPT_CHARS = 240
MAX_PROMPTS_SHOWN = 40
MAX_FILES_SHOWN = 40
EDIT_TOOLS = {"Edit", "Write", "NotebookEdit", "MultiEdit", "str_replace_editor"}


# --------------------------------------------------------------------------- utils

def load_config():
    """Optional per-vault config. All keys optional."""
    defaults = {
        "git_autosync": True,
        "min_prompts": 1,          # skip sessions with fewer real prompts than this (0 = log even empty ones)
        "ignore_cwd_patterns": [], # regexes; matching working dirs are never logged
        "redact_patterns": [       # applied to prompt text before it is written
            r"(?i)\b(sk-[A-Za-z0-9_\-]{16,})",
            r"(?i)\b(gh[pousr]_[A-Za-z0-9]{16,})",
            r"(?i)(api[_-]?key\s*[=:]\s*)\S+",
            r"(?i)(password\s*[=:]\s*)\S+",
            r"(?i)(token\s*[=:]\s*)\S+",
        ],
    }
    try:
        if CONFIG.exists():
            defaults.update(json.loads(CONFIG.read_text()))
    except Exception:
        pass
    return defaults


def run(cmd, cwd=None, timeout=15):
    """Run a command, return stdout or '' — never raises."""
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, check=False)
        return p.stdout.strip()
    except Exception:
        return ""


def machine_name():
    for env in ("CLAUDE_VAULT_MACHINE",):
        if os.environ.get(env):
            return slug(os.environ[env])
    override = Path.home() / ".claude-vault-machine"
    try:
        if override.exists():
            return slug(override.read_text().strip())
    except Exception:
        pass
    host = run(["hostname", "-s"]) or os.uname().nodename or "unknown"
    return slug(host.split(".")[0])


def slug(text, maxlen=48):
    text = re.sub(r"[^\w\-. ]+", "", str(text)).strip()
    text = re.sub(r"\s+", "-", text)
    return (text[:maxlen] or "unknown").strip("-.")


def redact(text, patterns):
    for pat in patterns:
        try:
            text = re.sub(pat, lambda m: (m.group(1) if m.lastindex else "") + "«redacted»", text)
        except Exception:
            continue
    return text


# ----------------------------------------------------------------- transcript parse

def iter_lines(path):
    try:
        with open(path, "r", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue
    except Exception:
        return


def blocks_of(msg):
    """Return content as a list of blocks, whatever shape it arrived in."""
    if msg is None:
        return []
    content = msg.get("content") if isinstance(msg, dict) else None
    if content is None:
        return []
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    return []


def role_of(entry):
    """Role, tolerant of top-level `type` or nested message.role."""
    msg = entry.get("message") if isinstance(entry.get("message"), dict) else None
    if msg and isinstance(msg.get("role"), str):
        return msg["role"]
    t = entry.get("type")
    return t if t in ("user", "assistant") else ""


def parse_transcript(path):
    """Extract prompts, tool usage, files touched and timestamps. Never raises."""
    out = {
        "prompts": [], "tools": {}, "files": [], "bash": [],
        "first_ts": None, "last_ts": None, "lines": 0, "models": set(),
    }
    seen_files = set()
    for entry in iter_lines(path):
        if not isinstance(entry, dict):
            continue
        out["lines"] += 1

        # Subagent and injected system messages are not the user's own turns.
        if entry.get("isSidechain") or entry.get("isMeta"):
            continue

        ts = entry.get("timestamp") or entry.get("ts")
        if isinstance(ts, str):
            out["first_ts"] = out["first_ts"] or ts
            out["last_ts"] = ts

        msg = entry.get("message") if isinstance(entry.get("message"), dict) else entry
        role = role_of(entry)
        blocks = blocks_of(msg)

        if role == "user":
            # A "user" entry carrying tool_result blocks is machine output, not a prompt.
            if any(b.get("type") == "tool_result" for b in blocks):
                continue
            text = " ".join(b.get("text", "") for b in blocks if b.get("type") == "text").strip()
            # Command wrappers like <command-name>/clear</command-name> are not prompts.
            if text and not text.startswith("<command-name>") and "<local-command-stdout>" not in text:
                out["prompts"].append(text)

        elif role == "assistant":
            if isinstance(msg.get("model"), str):
                out["models"].add(msg["model"])
            for b in blocks:
                if b.get("type") != "tool_use":
                    continue
                name = b.get("name") or "?"
                out["tools"][name] = out["tools"].get(name, 0) + 1
                inp = b.get("input") if isinstance(b.get("input"), dict) else {}
                fp = inp.get("file_path") or inp.get("notebook_path") or inp.get("path")
                if name in EDIT_TOOLS and isinstance(fp, str) and fp not in seen_files:
                    seen_files.add(fp)
                    out["files"].append(fp)
                if name == "Bash" and isinstance(inp.get("command"), str):
                    out["bash"].append(inp["command"])
    return out


# ------------------------------------------------------------------------- git info

def git_info(cwd):
    info = {"repo": "", "branch": "", "commits": [], "dirty": 0}
    if not cwd or not Path(cwd).is_dir():
        return info
    inside = run(["git", "rev-parse", "--is-inside-work-tree"], cwd=cwd)
    if inside != "true":
        return info
    remote = run(["git", "remote", "get-url", "origin"], cwd=cwd)
    info["repo"] = re.sub(r"^https://[^@]+@", "https://", remote)
    info["branch"] = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)
    since = run(["git", "log", "--since=12.hours", "--pretty=%h %s", "-n", "15"], cwd=cwd)
    info["commits"] = [l for l in since.splitlines() if l.strip()]
    status = run(["git", "status", "--porcelain"], cwd=cwd)
    info["dirty"] = len([l for l in status.splitlines() if l.strip()])
    return info


def git_sync_detached(vault):
    """Fork a fully detached child to pull/commit/push, so session exit never waits."""
    script = (
        'cd "$1" || exit 0; '
        'git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0; '
        'git add -A >/dev/null 2>&1; '
        'git diff --cached --quiet && exit 0; '
        'git commit -m "session log: $(hostname -s) $(date +%Y-%m-%dT%H:%M)" >/dev/null 2>&1; '
        'git remote get-url origin >/dev/null 2>&1 || exit 0; '
        'git pull --rebase --autostash origin "$(git rev-parse --abbrev-ref HEAD)" >/dev/null 2>&1; '
        'git push origin HEAD >/dev/null 2>&1; '
    )
    try:
        subprocess.Popen(
            ["/bin/sh", "-c", script, "sh", str(vault)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL, start_new_session=True,
        )
    except Exception:
        pass


# ------------------------------------------------------------------------ rendering

def parse_ts(ts):
    if not isinstance(ts, str):
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None


def render(payload, parsed, cfg):
    cwd = payload.get("cwd") or ""
    project = Path(cwd).name if cwd else "no-project"
    machine = machine_name()
    sid = str(payload.get("session_id") or "")
    gi = git_info(cwd)

    start = parse_ts(parsed["first_ts"])
    end = parse_ts(parsed["last_ts"]) or datetime.now(timezone.utc)
    local_end = end.astimezone()
    duration = int((end - start).total_seconds() // 60) if start else 0

    prompts = [redact(p, cfg["redact_patterns"]) for p in parsed["prompts"]]
    tools = sorted(parsed["tools"].items(), key=lambda kv: -kv[1])
    tool_line = " · ".join(f"{n} ×{c}" for n, c in tools) or "none recorded"

    stamp = local_end.strftime("%Y-%m-%d %H%M")
    fname = f"{stamp} {slug(project)} ({machine}).md"

    fm = {
        "title": f"{stamp} — {project} ({machine})",
        "type": "session",
        "machine": machine,
        "project": project,
        "cwd": cwd,
        "branch": gi["branch"],
        "repo": gi["repo"],
        "session_id": sid,
        "started": start.astimezone().isoformat(timespec="seconds") if start else "",
        "ended": local_end.isoformat(timespec="seconds"),
        "duration_min": duration,
        "prompts": len(prompts),
        "files_changed": len(parsed["files"]),
        "commits": len(gi["commits"]),
        "end_reason": payload.get("reason") or "",
    }

    L = ["---"]
    L.append(f"tags: [session, claude-code, machine/{machine}, project/{slug(project)}]")
    for k, v in fm.items():
        if isinstance(v, str):
            L.append(f'{k}: "{v}"' if (v == "" or any(c in v for c in ':#[]{}')) else f"{k}: {v}")
        else:
            L.append(f"{k}: {v}")
    L.append("---")
    L.append("")
    L.append(f"# {project} — {local_end.strftime('%Y-%m-%d %H:%M')}")
    L.append("")
    bits = [f"**{machine}**", f"`{cwd}`"]
    if gi["branch"]:
        bits.append(f"branch `{gi['branch']}`")
    bits.append(f"{duration} min" if duration else "short session")
    bits.append(f"{len(prompts)} prompts")
    L.append(" · ".join(bits))
    L.append("")

    L.append("## What I asked")
    L.append("")
    if prompts:
        shown = prompts[:MAX_PROMPTS_SHOWN]
        for p in shown:
            one = " ".join(p.split())
            if len(one) > MAX_PROMPT_CHARS:
                one = one[:MAX_PROMPT_CHARS].rstrip() + "…"
            L.append(f"- {one}")
        if len(prompts) > len(shown):
            L.append(f"- *…and {len(prompts) - len(shown)} more*")
    else:
        L.append("*No prompts recorded.*")
    L.append("")

    L.append("## Files touched")
    L.append("")
    if parsed["files"]:
        for f in parsed["files"][:MAX_FILES_SHOWN]:
            try:
                rel = os.path.relpath(f, cwd) if cwd else f
            except Exception:
                rel = f
            L.append(f"- `{rel}`")
        if len(parsed["files"]) > MAX_FILES_SHOWN:
            L.append(f"- *…and {len(parsed['files']) - MAX_FILES_SHOWN} more*")
    else:
        L.append("*No file edits recorded.*")
    L.append("")

    if gi["commits"]:
        L.append("## Commits (last 12h in this repo)")
        L.append("")
        for c in gi["commits"]:
            L.append(f"- `{c}`")
        L.append("")
    if gi["dirty"]:
        L.append(f"> [!warning] Left {gi['dirty']} uncommitted change(s) in `{project}`.")
        L.append("")

    L.append("## Tools")
    L.append("")
    L.append(tool_line)
    L.append("")
    L.append("## Notes")
    L.append("")
    L.append("<!-- Your own notes. Everything above is generated; this section is yours. -->")
    L.append("")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"[[MOC - Sessions]] · [[Home]]")
    L.append("")
    return fname, "\n".join(L)


# ----------------------------------------------------------------------------- main

def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()

    cfg = load_config()
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}

    if os.environ.get("CLAUDE_VAULT_LOG") == "0":
        return 0

    cwd = payload.get("cwd") or ""
    for pat in cfg["ignore_cwd_patterns"]:
        try:
            if re.search(pat, cwd):
                return 0
        except Exception:
            continue

    tpath = payload.get("transcript_path") or ""
    parsed = parse_transcript(tpath) if tpath else {
        "prompts": [], "tools": {}, "files": [], "bash": [],
        "first_ts": None, "last_ts": None, "lines": 0, "models": set()}

    if len(parsed["prompts"]) < cfg["min_prompts"]:
        return 0

    fname, body = render(payload, parsed, cfg)

    if "--dry-run" in args:
        sys.stdout.write(f"--- would write: Log/Sessions/{fname}\n\n{body}")
        return 0

    try:
        SESSIONS.mkdir(parents=True, exist_ok=True)
        (SESSIONS / fname).write_text(body)
    except Exception:
        return 0

    if cfg["git_autosync"]:
        git_sync_detached(VAULT)
    return 0


def self_test():
    import tempfile
    ok = True

    def check(label, cond):
        nonlocal ok
        ok = ok and bool(cond)
        print(("PASS  " if cond else "FAIL  ") + label)

    # Shape A: string content, standard nesting
    a = [
        {"type": "user", "message": {"role": "user", "content": "fix the dataloader leak"},
         "timestamp": "2026-08-21T14:02:11.000Z"},
        {"type": "assistant", "message": {"role": "assistant", "model": "claude-opus-5", "content": [
            {"type": "text", "text": "Looking."},
            {"type": "tool_use", "name": "Edit", "input": {"file_path": "/p/src/data.py"}},
            {"type": "tool_use", "name": "Bash", "input": {"command": "pytest -q"}}]},
         "timestamp": "2026-08-21T14:10:00.000Z"},
        {"type": "user", "message": {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": "x", "content": "ok"}]},
         "timestamp": "2026-08-21T14:10:05.000Z"},
        {"type": "user", "message": {"role": "user", "content": [
            {"type": "text", "text": "now add a test"}]},
         "timestamp": "2026-08-21T14:30:00.000Z"},
        {"isSidechain": True, "type": "user", "message": {"role": "user", "content": "subagent noise"}},
        {"isMeta": True, "type": "user", "message": {"role": "user", "content": "meta noise"}},
        {"type": "user", "message": {"role": "user", "content": "<command-name>/clear</command-name>"}},
    ]
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as fh:
        for e in a:
            fh.write(json.dumps(e) + "\n")
        pa = fh.name
    r = parse_transcript(pa)
    check("shape A: 2 real prompts, tool_result/sidechain/meta/command excluded",
          r["prompts"] == ["fix the dataloader leak", "now add a test"])
    check("shape A: edit file captured, bash not counted as file", r["files"] == ["/p/src/data.py"])
    check("shape A: tool counts", r["tools"] == {"Edit": 1, "Bash": 1})
    check("shape A: timestamps span", r["first_ts"].startswith("2026-08-21T14:02"))

    # Shape B: flat, no message nesting
    b = [{"role": "user", "content": "flat style prompt", "type": "user"},
         {"role": "assistant", "type": "assistant",
          "content": [{"type": "tool_use", "name": "Write", "input": {"file_path": "/p/a.py"}}]}]
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as fh:
        for e in b:
            fh.write(json.dumps(e) + "\n")
        pb = fh.name
    rb = parse_transcript(pb)
    check("shape B: flat schema still yields prompt", rb["prompts"] == ["flat style prompt"])
    check("shape B: flat schema still yields file", rb["files"] == ["/p/a.py"])

    # Shape C: garbage
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as fh:
        fh.write("not json\n{}\n[]\n{\"type\":\"user\"}\nnull\n")
        pc = fh.name
    rc = parse_transcript(pc)
    check("shape C: malformed lines survive without raising", isinstance(rc["prompts"], list))
    check("shape D: missing file returns empty, no raise", parse_transcript("/no/such")["lines"] == 0)

    cfg = load_config()
    fn, body = render({"cwd": "/p/ml-pipeline", "session_id": "abc123",
                       "reason": "prompt_input_exit"}, r, cfg)
    check("render: filename has date, project, machine",
          fn.endswith(").md") and "ml-pipeline" in fn)
    check("render: frontmatter opens and closes", body.startswith("---\n") and body.count("\n---\n") >= 1)
    check("render: prompts present in body", "fix the dataloader leak" in body)
    check("render: links to MOC", "[[MOC - Sessions]]" in body)

    red = redact("export OPENAI_API_KEY=sk-abcdefghijklmnopqrstuvwx and token: ghp_ABCDEFGHIJKLMNOPQRST",
                 cfg["redact_patterns"])
    check("redact: sk- key scrubbed", "sk-abcdefghijklmnop" not in red)
    check("redact: gh token scrubbed", "ghp_ABCDEFGHIJKLMNOPQRST" not in red)

    empty_fn, empty_body = render({}, parse_transcript("/no/such"), cfg)
    check("render: empty session still produces a valid note", "No prompts recorded" in empty_body)

    print("\n" + ("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # A logging hook must never break a session exit.
        sys.exit(0)
