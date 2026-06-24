# Week 7 — Starter instrument library

**Goal:** Build 10 personal instruments you'll reuse forever. **No track this week.** Pure library-building.

This is the recovery week between Project 1 (shipped Week 6) and Project 2 (built Week 8). Use it for instrument design without performance pressure.

**Manual references:** Instrument View (p.16), Instrument Modulation View (p.18), Wavsynth (p.50), Macrosynth (p.52), Sampler (p.54), FM Synth (p.58), Hypersynth (p.60).

**Strategy:** before designing from scratch, reverse-engineer 1–2 existing instruments. Open the Community Starter Pack or laamaa's instruments and inspect how their parameters and modulation slots are set up. Then design your own.

---

## Thread 1: M8 technique — Build the 10 instruments

### How every M8 instrument is built

Whatever the `TYPE`, every M8 instrument runs the same signal path — only the leftmost section changes per engine (Instrument View p.16, Modulation View p.18):

**Source → Filter → Amplifier → Mixer sends**, with **4 modulation slots** layered on top.

- **Source** — the engine-specific part: Wavsynth `SHAPE`, Macrosynth `SHAPE`/`TIMBRE`/`COLOR`, the FM operators, or a Sampler `SAMPLE`. This is the *only* part that differs between engines.
- **Filter** — `FILTER` type (`LP`/`HP`/`BP`/`BS`/`LP>HP`/ZDF), `CUTOFF`, `RES`. Identical on every engine.
- **Amplifier** — `AMP` plus `LIM` (`CLIP`/`SIN`/`FOLD`/`WRAP`) for level and drive.
- **Mixer sends** — `DRY`/`MFX`/`DEL`/`REV` out to the global effects.
- **Modulation (`MOD1`–`MOD4`)** — each slot is an `AHD ENV`, `ADSR ENV`, `DRUM ENV` (purpose-built for percussion), `LFO`, `TRIG ENV`, or `TRACKING` (maps note/velocity to a parameter), pointed at any `DEST` (p.20).

Every build below follows the same order — **pick the source, shape the amp envelope, set the filter, then add modulation.** Learn the Filter/Amp/Mixer/Mod sections once; they're the same on all 10 instruments.

### Setup

- [ ] Decide a naming convention. Suggested: `EG-Bass-Sub`, `EG-Bass-Acid`, `EG-Lead-Pluck`. M8 NAME field is limited length — keep short.
- [ ] Save each via Instrument View → `SAVE`. They save to `/Instruments/` on the SD card.

### Bass instruments

- [ ] **Sub bass** — `EG-Bass-Sub`
	- **Use case:** the foundation under everything — pure low-end weight, felt more than heard, with no harmonics to fight the kick or mids.
	- **Build it:**
		1. TYPE `Wavsynth`, SHAPE `SINE` (or `Macrosynth` `SINE TRIANGLE` for a touch more body, p.76) → a sine has almost no harmonics, so it stays out of the way of every other sound.
		2. `MOD1` `ADSR` → `VOLUME`, ATK=00 DEC=20 SUS=60 REL=20 → fast attack lands it on the beat; the moderate sustain lets notes hold their length.
		3. Leave the `FILTER` open on a pure sine → there are no harmonics to cut, so the filter has nothing to do.
		4. Keep `AMP` modest and avoid `LIM` drive → distortion *adds* harmonics, which is exactly what a clean sub must not have.
	- **Instrument EQ:** LOWCUT below 40Hz (pre-mixed for kick compatibility).
	- **Common failure mode:** adding drive or a bright shape grows harmonics that clash with the kick and muddy the low-mids. Keep it clean and let the kick own the transient.
- [ ] **Acid bass** — `EG-Bass-Acid`
	- **Use case:** squelchy 303-style bassline that moves under a beat — the filter sweep *is* the hook.
	- **Build it:**
		1. TYPE `Macrosynth`, SHAPE a saw model (`SAW SQUARE` or `SAW SYNC`, p.76) → a saw is harmonically rich, giving the resonant filter something to chew on.
		2. `FILTER` `LP`, CUTOFF low–mid (~`50`), RES high (~`B0`) → resonance is what makes the squelch; start cutoff low so the envelope has room to open *into*.
		3. `MOD1` `ADSR` → `CUTOFF`, ATK=00 DEC=30 SUS=00 AMT=60 → the per-note filter pluck. This envelope-on-cutoff is the core of the acid sound.
		4. `MOD2` `LFO` → `CUTOFF`, OSC=TRI FREQ=08 AMT=20 → a slow wobble layered over the pluck for bar-length movement.
		5. Table: a couple of `PIT` slide rows → the classic 303 glide between notes.
	- **Instrument EQ:** LOWCUT below 40Hz.
	- **Common failure mode:** RES too low → no squelch. CUTOFF parked too high → the envelope has nowhere to travel and the pluck disappears.
