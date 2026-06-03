# Week 3 — Pitch slides, velocity, and Tracking

**Goal:** Two more techniques in your toolbox: pitch slides via the `PSL` command (plus instant pitch jumps via `PIT`), and velocity-driven modulation via the **Tracking** modulation type.

**Manual references:** Scale View (mentions `PIT`, p.28), Tracking modulation type (p.21), Sequencer FX Commands (`PSL`, p.71), Instrument FX Commands (`PIT`, p.75), Effect Command Help View (p.48).

---

## Thread 1: M8 technique — Pitch slides and velocity response

### Two pitch commands: `PSL` (slide) and `PIT` (jump)

They sound similar but do different things:

- `PSL XX` (Pitch Slide, sequencer FX, manual p.71) — **portamento**. The note *glides* from the previous note's pitch to the new one. `XX` is the slide time in ticks (6 ticks = one row at default settings).
- `PIT XX` (Pitch, instrument FX, manual p.75) — **instant** offset of the note pitch in semitones. `0C` = up an octave, `F4` = down an octave (values above `7F` count downward). No glide.

- [ ] Open the bass instrument in Project 1.
- [ ] In Phrase View, position cursor on an FX column next to a bass note. Press `[EDIT]+[UP or DOWN]` to open the **Effect Command Help view** (manual p.48). Find `PSL` and `PIT` and read their help text — it shows the decimal equivalent and what each value does.

### Build an acid-style bassline

**Use case:** "acid" = the TB-303 sound — a short looping bass pattern that stays mostly on ONE note. The interest comes from octave jumps, slides between a few chosen notes, and accents — not from melody.

**Recipe:**

- [ ] Write one bar of straight 8th-note bass hits, all `C-2` (rows 00, 02, 04, … with a short envelope so each hit is a pluck).
- [ ] **Octave jumps:** change 2–3 of the hits to `C-3`. Still one "note," but now it bounces.
- [ ] **Slides:** pick 1–2 spots where the pitch changes and put `PSL` on the *destination* note. Leave the instrument column empty on that row — the note then legatos into the slide instead of retriggering. Community consensus: `PSL06`–`07` is closest to the 303's slide feel.
- [ ] **Gating:** the 303 sequencer cuts notes short. Community trick: put `KIL03` on the step *before* any note you're NOT sliding into — it chokes the previous note just before the new one hits.
- [ ] **Accents:** raise the `V` column on 2–3 hits. Once you've set up Tracking (next section), route velocity → `CUTOFF` so accented hits open the filter — that's the 303 accent.
- [ ] **Scale-aware:** if you have a `SCA` (scale) command active on the track, `PIT` offsets quantize to the scale (manual p.28). Useful for jumps that aren't octaves.

**Common failure mode:** the slide sounds like two separate notes instead of one glide. Cause: the instrument number is re-entered on the slide row, which retriggers the envelope. Delete it — note + `PSL`, no instrument number.

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
- [ ] Bass uses `PSL` for at least one slide (and optionally `PIT` for an instant jump).
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
