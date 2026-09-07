#!/usr/bin/env python3
"""
daily-brief.py — roll a day's Claude Code session notes into one brief.

Reads <vault>/Log/Sessions/*.md (already synced from every machine by git) and
writes <vault>/Log/Daily/YYYY-MM-DD.md: mechanical stats always, plus a short
prose paragraph when a model is reachable.

    ./daily-brief.py                  # yesterday (the scheduled default)
    ./daily-brief.py --today
    ./daily-brief.py --date 2026-08-19
    ./daily-brief.py --week           # last 7 days, one file each
    ./daily-brief.py --dry-run        # print, write nothing
    ./daily-brief.py --no-ai          # skip the model call
    ./daily-brief.py --auto           # scheduled mode: only the designated
                                      # machine, only if the file is missing

Why only one machine generates these: session notes have the machine name in the
filename so they can never collide, but a daily brief is one file per day. If two
machines both wrote it, git would conflict. `brief_machine` in _bin/config.json
names the single machine allowed to generate; everyone else just reads the result.

Recursion guard: the AI paragraph shells out to `claude -p`, which starts a real
Claude Code session — which would fire the SessionEnd hook — which could generate
another brief, forever. The child is invoked with CLAUDE_VAULT_LOG=0 so it never
logs, and --auto refuses to run if the target file already exists.
"""

import json
import os
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime, timedelta
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SESSIONS = VAULT / "Log" / "Sessions"
DAILY = VAULT / "Log" / "Daily"
CONFIG = VAULT / "_bin" / "config.json"

AI_TIMEOUT = 180
MAX_PROMPTS_TO_MODEL = 60


def cfg():
    d = {"brief_machine": "", "brief_ai": True, "git_autosync": True}
    try:
        if CONFIG.exists():
            d.update(json.loads(CONFIG.read_text()))
    except Exception:
        pass
    return d


def machine_name():
    if os.environ.get("CLAUDE_VAULT_MACHINE"):
        return os.environ["CLAUDE_VAULT_MACHINE"].strip()
    f = Path.home() / ".claude-vault-machine"
    try:
        if f.exists():
            return f.read_text().strip()
    except Exception:
        pass
    try:
        return subprocess.run(["hostname", "-s"], capture_output=True, text=True,
                              timeout=5).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


# ------------------------------------------------------------------ note parsing

def parse_note(path):
    """Pull frontmatter and the bullet sections out of one session note."""
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_raw, body = text[3:end], text[end + 4:]

    fm = {}
    for line in fm_raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        fm[k] = v

    def section(title):
        m = re.search(r"^##\s+" + re.escape(title) + r".*?$(.*?)(?=^##\s|\Z)",
                      body, re.M | re.S)
        if not m:
            return []
        out = []
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith("- "):
                item = line[2:].strip()
                if item.startswith("*") and item.endswith("*"):
                    continue          # the "…and N more" filler
                out.append(item.strip("`"))
        return out

    return {
        "path": path,
        "fm": fm,
        "prompts": section("What I asked"),
        "files": section("Files touched"),
        "commits": section("Commits"),
    }


def load_day(datestr):
    notes = []
    if not SESSIONS.is_dir():
        return notes
    for p in sorted(SESSIONS.glob("*.md")):
        n = parse_note(p)
        if not n:
            continue
        # Prefer frontmatter timestamps; fall back to the date in the filename so a
        # note with damaged frontmatter still lands on the right day.
        stamp = (n["fm"].get("ended") or n["fm"].get("started") or "")[:10]
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", stamp):
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", p.stem)
            stamp = m.group(1) if m else ""
        if stamp == datestr:
            notes.append(n)
    return notes


def as_int(v, default=0):
    try:
        return int(str(v).strip())
    except Exception:
        return default


def hm(minutes):
    h, m = divmod(max(0, int(minutes)), 60)
    return f"{h} h {m:02d} m" if h else f"{m} min"


# ---------------------------------------------------------------------- the model

