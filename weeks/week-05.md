# Week 5 — Mix Project 1

**Goal:** Take Project 1 from "draft complete" (Week 4) to "mixed and clear." **No new technique this week. No finalization yet.** Pure mixing focus.

This is the start of Phase 2 (Apply). The writing is done. Now you learn to make it sound right.

**Reference (read first):** [Mixing Reference](../reference/mixing.md) — full Scope A workflow.

**Time-box:** 60 min max per session, 2–3 sessions this week. **Do not exceed.** Mixing rewards stopping, not over-tweaking.

---

## Session 1 (~60 min) — Foundation: kick & bass

The most important relationship in the mix. Get this right and 50% of mixing is done.

Reference: Mixing Reference → Scope A, Steps 1–2.

- [ ] Open Project 1 on M8.
- [ ] Mute everything except kick (`[OPTION]+[SHIFT]` per track in Song View).
- [ ] In Mixer View, set kick volume to peak around `-6 dBFS`.
- [ ] EQ kick if needed: boost 60–80Hz (body), cut 200–400Hz (mud), optional boost 3–5kHz (click). Per-instrument EQ via Instrument View → EQ slot → `[SHIFT]+[RIGHT]`.
- [ ] Unmute bass. Listen with kick.
- [ ] Set bass volume so kick still cuts through.
- [ ] If they fight, in order of escalation:
	1. **Lower bass** volume
	2. **LOWCUT bass** below 40Hz (removes sub conflict)
	3. **Notch bass** at kick's fundamental (60–80Hz)
	4. **TRIG envelope side-chain** — bass ducks when kick triggers. See Mixing Reference → Tool 3 for the full setup (TYPE: TRIG ENVELOPE, SRC: kick instrument number, DEST: VOLUME, AMT: negative).
- [ ] Verify on **two systems**: M8 speakers AND headphones (or phone speakers). Both kick AND bass audible distinctly on both.
- [ ] **Stop at 60 min.** If kick and bass aren't working after an hour, the kick or bass instrument itself is wrong — note it for Week 7 (library week), don't fix it now.

---

## Session 2 (~60 min) — Drums as a kit + melodic balance

Reference: Mixing Reference → Scope A, Steps 3–4.

### Step 1: Drums coherent (25 min)

- [ ] Unmute snare and hats. Balance against kick + bass.
- [ ] EQ separation:
	- Snare: BELL boost ~200Hz (body), BELL boost ~5kHz (snap)
	- Hi-hats: LOWCUT ~300Hz, HI.SHELF boost above 8kHz
- [ ] Listen as a group. Drums should feel like one kit, not three separate elements.

### Step 2: Melodic elements (25 min)

- [ ] Unmute melodic tracks one at a time.
- [ ] EQ: LOWCUT melodic elements below 100–200Hz. Keeps low end clean for kick/bass.
- [ ] Add reverb/delay sends for depth on a few elements. **Less than you think.**
- [ ] Lead/main element = dry-leaning, central. Pads/atmosphere = wetter, wider.

### Step 3: Quick check (10 min)

- [ ] Full mix unmuted. Listen all the way through Project 1.
- [ ] One pass only. Note 1–2 issues if any. **Don't fix them this session.**

**What counts as an "issue"?** You're listening for problems on one of the [5 dimensions of a mix](../reference/mixing.md#the-5-dimensions-of-a-mix) — level, frequency, space, depth, or dynamics. Concretely:
- Something obviously too loud or buried (level).
- Muddy/boxy (low-mid buildup ~200–400Hz) or harsh/brittle (frequency).
- Everything piled in the center, or narrow/flat (space).
- Smeared with no clarity — usually too much reverb (depth).
- Kick swallowed when the bass plays, or one element poking out no matter the level (dynamics).

If you're not sure how to name what's wrong, check the symptom list in [Mixing Reference → When mixing fails](../reference/mixing.md#when-mixing-fails). A clean mix where nothing jumps out is a valid result — note "no issues" and skip Session 3.

---

## Session 3 (~60 min, optional) — Polish and verify

Only do this session if Session 2 left you with clear, specific issues (see Session 2 Step 3 for what counts).

- [ ] Address 1–2 specific issues from Session 2. **Maximum two fixes.** For the fix-per-symptom, use [Mixing Reference → When mixing fails](../reference/mixing.md#when-mixing-fails).
- [ ] Listen on a third system if available (laptop, car, somewhere new).
- [ ] **Final check question:** "Is anything obviously wrong on 2+ systems?" If no, you're done. If yes, do exactly one more fix and then stop.

---

## 🎯 Deliverable

- [ ] Project 1 is mixed. All elements balanced, audible, not fighting.
- [ ] Render a reference WAV (no master yet, just rendered mix).
- [ ] Listen to it once on a system you haven't used during mixing. Note your gut reaction.
- [ ] **Save mix state.** Next week is finalization, not more mixing.

---

## Mixing anti-patterns to watch for

- **Soloing for more than 30 seconds.** Mix happens in context, not in solo.
- **Looping one bar.** Sounds great in a loop, falls apart in a full track.
- **EQ'ing instead of fixing the instrument.** If something needs more than 6dB of EQ to work, the instrument is wrong.
- **Adding reverb to fix balance issues.** Reverb doesn't fix mix problems, it adds new ones.
- **Mixing late at night.** Ears get tired and you over-compensate. Mix when fresh.
