---
title: README
type: meta
created: 2026-08-21
---

# How this vault works

A hybrid vault: a few stable folders, with **links** doing the real organizing.
Folders answer *"what kind of note is this?"* Links answer *"what does it connect to?"*

Start at [[Home]].

## The folders

| Folder | Holds | One-line rule |
|---|---|---|
| `Concepts/` | Atomic notes — one idea per note | If you'd explain it in its own breath, it's a note |
| `Literature/` | Notes *on* papers, talks, books | One note per source, titled by the source |
| `Projects/` | Active work with an outcome | Dies when the project ships; findings graduate to `Concepts/` |
| `Log/` | Dated research log / daily notes | Chronological, never reorganized |
| `Maps/` | Maps of Content — hub notes | Curated tables of contents for a topic |
| `Templates/` | Note skeletons | Insert with the Templates plugin |
| `Attachments/` | Images, PDFs, figures | Obsidian drops files here automatically |

New notes default to `Concepts/`. Move them if they belong elsewhere.

## The five conventions

**1. One concept per note.** `Spin Temperature` is a note. `Notes on radio astronomy`
is not — it's a Map. Atomic notes get reused in contexts you didn't anticipate;
grab-bag notes get reused never.

**2. Title notes as the thing itself.** `Wouthuysen-Field Effect`, not
`Notes on the Wouthuysen-Field effect`. The title *is* the link text you'll type.

**3. Link generously, including to notes that don't exist yet.** An unresolved
link (dimmed in the editor) is not an error — it's a bookmark for future you.
Click it and Obsidian creates the note. Your unresolved links are your reading list.
Open **Graph view** and uncheck "Hide unresolved" to see what you keep gesturing at.

**4. Write for the version of you who has forgotten this.** Not the version who
just read the paper. That means: state the physical mechanism, not just the result;
say why it matters; keep the number *and* its units.

**5. Frontmatter carries the metadata.** Every note starts with a YAML block.
`status` tracks maturity:

- `seed` — a stub, a title and a hunch
- `growing` — real content, still incomplete or unverified
- `evergreen` — you'd defend it in a group meeting

## Tags vs. links

Use **links** for things (`[[Spin Temperature]]`). Use **tags** for *kinds* of
things (`#astro/ISM`, `#method/mcmc`, `#question`). Nested tags with `/` give you
a browsable tree in the tag pane. `#question` and `#todo` are worth being
disciplined about — they turn into a live task list via search.

## Daily log

`Cmd+P` → "Open today's daily note" creates a dated note in `Log/` from the
Daily Log template. Good for: what you ran, what broke, what surprised you.
Link out to concepts from there and the log becomes an index of your own thinking.

## Session logging

Claude Code sessions on any machine auto-append a note to `Log/Sessions/`, and the
vault syncs over git. Setup, options and troubleshooting: [[Claude Code Session Logging]].
Browse them from [[MOC - Sessions]].

## Growing it

The vault is deliberately near-empty. [[21 cm Line]] is the one worked example —
it shows the house style and it is full of unresolved links on purpose. Following
those links is the intended first hour of use.

Don't reorganize early. Write fifty notes first, then let the structure that
actually emerged tell you what folders you needed.
