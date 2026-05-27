# Week 3 — Pitch slides, velocity, and Tracking

**Goal:** Two more techniques in your toolbox: pitch slides via the `PIT` command (real, documented), and velocity-driven modulation via the **Tracking** modulation type.

**Manual references:** Scale View (mentions `PIT`, p.28), Tracking modulation type (p.21), Sequencer FX Commands (p.69), Instrument FX Commands (p.75), Effect Command Help View (p.48).

---

## Thread 1: M8 technique — Pitch slides and velocity response

### Pitch slides via `PIT`

The `PIT` command is a real M8 effect command (confirmed in Scale view section, manual p.28). It works as a pitch effect that can be quantized to the current scale.

- [ ] Open the bass instrument in Project 1.
- [ ] In Phrase View, position cursor on an FX column next to a bass note. Press `[EDIT]+[UP or DOWN]` to open the **Effect Command Help view** (manual p.48).
- [ ] Find `PIT` in the command list. The help view shows the parameter range and behavior.
- [ ] Build an acid-style bassline by alternating notes and `PIT` slides:
	- Row 00: `C-2`, FX1: `PIT` with positive value (slide up)
	- Row 04: `C-2`, FX1: `PIT` with negative value (slide down)
- [ ] Experiment with `PIT` values. Use the in-device help text at the bottom of the screen — it shows the decimal equivalent and what the value does.
- [ ] **Scale-aware:** if you have a `SCA` (scale) command active on the track, `PIT` slides quantize to the scale (manual p.28). Useful for keeping slides in key.

### Velocity-driven modulation via Tracking

This is where the M8 gets clever about humanization. Instead of manually setting volumes per step, you assign **Tracking** modulation that maps note velocity to any parameter.

- [ ] Open the hi-hat instrument (Sampler with a hat sample, or Wavsynth with noise + short envelope).
- [ ] Go to Instrument Modulation View (`[SHIFT]+[UP]` from Instrument View).
- [ ] Configure an unused MOD slot:
	- TYPE: `TRACKING`
	- `SRC`: `VELOCITY` (or `VELOCITY TAKEOVER` to disable velocity affecting volume directly)
	- `DEST`: pick a parameter — try `VOLUME`, `FILTER CUTOFF`, or `PITCH` for variety
	- `LVAL`: lowest source value (e.g. `00`)
	- `HVAL`: highest source value (e.g. `7F`)
- [ ] Reference: Tracking modulation, manual p.21.
- [ ] Back in Phrase View, vary the `V` column on hi-hat hits: some at `64` (default), some at `20`, some at `7F`. The Tracking modulation now translates velocity into your chosen parameter changes.
- [ ] **Ghost notes for snare:** same approach. Set Tracking on snare → velocity → volume. Then put low-velocity hits (e.g. `V=10`) between the main hits.

### Why this matters

Velocity ramping via tables (manual command in `V` column or table) works, but **Tracking is more flexible**: same velocity column can drive multiple parameters at once if you set up multiple MOD slots. This is how M8 patches feel alive without writing a million variations.

## Thread 2: Synthesis fundamental — Filters

*Goal: hear what filter cutoff and resonance actually do.*

- [ ] Open a Macrosynth bass instrument. Make sure `FILTER` section is active.
- [ ] Set `RES` (resonance) to a low value (~`20`).
- [ ] Manually sweep `CUTOFF` from `00` to `FF` while a note plays. Listen: muffled → bright → bright with the high harmonics audible.
- [ ] Now increase `RES` to ~`A0`. Sweep `CUTOFF` again. Hear the "vocal," whistling quality at the cutoff point. That's resonance.
- [ ] Macrosynth filter modes — check the Macrosynth reference (manual p.52) for the available filter types and how to switch between LP/HP/BP if available on the model.

### Guitar parallel

Cutoff is where the wah pedal points; resonance is how "vocal" the wah sounds. The lowpass filter is your tone knob.

## Thread 3: Arrangement principle — Add/remove with intent

*Goal: every element change should have a reason.*

- [ ] In Project 1: add ONE new element to the B section.
- [ ] Before adding, answer: **what does this make space for, or what does it replace?**
- [ ] Then remove ONE element from late A.
- [ ] Before removing, answer: **what now has room to breathe?**
- [ ] If either answer is "nothing" or "I don't know," the change is wrong. Undo and try a different one.
- [ ] This is the discipline: every arrangement decision is a tradeoff.

---

## 🎯 Deliverable

- [ ] Project 1 has intentional element changes between A and B.
- [ ] Bass uses `PIT` for at least one slide.
- [ ] Hats or snare have a Tracking modulation responding to velocity.
- [ ] ~52 bars / ~13 rows long (rows = 4-bar chains).
- [ ] Render to WAV (Render View, manual p.47).

---

## 🎛️ Mix focus this week: kick & bass relationship

The most important relationship in any electronic mix. Get this right and 50% of mixing is done.

Reference: [Mixing Reference](../reference/mixing.md) → Scope A, Steps 1–2.

- [ ] Solo kick. Set its volume to peak around -6dBFS in Mixer View.
- [ ] Unmute bass. Listen with kick. Can you hear both distinctly?
- [ ] If they fight, do one of these (in order):
	- **Easiest**: lower bass volume
	- **Better**: LOWCUT on bass below 40Hz (Instrument EQ, p.32). Removes subsonic conflict.
	- **Best**: TRIG envelope side-chain on bass, ducked by kick. See Mixing Reference → Tool 3 for full setup.
- [ ] Verify on headphones AND M8 speakers. Both elements audible on both systems = win.
