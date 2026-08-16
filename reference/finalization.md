# Finalization Reference

Use this page at the end of every finished track, **after mixing**. Linked from Week 6, Week 9, and Week 10.

**Mix first, master second.** If you haven't done a mixing pass yet, go to [Mixing Reference](mixing.md) first. Mastering can't fix a bad mix.

**What this is:** a checklist for getting a rendered M8 track from "raw mix" to "clear, balanced, loud enough, not embarrassing on headphones" in 30–60 minutes.

**What this is NOT:** professional mastering. That's a multi-year skill with reference monitors, treated rooms, and trained ears. This is *finalization* — the basic polish that makes a track listenable.

**Two scopes:**
- **Scope A — On-device only (M8 mixer + limiter).** Default. Use this for every track, including ones you release. **A Scope A render is a releasable file** — see [Releasing a Scope A render](#releasing-a-scope-a-render) below.
- **Scope B — M8 + minimal Ableton pass.** Optional refinement: metering, surgical EQ, precise loudness targeting. Not a requirement for publishing.

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
- [ ] Render settings: 44.1kHz WAV, MODE 16- or 32-bit (the M8's only two render bit depths — there is no 24-bit). **Default to 32-bit** — it's the faithful export and the one worth keeping, whether or not a Scope B pass follows. See [Which bit depth, and why it barely matters](#which-bit-depth-and-why-it-barely-matters).
- [ ] Save with a clear filename and date.
- [ ] **Done. Walk away.**

---

## Releasing a Scope A render

**You do not need a DAW to publish an M8 track.** The M8 renders a 44.1kHz stereo WAV (p.47) — that *is* the delivery format Bandcamp, Soundcloud, and every distributor (DistroKid, TuneCore, etc.) accept. And everything a mastering chain does, the M8 has on the main bus: all tracks and sends run through OTT → main EQ → limiter → DJ filter → main volume (p.30), with a scope and a peak readout to set it by (p.34).

What the M8 *doesn't* have is **metering**: it shows sample peak in dB, not integrated LUFS and not true peak. That's the entire gap. It's a measurement gap, not a capability gap.

### Why you don't need to chase a LUFS number

Every major platform loudness-normalizes on playback — Spotify and YouTube to around −14 LUFS, Apple Music to around −16. A quiet master gets turned **up**; an over-limited master gets turned **down** and keeps all the damage you did making it loud. So the target isn't "hit −14 LUFS." The target is **clean, controlled, and not clipped** — which you can judge on the device.

If you master by ear to the point where nothing distorts and the limiter is doing 2–4dB on peaks, you are inside the window where normalization does the rest.

### The one real trap: `MIX` is post-limiter

`MIX` (main mix volume) is applied **after** the limiter stage (p.34). This matters enormously: if you set a good limiter and then push `MIX` up for loudness, you are adding gain the limiter can no longer catch, and you will clip the render. The limiter's ceiling is not the file's ceiling — `MIX` is.

Set them in this order: **`LIM` for control, then `MIX` for output level.** Never the reverse.

### Release checklist

Do this after Step 6, before you upload anything.

- [ ] Set `LIM` first (Step 4 above). 2–4dB of activity on peaks.
- [ ] Go to Limiter & Mix Scope View, select `PEAK`, clear it with `[OPT]+[EDIT]`.
- [ ] Play the **loudest section** of the track all the way through. Let `PEAK` capture it.
- [ ] Read `PEAK`. **Target around `-1.0 dB`.** That's your headroom for lossy encoding — MP3/AAC conversion can overshoot the sample peaks slightly, and platforms encode everything.
- [ ] If `PEAK` is at or near `0.0`, or you see a red bar on the Mixer meter: **pull `MIX` down**, don't touch the limiter. Clear `PEAK` and re-run.
- [ ] `SOFT CLIP` only if you want the warmth — it's not a safety net, and it changes the sound.
- [ ] Render View: `MIXED` mode, `LIMITER` **on** (so the master limiter you just set is baked into the file), `MODFX` / `DELAY` / `REVERB` **on**, `MODE` `32`-bit.
- [ ] Rename the file from `/Renders` and upload it. That's the release.

### Which bit depth, and why it barely matters

**Render `32`-bit and keep that as your master.** It's the M8's most faithful export — the synthesis engine runs at 32-bit internally, so a 32-bit render is the file with nothing thrown away. It costs you disk space and nothing else. It's also the file you'd hand to a Scope B pass, a remaster, or a re-release years later.

For the *upload*, the honest answer is that **it makes no audible difference on a finished, limited master.** 16-bit gives you about 96dB of dynamic range, which is far more than a limited master uses. Nobody has ever heard the difference on a track like this.

So:

- [ ] **Default to `32`-bit.** Best archive, no downside beyond file size.
- [ ] **If an uploader rejects it**, just re-render at `16`-bit. The M8's 32-bit WAVs are integer, not float (community: The M8 Companion), and some distributor intake tools only expect 16- or 24-bit. The M8 has no 24-bit option.
- [ ] Re-rendering is free and takes a minute — **don't convert the file yourself** to work around a rejection. Let the M8 produce both.

What you should *not* do is agonize over this. Bit depth is the least consequential decision in this entire page.

**One caveat on OTT:** community reports from Dirtywave's own dev meetups say OTT is only applied when you render from Render View in `MIXED` mode — a quick selection-render doesn't include it, by design. If you're relying on OTT as part of your master, render the proper way.

### Optional: check the loudness off-device

If you want the number, you don't need Ableton for it — a free web loudness analyzer or a phone LUFS meter app will read integrated LUFS off the rendered WAV. Useful as a **one-time calibration**: measure two or three of your finished tracks, learn where your ear naturally lands, then stop measuring.

This is a check, not a processing step. If it reads −18 LUFS and sounds good, upload it anyway — the platform will bring it up.

### What Scope B actually buys you

Not permission to publish. It buys metering you can trust, EQ moves finer than 3 bands, and the ability to hit a specific loudness on purpose. Worth it eventually. **Not worth blocking a release on.**

---

## Scope B: Optional Ableton mastering pass

Optional. Use it when you want metering and finer tools than the M8's 3-band main EQ — not because a track "needs" it to be published. **If you already own Ableton, this isn't new gear.**

Goal: take the M8-rendered WAV and do a minimal mastering pass to hit a specific loudness target and improve clarity. **30 minutes max.**

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
