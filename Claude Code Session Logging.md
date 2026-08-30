---
title: Claude Code Session Logging
type: meta
tags: [claude-code, setup]
created: 2026-08-21
---

# Claude Code session logging

Every Claude Code session on every machine writes a note into `Log/Sessions/`.
The vault syncs over git, so all machines see all sessions.

```
MacBook ──┐                            ┌── Log/Sessions/2026-08-21 1440 ml-pipeline (macbook).md
          ├── SessionEnd hook ──► vault (git) ──► GitHub (private)
Cannon  ──┘                            └── Log/Sessions/2026-08-21 0915 sims (cannon).md
```

**One note per session, per machine.** The machine name is in the filename, so two
machines can never write the same path — git never sees a merge conflict on session
notes. That's the whole trick.

## Pieces

| File | Does what |
|---|---|
| `_bin/claude-session-log.py` | Reads the hook payload, parses the transcript, writes the note, syncs git in the background |
| `_bin/install-claude-hook.sh` | Registers the hook on one machine. Idempotent — run once per machine |
| `_bin/config.json` | Options: redaction patterns, ignore list, autosync on/off |
| `~/.claude/hooks/obsidian-session-log` | Generated wrapper. Exists because this vault's path contains a space |

---

## Setup

### 1 · Push the vault to a private repo (once, from the Mac)

The vault is already a git repo with an initial commit on `main`. Create an **empty
private** repo on GitHub named `knowledge-vault` (no README, no .gitignore), then:

The remote is already set to `https://github.com/rongrong00/knowledge-vault.git`.
There are no SSH keys on this Mac, so HTTPS is the path of least resistance:

```bash
brew install gh          # skip if you already have it
gh auth login            # browser flow; also stores git credentials
cd ~/Documents/Obsidian\ Vault
gh repo create rongrong00/knowledge-vault --private
git push -u origin main
```

Without `gh`: create the empty private repo in the browser, then push and paste a
[fine-grained personal access token](https://github.com/settings/tokens) as the
password when git asks. `git config --global credential.helper osxkeychain` will
keep you from retyping it.

> [!warning] Make it private
> Session notes contain your prompts and file paths. The logger redacts obvious
> secrets (API keys, tokens, passwords) but redaction is a safety net, not a guarantee.

### 2 · Install the hook on the Mac

```bash
bash ~/Documents/Obsidian\ Vault/_bin/install-claude-hook.sh
```

Claude Code isn't installed on this Mac yet — install it first if you want laptop
sessions logged. The hook doesn't care when it arrives; register it now or later.

### 3 · Clone and install on Cannon

```bash
ssh you@login.rc.fas.harvard.edu
git clone https://github.com/rongrong00/knowledge-vault.git ~/knowledge-vault
echo cannon > ~/.claude-vault-machine       # see note below
bash ~/knowledge-vault/_bin/install-claude-hook.sh
```

> [!important] Pin the machine name on a cluster
> Without `~/.claude-vault-machine`, the logger uses `hostname -s` — which on a
> cluster is whatever login or compute node you landed on (`holylogin04`,
> `holygpu7c26301`). You'd get a different "machine" every session and the tags
> would be useless. Pin it to one name.

**If GitHub over SSH is blocked** (some clusters block outbound port 22):

```bash
# Option A — SSH over 443
printf 'Host github.com\n  Hostname ssh.github.com\n  Port 443\n' >> ~/.ssh/config

# Option B — HTTPS with a fine-grained personal access token
git remote set-url origin https://github.com/rongrong00/knowledge-vault.git
git config credential.helper 'store --file ~/.git-credentials-vault'
```

### 4 · Verify

Run a real session — any directory, one prompt, then exit. Then:

```bash
bash ~/knowledge-vault/_bin/install-claude-hook.sh --check
```

It prints what's registered and the most recent session notes. A new note should be
listed.

---

## If no note appears

Work down this list.

**1. Is the hook registered?** `--check` shows the `SessionEnd` entries. If yours
isn't there, the installer refused to write — most likely your `settings.json` had a
syntax error. It says so rather than clobbering the file.

**2. Wrong hook schema.** Claude Code has used two shapes for hook entries. The
installer writes the flat one by default. If nothing fires, switch:

```bash
bash <vault>/_bin/install-claude-hook.sh --nested
```

This is the most likely failure, and it's a one-command fix.

**3. Does the logger work at all?** Feed it a payload by hand:

```bash
echo '{"cwd":"'$PWD'","transcript_path":"'$(ls -t ~/.claude/projects/*/*.jsonl | head -1)'"}' \
  | python3 <vault>/_bin/claude-session-log.py --dry-run
```

`--dry-run` prints the note it *would* write and touches nothing. If that produces a
sensible note, the logger is fine and the problem is hook registration.

**4. Empty sessions are skipped on purpose.** `min_prompts: 1` in `_bin/config.json`.
A session where you typed nothing isn't worth a note. Set it to `0` to log everything.

**5. Python.** Needs python3 ≥ 3.7 on `PATH`. On a cluster you may need `module load
python` in your shell rc so it's present in non-interactive shells.

**6. Nothing pushed.** The git sync is detached and silent by design — it must never
delay your session exit. Check by hand:

```bash
cd <vault> && git log --oneline -3 && git status
```

---

## Options

`_bin/config.json` is tracked in git, so it applies on every machine:

| Key | Default | Meaning |
|---|---|---|
| `git_autosync` | `true` | Commit and push after each session. `false` = write notes only |
| `min_prompts` | `1` | Skip sessions with fewer real prompts than this |
| `ignore_cwd_patterns` | `[]` | Regexes; sessions in matching directories are never logged |
| `redact_patterns` | 5 patterns | Applied to prompt text before writing |

Per-session escape hatch — log nothing for one session:

```bash
CLAUDE_VAULT_LOG=0 claude
```

Skip a whole tree by adding to `ignore_cwd_patterns`, e.g. `"/private-research/"`.

## Uninstall

```bash
bash <vault>/_bin/install-claude-hook.sh --uninstall
```

Removes the hook and wrapper, leaves every existing note alone. Other hooks in your
`settings.json` are untouched.

---

## What the notes contain

Frontmatter (`machine`, `project`, `branch`, `duration_min`, `prompts`,
`files_changed`, `commits`, `session_id`) plus your prompts, files touched, recent
commits, and tool counts. Structured for Dataview if you ever install it — see
[[MOC - Sessions]].

The `## Notes` section at the bottom of each generated note is yours. The script
writes a file once and never rewrites it, so anything you add there stays.

## Known limitation

The transcript format Claude Code writes to disk is not publicly documented. The
parser handles the shapes seen so far and degrades gracefully — a format change makes
notes thinner, never breaks your session exit (the script exits 0 unconditionally).
If notes suddenly lose their prompts, run the `--dry-run` command above against a
fresh transcript and the new shape will be obvious.

*Back to [[README]] · [[MOC - Sessions]] · [[Home]]*