- [ ] **FM bass** — `EG-Bass-FM`
	- **Use case:** bass with bite and metallic harmonics a subtractive synth can't make — for DnB/neuro/electro where the bass needs *character*, not just weight.
	- **Build it:**
		1. TYPE `FM Synth` (p.58). Browse the factory FM presets and start from one you like → FM is far faster to modify than to build from a blank 4-op patch.
		2. Pick an `ALGO` with a clear carrier chain (e.g. `A>B>C>D`) and set operator `RATIO`s to integers (`1.00`, `2.00`) → integer ratios stay harmonic and musical; non-integer ratios go clangy (Thread 2 covers why).
		3. Add grit with operator feedback (`FBK`) or a higher modulator `RATIO`/`LEV` → feedback and deep modulation are where FM's edge comes from.
		4. `MOD1` `ADSR` → a filter `CUTOFF` or an operator `LEV` → an envelope on a modulator level makes the timbre *evolve* as the note decays, instead of sitting static.
	- **Instrument EQ:** LOWCUT below 40Hz.
	- **Common failure mode:** cranking modulation until it's pure noise — FM gets harsh fast. Back off modulator level until the pitch is clearly audible again.

### Lead/melodic instruments

- [ ] **Pluck lead** — `EG-Lead-Pluck`
	- **Use case:** short, percussive melodic stabs — arps, plucks, the rhythmic top-line that drives a track.
	- **Build it:**
		1. TYPE `Macrosynth` `PLUCKED` model (p.77) for instant plucked-string physics, or any saw model / `Wavsynth` `SAW` if you want to shape it by hand → `PLUCKED` does the work for you; a saw gives full manual control.
		2. `MOD1` `ADSR` → `VOLUME`, ATK=00 DEC=10 SUS=00 REL=08 → no sustain + fast decay = the percussive "pluck." Sustain at `00` is what keeps it short.
		3. `MOD2` `ADSR` → `CUTOFF`, ATK=00 DEC=30 SUS=00 AMT=60 → a filter snapping shut as the note decays adds the bright-to-dark pluck timbre on top of the volume shape.
		4. `FILTER` `LP`, CUTOFF mid → gives that cutoff envelope somewhere to travel from.
	- **Instrument EQ:** LOWCUT below 100–200Hz.
	- **Common failure mode:** SUS above `00` → the note rings instead of plucking. If it sounds like a pad, your sustain is too high.
- [ ] **Pad** — `EG-Pad`
	- **Use case:** sustained harmonic bed that fills space behind the lead and glues a section together.
	- **Build it:**
		1. TYPE `Macrosynth`, a soft/smooth model (e.g. `MORPH`, p.76) → pads want a mellow source, not a buzzy saw.
		2. `MOD1` `ADSR` → `VOLUME`, ATK=60 DEC=00 SUS=7F REL=A0 → slow attack + full sustain + long release = it swells in and fades out instead of stabbing.
		3. `MOD2` `LFO` → `CUTOFF`, OSC=SIN FREQ=20 AMT=20 → slow filter drift so the pad breathes instead of sitting still.
		4. `FILTER` `LP`, CUTOFF mid-low → keeps the pad *behind* the lead, not on top of it.
	- **Instrument EQ:** LOWCUT below 200Hz, cut 200–500Hz to avoid mud.
	- **Common failure mode:** attack too fast → the pad stabs and competes with the lead. If you can hear the note "start," lengthen ATK.
- [ ] **Stab/chord** — `EG-Stab`
	- **Use case:** rhythmic chord hits — house/garage stabs, the harmonic punctuation between melodic phrases.
	- **Build it:**
		1. TYPE `Macrosynth` (play a chord across tracks) or `Hypersynth` (p.60) to generate the chord from a single note → Hypersynth saves you voicing chords by hand (see Thread 3 Option B).
		2. `MOD1` `ADSR` → `VOLUME`, ATK=00 DEC=18 SUS=00 REL=10 → short attack, short decay, no sustain = a tight stab, not a held chord.
		3. `FILTER` `LP`, CUTOFF mid with a little `RES` → adds a "pluck" snap to the chord's front edge.
		4. Add a short `REV` or `DEL` send → stabs sit better with a touch of tail behind them.
	- **Instrument EQ:** LOWCUT below 150Hz.
	- **Common failure mode:** long decay/sustain → stabs blur into each other and lose their rhythmic punch.

### Drum instruments

