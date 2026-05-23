# Week 7 — Starter instrument library

**Goal:** Build 10 personal instruments you'll reuse forever. **No track this week.** Pure library-building.

This is the recovery week between Project 1 (shipped Week 6) and Project 2 (built Week 8). Use it for instrument design without performance pressure.

**Manual references:** Instrument View (p.16), Instrument Modulation View (p.18), Wavsynth (p.50), Macrosynth (p.52), Sampler (p.54), FM Synth (p.58), Hypersynth (p.60).

**Strategy:** before designing from scratch, reverse-engineer 1–2 existing instruments. Open the Community Starter Pack or laamaa's instruments and inspect how their parameters and modulation slots are set up. Then design your own.

---

## Thread 1: M8 technique — Build the 10 instruments

### Setup

- [ ] Decide a naming convention. Suggested: `EG-Bass-Sub`, `EG-Bass-Acid`, `EG-Lead-Pluck`. M8 NAME field is limited length — keep short.
- [ ] Save each via Instrument View → `SAVE`. They save to `/Instruments/` on the SD card.

### Bass instruments

- [ ] **Sub bass** — `EG-Bass-Sub`
	- TYPE: `Wavsynth` (sine) or `Macrosynth` (clean sine model)
	- MOD1: ADSR → VOLUME, ATK=00, DEC=20, SUS=60, REL=20
	- **Instrument EQ**: LOWCUT below 40Hz (pre-mixed for kick compatibility)
- [ ] **Acid bass** — `EG-Bass-Acid`
	- TYPE: `Macrosynth`, model with strong filter (Macrosynth Models, p.76)
	- FILTER CUTOFF mid (~`50`), RES high (~`B0`)
	- MOD1: LFO → FILTER CUTOFF, OSC=TRI, FREQ=08, AMT=40
	- Table: a few `PIT` slides built in
	- **Instrument EQ**: LOWCUT below 40Hz
- [ ] **FM bass** — `EG-Bass-FM`
	- TYPE: `FM Synth` (manual p.58)
	- Browse factory FM presets first. Modify for grit.
	- Add filter movement via MOD slot.
	- **Instrument EQ**: LOWCUT below 40Hz

### Lead/melodic instruments

- [ ] **Pluck lead** — `EG-Lead-Pluck`
	- TYPE: Macrosynth or Wavsynth, sawtooth
	- MOD1: ADSR → VOLUME, ATK=00, DEC=10, SUS=00, REL=08 (very short)
	- MOD2: ADSR → FILTER CUTOFF, ATK=00, DEC=30, SUS=00, REL=00, AMT=60
	- **Instrument EQ**: LOWCUT below 100–200Hz
- [ ] **Pad** — `EG-Pad`
	- TYPE: Macrosynth, soft model
	- MOD1: ADSR → VOLUME, ATK=60, DEC=00, SUS=7F, REL=A0
	- MOD2: LFO → FILTER CUTOFF, OSC=SIN, FREQ=20, AMT=20
	- **Instrument EQ**: LOWCUT below 200Hz, cut 200–500Hz to avoid mud
- [ ] **Stab/chord** — `EG-Stab`
	- TYPE: Macrosynth or `Hypersynth` (p.60) for built-in chords
	- Short attack, short decay, no sustain
	- **Instrument EQ**: LOWCUT below 150Hz

### Drum instruments

- [ ] **Kick** — `EG-Drum-Kick`
	- TYPE: `Sampler` with kick sample, OR `FM Synth` for FM kick
	- If FM: ADSR on pitch (high→low, fast) + ADSR on volume (short)
	- **Instrument EQ**: boost 60–80Hz, cut 200–400Hz
- [ ] **Snare** — `EG-Drum-Snare`
	- TYPE: Sampler with snare, OR Wavsynth noise layered with tonal
	- Tracking modulation: VELOCITY → VOLUME for natural feel
	- **Instrument EQ**: BELL boost ~200Hz, BELL boost ~5kHz
- [ ] **Closed hat** — `EG-Drum-Hat-C`
	- TYPE: Wavsynth (noise) or Sampler
	- ATK=00, DEC=04, SUS=00, REL=02
	- Tracking modulation: VELOCITY → VOLUME
	- **Instrument EQ**: LOWCUT 300Hz, HI.SHELF boost above 8kHz
- [ ] **Open hat** — `EG-Drum-Hat-O`
	- Same as closed but DEC=20, REL=10
	- **Instrument EQ**: same as closed hat

### Bonus

- [ ] **Noise sweep** — `EG-FX-Sweep`
	- TYPE: Wavsynth, noise
	- Long table or modulation slot automating filter cutoff closed → open
	- For transitions. Trigger once at end of A section.

### Cross-check by reverse-engineering