def ai_paragraph(datestr, projects, notes, enabled=True):
    """Short prose summary via `claude -p`. Returns (text, note_about_failure)."""
    if not enabled:
        return "", "AI summary turned off"

    claude = None
    for cand in ("claude",):
        try:
            r = subprocess.run(["which", cand], capture_output=True, text=True, timeout=5)
            if r.returncode == 0 and r.stdout.strip():
                claude = r.stdout.strip()
        except Exception:
            pass
    if not claude:
        return "", "no `claude` CLI on PATH"

    lines = [f"Date: {datestr}", ""]
    for proj, d in projects.items():
        lines.append(f"## Project: {proj} ({d['machines_str']}, {hm(d['minutes'])}, "
                     f"{d['sessions']} session(s))")
        for p in d["prompts"][:MAX_PROMPTS_TO_MODEL]:
            lines.append(f"- asked: {p}")
        for c in d["commits"][:10]:
            lines.append(f"- commit: {c}")
        if d["files"]:
            lines.append("- files: " + ", ".join(sorted(d["files"])[:20]))
        lines.append("")
    facts = "\n".join(lines)

    prompt = (
        "Below is a factual log of one day of my programming/research work, "
        "reconstructed from what I asked an AI coding assistant and what changed on disk.\n\n"
        "Write 3-5 sentences, in past tense, first person plural is forbidden - use "
        "\"you\" to address me directly (e.g. \"You spent the morning on...\"). "
        "Describe what was actually worked on and what progress was made. Group by theme, "
        "not chronologically. Name the projects. If something looks unfinished or "
        "was left broken, say so plainly. No preamble, no bullet points, no headings, "
        "no praise, no speculation beyond the log. Output only the paragraph.\n\n"
        f"{facts}"
    )

    env = dict(os.environ)
    env["CLAUDE_VAULT_LOG"] = "0"      # stop the child session logging itself
    env["CLAUDE_VAULT_NO_BRIEF"] = "1" # and stop it generating a brief
    try:
        r = subprocess.run([claude, "-p", prompt], capture_output=True, text=True,
                           timeout=AI_TIMEOUT, env=env, cwd=str(VAULT))
        out = (r.stdout or "").strip()
        if r.returncode != 0 or not out:
            return "", f"`claude -p` returned {r.returncode}"
        return " ".join(out.split()), ""
    except subprocess.TimeoutExpired:
        return "", f"`claude -p` timed out after {AI_TIMEOUT}s"
    except Exception as e:
        return "", f"`claude -p` failed: {type(e).__name__}"


# ---------------------------------------------------------------------- rendering

