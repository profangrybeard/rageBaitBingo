# Rage Bait Bingo 2.0

Read this first. Then read `docs/INDEX.md`, which maps every other file.

## What this repo is

Rage Bait Bingo is a deliberately broken classroom game for teaching game design. Students play bingo while a student Caller ships absurd rule patches, cheats for the house, and never explains anything. The rage the room feels is the lesson. Afterward the instructor walks through which of the ten basic game design tools (Sharp and Macklin, *Games, Design and Play*, Chapter 2) each patch broke.

It exists in two editions that share one set of cards:

- **Paper edition** for an in-room class: `print/` (HTML sources) and `pdf/` (print-ready output).
- **Online edition** for a remote class: `index.html`, a single static page served by GitHub Pages. No login, no server, no build step.

The owner is a game design professor. Other instructors now run this exercise too, so every shipped file must work for a teacher who has never met him and never seen his course.

## Non-negotiables

1. **Standalone.** Shipped materials never reference a specific instructor, course, school, session number, or any other exercise. "The instructor," never a name. `tests/check_text.py` enforces this.
2. **No em dashes.** Anywhere. Use periods or commas. Also enforced by `tests/check_text.py`.
3. **No login walls.** The online edition must open from a plain link. No accounts, no backend, no API keys, no claude.ai artifact links as the delivery path.
4. **Static and self-contained.** One HTML file per page, inline CSS and JS. The only external request allowed is Google Fonts, and every font stack must fall back cleanly to Arial Narrow.
5. **Paper and online cards must match.** Card N online is card N on paper. Both use the same seeded shuffle. Do not touch `layout()`, the seed formula, `CALL_ORDER`, or the House card seed without changing all three editions together. `tests/smoke_online.py` checks this.
6. **The game has to stay broken on purpose, and stay fair to teach from.** Every patch must break exactly one Chapter 2 tool in a way a student can name afterward. A patch that is only random, or only mean, is a bad patch. See `docs/pedagogy.md`.

## How to work here

- Before changing game rules or patches, read `docs/design.md` and `docs/pedagogy.md`. A patch change usually touches four places: `index.html` PATCHES (the rule text `x` and the console quick card's disqualifier line `dq`), `print/caller-packet.html` patches, `print/wrap-up-lecture-sheet.html`, and `docs/design.md`. Online and paper rule text must match word for word, except Sync Penalty and Ping Penalty.
- After any change to `print/`, run `python tools/render_pdfs.py`. It re-renders `pdf/` and fails if page counts drift.
- After any change to `index.html`, run `python tests/smoke_online.py`.
- Before any commit, run `python tests/check_text.py`.
- Log real design decisions in `docs/decisions.md`, newest first, with the reason. The reason matters more than the decision.

## Writing voice

For anything a teacher or student reads: plain, direct, short sentences, no hedging, no marketing tone. The Caller never explains, and the materials should sound like it. Full rules in `docs/style.md`.

## Owner working preferences

- Brutally honest assessment. If something is weak, say so and say exactly why.
- Flag it early when a design is getting more complex than an instructor can run without prep time. Administrative load is a hard filter.
- Prose over bullets in teaching documents.
- Lead with what works before naming gaps. Name the exact thing, the exact gap, the exact fix.
