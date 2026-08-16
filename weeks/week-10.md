# Week 10 — Scope B mix + master in Ableton (optional)

**This week is optional.** Skip if Project 2's Scope A version (Week 9) is good enough, or if you're burnt out, or if you don't care about streaming loudness.

**Goal:** Take Project 2's stems through a Scope B pass in Ableton. End with a release-ready file you'd publish to Bandcamp/Soundcloud/Spotify.

**Time commitment:** 3 sessions, 60 min each. **Hard limits.**

**References:**
- [Mixing Reference](../reference/mixing.md) → Scope B workflow
- [Finalization Reference](../reference/finalization.md) → Scope B mastering chain

---

## Session 1 (~60 min) — Render stems + Ableton mix

### Step 1: Render stems from M8 (15 min)

Reference: Mixing Reference → Scope B → Stem rendering.

M8 does this in one pass — Render View has a `STEMS` mode that writes a separate WAV per track (manual p.47). Don't mute-and-render eight times.

- [ ] Open Project 2 on M8.
- [ ] Project View → `RENDER`.
- [ ] Set the render mode to `STEMS` (not `MIXED`).
- [ ] `SONG ROW START` / `SONG ROW LAST`: cover the whole song. `TRACKS`: all 8 enabled.
- [ ] `MODFX`, `DELAY`, `REVERB`: **on** — render the M8 sound, including sends, not raw oscillators.
- [ ] `LIMITER`: **off** — you're limiting in the master chain in Session 2.
- [ ] `MODE`: `32`-bit for DAW headroom.
- [ ] `NAME` it, then render. Files land in `/Renders` on the SD card.
- [ ] Copy `/Renders` off the card. You should have up to 8 stem WAVs — tracks with no chains in range are skipped.

### Step 2: Scope B mix in Ableton (40 min)

Reference: Mixing Reference → Scope B → Minimal Ableton mix.

- [ ] New Ableton project. Import all stems on separate audio tracks.
- [ ] Pull all faders down. Start from silence.
- [ ] Follow mix order: kick → bass → drums → melodic → effects.
- [ ] Apply EQ on each stem (same Scope A principles, but with surgical Ableton EQ).
- [ ] Optional: bus compression on drum group, side-chain via Ableton's sidechain compressor.
- [ ] Reference against one professional track.
- [ ] **Hard limit: 40 min.**

### Step 3: Render mix (5 min)

- [ ] Render the mixed track (no master chain yet) to WAV. 44.1kHz, 24-bit.
- [ ] Save as `Project2_mixed.wav`. **Don't apply master in this session.**

---

## Session 2 (~60 min) — Mix triage + master

### Step 1: Listen fresh (10 min)

- [ ] Listen to `Project2_mixed.wav` once, no notes during.
- [ ] Write 1–3 specific issues after.

### Step 2: Decide — triage or master as-is? (5 min)

- [ ] 0–1 issues: master as-is.
- [ ] 2–3 obvious issues: triage in Ableton (Step 3).
- [ ] 4+ issues: pick 2 worst or accept and master as-is. **Don't rebuild.**

### Step 3: Mix triage in Ableton (15 min, if needed)

- [ ] Fix 1–2 issues only. Levels, EQ, sends.
- [ ] **Do not touch arrangement.**
- [ ] Re-render as `Project2_mixed_v2.wav`.

### Step 4: Scope B mastering pass (30 min, hard limit)

Reference: Finalization Reference → Scope B chain.

- [ ] New Ableton project (or new chain). Import mixed render.
- [ ] Import reference track.
- [ ] Apply: HP filter → bus EQ → Glue Compressor → Limiter.
- [ ] Target ≈14 LUFS (or genre-appropriate).
- [ ] A/B against reference. Close the gap, don't match perfectly.
- [ ] **Stop at 30 min.** Set a timer.

Save as `Project2_master_v2.wav`.

---

## Session 3 (~60 min) — Multi-system check + acceptance

### Step 1: Three-system test (30 min)

Listen on:
- [ ] Phone speakers
- [ ] Headphones
- [ ] Laptop or car

1–2 notes per system.

### Step 2: Decision (10 min)

- [ ] No cross-system issues: done. Step 4.
- [ ] One consistent issue: one allowed fix. Step 3.
- [ ] Multiple consistent issues: accept as-is, note for next time.

### Step 3: One allowed fix (15 min, if needed)

- [ ] Open master project.
- [ ] One adjustment, re-render.
- [ ] **Done.** No more passes.

### Step 4: Acceptance + release

- [ ] Rename final: `Project2_RELEASE.wav`.
- [ ] If actually releasing: upload to Bandcamp/Soundcloud/Spotify via DistroKid/etc.
- [ ] If not: file it where you won't lose it.
- [ ] Send to a few people.

---

## 🎯 Deliverable

- [ ] Release-quality master of Project 2.
- [ ] Hits streaming loudness target.
- [ ] Translates across systems.

---

## Anti-perfectionism rules

- **Maximum two master passes total.** Session 2 + one Session 3 fix. After that, done.
- **One mix pass + one mix triage allowed.** No mix rebuilds after Session 2 Step 3.
- **No referencing after Session 3.** Don't compare next day and feel bad.
- **The bad first masters are the point.** Master 5–10 tracks before judging your mastering skill.

---

## After Week 10

- [ ] **Full week off.** Active rest. No M8, no other gear, no browsing.
- [ ] Then reflect on the full cycle: what worked, what didn't, what changes for the next cycle.
