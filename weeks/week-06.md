# Week 6 — Finalize and ship Project 1

**Goal:** Take the mixed Project 1 (Week 5 output) through finalization and ship it. **First release-ready track shipped in this cycle.**

No new technique. No new mixing. Just finalize, render, share.

**Reference (read first):** [Finalization Reference](../reference/finalization.md) — Scope A workflow.

**Time-box:** 60 min for finalization, 35 min for verification and release, total ~95 min over 1–2 sessions.

---

## Session 1 (~60 min) — Finalization pass

Follow the Scope A workflow from the Finalization Reference exactly.

### Step 1: Pre-master mix check (10 min)

This is a *verification*, not a real mix. You did the real mix last week.

- [ ] Play Project 1 from Song View, start to finish.
- [ ] In Mixer View, watch the meters for red bars (clipping).
- [ ] If you notice major balance issues, **stop and go back to Week 5 mixing.** Don't fix mix problems at the master stage.
- [ ] If the mix is solid, proceed.

### Step 2: Main mix EQ (10 min)

- [ ] Mixer View → `EQ` → `[SHIFT]+[RIGHT]` to enter EQ Editor.
- [ ] **High-pass the mix**: LOW band TYPE=`LOWCUT`, FREQ~30Hz.
- [ ] Optional gentle moves on MID/HIGH bands. **Max 3dB.**

### Step 3: OTT compression (5 min)

- [ ] Mixer View → `OTT` parameter.
- [ ] Bring up slowly. Target `20–40`. Above `60` it gets crushed.
- [ ] If it makes the track worse, leave at `00`.

### Step 4: Limiter (10 min)

- [ ] Mixer View → `LIM` → `[SHIFT]+[RIGHT]` to Limiter & Mix Scope View.
- [ ] Start `LIM` at `40`, push up while watching the compression line.
- [ ] Target: 2–4dB compression on peaks. **6dB+ = squashing.**
- [ ] `ATK`: `20–40`. `REL`: `00` (AUTO).
- [ ] `SOFT CLIP`: gentle. Adds warmth.

**How to read the compression:** With `LIM` selected, the scope shows the input signal along the bottom and the **limiter activity highlighted along the top** — that top band *is* the compression (manual p.34). The further it dips **down from the top**, the more gain reduction on that peak. A thin sliver = barely working; a thick band carving in continuously = past 6dB, back off `LIM`. (On the `MIX` indicator the same activity shows as a white line, manual p.30.) Play the loudest section and judge the band there, not on quiet parts.

- [ ] `ZOOM` sets the scope's lower limit **in dB** — set it so the few-dB window you care about is legible instead of a guess.
- [ ] `PEAK` shows the main mix's current peak dB (resets on `MIX`/`LIM` change; clear with `[OPT]+[EDIT]`). Use it to confirm you're controlling peaks, not crushing the body.

The M8 gives no single "gain reduction = 3dB" number — you're eyeballing that top band against the `ZOOM` dB scale. That's the intended way to check it.

### Step 5: Render (5 min)

- [ ] Project View → Render.
- [ ] 44.1kHz WAV, `MODE` `32`-bit. The M8 renders 16- or 32-bit only (no 24) — 32 is the faithful export and the one worth keeping, whether or not Week 10 follows.
- [ ] Save with clear filename: `Project1_master_v1.wav` or similar.

### Step 6: First listen (20 min, fresh)

- [ ] Listen to the rendered WAV once, end to end. **No fixing yet.**
- [ ] Note 1–2 things you'd want to verify on other systems.
- [ ] **Don't open the project again today.**

---

## Session 2 (~35 min) — Multi-system verification + ship

### Step 1: Three-system listening test (15 min)

Listen to `Project1_master_v1.wav` on three systems:
- [ ] **Phone speakers** — worst case. Bass audible? Leads clear? Anything painful?
- [ ] **Headphones** — stereo image, depth, detail.
- [ ] **Laptop speakers** or car — overall balance.

For each: 1–2 short notes.

### Step 2: One allowed fix (10 min, only if needed)

Are there problems on **2+ systems consistently**?

- [ ] If no: master is done. Skip to Step 3.
- [ ] If yes, one consistent issue: **one allowed fix**. Adjust master, re-render. **Done.**
- [ ] If yes, multiple consistent issues: the mix has problems. Note them for next time. **Ship as-is anyway.**

### Step 3: Release check (5 min)

The M8's render is a real delivery file — 44.1kHz stereo WAV is what Bandcamp, Soundcloud, and distributors accept. You don't need a DAW to publish this. Full context: [Finalization Reference → Releasing a Scope A render](../reference/finalization.md#releasing-a-scope-a-render).

- [ ] Limiter & Mix Scope View → select `PEAK`, clear it with `[OPT]+[EDIT]`.
- [ ] Play the **loudest section** through. Read `PEAK`. **Target around `-1.0 dB`.**
- [ ] If it's at `0.0` or the Mixer meter shows red: pull `MIX` down — **not** the limiter. `MIX` is applied *after* the limiter (manual p.34), so it's `MIX` that clips your render, not `LIM`.
- [ ] Re-render with `LIMITER` **on**, `MODE` `32`-bit. Only drop to `16` if an uploader rejects the file — re-rendering is free, don't convert it yourself.

**Don't chase a loudness number.** Streaming platforms normalize on playback (≈−14 LUFS), so they turn quiet masters up and loud ones down. Clean and controlled beats loud.

### Step 4: Ship it (5 min)

- [ ] Rename final WAV: `Project1_FINAL.wav` (or your naming).
- [ ] Put it somewhere you won't lose it.
- [ ] Send it to **one person outside your own ears.** Discord, friend, partner. Sharing is part of finishing.
- [ ] Optional: post to Bandcamp/Soundcloud as a private/unlisted track. Doesn't have to be public release — just out of your hands.

---

## 🎯 Deliverable — PROJECT 1 SHIPPED

- [ ] First M8 track finished in this cycle. Properly mixed, finalized, shipped.
- [ ] WAV exists. One other person has heard it.
- [ ] Notice what you just did. The gear hasn't been the blocker, this whole time. The structure was.

---

## After Week 6

- [ ] Week 7 is the library week — no track, just instruments. Use it as recovery.
- [ ] **Don't immediately start thinking about Project 2.** Phase 2 ended successfully. Sit with that for a moment.

---

## Anti-perfectionism rules

- **Master once, walk away.** No second passes after the one allowed fix.
- **Don't compare Project 1 to professional tracks.** They had years and proper monitoring.
- **The bad first masters are the point.** This is master #1 of many. Quality compounds with quantity.
- **Shipping > polishing.** A shipped imperfect track teaches more than a perfect unfinished one.
