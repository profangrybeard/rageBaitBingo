# Index

Every file in the repo and what it is for.

## Start here

| File | What it is |
|---|---|
| `CLAUDE.md` | Rules and working agreement for Claude Code. Read first. |
| `README.md` | For teachers. How to run the game in a room or online. |
| `docs/retrospective.md` | Full history: version 1.0 in 2025, the 2.0 rebuild in 2026, what worked, what didn't, and why. |

## The game

| File | What it is |
|---|---|
| `docs/design.md` | How the game works. Components, the core joke, every patch, house moves, ending. The design reference. |
| `docs/pedagogy.md` | Why it works as a lesson. The ten Chapter 2 tools, which patch breaks which tool, and how the debrief runs. |
| `docs/online.md` | How the online edition is built. Routes, state, the console to stage link, claim codes, known limits. |

## Records

| File | What it is |
|---|---|
| `docs/decisions.md` | Decision log, newest first, with reasons. |
| `docs/style.md` | Writing rules and visual design tokens. |
| `docs/roadmap.md` | Open items and ideas, ranked. |

## Shipped materials

| File | Edition | What it is |
|---|---|---|
| `index.html` | Online | The whole online game. Landing, player card, Caller console, stage. |
| `print/player-cards.html` | Paper | 30 player cards, two per landscape letter sheet, cut to 5.5 x 8.5. |
| `print/caller-packet.html` | Paper | Caller brief, house moves, call sheet, 11 patch strips, House card, instructor key. |
| `print/wrap-up-lecture-sheet.html` | Both | The debrief. Every place the game ignored, broke, or mocked one of the ten tools. |
| `pdf/*.pdf` | Paper | Rendered output of `print/`. Regenerate, never hand edit. |

## Tooling

| File | What it does |
|---|---|
| `tools/render_pdfs.py` | Renders `print/` to `pdf/` and checks page counts. |
| `tests/smoke_online.py` | Plays one full online loop in a headless browser and checks it. |
| `tests/check_text.py` | Fails on em dashes, instructor names, course references, or the old misspelling. Owner-specific names load from a local, gitignored `tests/private_terms.txt`. |
