# Style

## Writing

These rules apply to everything a teacher or student reads, and to these docs.

- No em dashes. Ever. Use periods or commas.
- Plain and direct. Short sentences, short paragraphs.
- No hedging. Not "you might consider." Say what to do.
- No marketing tone, no exclamation points, no formatting flourishes.
- Be specific. Name the exact thing.
- Sentence case for headings and buttons.
- "The instructor," never a name. "The Caller," always capitalized.
- Player-facing copy is deadpan corporate, like a real patch note. The joke is in the rule, not the wording. "Invalid code. Please contact support." "Already up to date." "Cooldown skipped. Thank you for your purchase."
- The Caller's brief is written as orders.

## Visual design

The look is a bingo hall printout crossed with a live-service patch notice. Deliberately not the usual generated-page look: no dark surfaces, no cream background with a serif, no gold accents, no rounded card kit.

**Type.** Big Shoulders Display (700, 900) for display and numbers. Big Shoulders Text (400, 600, 800) for body. Fallback: Arial Narrow, Helvetica Neue, Arial. The condensed face keeps numbers huge in small squares.

**Color.**

| Token | Hex | Use |
|---|---|---|
| `--spot` | `#C8175D` | Player cards, patches, marks, call numbers |
| `--spot-soft` | `#FBE3EC` | Patch-now call sheet cells, button hover |
| `--house` | `#1F4FA3` | The House card, circles, the instructor-only key, Mocked tags |
| `--ink` | `#141414` | Borders, text on paper |
| `--paper` | `#FFFFFF` | Cards and panels |
| `--hall` | `#D6DBE0` | Page background, light |
| `--hall` (dark) | `#1E2328` | Page background, dark |

Pink belongs to the players and the patches. Blue belongs to the house. Keep that split.

**Shapes.** 3px ink borders, square corners, no shadows, no gradients. Print backgrounds forced on with `print-color-adjust: exact`.

**Dark mode.** Only the page background and page text change. Cards and panels stay white paper in both modes, because they are objects.

**Print.** Letter paper. Player cards landscape, everything else portrait. Every page must render at 100% scale with no manual fitting.

**Screen.** Works at phone width with a 16px side gutter and no horizontal scroll. The player card must be usable on a phone.