def build(datestr, use_ai=True):
    notes = load_day(datestr)
    if not notes:
        return None, None

    projects = OrderedDict()
    machines, all_files, all_commits = set(), set(), []
    total_min = 0

    for n in sorted(notes, key=lambda x: x["fm"].get("ended", "")):
        fm = n["fm"]
        proj = fm.get("project") or "no-project"
        mach = fm.get("machine") or "unknown"
        mins = as_int(fm.get("duration_min"))
        total_min += mins
        machines.add(mach)
        all_files.update(n["files"])
        all_commits.extend(n["commits"])

        d = projects.setdefault(proj, {"minutes": 0, "sessions": 0, "prompts": [],
                                       "files": set(), "commits": [], "machines": set(),
                                       "notes": []})
        d["minutes"] += mins
        d["sessions"] += 1
        d["prompts"].extend(n["prompts"])
        d["files"].update(n["files"])
        d["commits"].extend(n["commits"])
        d["machines"].add(mach)
        d["notes"].append((n["path"].stem, mins, len(n["prompts"])))

    for d in projects.values():
        d["machines_str"] = ", ".join(sorted(d["machines"]))

    para, why = ai_paragraph(datestr, projects, notes, enabled=use_ai)

    dt = datetime.strptime(datestr, "%Y-%m-%d")
    L = ["---",
         f"title: {datestr} — Daily brief",
         "type: daily-brief",
         f"date: {datestr}",
         "tags: [daily-brief, claude-code]",
         f"sessions: {len(notes)}",
         f"projects: {len(projects)}",
         f"active_min: {total_min}",
         f"files_changed: {len(all_files)}",
         f"commits: {len(all_commits)}",
         f"machines: [{', '.join(sorted(machines))}]",
         f'generated: "{datetime.now().astimezone().isoformat(timespec="seconds")}"',
         "---", "",
         f"# {dt.strftime('%A %-d %B %Y')}" if os.name != "nt" else f"# {datestr}",
         ""]

    L += ["## Summary", ""]
    if para:
        L += [para, ""]
    else:
        L += [f"*Stats only — {why}.*", ""]

    L += ["## At a glance", "",
          "| | |", "|---|---|",
          f"| Time in sessions | {hm(total_min)} |",
          f"| Sessions | {len(notes)} across {len(machines)} machine(s) |",
          f"| Projects | {', '.join(projects.keys())} |",
          f"| Files touched | {len(all_files)} |",
          f"| Commits | {len(all_commits)} |", ""]

    L += ["## By project", ""]
    for proj, d in sorted(projects.items(), key=lambda kv: -kv[1]["minutes"]):
        L.append(f"### {proj} — {hm(d['minutes'])}, {d['sessions']} session(s) "
                 f"on {d['machines_str']}")
        L.append("")
        if d["prompts"]:
            L.append("**Asked:**")
            L.append("")
            seen = set()
            for p in d["prompts"]:
                if p in seen:
                    continue
                seen.add(p)
                L.append(f"- {p}")
            L.append("")
        if d["commits"]:
            L.append("**Landed:**")
            L.append("")
            for c in dict.fromkeys(d["commits"]):
                L.append(f"- `{c}`")
            L.append("")
        if d["files"]:
            fl = sorted(d["files"])
            shown = fl[:12]
            L.append("**Files:** " + " · ".join(f"`{f}`" for f in shown) +
                     (f" *(+{len(fl)-len(shown)} more)*" if len(fl) > len(shown) else ""))
            L.append("")

    L += ["## Sessions", ""]
    for proj, d in projects.items():
        for stem, mins, np in d["notes"]:
            L.append(f"- [[{stem}]] — {hm(mins)}, {np} prompts")
    L += ["", "---", "", "[[MOC - Sessions]] · [[Home]]", ""]

    return f"{datestr}.md", "\n".join(L)


# --------------------------------------------------------------------------- main

def main():
    args = sys.argv[1:]
    conf = cfg()
    use_ai = "--no-ai" not in args and conf.get("brief_ai", True)
    dry = "--dry-run" in args
    auto = "--auto" in args

    if auto and os.environ.get("CLAUDE_VAULT_NO_BRIEF") == "1":
        return 0

    if auto:
        want = (conf.get("brief_machine") or "").strip()
        if not want:
            return 0                                  # auto mode not configured
        if machine_name() != want:
            return 0                                  # not the designated machine

    if "--date" in args:
        try:
            datestr = args[args.index("--date") + 1]
            datetime.strptime(datestr, "%Y-%m-%d")
        except Exception:
            print("--date needs YYYY-MM-DD", file=sys.stderr)
            return 2
        days = [datestr]
    elif "--today" in args:
        days = [datetime.now().strftime("%Y-%m-%d")]
    elif "--week" in args:
        days = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
                for i in range(1, 8)]
    elif auto:
        # Backfill: any of the last 7 days that has no brief yet. Without this, a day
        # on which you never opened a session on the designated machine would never
        # get a brief at all, and cron would be mandatory rather than optional.
        days = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
                for i in range(1, 8)]
    else:
        days = [(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")]

    wrote = 0
    for datestr in days:
        target = DAILY / f"{datestr}.md"
        if auto and target.exists():
            continue                                   # already done today
        fname, body = build(datestr, use_ai=use_ai)
        if not body:
            if not auto and len(days) == 1:
                print(f"No sessions recorded on {datestr}.")
            continue
        if dry:
            print(f"--- would write: Log/Daily/{fname}\n\n{body}")
            continue
        DAILY.mkdir(parents=True, exist_ok=True)
        target.write_text(body)
        wrote += 1
        print(f"wrote Log/Daily/{fname}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"daily-brief failed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
