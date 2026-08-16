# Mixing Reference

Use this page when balancing tracks against each other — before finalization. Linked from Week 3, Week 5, Week 8, Week 9, Week 10, and the Finalization Reference.

**What this is:** procedures and checklists for getting from "the elements exist" to "the elements are balanced, clear, and don't fight each other."

**What this is NOT:** professional mixing. That's a multi-year skill. This is *functional mixing* — reliably getting tracks to a state where finalization can do its job.

**Two scopes:**
- **Scope A — On-device M8 only.** Default. Mixer View, per-instrument EQ, send levels, TRIG-based side-chain. Used in Weeks 5, 8, 9.
- **Scope B — Render stems to Ableton.** Optional refinement when you want per-stem processing and DAW metering. Not needed to publish — see [Finalization Reference → Releasing a Scope A render](finalization.md#releasing-a-scope-a-render). Used in Week 10.

**The hardest rule of mixing:** time-box. 60 min per session, max. If you've been mixing the same track for 3 hours, you've stopped hearing it.

---

## The 5 dimensions of a mix

Mixing is shaping how sounds relate to each other along five axes. Different problems live on different axes — fixing the wrong one wastes time.

| Dimension | Problem it solves | Tools on M8 |
|---|---|---|
| **Frequency** | Two elements fighting in the same range; mud; harshness | Per-instrument EQ (p.32), main mix EQ |
| **Level** | One element too loud or too quiet | Track volume in Mixer View, instrument volume |
| **Space** | Mix sounds narrow, flat, or cluttered in the middle | Stereo width on ModFX/Delay/Reverb, instrument pan |
| **Depth** | Mix sounds 2D, no foreground/background | Reverb send levels, delay send levels |
| **Dynamics** | Kick gets buried by bass; mix feels static or pumpy | TRIG envelope side-chain (p.21), OTT (p.30), per-instrument modulation |

**Diagnostic question when something sounds wrong:** which dimension is the problem? Most mix problems are misdiagnosed as level problems when they're actually frequency or dynamics problems.

---

## The mix order

Always mix from the loudest, lowest, most-important elements first. Don't start with the lead synth and work down — you'll keep redoing everything.

1. **Kick first.** Get its volume right against silence. Reference -6dBFS peak.
2. **Bass against kick.** This is the most important relationship in the mix. They share frequency space below 200Hz — they MUST share it intentionally, not by accident.
3. **Rest of drums** (snare, hats, percussion) as a coherent group. Treat the drums as one element.
4. **Drums vs bass.** Does the bass disappear under the drums? Does the kick disappear under the bass? Fix now.
5. **Melodic / harmonic elements** (pads, leads, chords). Last priority. They fit around the rhythm section.
6. **Effects / atmosphere.** Reverb, delay, FX risers, transitions. Last.

If you go out of order, you mix everything to the lead, then can't hear the kick, then turn up the kick, then re-mix everything.

---

## Scope A: On-device M8 mixing

Manual references: Mixer View (p.30), EQ Editor View (p.32), Effect Settings View (p.36), Instrument Modulation View (p.18), Trig Envelope (p.21).

### Tool 1: Track volume (Mixer View)

- Mixer View: `[SHIFT]+[DOWN]` from Song View.
- Each of 8 tracks has volume.
- Watch the meter — red bars = clipping. Lower offenders.
- Rule: aim for peaks around `-6 dBFS` on individual tracks. Leaves headroom for limiter.
- Track volume also affects send levels proportionally.

### Tool 2: Per-instrument EQ (3-band)

M8 has a 3-band parametric EQ per instrument with 128 shareable EQ banks (manual p.32). This is your primary mix tool.

Access: Instrument View → EQ slot → `[SHIFT]+[RIGHT]` or `[EDIT]` to open EQ Editor.

Each band has GAIN, FREQ, Q (bandwidth), TYPE (LOWCUT, LOWSHELF, BELL, BANDPASS, HI.SHELF, HI.CUT, ALLPASS), and MODE (STEREO, MID, SIDE, LEFT, RIGHT).

#### Frequency carving recipes

**Kick:** boost around 60–80Hz (body), cut 200–400Hz (mud), boost 3–5kHz if you want click/attack. HI.CUT above 8kHz to leave room for hats.

**Bass:** LOWCUT below 40Hz (kills subsonic that fights kick). Cut a notch where the kick's body lives (60–80Hz) so they don't pile up. Most bass character lives 80–250Hz.

**Snare:** boost around 200Hz (body), boost 5kHz (snap/snare wires).

**Hi-hats:** LOWCUT around 300Hz (removes any bleed/lows). HI.SHELF boost above 8kHz for air.

**Lead/melodic:** depends on the instrument. Generally LOWCUT below 100–200Hz to keep low end clean for kick/bass.

**Pad:** carve out 200–500Hz to avoid mud. Pads usually sound better with a slight scoop in the low-mids.

#### EQ rules

- **Cuts are usually better than boosts.** If two elements fight, cut one rather than boosting the other. Stops the mix getting louder and louder.
- **Wide cuts, narrow boosts.** Low Q for cuts (gentle), higher Q for boosts (surgical).
- **Max 6dB moves.** If you need more, the instrument is wrong, not the mix.
- **EQ in context, not solo.** Soloing an instrument and EQ'ing it sounds great but ignores the mix. Always check in the full mix.

### Tool 3: Side-chain via TRIG envelope

The classic "kick ducks bass" effect. Real M8 mechanism (manual p.21, Trig Envelope).

Setup:
- [ ] On the bass instrument, go to Instrument Modulation View (`[SHIFT]+[UP]` from Instrument View).
- [ ] Pick an unused MOD slot.
- [ ] TYPE: `TRIG ENVELOPE`
- [ ] `SRC`: set to the kick's instrument number (e.g. `00` if kick is instrument 00), OR `80` + track number for "any instrument on track N" (e.g. `80` = track 1).
- [ ] `DEST`: `VOLUME` (or `AMP`).
- [ ] `AMT`: negative value (e.g. `-60`) — this ducks the bass when the kick triggers.
- [ ] `ATK`: `00` (instant duck).
- [ ] `HOLD`: short (`08–10`).
- [ ] `DEC`: medium (`20–30`) — controls how fast the bass comes back.

Result: every time the kick hits, bass ducks. Kick gets through cleanly. Classic side-chain.

Variations:
- Side-chain pads to the kick for breathing/pumping motion.
- Side-chain reverb sends to the lead for clearer dry signal under busy moments.

### Tool 4: Send effects as depth (Reverb / Delay)

Front-to-back depth comes from reverb and delay sends, not just from levels.

- Lead vocals/melodies = dry (foreground)
- Snare with medium reverb = mid-ground
- Pad with long reverb + delay = background

Manual: Effect Settings View, p.36–37. Three send effects: ModFX, Delay, Reverb.

- Per-instrument send levels: `MFX`, `DEL`, `REV` in Instrument View.
- Global effect settings: Effect Settings View (`[SHIFT]+[DOWN]` from Mixer View).

Rule: not everything needs reverb. **Less reverb than you think.** Most amateur mixes drown in reverb.

### Tool 5: Stereo width

- Each send effect has a WIDTH parameter (manual p.36): `00` = mono, `FF` = stereo.
- ModFX (chorus/phaser/flanger) inherently widens.
- Reverb width adds spatial dimension to the wet signal.

General approach:
- Kick, bass, lead vocal/main melody = center, mono-leaning.
- Hats, percussion, secondary elements = wider, off-center.
- Pads, ambient layers = widest.

### The full Scope A mix pass

Step-by-step. Target: 30–60 min depending on complexity.

#### Step 1: Mute everything except kick (5 min)

- [ ] Mute all tracks except kick (`[OPTION]+[SHIFT]` per track).
- [ ] Set kick volume to peak around `-6 dBFS`. Watch the meter.
- [ ] EQ kick if needed (see recipe above).

#### Step 2: Add bass, balance against kick (10 min)

- [ ] Unmute bass. Hear them together.
- [ ] Set bass volume so kick still cuts through.
- [ ] If they fight: EQ. Carve a hole in bass at kick's fundamental, OR roll off bass sub below kick.
- [ ] If still fighting: side-chain bass to kick via TRIG envelope.
- [ ] **You should hear both the kick AND the bass distinctly. If you don't, fix it now.**

#### Step 3: Add rest of drums (10 min)

- [ ] Unmute snare, hats, perc. Balance against kick + bass.
- [ ] EQ for separation: snare body around 200Hz, hat air above 8kHz.
- [ ] Check: are the drums a coherent group? Do they swing together?

#### Step 4: Add melodic elements (15 min)

- [ ] Unmute one melodic element at a time. Balance against drums + bass.
- [ ] EQ: LOWCUT melodic elements below 100–200Hz to keep low end clean.
- [ ] Add reverb/delay sends for depth where appropriate. Less than you think.
- [ ] Pan/widen secondary elements.

#### Step 5: Full-mix check (10 min)

- [ ] All tracks unmuted. Listen to full sections.
- [ ] Is anything getting buried? Is anything too loud?
- [ ] **Check on 2 systems**: M8 speakers + headphones, OR phone + headphones.
- [ ] Fix glaring issues. Ignore minor ones.
- [ ] **Stop at 60 min total.**

---

## Scope B: Render stems to Ableton

For when you want per-stem control the M8's 8 tracks can't give you. Used in Week 10. A Scope A mix is enough to publish.

### Stem rendering on M8

M8 renders stems natively — one pass, one file per track. No muting, no re-rendering eight times.

Manual: Render View (p.47), Selection to Sample (p.48).

- [ ] Project View → `RENDER` to open Render View.
- [ ] Set the bottom switch to `STEMS` (the other option, `MIXED`, gives you one stereo file of the whole song).
- [ ] `SONG ROW START` / `SONG ROW LAST`: the range to render. `REPEAT SONG` if you want multiple passes captured.
- [ ] `TRACKS`: selectively enable which tracks get rendered. Leave all 8 on for a full stem set.
- [ ] `MODFX` / `DELAY` / `REVERB`: **on** — you want the M8 sound, including its sends, not raw oscillators.
- [ ] `LIMITER`: **off** for Scope B — you're limiting in the master chain later, so don't bake it in.
- [ ] `MODE`: `32`-bit. Stems are working files headed into a DAW — take the faithful export.
- [ ] `NAME`: name the render. Files land in `/Renders` on the SD card as 44.1kHz stereo WAVs.

`STEMS` writes a file for each *enabled* track that actually has chains in the selected range — silent tracks are skipped, so expect up to 8 files, not always exactly 8.

**Caveat:** External Instrument tracks can't be rendered this way — the audio is processed in real time. Capture those with the Sample Editor instead, selecting the playing track as input source (p.62).

### Minimal Ableton mix

Import all 8 stems on separate audio tracks. Then:

1. **Levels first.** Pull all faders down. Bring up kick to peak around -10dBFS. Build the rest against it.
2. **EQ on each stem as needed.** Same principles as Scope A: LOWCUT melodic stems, carve frequency space, max 6dB moves.
3. **Bus compression on drum bus (optional).** Glue Compressor, 2:1, slow attack, 1–2dB GR. Tightens the drums.
4. **Side-chain via Ableton sends.** Use the dedicated side-chain compressor on the bass/pads triggered by the kick stem.
5. **Reference against one professional track.** Match perceived balance.
6. **Time-box: 60 min.**

Then Master with the Scope B chain (see [Finalization Reference](finalization.md)).

---

## Reference checking

Same principle as mastering, but at the mix stage:
- Pick one reference track in your genre. Have it on hand.
- A/B between your mix and the reference at matched volumes.
- Ask: where does the kick sit? How loud is the bass relative to the kick? Where are the leads? How dry/wet is the reference?
- Don't try to copy. Try to understand what "normal" looks like in your genre.

Reference tracks (same as Finalization Reference):
- [laamaa — seven weeks](https://laamaa.bandcamp.com/album/seven-weeks)
- [Nullsleep — Lossless Experience](https://nullsleep.bandcamp.com/album/lossless-experience)
- [Jeremy Blake — Rituals](https://soundvision.bandcamp.com/album/rituals)

---

## Anti-perfectionism rules

- **Time-box.** 60 min per mix session. Hard limit.
- **Listen to full sections, not loops.** Looping a single bar makes everything sound fine.
- **Don't solo for more than 30 seconds.** Mixes happen in context, not in isolation.
- **The mix is done when nothing obvious is wrong on 2 systems.** Not when it's perfect.
- **Bad mixes are how you learn.** Your first 20 mixes will be over-EQ'd, weirdly panned, too dry, or too wet. Ship anyway.
- **80/20 rule.** Most mix problems are levels and EQ between kick and bass. Get those right and 80% of the mix is done.

---

## When mixing fails

Symptoms:
- Track sounds clear on M8 speakers but muddy on headphones → too much low-mid buildup. EQ cuts around 200–400Hz on multiple elements.
- Sounds clear on headphones but thin on speakers → not enough mids. Boost 500Hz–2kHz on snare, lead, or stab elements.
- Kick disappears when everything is playing → either bass is too loud sub-100Hz, or kick lacks click around 3kHz, or you need side-chain.
- Everything sounds smeared / no clarity → too much reverb. Pull all send levels down 50% and re-balance.
- One element keeps poking out no matter what you do → dynamics problem. Try a TRIG envelope or per-instrument volume modulation to tame peaks.

**If you can't fix it in a 60-min session, the instrument design is wrong, not the mix.** Go back to Instrument View, fix the offending sound (different envelope, different filter, different osc), and re-mix.
