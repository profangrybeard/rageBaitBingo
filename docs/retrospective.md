# Retrospective

The full story of this game, so anyone picking up the repo knows what has been tried, what landed, and what the goals are.

## Version 1.0, September 2025

The owner built the first version at the last minute, the night before class. It ran in September 2025 in a game design course, as an in-class exercise.

**What existed.** Three printouts.

- 20 bingo cards, 5 x 5, numbers 1 to 25. Every card held all 25 numbers in a different order. The cards were generated with ChatGPT and carried a "Created by ChatGPT" footer.
- A Patch Notes sheet with seven bad rules: provisional evens, lines only counting between odd endpoints, diagonals only counting if the center is "prime" (with primes defined wrong as 1, 2, 3, 5, 9), a verification tax that froze your row when checked, a cooldown on marking, a sync penalty for simultaneous marks, and a hotfix that swapped the winning pattern to long diagonals with alternating colors.
- A debrief worksheet asking each student to list ten design problems they observed, each with what happened, the principle it broke, and one fix.

**How it ran.** The owner elected one student as his assistant. That student called numbers, announced patches, and cheated for him. Nothing about the cheating was written down. The assistant improvised it.

**What worked.** It went great. The room got genuinely angry at a game that was clearly written and still unplayable, and that anger turned into vocabulary in the debrief. Putting a student in the Caller seat made the unfairness social instead of coming from the instructor, which kept it funny instead of hostile.

**What didn't.**

- The title was spelled "Rage Bate Bingo." It was a joke. Nobody got it. It read as a typo.
- The ChatGPT footer undercut the instructor's standing on AI use in student work.
- The ten-problem worksheet was individual take-home style writing. It was slow to grade and easy to fake.
- The cheating lived in one student's improvisation. A different assistant would have run a different game, and nothing could be handed to another teacher.
- The patches were the only broken thing. The cards, the ending, and the Caller's behavior were never designed as part of the lesson.

## Version 2.0, September 2026

Rebuilt in 2026 and retired the ChatGPT version. Other instructors now run the exercise as well, which changed what the materials had to be.

### Goals for 2.0

1. Keep what made 1.0 work: a student Caller, clearly written rules that are still broken, and rage that turns into a design lesson.
2. Design the cheating. Turn the assistant's improvisation into written house moves so any student can run it and any teacher can hand it off.
3. Make every broken thing teachable. Each patch breaks exactly one of the ten basic game design tools from Sharp and Macklin, Chapter 2, so the debrief has a map.
4. Fix the title, drop the AI footer, and make everything look like one designed object.
5. Make it standalone. No instructor name, course number, session number, or dependency on any other exercise. Any teacher can run it cold.
6. Build an online edition for remote classes that anyone can open from a link with no login.

### What was built

**Paper edition.**

- *Player cards.* 30 cards. Still all 25 numbers on every card, because the core joke is that bingo has no decisions. New touches: B I N G O column heads that the numbers ignore (the abstraction lies about itself) and a rules line that reads "Rules as of patch 1.0," which tells players the game will change without saying how. Laid out two per landscape letter sheet so each cut board is a tall 5.5 x 8.5 with roughly 0.9 inch squares, readable at arm's length.
- *Caller packet.* A brief written as orders, four one-use house moves, a fixed call sheet with patch drops marked, eleven patch strips, the House card, and an instructor-only key mapping each patch to the Chapter 2 tool it breaks.
- *Wrap-up lecture sheet.* All ten tools, with every place the game ignored, broke, or mocked each one.

**Online edition.** One static HTML file for GitHub Pages. Players open their own card by number. The Caller runs a private console and screen shares a separate stage window. Patches ship with install codes. Claims happen in chat with a verification code the console decodes. The software enforces some of the broken rules, which the paper version cannot.

### Changes from 1.0 to 2.0, patch by patch

The seven original patches survived, cleaned up. Four new ones were added:

- *Silent Patch.* A rule that is never announced and is only enforced on a claim.
- *Goal Rebalance.* You now win by being unable to make any line.
- *Rollback.* "The last three patches are reverted. Except the ones that weren't."
- *Premium Skip.* Pay the Caller a compliment to skip Cooldown.

In the online edition, Sync Penalty became **Ping Penalty**, where two BINGO claims in chat within the same second void each other. It still breaks the same tool, context of play.

### Iterations inside the 2.0 build

These happened in order during the rebuild and each one is a lesson worth keeping.

1. *Cards were first laid out portrait, two stacked per page.* The owner pointed out that landscape with two tall 5.5 x 8.5 halves used the sheet far better. Switched. Bigger squares, same paper.
2. *The instructor key first used "Indirect actions" for Sync Penalty.* That is not one of the ten Chapter 2 tools. Corrected to "Context of play" once the lecture sheet forced a strict mapping to the ten.
3. *The first 2.0 materials still referenced the course the game was first built for.* Ties to other exercises in that course, the instructor's name on the Caller signal, a callback to an earlier session. All of that was stripped once other teachers started using the game. The course-specific framing now lives in the owner's own notes, not in the shipped materials.
4. *The first online delivery path was a claude.ai artifact, which needs a login.* Rebuilt as a plain static file for GitHub Pages.

## Where things stand

- Paper edition: complete, print-tested, PDFs rendered.
- Online edition: complete, smoke-tested end to end, not yet run with a live class.
- The 2025 version 1.0 files are archived outside this repo. They are retired. Do not rebuild from them.

## What to watch the first time 2.0 runs live

- Does the Caller actually use the house moves, or freeze? If students freeze, the brief needs a line that says when to use each move.
- Online: does the install-code friction read as funny or just tedious after the fourth patch?
- Does the debrief land on the tools, or stall on "the Caller was mean"? If it stalls on the Caller, the lecture sheet's context of play section needs to come earlier.
- How long does play run before the room is ready to stop? The call sheet assumes up to 25 calls. Nobody should need all 25.
