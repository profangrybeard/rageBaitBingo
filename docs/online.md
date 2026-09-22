# Online edition

How `index.html` works. One static file, no build, no server, no login. Served from GitHub Pages.

## Routes

Hash routing, so any static host works.

| Route | Who | What |
|---|---|---|
| `#` (none) | Everyone | Landing. Player door, Caller door, instructor setup notes, links to the paper edition. |
| `#player/N` | Players | Card N, 1 to 99. Mark, install patches, get a claim code, read patch notes. |
| `#console` | Caller only | Private. Quick card, next call, ship patches, check claims, house moves, House card ending. |
| `#stage` | Caller, screen shared | Big number, patch install cards, House card win screen. |

## How a session runs

1. The instructor sends the Caller the link privately. The Caller opens `#console` and `#stage` in two windows of the same browser, and screen shares only the stage. The Open stage buttons open the stage as its own pop-up window, never a tab, so sharing that window can't expose the console.
2. Every other student opens the link, enters their card number, and gets their card.
3. The Caller clicks Next call. The stage updates. The Caller also says the number aloud on voice.
4. The Caller clicks Ship on a patch. The stage shows an "Update required" card with an install code. Players type the code into Updates on their card.
5. To claim, a player types BINGO in chat, clicks Get verification code, and pastes the code in chat. The Caller pastes it into the console.
6. On the instructor's signal, the Caller clicks House wins. The stage shows the House card, fully marked.

## Caller quick card

A one-screen card in the console: when to call, when to ship, what to do on a claim, when to use each house move, and how each patch disqualifies a claim. It opens by itself on a fresh game, before the first call, and stays closed once the Caller clicks Got it. The Quick card button reopens it. Esc closes it.

The disqualifier list comes from each patch's `dq` field in PATCHES, so it can't drift from the rule text. Shipped patches show in pink and the rest in gray, so the Caller only cites rules that are live. It fits a 1366 by 768 laptop screen without scrolling in three columns.

## State

Everything lives in the browser. No shared server state.

- **Player:** `localStorage["rbb2-player-N"]` holds marks (0 empty, 1 X, 2 circle), installed patch versions, cooldown flag, and which patches already failed an install once.
- **Caller:** `localStorage["rbb2-caller"]` holds call index, shipped patches, house move checkboxes, the current number, and whether the quick card was dismissed. Reset game clears all of it, so the card opens again for the next Caller.
- **Stage:** reads `localStorage["rbb2-stage"]`.

All localStorage access is wrapped in try/catch. The page still works in a private window, it just forgets on refresh.

## Console to stage

The console broadcasts on a `BroadcastChannel("rbb2")` and also writes `rbb2-stage` to localStorage. The stage listens to both. This is why console and stage must be open in the same browser on the same machine. It is the price of having no server.

## Install codes

Each shipped patch has a four character code (`EV3N`, `L1TE`, `PR1M`, `TAX4`, `C00L`, `P1NG`, `SWAP`, `B4L4`, `R0LL`, `P4Y2`). Silent Patch has none and cannot be installed. Codes accept O for 0 and I for 1, since students will type them wrong.

The console lists every code next to its patch, before and after shipping. The Caller needs this for the one-player house move, which means sending a code privately without putting it on stage.

About one install in four fails once with "Error 0x8BAD" and must be retried. A given patch fails at most once per card.

## Rules the software enforces

- **Provisional Evens.** Tapping an even number circles it instead of marking it.
- **Cooldown.** After a mark, the next new mark is eaten with a toast.
- **Rollback.** Reverts a subset of the last three installed patches, seeded by card number, so different cards end up on different versions.
- **Premium Skip.** Adds a button that clears Cooldown after the player confirms the Caller accepted their compliment. Honor system.

Everything else is enforced by the Caller at claim time, the same as paper.

## Claim codes

The claim code packs card number, all 25 marks, and the installed patch set into a 14 character Crockford-style base32 string, grouped as `XXXX-XXXX-XXXX-XX`.

Bit layout, most significant first: card (7 bits), 25 marks (2 bits each), installed patch mask (11 bits, one per patch in PATCHES order).

The console decodes it and flags:

- an outdated client (shipped patches the player never installed, excluding Silent Patch),
- marked numbers that were never called,
- marked numbers ending in 7 once Silent Patch is live.

If nothing is flagged, it says "Nothing obvious. Check the patch notes. There is always one."

Changing the PATCHES array order or length changes the mask meaning and breaks old codes. That is fine between sessions and not fine during one.

## Shared seed invariant

`layout(seed)` is a mulberry32 shuffle seeded with `seed * 7919 + 256`. Player cards use their card number. The call order uses 9999. The House card uses 0. The paper edition uses the identical function. `tests/smoke_online.py` checks that online card 14 matches printed card 14.

## Known limits

- Console and stage must share a browser.
- Nothing is pushed to players. Calls and patches reach them through voice and the screen share. This is deliberate. It keeps the friction manual.
- A player's card lives in their browser. Switching devices mid-game means starting over.
- Premium Skip is honor system.
- No way for the instructor to see every card at once. Claims are the only window.

## Deploying

Push to the default branch and enable GitHub Pages from the repo root. `index.html` is the landing page. The `print/` pages are linked from the landing setup notes, so the paper edition is served from the same site.