- [ ] Load the [Community Starter Pack](https://archive.org/download/ChipmusicResources/M8_Community_SD-card_Starter_Pack.7z) onto your SD card.
- [ ] Open a few instruments. See modulation slot setups. Borrow what you like.
- [ ] Open [laamaa's instruments](https://github.com/laamaa/m8i) too.

## Thread 2: Synthesis fundamental — FM basics

*Goal: stop being afraid of the FM Synth.*

- [ ] Open FM Synth instrument type (manual p.58). 4-op FM.
- [ ] Concept: one operator's frequency modulates another's. The modulator's frequency RATIO to the carrier defines timbre.
- [ ] Integer ratios (1:1, 1:2, 2:1) = harmonic, musical.
- [ ] Non-integer ratios (1:1.41) = clangy, bell-like, metallic.
- [ ] Play with operator ratios. Don't aim for mastery — just lose the fear.

## Thread 3: Generative exploration

*Library week is the right time for low-stakes feature exploration. No track pressure means you can play with things that didn't click before.*

See [Generative Toolkit Reference](../reference/generative.md) → #4 and #5 for full context. Pick one or more — not required to complete the library week.

### Option A: Table TIC modes (velocity- or note-mapped instruments)

This is what tables look like when they stop being step sequencers and become input-responsive instruments. Manual p.24, Table TIC Modes.

**Recipe — velocity-mapped drum hit:**

- [ ] Pick one of your starter drum instruments (kick or snare).
- [ ] In Instrument View, set `TABLE TIC` to `TICFD` (velocity map).
- [ ] Enter the instrument's table. Each row now corresponds to a velocity range.
- [ ] Row 00: leave default (lowest velocity hits)
- [ ] Row 04: add `PIT` with small positive value (medium velocity = slight up-pitch)
- [ ] Row 08: more `PIT` + slight volume boost
- [ ] Row 0C: significant `PIT` + add reverb send via FX command
- [ ] Now varying velocity on this drum produces real variations, not just volume changes.
- [ ] **Save as a new instrument** (e.g. `EG-Drum-Snare-V` for velocity-responsive version).

**Common failure mode:** forgetting to change `TABLE TIC`. Without setting it to `TICFD`/`TICFE`/`TICFC`, the table just plays linearly and none of the input mapping happens.

### Option B: Hypersynth (chord generation)

Manual p.60. Hypersynth is a different model from the synths you've used — it generates chords from single notes rather than producing one tone.

- [ ] Open an empty instrument slot. Set TYPE to `Hypersynth`.
- [ ] Spend 15–20 min exploring its parameters in Instrument View. Don't aim for a finished sound — just understand what each parameter does.
- [ ] Hypersynth respects the project's Scale (p.28). Set a scale on the track via `SCA` FX command, or globally via `SCG`.
- [ ] Play a single note in Phrase View. Hypersynth generates the chord around it.
- [ ] Try different scale settings. Hear how the same note produces different chords depending on the scale.
- [ ] **If you like it**: save as `EG-Hyper-Chord` or similar, add to library.
- [ ] **If not**: no worries, you've at least lost the fear of opening it.

**Common failure mode:** treating Hypersynth like Wavsynth (picking a wave shape). It's a chord-generation model — you're configuring how chords are built, not what waves they're made of. If a Hypersynth note sounds like a single tone, the chord parameters need tweaking.

### Option C: Sliced drum kit (one Sampler, multiple sounds)

The "drum rack" approach that Week 1 deliberately avoided. Worth exploring now that you have separate drum instruments working.

**Recipe — chromatic slice playback:**

- [ ] Find or make a multi-hit drum chain `.wav` (one file with kick, snare, hat, etc. concatenated). [DigiChain](https://brian3kb.itch.io/digichain) is a browser tool that builds these and writes M8-compatible slice markers.
- [ ] Open an empty instrument slot. TYPE: `Sampler`. SAMPLE: load the drum chain `.wav`.
- [ ] **Slice the sample.** Open the Sample Editor (from the Sampler's loaded sample) and create slice markers with the `SLICE:` process (manual p.56–57). Two modes you'll typically use:
	- `SLICE:AUTO` — slices on transients. Best when drum hits have clear attack peaks (most drum kits).
	- `SLICE:SILENC` — slices on silence gaps. Best when hits are separated by clear silence (one-shot recordings with padding).
	- (`SLICE:[0-128]` also slices into up to 128 evenly-distributed divisions, but for variable-length drum chains AUTO or SILENCE give better results.)
- [ ] **Trigger slices chromatically by note.** Back in Instrument View, set the Sampler's `SLICE` parameter to `FILE` — this plays the markers you just created, mapped to notes from `C-1` up (manual p.54, p.57). In Phrase View, different notes (e.g. `C-4`, `C#4`, `D-4`) now trigger consecutive slices. (A *numeric* `SLICE` value instead does equal-length slicing and ignores your AUTO/SILENCE markers.)
- [ ] Build a drum pattern using note variation instead of instrument-number variation — like playing a drum rack.

**When to use this vs separate Samplers (Week 1 approach):**
- Separate Samplers (Week 1) — simpler, more flexible per-sound, what most M8 users do.
- Sliced kit (this option) — saves instrument slots when you need many sounds and only have a few free slots. Also great for chopped breakbeats and vocal phrase manipulation.

**Common failure mode:** loading a sliced chain into a Sampler with `SLICE 00OFF` (default) and expecting it to behave like a drum kit. With `SLICE 00OFF`, the instrument just plays the whole file and transposes by note. You need slice markers (via AUTO or SILENCE) AND the `SLICE` parameter set to `FILE` so notes map to those markers.

## Mix focus this week: instruments are pre-mixed

Every instrument above has an instrument EQ pre-configured. This prevents 90% of future mix problems and means Week 8 builds tracks that mix faster.

Reference: [Mixing Reference](../reference/mixing.md) → Frequency carving recipes.

---

## 🎯 Deliverable

- [ ] 10 instruments saved to `/Instruments/EG-*` on SD card with consistent naming.
- [ ] Each has its instrument EQ pre-configured per its role.
- [ ] Render a 30-second demo cycling through each instrument (16 bars each, all 10 instruments in sequence). This is your reference for Week 8.
- [ ] No track this week.