- [ ] **Kick** — `EG-Drum-Kick`
	- **Use case:** the transient + weight that anchors the whole beat.
	- **Build it:**
		1. TYPE `Sampler` with a kick sample (simplest), OR `FM Synth` for a synthesized kick you can tune → a sample is fastest; FM lets you dial pitch and punch exactly.
		2. If synthesized: `MOD1` `DRUM ENV` → `PITCH`, a fast high→low sweep → the pitch drop *is* the "thump." The `DRUM ENV` is purpose-built for percussion (p.20) — sharper than an ADSR for this.
		3. `MOD2` `DRUM ENV` → `VOLUME`, short → the body envelope that gives the kick its length.
		4. Keep it mono and short → a long kick tail eats the headroom the bass needs.
	- **Instrument EQ:** boost 60–80Hz, cut 200–400Hz.
	- **Common failure mode:** pitch sweep too slow → you hear a "boing" instead of a thump. Speed up the pitch envelope's decay.
- [ ] **Snare** — `EG-Drum-Snare`
	- **Use case:** the backbeat crack — a noise body plus a tonal "snap."
	- **Build it:**
		1. TYPE `Sampler` with a snare (simplest), OR layer two `Wavsynth` instruments: one `NOISE` for the body, one `SINE`/`TRIANGLE` for the tonal snap → real snares are noise + a tuned shell, and layering recreates that.
		2. `MOD1` `DRUM ENV` (or `ADSR`) → `VOLUME`, short decay, no sustain → a snare is a fast burst, not a sustained tone.
		3. `MOD2` `TRACKING` → `VOLUME`, SRC `VELOCITY` → ghost notes at low velocity, hard backbeats at high velocity = a human-feeling snare (p.20).
		4. `FILTER` `BP` or `HP` on the noise layer → focuses the crack in the upper-mids.
	- **Instrument EQ:** BELL boost ~200Hz (body), BELL boost ~5kHz (snap).
	- **Common failure mode:** all noise, no tone → a "pfft" with no crack. Add or raise the tonal layer / the ~200Hz body.
- [ ] **Closed hat** — `EG-Drum-Hat-C`
	- **Use case:** the high-frequency timekeeper that drives the groove.
	- **Build it:**
		1. TYPE `Wavsynth` `NOISE` (or `Sampler`) → hats are filtered noise, and Wavsynth noise needs no sample to load.
		2. `MOD1` `DRUM ENV`/`ADSR` → `VOLUME`, ATK=00 DEC=04 SUS=00 REL=02 → a very short envelope = the closed "tick."
		3. `MOD2` `TRACKING` → `VOLUME`, SRC `VELOCITY` → velocity variation is what makes hi-hats groove instead of machine-gun.
		4. `FILTER` `HP`, CUTOFF high → removes the low rumble so the hat sits up top.
	- **Instrument EQ:** LOWCUT 300Hz, HI.SHELF boost above 8kHz.
	- **Common failure mode:** decay too long → a closed hat that rings like an open one. Shorten DEC/REL.
- [ ] **Open hat** — `EG-Drum-Hat-O`
	- **Use case:** the off-beat lift that answers the closed hat.
	- **Build it:**
		1. Start from a *copy* of the closed hat → the two should share a timbre and differ only in length, so the pair reads as one kit.
		2. Lengthen the envelope: DEC=20 REL=10 → the longer tail is the only thing that makes it "open."
		3. (optional) A `TRIG ENV` choke so a closed hat cuts the open hat's tail → real hi-hats can't ring while the pedal closes (p.20).
	- **Instrument EQ:** same as closed hat.
	- **Common failure mode:** giving it a different timbre from the closed hat → the two stop sounding like the same instrument. Copy first, then only change length.

### Bonus

- [ ] **Noise sweep** — `EG-FX-Sweep`
	- **Use case:** transition riser/faller — covers the seam between sections.
	- **Build it:**
		1. TYPE `Wavsynth`, SHAPE `NOISE`.
		2. Automate `CUTOFF` closed→open with a long `AHD ENV` (long ATK), or a table ramp spread over many rows → the slow filter open is the "whoosh."
		3. `FILTER` `BP` for a wind-like character, or `LP` for a fuller sweep.
		4. Trigger it once at the end of a section → it's a one-shot transition, not a loop.
	- **Common failure mode:** ramp too short → a quick "pfft" instead of a building riser. Spread the cutoff move over more rows/ticks.

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
- [ ] Render a ~16-bar / ~4-row demo (≈30s at 120 BPM) cycling through all 10 instruments in sequence — roughly a bar or two each. This is your reference for Week 8.
- [ ] No track this week.
