# Generative Toolkit Reference

The M8 has a family of generative features. They serve different musical purposes — they're not interchangeable. This page documents each one with a concrete recipe, a clear use case, and the most common failure mode.

**Strategy:** if a generative feature isn't clicking, you're probably using it for the wrong use case. Match the technique to the goal.

**Manual references:** Phrase View shortcuts (p.15), LFO modulation type (p.20–21), Table View + TIC modes (p.24), Hypersynth (p.60).

---

## 1. Phrase View randomization (selection mode)

**Use case:** You have a hi-hat or percussion pattern that feels too rigid. You want humanization without writing every variation by hand.

**Recipe:**
- [ ] In Phrase View, position cursor over the notes you want to vary.
- [ ] Enter selection mode: `[SHIFT]+[OPTION]`.
- [ ] Make sure the **note column** is selected (not velocity/instrument/FX).
- [ ] Apply one of:
	- `[OPTION]+[UP or DOWN]` — randomize note value up or down
	- `[OPTION]+[LEFT]` — cycle through note fill modes
	- `[OPTION]+[RIGHT]` — randomize note AND instrument triggers
- [ ] Exit selection mode. The result is now committed to the phrase.
- [ ] **If you don't like it:** immediately paste (`[SHIFT]+[EDIT]`) to undo the fill action.

**Common failure mode:** Trying to randomize the volume or FX columns instead of the note column. The fill modes only work on the note column. Other columns just navigate normally with those keys.

**When to reach for it:** end of a writing session, when patterns feel locked. 30 seconds of randomization vs 10 minutes of manual variation.

---

## 2. Random / Drunk LFO shapes

**Use case:** You want filter movement (or any modulation) that never repeats exactly the same way. Evolving textures, pads that breathe, sound design that doesn't loop predictably.

**Two distinct shapes:**
- **RANDOM** — each LFO cycle picks a new random value. Stepped, unpredictable, jumpy.
- **DRUNK** — random walk. Each new value is a small offset from the previous one. Smoother, organic, never returns exactly.

**Recipe — evolving pad:**
- [ ] Open a pad instrument. Go to Instrument Modulation View (`[SHIFT]+[UP]` from Instrument View).
- [ ] Set `MOD2` (keep MOD1 for envelope):
	- TYPE: `LFO`
	- `DEST`: `FILTER CUTOFF`
	- `OSC`: `DRUNK`
	- `TRIG`: `FREE` (keep walking across notes)
	- `FREQ`: slow (try `20–40`)
	- `AMT`: moderate (`30–50`)
- [ ] Hold a note. The filter wanders.
- [ ] Try the same with `OSC: RANDOM`. Hear the difference: jumpy vs continuous.

**Tick-rate variants:** add T to the shape (`RANDOM T`, `DRUNK T`). Frequency now runs in ticks instead of 16th notes — much faster modulation, useful for textural sound design rather than slow movement.

**Common failure mode:** Setting AMT too high. Random/Drunk at high amounts sounds chaotic. Subtle (`20–40`) is usually better than dramatic.

**When to reach for it:** anywhere a static parameter should feel alive — filter, pitch (subtle vibrato that wanders), volume (organic dynamics), pan (drifting stereo image).

---

## 3. Probability and fill modes (combined with randomization)

**Use case:** "Every 4th time the pattern loops, maybe the snare has an extra ghost note." Subtle per-cycle variation without manual programming.

**Recipe:**

The M8's probability mechanism lives partly in Phrase View selection mode (see #1 above) and partly via FX commands you find in the in-device **Effect Command Help view** (`[EDIT]+[UP or DOWN]` on any FX column).

- [ ] Open Effect Command Help. Browse for probability-related commands available for your instrument type.
- [ ] The commands available depend on instrument type — the help view is the source of truth.
- [ ] Alternative approach: use the note-fill randomization from #1 on duplicate copies of your pattern, then use chain transpose / phrase variation to alternate between them.

**Common failure mode:** Expecting one universal probability command. The M8 has multiple ways to get probabilistic behavior depending on instrument type and what you're trying to vary. Use the Effect Command Help view to discover what's available right now.

**When to reach for it:** late-stage humanization, when arrangement is locked but patterns still feel too predictable.

---

## 4. Table TIC modes (note/velocity/octave mapping)

This is where tables stop being "step sequencers" and become "input-responsive instruments."

**Use case:** "I want the same instrument slot to play different sounds depending on which note I trigger, or how hard I trigger it, or what octave I'm in."

Manual: Table TIC Modes, p.24.

- `TIC00` — increments table row each time the instrument is triggered (one row per note hit)
- `TIC01 TO TICFB` — standard tick-per-row playback
- `TICFC` — **Octave Map**: maps playing octave to table row
- `TICFD` — **Velocity Map**: maps velocity to table row
- `TICFE` — **Note Map**: maps note value to table row (use `HOP00` on row `0C` to limit to 12 notes/octave)
- `TICFF` — increments at 200Hz (super fast)

**Recipe — velocity-mapped drum hits:**
- [ ] Set up a Sampler instrument. Load one drum sample.
- [ ] In Instrument View, set `TABLE TIC` to `TICFD` (velocity map).
- [ ] Enter the instrument's table. Each row now corresponds to a velocity range.
- [ ] In row `00`: leave default (lowest velocity)
- [ ] In row `04`: add a `PIT` command to slightly pitch up (medium velocity, slight up-pitch)
- [ ] In row `08`: pitch up more + slight volume boost
- [ ] In row `0C`: pitch up significantly + add reverb send via FX command
- [ ] Now varying velocity on this drum produces actual variations, not just volume changes.

