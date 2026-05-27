# Week 4 — Retriggers, arpeggios, LFO concept

**Goal:** Third table-class technique. Project 1 reaches its ~60-bar / 15-row draft state (≈2 min at 120 BPM), but **doesn't finish this week** — finishing happens in Weeks 5–6 with proper mix and finalization.

This is the last pure-technique week before Phase 2 (Apply).

Both commands are documented in the manual: `ARP` (p.8, p.28) and `RET` (Sequencer FX Commands, p.69 — "Retrigger the current row with volume ramping"). The in-device **Effect Command Help view** is still the fastest way to confirm a command is valid for the current instrument type.

**Manual references:** Effect Command Help View (p.48), Sequencer FX Commands (p.69), Instrument FX Commands (p.75), Common Groove Examples (p.81).

---

## Thread 1: M8 technique — Retriggers and arpeggios

### Verify before using

- [ ] On any FX column in Phrase or Table View, press `[EDIT]+[UP or DOWN]` to open the **Effect Command Help view** (manual p.48).
- [ ] Browse the available commands. The view shows real-time which commands are valid for the current instrument type.
- [ ] Confirm `ARP` (arpeggio — definitely real, see p.8 example "ARP37").
- [ ] Confirm `RET` (retrigger, Sequencer FX Commands p.69) appears in the help view for your instrument type.

### Arpeggios

`ARP37` = arpeggio with first interval +3 semitones, second +7 semitones. Two digits = two intervals (manual p.8).

- [ ] On a melodic instrument in Project 1, add `ARP` to a chord-stab note.
- [ ] Try `ARP47` (major triad: +4 major third, +7 fifth), `ARP37` (minor triad: +3 minor third, +7 fifth), `ARP57` (sus4: +5 fourth, +7 fifth).
- [ ] `ARP` respects the scale set via `SCA` command (manual p.28) — useful for keeping arpeggios in key.

### Retriggers / rolls

- [ ] Use `RET` (retrigger) for snare rolls, glitched hat patterns, the staccato tracker feel. `RET XY` retriggers the current row with volume ramping over `Y` ticks (manual p.69).
- [ ] Add a retrigger to a snare hit somewhere in Project 1 (test a snare roll fill).
- [ ] Try it on a hi-hat for stuttery effect.

### Probability and fills (generative variation)

*See [Generative Toolkit Reference](../reference/generative.md) → #1 and #3 for the full toolkit context.*

The M8 has built-in randomization in Phrase View selection mode (manual p.15). This is your generative tool for late-stage humanization — patterns that feel alive without writing variations.

**Recipe — humanize a hi-hat pattern that feels rigid:**

- [ ] In Phrase View, position cursor over the hi-hat notes you want to vary.
- [ ] Enter selection mode: `[SHIFT]+[OPTION]`.
- [ ] **Important: note column must be selected** (not velocity or instrument column). The fill modes only work on note column.
- [ ] Try each of these in order:
	- `[OPTION]+[UP or DOWN]` — randomizes note values up/down (subtle pitch variation)
	- `[OPTION]+[LEFT]` — cycles through note fill modes
	- `[OPTION]+[RIGHT]` — randomizes note AND instrument triggers
- [ ] Exit selection mode. The result is committed.
- [ ] **If you don't like the result:** paste immediately (`[SHIFT]+[EDIT]`) to undo the fill action. This is per-manual: "When exiting selection mode after a fill action, perform a paste to undo."

**Common failure mode:** Trying these key combos on the velocity, instrument, or FX columns. They only work on the note column. Other columns just navigate normally.

**Try this on Project 1:**

- [ ] Find one rigid-feeling pattern in Project 1. Hi-hats are the usual culprit.
- [ ] Apply randomization. Render and listen.
- [ ] Keep if better, undo if worse. No commitment.

## Thread 2: Synthesis fundamental — LFOs as a concept

*Goal: realize the LFO from Week 2 and the table-based modulation from Week 2 are the same family.*

An LFO is anything that:
- Oscillates slowly
- Modulates a destination

Three properties: **rate** (FREQ), **depth** (AMT), **destination** (DEST).

- [ ] Take a Wavsynth instrument. In Instrument Modulation View, set up two LFO slots simultaneously:
	- `MOD1`: LFO → `PITCH`, slow rate, low amount = subtle vibrato
	- `MOD2`: LFO → `VOLUME`, faster rate, medium amount = tremolo
- [ ] Same LFO concept, different destinations = totally different effects.
- [ ] Now you understand: the table from Week 2's "Method B" was just a *manual, stepped LFO*. Same family.

## Thread 3: Arrangement principle — Designed transitions

*Goal: A→B should have a moment of motion, not just a cut.*

- [ ] Add **one designed transition** between A and B in Project 1. Pick one:
	- **Snare roll** — use the retrigger command from Thread 1
	- **Filter sweep** — automate `DJ filter` (DJF) in Mixer View, or use a table on a noise sweep instrument
	- **Pitch downsweep** on a bass note — use `PIT` over consecutive table rows
	- **Beat repeat / stutter** via retriggers
	- **Silence** — one bar of nothing right before B drops
- [ ] Commit to **one**. Don't stack five.

---

## 🎯 Deliverable — PROJECT 1 DRAFT COMPLETE

- [ ] Project 1 is now a ~60-bar / 15-row track (≈2 min at 120 BPM) with A section, B section, designed transition, dynamic elements.
- [ ] Render a rough WAV for reference (no mix or master pass yet).
- [ ] **Save and walk away.** Don't try to mix or polish — that's Weeks 5–6.
- [ ] Notice: this is the first time you've gotten a track to "draft complete" on M8 in this cycle. The hard part starts next week (mixing), but the writing is done.
