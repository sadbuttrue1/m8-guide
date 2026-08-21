# Week 2 — LFO to filter (modulation slots + tables)

**Goal:** Crack the modulation system. Learn the difference between **modulation slots** (instrument-level, the cleanest way to do LFOs) and **tables** (per-step automation, for things slots can't do).

**The big realization for this week:** the M8 has 4 dedicated modulation slots per instrument before you even touch tables. For "LFO to filter," the modulation slot is usually the right tool. Tables are for *stepped* automation, arpeggios, multi-stage envelopes — things slots can't do cleanly.

**Manual references:** Instrument Modulation View (manual p.18), Modulation Types: LFO (manual p.20–21), Table View (manual p.24), Macrosynth (manual p.52), Effect Command Help View (manual p.48).

---

## Thread 1: M8 technique — LFO to filter, two ways

### Method A: Modulation slot (recommended for LFO → filter)

This is the clean, idiomatic way.

- [ ] Open the bass instrument in Project 1. Make sure `TYPE` is `Macrosynth` (manual p.52).
- [ ] In Instrument View, the Macrosynth has a `FILTER` parameter section with `CUTOFF` and `RES`. Set `CUTOFF` to a low-ish value (~`40`) so there's room for the LFO to open it.
- [ ] Navigate `[SHIFT]+[UP]` from Instrument View → Instrument Modulation View (manual p.18).
- [ ] You'll see 4 modulation slots (`MOD1`–`MOD4`). Each has TYPE, DEST, and parameters.
- [ ] Configure `MOD1`:
	- `MOD1` type: `LFO`
	- `DEST`: `FILTER CUTOFF` (cycle with `[EDIT]+[DIRECTION]`)
	- `AMT`: try `40` to start (range 00–FF). This is modulation depth.
	- `OSC`: `TRI` (triangle — smooth, classic LFO shape). Other shapes listed manual p.21.
	- `TRIG`: `FREE` (loops continuously, doesn't reset per note). Options: FREE/RETRIG/HOLD/ONCE.
	- `FREQ`: `08` (a value in 16th-note steps when OSC is non-tick).
- [ ] Preview with `[EDIT]+[PLAY]`. Hear the filter slowly open and close.
- [ ] Experiment: change `FREQ` to `04` (faster), `10` (slower). Change `OSC` to `SIN` (smoother), `SQU DN` (gated). Change `AMT` to taste.

### Generative bonus: RANDOM and DRUNK shapes

*See [Generative Toolkit Reference](../reference/generative.md#2-random--drunk-lfo-shapes) for full context.*

- [ ] On the same instrument, change `OSC` to `DRUNK`. Hear: filter wanders organically, never repeats exactly.
- [ ] Change `OSC` to `RANDOM`. Hear: stepped, jumpy values per cycle.
- [ ] Both are documented LFO shapes (manual p.21).
- [ ] **Use case:** any time a parameter should feel alive rather than mechanical. Pads, evolving textures, sound design.
- [ ] **Watch out:** AMT too high = chaotic. Subtle (`20–40`) is usually better than dramatic.

### Method B: Table-based "manual LFO" (when you need stepped/synced control)

This is the table approach. Use when you want each step of the phrase to have an explicit filter value — not smooth automation.

- [ ] Stay on the bass instrument. Navigate `[SHIFT]+[RIGHT]` from Instrument View → Table View (manual p.24).
- [ ] The table has 16 rows with `N` (transpose), `V` (volume), and 3 `FX` columns.
- [ ] To open the FX command helper: position cursor on an FX column, press `[EDIT]+[UP or DOWN]` to launch the **Effects Command Help view** (manual p.48).
- [ ] Filter cutoff is a Macrosynth-specific parameter. The FX command to set the Macrosynth filter cutoff is found in **Instrument FX Commands** (manual p.75) — look for the Macrosynth filter command (browse the Effect Command Help view in-device).
- [ ] Build a 4-step stepped filter sweep using whichever command the help view shows for Macrosynth filter cutoff. Example pattern (values are illustrative, use the actual command code shown):
	- Row 00: cutoff = 20
	- Row 01: cutoff = 50
	- Row 02: cutoff = 80
	- Row 03: cutoff = 50
- [ ] Set `TABLE TIC` in Instrument View to control table speed. Default `01` = 1 tick per step.
	- A phrase row is **6 ticks**, so `TIC 01` advances the table six times per row — much faster than it looks. `TIC 06` gives one table row per phrase row. See [Timing Reference](../reference/timing.md).
- [ ] Compare: the slot LFO is smooth and continuous, the table is stepped and locked to your tic rate. **Use whichever fits the sound.**

### Tip

- Use [M8 table editor](https://twinside.github.io/m8table/) in your browser to experiment with table layouts before entering them on the device.

## Thread 2: Synthesis fundamental — Envelopes (ADSR)

*Goal: understand that envelope shape defines instrument identity more than oscillator does.*

The Instrument Modulation View also handles envelopes. The same modulation slots that can be LFOs can also be AHD, ADSR, DRUM, TRIG, or TRACKING envelopes (manual p.18–21).

- [ ] Open a fresh Wavsynth or Macrosynth instrument.
- [ ] In Instrument Modulation View, set `MOD1` to `ADSR ENVELOPE`, `DEST` to `VOLUME` (or `AMP`).
- [ ] Configure ADSR (manual p.20):
	- `AMT` (amount): the envelope's **depth and direction** — set this first (see below). For volume, keep it positive; `7F` = full depth.
	- `ATK` (attack): time to reach `AMT`
	- `DEC` (decay): time to reach sustain
	- `SUS` (sustain): hold level while note plays
	- `REL` (release): time to fall to zero after note ends
- [ ] **Pluck**: AMT=7F, ATK=00, DEC=20, SUS=00, REL=10. Hear: percussive, snappy.
- [ ] **Pad**: AMT=7F, ATK=60, DEC=00, SUS=7F, REL=80. Same oscillator, completely different instrument.
- [ ] Realize: attack and release are doing 80% of the work in defining what something *sounds like*.

### Why `AMT` looks split at `80`

`AMT` is **bipolar** — a signed value, not a `00`→max ramp, which is why the interface looks divided at `80`:

- `00`–`7F` → **positive** amount (`00` = none, `7F` = +127, full depth)
- `80`–`FF` → **negative** amount (`80` ≈ most negative, `FF` ≈ −1)

So scrolling past `7F` flips the modulation *direction* rather than adding more depth. Read `AMT` as **how far, and which way**, the envelope pushes its destination.

- [ ] For a normal volume envelope, keep `AMT` positive — `7F` is full depth. (That's why the Pluck and Pad above both use `AMT=7F`.)
- [ ] A **negative** `AMT` on volume *inverts* the envelope: louder envelope = quieter sound, i.e. a ducking/gate effect. Deliberate, not what you want for a standard amp shape.
- [ ] Negative depth is more useful on `CUTOFF` (envelope *closes* the filter) or `PITCH` (downward dive for kicks/zaps).
- [ ] **Common failure mode:** leaving `AMT` at `00` (no depth — the envelope does nothing) or landing in `80`+ by accident (inverted), then wondering why the shape is backwards. The hex logic: a negative *volume* is meaningless, but a negative *change* in volume isn't — so modulation amounts are signed (manual p.21; The M8 Companion §2.4).

### Guitar parallel

How a note attacks (pick vs. tap vs. volume-knob swell) and decays (palm mute vs. full sustain) defines tone more than which guitar is plugged in. Same principle.

## Thread 3: Arrangement principle — A/B contrast

*Goal: make Project 1 have two clearly different sections.*

- [ ] Add a **B section** to Project 1. Like A, B is a *block of song rows spanning your tracks* — not a single cell. Scroll down past your Week 1 rows to the empty cells below and build B there:
	- The track you're **changing** gets a **new chain**: on its empty cell, `[EDIT]` inserts a chain, then `[EDIT]+[EDIT]` (double-tap) makes it a fresh empty chain to fill (manual p.11).
	- Tracks that **carry on unchanged** simply reuse their A chains in B's rows.
	- A track you want to **drop out** gets the empty/`FE` chain — the same dynamics trick from Week 1.
- [ ] B differs from A in **exactly one specific way**. Not "different everything."
- [ ] Pick one:
	- Drums drop out for the B section
	- One new melodic element enters that's absent from A
	- Filter on bass opens fully (LFO depth or chain transpose change)
	- Key transposes (use `TSP` column in Chain View — transposes in semitones)
- [ ] Commit to one. If you find yourself adding a second change, undo it.

---

## 🎯 Deliverable

- [ ] Project 1 now has A and B sections in Song View.
- [ ] Bass instrument has either a modulation-slot LFO or a table-based filter sweep — your choice.
- [ ] At least one instrument has a deliberate ADSR shape (not default).
- [ ] Song runs at least ~48 bars total — your ~32-bar A (≈8 song rows of a 4-bar chain) plus a B of ~16 bars (≈4 more rows). Measured in bars, not seconds: tempo moves the clock but not the arrangement — at 120 BPM your A alone is already ~64s.
- [ ] Render to WAV (Render View, manual p.47).
