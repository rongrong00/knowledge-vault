---
title: MOC - Sessions
type: moc
tags: [moc, claude-code]
created: 2026-08-21
---

# MOC — Sessions

Auto-generated session notes from Claude Code live in `Log/Sessions/`. One note per
session, per machine. You never create these by hand — but the `## Notes` section at
the bottom of each one is yours to write in.

## All sessions

```query
tag:#session
```

## By machine

```query
tag:#machine/cannon
```

> [!tip] Better views
> The blocks above use Obsidian's built-in search. If you install the **Dataview**
> community plugin you can replace them with real tables — the frontmatter is already
> structured for it (`machine`, `project`, `duration_min`, `prompts`, `files_changed`):
>
> ````
> ```dataview
> TABLE machine, project, duration_min AS "min", prompts, files_changed AS "files"
> FROM "Log/Sessions"
> SORT file.name DESC
> LIMIT 30
> ```
> ````

## How it works

A `SessionEnd` hook runs `_bin/claude-session-log.py`, which reads the session
transcript and writes the note, then syncs the vault over git in the background.
Setup and troubleshooting: [[Claude Code Session Logging]].

## Neighbouring maps

- [[Home]]
- [[MOC - Astrophysics]]
