# Roadmap

Ranked. Top items first. Each one should stay runnable by a teacher with no prep time. If an idea adds instructor workload, it goes to the bottom or gets cut.

## Next

1. **Run 2.0 live and write down what happened.** Paper and online both. Add findings to `docs/retrospective.md` under a new dated section. Watch list is at the end of the retrospective.
2. **Online debrief note on the lecture sheet.** One line about software enforcing nonsense, visible only when the sheet is used for an online class, or a short separate online addendum. Keep the main sheet identical for both.

## Soon

3. **Card count settings.** A `?cards=40` style option for the paper print page so a teacher with a big room doesn't need to edit the file.
4. **Stage call history.** A small strip of the last few calls on stage so latecomers can catch up. Only if it doesn't make the game fairer by accident. The repeat-call house move depends on nobody being sure.
5. **Test the phone layout** of the player card on a real small phone during a live session.

## Maybe

6. **Instructor overview.** A way to see every card at once. Would need shared state, which means a backend. Violates the no-server rule unless it can be done with a free, no-login service. Not worth it unless teachers ask.
7. **More patches.** Only through the design tests in `docs/design.md`. Candidates should target the tools with the fewest hits: abstraction and storytelling.

## Done

- Paper edition 2.0: cards, caller packet, wrap-up lecture sheet, PDFs.
- Online edition 2.0: landing, player, console, stage, claim codes.
- Materials made standalone for other teachers.
- Repo set up with context for Claude Code.
- Mixed room run instructions in README and on the landing page.
- Pre-flight fixes: packet handoff wording, install codes in the console, stage in its own window.
- Caller quick card in the console.
