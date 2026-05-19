# Finalization Reference

Use this page at the end of every finished track, **after mixing**. Linked from Week 6, Week 9, and Week 10.

**Mix first, master second.** If you haven't done a mixing pass yet, go to [Mixing Reference](mixing.md) first. Mastering can't fix a bad mix.

**What this is:** a checklist for getting a rendered M8 track from "raw mix" to "clear, balanced, loud enough, not embarrassing on headphones" in 30–60 minutes.

**What this is NOT:** professional mastering. That's a multi-year skill with reference monitors, treated rooms, and trained ears. This is *finalization* — the basic polish that makes a track listenable.

**Two scopes:**
- **Scope A — On-device only (M8 mixer + limiter).** Default. Use this for Project 1 and any learning track.
- **Scope B — M8 + minimal Ableton pass.** Optional upgrade for tracks you'll share or publish (Project 2 onwards).

**The most important rule:** time-box this. If you've been finalizing for over 60 minutes, you're hurting more than helping. Render, walk away.

---

## Scope A: On-device M8 finalization

Manual references: Mixer View (p.30), EQ Editor View (p.32), Limiter & Mix Scope View (p.34), Effect Settings View (p.36), Render View (p.47).

The M8 has a real mastering chain built into the Mixer: track volumes → send effects (ModFX, Delay, Reverb) → OTT compressor → main EQ → Limiter → DJ filter → Main mix volume. Use it.

### Step 1: Pre-master mix check (15 min)

This is a quick verification, not a real mix. The real mix should have happened already via the [Mixing Reference](mixing.md).

- [ ] Play the full track from Song View. Listen all the way through.
- [ ] In **Mixer View** (`[SHIFT]+[DOWN]` from Song View): watch the meter — any red bars mean clipping. Lower offending tracks.
- [ ] If you notice major balance issues (bass too loud, kick buried, reverb washing out everything), **stop mastering and do a real mix pass** via Mixing Reference. Don't try to fix mix problems at the master stage.
- [ ] If the mix is solid, proceed to Step 2.

### Step 2: Main mix EQ (10 min)

- [ ] In Mixer View, select `EQ` and press `[SHIFT]+[RIGHT]` or `[EDIT]` to enter EQ Editor View (p.32).
- [ ] M8 main mix EQ has 3 bands (LOW, MID, HIGH).
- [ ] **High-pass the mix** at the LOW band: TYPE = `LOWCUT`, FREQ around 30Hz. Removes subsonic rumble that eats limiter headroom.
- [ ] **Optional gentle MID adjustments:** if the track sounds boxy (200–400Hz buildup), small cut. If it sounds dull, small high-shelf boost on HIGH band around 8–12kHz.
- [ ] **Rule:** max 3dB moves on any band. If you need more, the mix is wrong, not the EQ.

### Step 3: OTT compression (5 min)

OTT (Over The Top) is parallel multi-band upward/downward compression. Brings forward quiet stuff, controls loud stuff. Adds polish.

- [ ] Mixer View → `OTT` parameter.
- [ ] Bring up slowly from `00`. Listen as it engages.
- [ ] Target: `20–40` (subtle). Above `60` it gets crushed/lo-fi. Above `80` it starts ducking the main signal (read manual p.30).
- [ ] If OTT makes the track sound worse, leave it at `00`. Not every track wants OTT.

### Step 4: Limiter (5 min)

The limiter prevents clipping and increases perceived loudness.

- [ ] In Mixer View, select `LIM` and press `[SHIFT]+[RIGHT]` to enter Limiter & Mix Scope View (p.34).
- [ ] `LIM` parameter: start at `40`, push up while watching the scope.
- [ ] White line on the MIX indicator shows compression activity. **2–4dB of compression on peaks is healthy. 6dB+ is squashing the dynamics.**
- [ ] `ATK` (attack): `20–40` is a safe range. Faster = more aggressive limiting.
- [ ] `REL` (release): `00` = AUTO mode (adaptive). Use AUTO unless you have a reason not to.
- [ ] `SOFT CLIP`: gentle saturation after limiter. Adds warmth/glue. Bring up MIX value to exaggerate — use sparingly.

### Step 5: Final check (10 min)

- [ ] Listen on **at least two different playback systems**. The M8's built-in speakers count as one (terrible reference, but useful for catching obvious problems). Headphones count as another.
- [ ] Listen for: bass too loud/quiet? Vocals/leads buried? Anything harsh or fatiguing? Anything missing on phone speakers?
- [ ] If something's clearly wrong, fix it. If it's "could be a little better," leave it. Time-box.

### Step 6: Render (5 min)

- [ ] Project View → Render (manual p.47).
- [ ] Render settings: 44.1kHz, 16-bit or 24-bit WAV. 24-bit if planning Scope B mastering pass; 16-bit if M8-only is the final.
- [ ] Save with a clear filename and date.
- [ ] **Done. Walk away.**

