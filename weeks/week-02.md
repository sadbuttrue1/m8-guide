# Week 2 — LFO to filter (modulation slots + tables)

**Goal:** Crack the modulation system. Learn the difference between **modulation slots** (instrument-level, the cleanest way to do LFOs) and **tables** (per-step automation, for things slots can't do).

**The big realization for this week:** the M8 has 4 dedicated modulation slots per instrument before you even touch tables. For "LFO to filter," the modulation slot is usually the right tool. Tables are for *stepped* automation, arpeggios, multi-stage envelopes — things slots can't do cleanly.

**Manual references:** Instrument Modulation View (p.18), Modulation Types: LFO (p.20–21), Table View (p.24), Macrosynth (p.52), Effect Command Help View (p.48).

---

## Thread 1: M8 technique — LFO to filter, two ways

### Method A: Modulation slot (recommended for LFO → filter)

This is the clean, idiomatic way.

- [ ] Open the bass instrument in Project 1. Make sure `TYPE` is `Macrosynth` (manual p.52).
- [ ] In Instrument View, the Macrosynth has a `FILTER` parameter section with `CUTOFF` and `RES`. Set `CUTOFF` to a low-ish value (~`40`) so there's room for the LFO to open it.
- [ ] Navigate `[SHIFT]+[UP]` from Instrument View → Instrument Modulation View (p.18).
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
- [ ] Compare: the slot LFO is smooth and continuous, the table is stepped and locked to your tic rate. **Use whichever fits the sound.**

### Tip

- Use [M8 table editor](https://twinside.github.io/m8table/) in your browser to experiment with table layouts before entering them on the device.

## Thread 2: Synthesis fundamental — Envelopes (ADSR)

*Goal: understand that envelope shape defines instrument identity more than oscillator does.*

The Instrument Modulation View also handles envelopes. The same modulation slots that can be LFOs can also be AHD, ADSR, DRUM, TRIG, or TRACKING envelopes (manual p.18–21).

- [ ] Open a fresh Wavsynth or Macrosynth instrument.
- [ ] In Instrument Modulation View, set `MOD1` to `ADSR ENVELOPE`, `DEST` to `VOLUME` (or `AMP`).
- [ ] Configure ADSR (manual p.20):
	- `ATK` (attack): time to reach `AMT`
	- `DEC` (decay): time to reach sustain
	- `SUS` (sustain): hold level while note plays
	- `REL` (release): time to fall to zero after note ends
- [ ] **Pluck**: ATK=00, DEC=20, SUS=00, REL=10. Hear: percussive, snappy.
- [ ] **Pad**: ATK=60, DEC=00, SUS=7F, REL=80. Same oscillator, completely different instrument.
- [ ] Realize: attack and release are doing 80% of the work in defining what something *sounds like*.

### Guitar parallel

How a note attacks (pick vs. tap vs. volume-knob swell) and decays (palm mute vs. full sustain) defines tone more than which guitar is plugged in. Same principle.

## Thread 3: Arrangement principle — A/B contrast

*Goal: make Project 1 have two clearly different sections.*

- [ ] Add a **B section** to Project 1. Build a new chain (Song View: navigate to empty column, `[EDIT]` then `[EDIT]+[EDIT]` to create new empty chain).
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
- [ ] ~60 second loop minimum.
- [ ] Render to WAV (Render View, manual p.47).
