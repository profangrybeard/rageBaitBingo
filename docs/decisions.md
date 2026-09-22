# Decisions

Newest first. The reason is the important part.

## 2026-09-21 · Caller quick card lives in the console

**Decision.** The Caller quick card is a one-screen card inside the console, not a printed half-sheet. It opens by itself on a fresh game. It covers when to call, when to ship, the claim routine, when to use each house move, and one disqualifier line per patch, with only shipped patches highlighted.
**Why.** The retrospective's first worry is a Caller who freezes, especially on house moves. The console is where the Caller already is, so a card there costs the instructor no prep and can't be left at home. Opening before the first call means a first-time Caller reads it without being told to. The disqualifier list turns "there is always one" from a promise into something a student can do in ten seconds. Each line sits in PATCHES next to its rule, so changing a patch without its disqualifier is hard to miss.
**Cost.** The paper packet's brief still has no "when" for house moves. If paper-only Callers freeze, copy the house move lines to page one of the packet.

## 2026-09-21 · Patch text is identical in both editions, except Ping Penalty

**Decision.** The online patch text now matches the paper strips word for word. Pattern Swap alternates circle, X, circle. Premium Skip reads "ignore Cooldown by paying the Caller a compliment," with no "in chat." Sync Penalty and Ping Penalty are the one deliberate difference.
**Why.** Online said "X, circle, X" and paper said "circle, X, circle." In a mixed room, a student holding the paper rule and a student reading the stage would be playing different patches, and the difference was an accident, not a joke. Premium Skip's "in chat" told room players, who read the projected stage, that a compliment had to be typed. The owner picked the paper wording both times.

## 2026-09-21 · Mixed rooms are a supported way to run it

**Decision.** README and the landing setup notes cover a mixed room: paper in the room, the site for remote players, one Caller on the console. Remote players take card numbers from 31 up. Ping Penalty applies to BINGOs said out loud as well as typed.
**Why.** The owner teaches in person and online in the same session every week, so this is the normal case. Numbers from 31 keep remote players off printed layouts, so nobody shares a card. The console already carries the call sheet, patches, and House card, so the paper packet isn't needed. Ping Penalty only named chat, which left room players outside the one patch that breaks context of play.

## 2026-09-21 · Private terms moved out of the public text check

**Decision.** The owner's name, school, and course code no longer appear in `tests/check_text.py`. They live in a gitignored `tests/private_terms.txt` that the check loads when present. Personal details were also trimmed from the retrospective and this log before the repo went public.
**Why.** A public test that bans a name has to spell out that name. Keeping the list local keeps enforcement on the owner's machine without publishing the details.

## 2026-09-21 · Pre-flight fixes before the first live run

**Decision.** Three fixes found while preparing the first live class. The caller packet handoff now says "every page except the last" instead of "the first four pages." The console shows each patch's install code. Open stage opens a separate pop-up window instead of a tab.
**Why.** The packet is six pages, so "first four" left the House card with the instructor, and the Caller needs it for the ending. The one-player house move tells the Caller to send a code privately, but codes only appeared on the shared stage, so the move could not be done. And on Zoom or Teams a Caller shares a browser window. If the stage is a tab next to the console, the first tab switch shows the whole class the call order and patch list.
**Also.** The PDFs were re-rendered with Big Shoulders embedded. The earlier render ran without network, so Google Fonts never loaded and everything printed in a generic fallback sans.

## 2026-09-21 · Repo created for Claude Code

The game moved into its own repo so development can continue in Claude Code with full context. Online edition at the root for GitHub Pages, paper edition in `print/` and `pdf/`, context in `docs/`.

## 2026-09-21 · Online edition is a static file on GitHub Pages

**Decision.** The online edition is one self-contained HTML file with no backend.
**Why.** It must open from a plain link with no login. The first delivery path was a claude.ai artifact, which requires a Claude account. That fails every student and every other teacher. A static file on Pages costs nothing, needs no accounts, and outlives any one platform.
**Cost.** No shared state. Console and stage must share a browser. Nothing is pushed to players.

## 2026-09-21 · Sync Penalty becomes Ping Penalty online

**Decision.** Online, the simultaneity penalty applies to BINGO claims in chat instead of marks.
**Why.** Remote players can't see neighbors mark. Chat is the shared space online, so that's where collisions happen. It still breaks context of play.

## 2026-09-21 · Software enforces some broken rules online

**Decision.** Cooldown, Provisional Evens, Rollback, and Premium Skip are enforced by the page.
**Why.** Remote play loses the arguing that drives the paper version. Letting the software enforce nonsense gives the online room a different version of the same frustration, and it teaches its own point: software removes rule disputes and enforces bad rules just as reliably as good ones.

## 2026-09-20 · Materials must stand alone

**Decision.** Removed every reference to the course the game was first built for: ties to other exercises in that course, the instructor's name on the Caller signal, and callbacks to earlier sessions. The debrief is now a plain three-problem prompt.
**Why.** Other teachers now run this. Anything that assumes a specific course makes the exercise break for them.

## 2026-09-20 · Each patch maps to exactly one Chapter 2 tool

**Decision.** The instructor key and lecture sheet use only the ten tools from Sharp and Macklin, Chapter 2. "Indirect actions" was removed as a label.
**Why.** A debrief works when students can check their answer against a fixed list. A made-up category breaks that.

## 2026-09-19 · Landscape cards, two tall boards per sheet

**Decision.** Player cards print landscape letter, two per sheet, cut down the middle to 5.5 x 8.5.
**Why.** Uses the sheet fully. Squares grew from about 0.7 inch to about 0.9 inch.

## 2026-09-19 · The cheating is written down as house moves

**Decision.** Four one-use house moves replace the Caller's improvised cheating.
**Why.** In 1.0 the cheating lived in one student's head. Written moves make the game repeatable and transferable to any teacher.

## 2026-09-19 · Spelling fixed to "Bait," AI footer removed

**Decision.** Title is Rage Bait Bingo. No "Created by ChatGPT" anywhere.
**Why.** "Bate" was a joke nobody got. The AI footer undercut the instructor's standing on AI use in student work.

## 2026-09-19 · Keep all 25 numbers on every card

**Decision.** Every card still holds every number.
**Why.** It is the core joke. Every call hits every player. Bingo has no decisions, and the patches bolt fake ones on.

## 2026-09-19 · Individual ten-problem worksheet dropped

**Decision.** Replaced by a table-level debrief: three problems, each with what happened, which tool broke, and one fix.
**Why.** Ten written problems per student was slow to grade and easy to fake. Spoken, table-level answers are fast and happen in the room.