---

## Scope B: Optional Ableton mastering pass

Use this for Project 2 onward, or any track you'll share/publish. **If you already own Ableton, this isn't new gear.**

Goal: take the M8-rendered WAV and do a minimal mastering pass to hit streaming loudness targets and improve clarity. **30 minutes max.**

### Setup

- [ ] Import the rendered WAV onto an audio track in a fresh Ableton project. Don't import the M8 project — just the rendered stereo file.
- [ ] Add a **reference track** on a second audio track: pick one professional track in a similar genre that you like the sound of. Match output levels by ear before comparing.
- [ ] On the master bus, add this chain in order:

### The minimal master chain

#### 1. High-pass filter (EQ Eight)
- HP at 30Hz, 24dB/oct slope. Removes inaudible sub that wastes headroom.

#### 2. Bus EQ (EQ Eight)
- Subtle. **Max 2dB moves per band.**
- Common moves: gentle high-shelf boost (8–12kHz, +1–2dB) for air; tiny low-mid cut (200–300Hz, -1dB) if muddy.
- If you need more than this, the mix is wrong.

#### 3. Bus compressor (Glue Compressor)
- Ratio: 2:1 or 4:1
- Attack: 10–30ms (slow enough to let transients through)
- Release: AUTO
- Threshold: aim for 1–3dB of gain reduction on peaks. **No more.**
- Makeup gain: match levels with bypass on/off.

#### 4. Limiter (Ableton's built-in Limiter or any brickwall)
- Ceiling: `-1.0 dBTP` (gives streaming platforms headroom)
- Threshold: lower until you hit your loudness target
- Release: AUTO or 50ms

#### 5. Loudness target
- **Streaming target: ≈14 LUFS integrated** (Spotify normalizes to -14 LUFS).
- Use Ableton's built-in loudness meter or a free plugin like Youlean Loudness Meter.
- Some genres (drum & bass, hardcore, modern pop) sit louder around −10 to −12 LUFS. Ambient/IDM often sits quieter at −16 to −18 LUFS.

### Reference checking

- [ ] A/B against the reference track. Toggle between your master and the reference at matched volumes.
- [ ] Specific questions to ask:
	- Is my bass louder or quieter than theirs?
	- Is my high end harsher or duller?
	- Does my master sound thin or full compared?
	- Where is my low-mid sitting?
- [ ] Adjust your chain to close the gap. **Don't try to match perfectly.** Match "close enough."

### Final render

- [ ] Render to stereo WAV, 44.1kHz, 16-bit (or 24-bit if archiving).
- [ ] Listen to the rendered file (not the live Ableton playback) on multiple systems one more time.
- [ ] **Render once. Don't do a second pass.** Time-box.

---

## Anti-perfectionism rules

- **Master once.** No second passes. No "let me just tweak the high end one more time."
- **Time-box.** Scope A = 60 min max. Scope B = 30 min max on top of A.
- **Three-system check, then done.** If it sounds reasonable on headphones, laptop speakers, and phone, it's mastered. Stop.
- **No reference comparison after the 30 minutes is up.** Reference checking is for during the process, not for second-guessing after.
- **Bad mastering is fine.** Your first 10 mastered tracks will be over-compressed, over-EQ'd, or under-loud. That's the only way to learn.
- **The mix matters more than the master.** If a master sounds wrong, 80% of the time the mix is the problem. Go back to the M8 and fix the mix, don't compensate at the master.

---

## Reference tracks to A/B against

Pick one in your target genre and use it consistently. Examples from the M8 community:
- [laamaa — seven weeks](https://laamaa.bandcamp.com/album/seven-weeks) (downtempo electronic, M8)
- [Nullsleep — Lossless Experience](https://nullsleep.bandcamp.com/album/lossless-experience) (chiptune-adjacent)
- [Jeremy Blake — Rituals](https://soundvision.bandcamp.com/album/rituals) (ambient electronic)
- For broader electronic references, pick any commercially mastered track on Bandcamp/streaming in the genre you're targeting.

---

## What to do when finalization fails

Sometimes a track just won't master well. Symptoms:
- Can't get it loud without crushing it
- Sounds great on headphones, dies on phone speakers (= no mids)
- Sounds great on phone, mush on headphones (= no high detail)
- One element keeps poking out no matter what you do

**This is a mix problem, not a master problem.** Don't fight it at the master. Go back to the M8 and:
- Re-balance the levels in Mixer View
- Fix the EQ on the offending instrument (Instrument EQ, p.32)
- Tame the offending instrument's send levels
- Re-render, try again

If after one mix fix it still won't master, **render it as-is and move on.** Bad finished tracks teach more than great unfinished ones.