**Recipe — note-mapped sample kit:**
- [ ] Set `TABLE TIC` to `TICFE` (note map).
- [ ] Add `HOP00` on row `0C` to limit to 12 notes/octave (per manual instructions).
- [ ] Each row of the table now corresponds to a note. Use `INS` commands (or instrument-changing FX commands) per row to play different sounds per note.
- [ ] Result: one "instrument" slot, but plays a drum kit mapped to notes.

**Common failure mode:** Forgetting to set the `TABLE TIC` mode. The table works normally until you change TIC to one of the special FC/FD/FE values. Without that, none of the input mapping happens.

**When to reach for it:** building instruments that respond expressively to playing input. Critical for finger-drum-style kits and for sample chains.

---

## 5. Hypersynth

**Use case:** You want musical chord progressions or scale-aware playback without writing every voice individually. Built for harmonic content (pads, ambient, chord stabs).

Manual: Hypersynth, p.60. The Hypersynth section is dense — budget 30 min to explore it on its own.

**General approach (verify exact parameters in-device):**
- [ ] Set an instrument's TYPE to `Hypersynth`.
- [ ] Hypersynth uses the project's Scale (Scale View, p.28) and supports the `SCG` global scale command.
- [ ] Explore the instrument-level parameters via Instrument View — chord type, voicing, scale degree.
- [ ] Play a single note in Phrase View. Hypersynth generates the chord around that note based on its settings.

**Common failure mode:** Treating Hypersynth like Wavsynth/Macrosynth. It's a different model — you're not picking a wave shape, you're configuring chord generation. If a Hypersynth note sounds like a single tone instead of a chord, the chord parameters aren't set up.

**When to reach for it:** ambient/harmonic tracks where you want progressions without programming every voice. Also great for stab/chord instruments in dancier music.

---

## 6. Tables as arpeggiators / generative sequencers

**Use case:** One note in Phrase View should trigger an evolving phrase — arpeggio, melodic riff, or sequence of pitches/effects that plays automatically.

This is what tables were designed for. Per the manual (p.24): "Tables are little sequencers that play alongside instruments... an incredibly powerful tool to transform instruments and compositions, from arpeggios and volume slides to multi-stage envelopes and effects."

**Recipe — generative arpeggio:**
- [ ] On a melodic instrument, set `TABLE TIC` to a low tick value like `02` or `04` (faster table playback than the phrase).
- [ ] Enter the instrument's table.
- [ ] In the `N` (transpose) column, write a sequence of values: `00`, `04`, `07`, `0C`, `07`, `04`, `00`, `-05` (this is a major-7th-up arp and back).
- [ ] In Phrase View, trigger ONE note on this instrument. The table plays the arp.
- [ ] Use `HOP` commands in the table to loop a subsection or jump around — creates evolving rather than just-repeating arps.

**Recipe — polyrhythmic interest:**
- [ ] On a second instrument's table, do the same but with a DIFFERENT number of rows (use `HOP00` to loop after, say, row 7 instead of 16).
- [ ] Trigger both instruments simultaneously in the phrase. The two arps loop at different rates, creating polyrhythms.

**Common failure mode:** Setting TABLE TIC too slow. If TIC matches the phrase tick rate, the table feels like just a constant note, not a sequence. Set it 2–4x faster than phrase rate for arp-feel.

**When to reach for it:** generative melody composition. Write fewer notes in Phrase View, let the table generate the rest. Excellent for IDM, ambient, generative-leaning electronic music.

---

## Combining techniques

The power comes from combining these, not using them in isolation:
- **Random LFO + Table TIC** — a velocity-mapped drum with Drunk LFO on filter cutoff. Every hit is slightly different, and the filter wanders independently.
- **Hypersynth + Generative table** — Hypersynth provides chord content, table provides chord-stab rhythm pattern.
- **Selection-mode randomization + probability-driven table** — randomize note positions, then have tables generate variations on each note hit.

**Discipline:** don't combine more than 2 techniques per instrument. Combining 4 gives you sonic chaos that you can't reason about when something sounds wrong.

---

## When generative tools backfire

- **Track has no identity.** You delegated all the writing to randomness; nothing has authorial voice. Fix: keep the chorus/hook deliberate, use generative only for variation/fills.
- **Can't reproduce a sound you liked.** Random shapes don't seed deterministically. Fix: when you find a good random pattern, freeze it by rendering to sample (Selection to Sample, p.48) and using the sample instead.
- **Patterns feel "twitchy."** Too much randomization. Fix: lower the LFO AMT, reduce probability density, use Drunk instead of Random.
- **Sounds great in isolation, terrible in mix.** Generative elements competing for the same frequency space. Fix: mix discipline (see [Mixing Reference](mixing.md)) applies to generative elements too.

---

## How to learn this set

Don't try to learn all 6 techniques in one sitting. The plan weaves them into specific weeks:
- **Week 2** — Random/Drunk LFO shapes (extension of LFO learning)
- **Week 4** — Phrase randomization + probability (extension of pattern variation)
- **Week 7** — Table TIC modes (FC/FD/FE) + Hypersynth (library week, no track pressure)
- **Week 8** — Tables as arpeggiators (use as melodic shortcut for Project 2)

After the plan: revisit this page and combine. The combinations are where the M8 gets uniquely powerful.
