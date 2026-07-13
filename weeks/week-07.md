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
		5. Table: this is where the 303 glide and pitch moves live. Two commands handle pitch, and they do different jobs:
			- `PIT XX` — offsets the note pitch in **semitones** (p.75): `PIT 0C` throws the row up an octave, and the upper half of the range (`80`–`FF`) offsets *downward*. It's a stepped jump, not a slide, and it's scale-quantized (p.28) so the offset snaps to the track's scale. Drop a `PIT` row or two for an octave jump or a quick accent-wail into the next note.
			- `PSL XX` — **pitch slide** (portamento) is the command that actually makes the smooth 303 glide *between* notes. The value is in *ticks* (p.71) — higher = slower glide. The community-standard acid glide is around `PSL 06`–`07`, with the instrument set to **legato (no retrigger)** so consecutive notes slide into each other instead of re-plucking.
			- **Where to put `PSL`:** it slides *from* the previous note, so place it the moment the *destination* note triggers — on the **same row as the note you're sliding to**, not the starting note. Two options: in the **phrase**, put `PSL` on the target note's row and drop the instrument number on that row so it legatos instead of re-plucking (slides only the notes you choose — the realistic 303 way); or in the **instrument table**, put `PSL` on **row `00`** so every note this instrument plays glides automatically. When editing the value, the help text at the bottom of the screen shows **how many steps the slide will last** — bump it until that matches the gap between your two notes. For a 303-accurate line, keep `PSL` in the table and put `KIL03` on the step *before* any note you *don't* want to glide into, so only tied/accent notes slide.
	- **Instrument EQ:** LOWCUT below 40Hz.
	- **Common failure mode:** RES too low → no squelch. CUTOFF parked too high → the envelope has nowhere to travel and the pluck disappears.
- [ ] **FM bass** — `EG-Bass-FM`
	- **Use case:** bass with bite and metallic harmonics a subtractive synth can't make — for DnB/neuro/electro where the bass needs *character*, not just weight.
	- **Build it (from a blank patch — no presets needed):**
		The whole sound is really just **two operators**: a *carrier* you hear, and a *modulator* that vibrates the carrier's pitch fast enough to turn into timbre. Set those two, silence the other two.
		1. TYPE `FM Synth` (p.58). Leave `ALGO` on the first one, `A>B>C>D` (`00`) — a single 4-operator chain. The arrows mean "modulates," so the **last operator `D` is the carrier** (the one you actually hear) and **`C` is its modulator**.
		2. **Carrier — operator `D`:** shape `SIN`, `RATIO 1.00`, `LEV` full. This is the fundamental: `RATIO 1.00` plays the note you press, `2.00` an octave up, `0.50` an octave down (p.58).
		3. **Modulator — operator `C`:** shape `SIN`, `RATIO 1.00`. Its `LEV` is the **FM amount (index)** — at `00` you hear a pure sine; raise it and harmonics pile on. Set it around a third up for now (this becomes the envelope's peak in step 6).
		4. **Silence `A` and `B`:** set both their `LEV` to `00` so only the `C>D` pair sounds. You now have a clean 2-operator FM bass.
		5. **Choose the timbre with the modulator `RATIO`.** Integer ratios stay harmonic and musical: `1.00` = round and warm, `2.00`/`3.00` = brighter and more hollow. A non-integer ratio (e.g. `1.41`) goes clangy and metallic — great for neuro/DnB bite, wrong for a clean sub (Thread 2 covers why).
		6. **Make it evolve — the move that turns a static FM tone into a *bass*.** In the Modulation view (p.18) set `MOD1` to `ADSR`: ATK=00 DEC=30 SUS=00. Then in operator **`C`**'s `MOD` slot, route `MOD1` → `LEV`. C's level now snaps up on the attack and decays back toward `00` — the `LEV` destination sweeps the operator from `00` up to its set level (p.58) → the FM brightness *blooms, then fades to a near-pure tone*. That bright "pock" over a clean tail is the signature DX/FM bass shape. (Raise `SUS` if you want the harmonics to stay through held notes.)
		7. **Add grit (optional):** raise operator `C`'s `FB` (feedback), or route a second envelope `MOD2` `ADSR` → C's `FBK`. Feedback frays the sine into a metallic edge a subtractive synth can't make.
	- **Instrument EQ:** LOWCUT below 40Hz.
	- **Common failure mode:** cranking the modulator `LEV` until it's pure noise — FM gets harsh fast; back it off until the pitch is clearly audible again. If it sounds detuned or bell-like when you didn't want that, your `RATIO`s aren't landing on whole integers.

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
		1. **Source (pick one) — a snare is noise + a tuned shell, so you want both parts:**
			- `Sampler` with a snare sample → simplest.
			- Two `Wavsynth` instruments layered — one `NOISE` body, one `SINE`/`TRIANGLE` tonal snap. M8 has no per-instrument layering, so "layer" here means putting the two on two tracks and triggering the same note on the same phrase row → this makes the noise-plus-shell model *visible*, at the cost of a second track.
			- One `FM Synth` → the efficient single-instrument route, consistent with the kick above. Set `ALGO` to the last one (additive mode: all four operators run in parallel to the output, p.58). Give one operator a maxed `FB` for the noise body — cranking feedback all the way *is* how M8 FM generates noise — and a second operator a `SINE`/`CLICK` tuned via `RATIO` to sit ~200Hz for the tonal snap; balance the two with `LEV`. M8's own factory clap is this exact trick (maxed-out FM noise).
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
		3. (optional) **`TRIG ENV` choke** so a closed hat cuts the open hat's tail → real hi-hats can't ring while the foot closes the pedal. A `TRIG ENV` is an AHD envelope (`ATK`/`HOLD`/`DEC`) that fires when *another* instrument or track plays — not the one it lives on — and it's **bipolar**, so it can push its `DEST` *down* as well as up (p.20–21). That negative push is the choke:
			- On the **open hat**, add a `MOD` slot → `TRIG ENV`, `DEST` `VOLUME`, with a **negative `AMT`** big enough to slam the volume to zero.
			- Set `SRC` to the **closed hat's instrument number** (`00`–`7F`), or to its **track** (`80`–`87` = Tracks 1–8) so *anything* on that lane chokes the open hat.
			- Shape the duck with `ATK 00` (instant cut), then enough `HOLD`/`DEC` that the tail stays killed until the open hat would have died on its own.
			- Now every closed-hat hit ducks the ringing open hat to silence, exactly like a real pedal closing.
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

*Goal: stop being afraid of the FM Synth. Do this before (or alongside) the FM bass build above — it's the same two-operator patch, explored instead of aimed at a result.*

- [ ] Open FM Synth instrument type (manual p.58). 4-op FM, 12 algorithms.
- [ ] Concept: one operator (the **modulator**) bends another's (the **carrier**) frequency fast enough to become *timbre* instead of audible vibrato. The modulator's `RATIO` to the carrier defines *which* harmonics appear; its `LEV` (the FM *index*) defines *how strong* they are.
- [ ] Build the bare 2-op patch from the FM bass recipe: `ALGO 00`, carrier `D` (`SIN`, `RATIO 1.00`), modulator `C` (`SIN`), `A`/`B` silenced (`LEV 00`). Now you have just one knob — C's `RATIO` — to hear what FM actually does.
- [ ] Sweep C's `RATIO`: integer ratios (`1.00`, `2.00`, `3.00`) = harmonic and musical; non-integer (`1.41`) = clangy, bell-like, metallic.
- [ ] Sweep C's `LEV` from `00` up: `00` = pure sine, higher = more harmonics. This is the FM *index* — the single most important FM control.
- [ ] Learn the routing wrinkle: to make timbre move over time you *don't* point an envelope at a global `DEST`. You set up `MOD1` as an `ADSR` in the Modulation view (p.18), then assign it *inside an operator's* `MOD` slot — e.g. operator `C` → `LEV` (p.58). That's exactly the FM bass "make it evolve" step, and it's the one thing that works differently from every other engine.
- [ ] Don't aim for mastery — just lose the fear.

## Thread 3: Generative exploration

*Library week is the right time for low-stakes feature exploration. No track pressure means you can play with things that didn't click before.*

See [Generative Toolkit Reference](../reference/generative.md) → #4 and #5 for full context. Pick one or more — not required to complete the library week.

### Option A: Table TIC modes (velocity- or note-mapped instruments)

This is what tables look like when they stop being step sequencers and become input-responsive instruments. Manual p.24, Table TIC Modes.

**Where to find it (this is the part people miss):** there is no separate "TIC type" menu. `TABLE TIC` is a single numeric field in Instrument View — the one you normally leave at `01` (one tick per table row), `02` for two ticks, and so on (p.23). The special modes live at the *top* of that same field: dial the value all the way up past the tick-count range to hit `FC` = octave map, `FD` = velocity map, `FE` = note map, `FF` = 200 Hz (p.24). So "set it to `TICFD`" really means "scroll the `TABLE TIC` value up to `FD`" — the M8 doesn't show these as named options, just as the high hex values of the field. (The `TICxx` spelling is the FX-command form: dropping `TICFD` in a phrase or table FX column does the same thing and overrides the instrument's field — p.23.)

