# Design

How Rage Bait Bingo works. This is the reference for anyone changing rules.

## The core joke

Bingo has no decisions. Every card in this game holds all 25 numbers, so every call hits every player. The only thing separating players is where the numbers happened to print. The patches then bolt fake decisions onto a game that has none, and the Caller enforces them unfairly. The rules are always written clearly. The game is still broken. That gap is the lesson.

## Roles

**Players.** Everyone except the Caller. Each gets one card and marks it.

**The Caller.** One student, chosen by the instructor. Calls numbers, ships patches, checks claims, and cheats for the house. Never explains a patch. If asked, reads it again, slower. The Caller is a student on purpose. Unfairness from a peer reads as a bit. The same unfairness from the instructor reads as hostility.

**The instructor.** Chooses the Caller, decides when the game ends, and runs the debrief.

## Components

**Player cards.** 5 x 5 grid, numbers 1 to 25, each card a different seeded shuffle. Columns are headed B I N G O, and the numbers ignore the column convention. Footer rules line: "Rules as of patch 1.0: mark each number the Caller calls. Five in a row wins." 30 cards on paper. Online cards run 1 to 99 and match paper for 1 to 30.

**Call sheet.** A fixed order for all 25 numbers. Patch drops are marked after calls 5, 8, 11, 14, 17, 20, and 23. The first five calls are always clean so players learn how pointless the base game is before anything changes.

**Patch strips.** Eleven patches, shipped in order.

**House card, No. 00.** The Caller's card. It never loses.

## Patches

| Patch | Name | Rule as written | Tool it breaks |
|---|---|---|---|
| 1.1 | Provisional Evens | Even numbers are provisional. Circle them. A circle becomes a mark only if the next odd number you mark is higher. | Decision-making and feedback |
| 1.2 | Blackout Lite | Lines only count if both end squares are odd. | Goals |
| 1.3 | Diagonal Lock | Diagonals only count if the center is prime. The primes are 1, 2, 3, 5, and 9. | Constraint |
| 1.4 | Verification Tax | When your card is checked, your whole row freezes until the next even call. | Challenge |
| 1.5 | Cooldown | After you mark a number, skip your next mark. | Direct actions |
| 1.6 | Sync Penalty (paper) / Ping Penalty (online) | Paper: simultaneous marks by neighbors void both. Online: two BINGOs in chat in the same second void both. | Context of play |
| 1.7 | Pattern Swap | Only the two long diagonals count. Marks along a diagonal must alternate. | Goals |
| 1.8 | Silent Patch | Numbers ending in 7 no longer count. Never announced. Enforced only on a claim. | Decision-making and feedback |
| 1.9 | Goal Rebalance | You win by being the first player who can no longer make any line. | Goals and challenge |
| 2.0 | Rollback | The last three patches are reverted. Except the ones that weren't. | Skill, strategy, chance, and uncertainty |
| 2.1 | Premium Skip | Skip Cooldown by paying the Caller a compliment. The Caller decides what counts. | Skill, strategy, chance, and uncertainty |

Goals is hit three times on purpose. Moving the goal is the most visible way a live game betrays its players, and students feel it hardest.

## Caller rules

- Say each number twice.
- Read each patch word for word. Never explain.
- Any time a player claims bingo, ship the next patch before checking them.
- When checking a claim, read the card aloud slowly and find the patch that disqualifies it. There is always one.

## House moves

One use each, whenever the Caller likes.

1. Call a number that was already called. If challenged, it was a different 14.
2. Apply a patch to one table only (online: send one player the code privately).
3. Misread a player's card aloud during a check.
4. Take a mark back from a player for lag.

These replace the improvised cheating from version 1.0. Written down, any student can run them and any teacher can hand them off.

## Ending

The instructor signals the Caller. The Caller holds up (or puts on stage) the House card and calls bingo. Explains nothing. Then the debrief starts.

## Design tests for any new patch

A new patch must pass all of these or it does not ship.

1. It is written clearly. The joke is never that the wording is confusing.
2. It breaks exactly one of the ten Chapter 2 tools, and a student could name which one.
3. It can be run by a student Caller with no prep and no judgment call beyond what the patch says.
4. It works on paper. Online-only patches are allowed only if the paper edition has an equivalent that breaks the same tool.
5. It is not cruel to a specific player. Every patch hits the room, or hits whoever the Caller picks by a house move.
