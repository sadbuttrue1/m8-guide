# Timing Reference — Ticks, PPQ, Groove

**What this is:** the tick — M8's underlying unit of time — and the three places you meet it: `TABLE TIC`, the `RET`/`PSL`/`OFF` command values, and Groove View. Consulted from Week 2 (tables), Week 4 (retriggers and transitions), and Week 7 (TIC modes).

**What this is NOT:** a groove-design course. Swing is a taste decision. This page gives you the arithmetic so the taste decision is the only one you're making.

**Manual references:** Groove View (manual p.26), Table View / Table TIC Modes (manual p.24), Sequencer FX Commands (manual p.69), Common Groove Examples (manual p.81).

---

## The one number that explains everything

M8's clock runs in **ticks**. A groove's default rate is **24 PPQN** — parts (ticks) per quarter note (manual p.26).

A phrase row is a sixteenth note by default, and there are four sixteenths in a quarter note. So:

**24 PPQ ÷ 4 sixteenths = 6 ticks per row.**

That single division is the source of every other number on this page:

| Unit | Ticks (at 24 PPQ) |
|---|---|
| One phrase row (16th note) | 6 |
| One quarter note (4 rows) | 24 |
| One full 16-step phrase | 96 |
| One tick, subdivided by `MTT` | 8 subticks |

The manual states the 6-ticks-per-row derivation and the 96-tick phrase total directly (manual p.26). If you are ever unsure whether a command value is "a lot," measure it against 6.

### Why this matters in practice

- `TABLE TIC 01` advances the table one row per tick — **six table rows per phrase row** (manual p.24). A 16-row table at `TIC 01` finishes in under three phrase rows. This is why Week 2's table-as-LFO feels so fast until you slow it down.
- `PSL 06` is a slide lasting exactly one row. `PSL 0C` spans two. That's why the community-standard acid glide sits at `PSL 06`–`07` — it's "one row, or a touch over."
- `RET` values are ticks too. A retrigger of `03` fires twice per row; `06` fires once per row and does nothing audible.
- `OFF XX` counts ticks before the note-off (manual p.72). `OFF 06` = one row later.

---

## Groove View

Grooves define how many ticks **each of the 16 steps** in a phrase consumes (manual p.26). Longer steps and shorter steps alternating is swing; uniformly shorter steps is a faster phrase; skipped steps change the bar length.

- Groove `00` is the default for all 8 tracks. Each track can use a different groove independently.
- Assign a groove to a track with the `GRV` FX command in a phrase.
- Groove View sits **above** Phrase View — `[SHIFT]+[UP]`.

### Adding swing

- [ ] From Phrase View, press `[SHIFT]+[UP]` to reach Groove View.
- [ ] Start the song with `[SHIFT]+[PLAY]` so you hear the change as you make it.
- [ ] Edit the value in row `0` with `[EDIT]+[UP or DOWN]`. Note that this **alters rows 0 and 1 together** — M8 keeps the pair summing correctly for you.
- [ ] Common swing settings are `07,05` or `08,04` (manual p.26). Both sum to 12, so two steps still occupy the same total time — only their split changes.

### Two rules that catch people

- The groove **loops back to the beginning at the first empty row (`--`)**. A groove doesn't have to be 16 rows long; it repeats from wherever it runs out.
- A row of **`00` skips that phrase step entirely.** This is how the triplet and 3/4 examples below shorten the bar.

When editing, the help line at the bottom of the screen **sums the ticks for you**. If you want to keep the same bar length, keep that total at 96.

### Finer resolution

A groove can be set to **24, 48, 96, or 192 PPQN** (manual p.26). Higher PPQ doesn't change how long a step lasts musically — it subdivides the grid more finely, so subtler swings become expressible.

Ticks per row scale with the rate (`PPQ ÷ 4`):

| Groove PPQ | Ticks per row | Ticks per 16-step phrase |
|---|---|---|
| 24 (default) | 6 | 96 |
| 48 | 12 | 192 |
| 96 | 24 | 384 |
| 192 | 48 | 768 |

*The manual states the 24 PPQ row explicitly; the other three follow from the same `PPQ ÷ 4` division.*

**Trade-off:** at 192 PPQ you can nudge a step by 1/48th of a row, but every groove value you type is 8× larger, and command values elsewhere (`RET`, `PSL`, `OFF`) still count real ticks — so they now mean something different relative to a row. Start at 24. Move up only when 24 can't express the swing you hear.

---

## Ready-made grooves

From the manual's Common Groove Examples (manual p.81). Rows not listed are left empty (`--`), which loops the groove.

| Groove | Rows | What it does |
|---|---|---|
| Swing 1 | `07` `05` | Standard swing — the usual starting point |
| Swing 2 | `08` `04` | Harder swing, more pronounced shuffle |
| 2× Speed | `03` | Every step half as long; phrase plays twice as fast |
| Triplets | `08` `08` `08` `00` | Three steps of 8 ticks = one quarter note; fourth step skipped |
| 3/4 Time | `06` ×12, then `00` `00` `00` `00` | 12 steps of 6 = 72 ticks; last four steps skipped |
| Swing Last Step | `06` ×14, then `07` `05` | Straight until the end of the bar, then a nudge |

Check the arithmetic against the totals: triplets give 24 ticks per repeat (one quarter note), 3/4 gives 72 (three quarters), the swings give 96 (a full bar).

---

## `MTT` — micro-timing a single row

`MTT XX` shifts the current row's playback earlier or later in **subticks of 1/8 tick** (manual p.72). This is the tool for flams, for pushing a snare fractionally late, for a hat that sits slightly ahead — placement between the ticks, not a groove for the whole track.

Three constraints from the manual:

- **A negative amount does not work on the first phrase row.** There's no earlier time inside the phrase for it to borrow from.
- **`MTT` currently has no action in tables.** Phrase FX columns only.
- It moves one row. For anything track-wide, use a groove.

**Common failure mode:** using `MTT` where a groove belongs. If you find yourself putting the same `MTT` on every other row, you've hand-built a swing — write it as a groove instead and get it on every phrase for free.

---

## When timing feels wrong

- **Table runs faster than expected.** `TABLE TIC` is in ticks, not rows — `01` is six times per row. Raise it to `06` for one table row per phrase row.
- **Slide doesn't reach the target note.** `PSL` is in ticks; if the gap between the notes is two rows, you need roughly `0C`, not `06`. The help text at the bottom of the screen shows how many steps the slide will last.
- **Groove changed the bar length.** Sum the ticks (the help line does it): 96 keeps a 4/4 bar. A `00` row skips a step; an empty row ends the groove early and loops it.
- **Retrigger sounds like one hit.** `RET` at `06` or higher fires once per row. Go lower.
- **Swing disappears on one track.** Grooves are per-track and assigned with `GRV`. Check the track actually has the command.