**Recipe — velocity-mapped drum hit:**

- [ ] Pick one of your starter drum instruments (kick or snare).
- [ ] In Instrument View, dial the `TABLE TIC` value up to `FD` (velocity map).
- [ ] Enter the instrument's table. Each row now corresponds to a velocity range.
- [ ] Row 00: leave default (lowest velocity hits)
- [ ] Row 04: add a small `FIN` (medium velocity = a touch tighter/higher — sub-semitone, so it doesn't detune)
- [ ] Row 08: more `FIN` + a slight volume boost via a `VOL` FX command (see note below) + a little `CUTOFF` to open the tone
- [ ] Row 0C: `FIN` at its top + a short `REV` send via FX command → the hardest hits read as "hit harder" through *tone*, not pitch
- [ ] Now varying velocity on this drum produces real variations, not just volume changes.
- [ ] **Save as a new instrument** (e.g. `EG-Drum-Snare-V` for velocity-responsive version).

**Why `FIN`, not `PIT`, on a tuned drum:** `PIT` moves in whole **semitones** and is **scale-quantized** (p.28), so on a snare (whose tuned shell is recognizable) a hard hit jumps to an obviously different pitch and just sounds *detuned*. `FIN` offsets by less than a semitone (p.75), giving lifelike variation without the "wrong note" effect. Carry most of the hard-vs-soft difference in **tone** (`CUTOFF`, a `REV`/`DEL` send) rather than pitch. On a non-tuned source (noise hat, FX) big `PIT` jumps are fair game.

**On table volume — the `V` column is *relative*, not a boost:** the table's `V` (volume) column is *multiplied* by the phrase's `V` (p.24), so it can only scale the incoming level down/up proportionally — it can't add a fixed amount on its own. To actually *offset* the level on a row, use the **`VOL XX` FX command** ("offset the instrument volume", p.75) in one of the three FX columns. That's why the steps above put a volume *boost* in an FX column rather than in the `V` column.

**Common failure mode:** forgetting to change `TABLE TIC`, or looking for a labeled "type" that isn't there. Until you raise the `TABLE TIC` value into the `FC`/`FD`/`FE` range, the table just plays linearly at that tick speed and none of the input mapping happens.

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
