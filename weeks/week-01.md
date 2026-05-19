# Week 1 — Re-entry

**Goal:** Remove cold-start friction. Rebuild muscle memory. No new techniques — prove the device still works for you.
**Mindset:** Deliberately low bar. Success = boot it, use it, render something.
**Manual references:** Getting Started (p.5), Navigation (p.6), Global Key Shortcuts (p.7), Loading a Demo Song (p.9), Song View (p.10), Chain View (p.12), Phrase View (p.14), Render View (p.47).

---

## Thread 1: M8 technique — Re-entry

### Boot and recall

- [ ] Charge M8 if battery low. Boot with power button (right side, 1 sec hold). Reference: Powering Up, p.3.
- [ ] In Song View: `Project View` is above Song View — navigate `[SHIFT]+[UP]` from Song View, choose `LOAD`, `[EDIT]` to enter file browser. Reference: Loading a Demo Song, p.9.
- [ ] Load one of your previously finished tracks (or a demo if starting fresh).
- [ ] Press `[SHIFT]+[PLAY]` to play the whole song. Listen all the way through.
- [ ] Navigate around while it plays: `[SHIFT]+[DIRECTION]` moves between views (mini-map bottom right shows where you are).
- [ ] Open one of its instruments: from Phrase View, position cursor on instrument column (I), press `[SHIFT]+[RIGHT]` to jump to Instrument View. Look at settings. **Don't edit.**

### Start Project 1

- [ ] In Project View, choose `NEW` (or load a fresh song slot). Name it `Project1` in the project settings.
- [ ] Build a 4-bar loop using 3 tracks:
	- Track 1: drums. **The M8 has no "kit" concept** — a Sampler instrument loads ONE sample file and plays it back. Use three separate Sampler instruments:
		- Instrument 00: `Sampler`, SAMPLE = a kick `.wav` from `/Samples/` (one-shot, not a sliced chain)
		- Instrument 01: `Sampler`, SAMPLE = a snare `.wav`
		- Instrument 02: `Sampler`, SAMPLE = a hi-hat `.wav`
		- In Phrase View on the drum track, vary the `I` column per row to switch which sound plays (e.g. kick on row 00, snare on row 04, hat on rows 02/06). Note value stays constant (e.g. `C-4`).
		- **Note on sliced kit files:** if you load a multi-hit drum chain into one Sampler with `SLICE 00OFF`, it just plays the whole file pitched by note — not what you want. To trigger slices chromatically you need slice markers (via the Sampler's `AUTO` or `SILENCE` slicing modes) plus a non-zero `SLICE` parameter in Instrument View. **Skip this for Week 1** — it's covered in Week 7.
	- Track 2: bass (use `Macrosynth`, default model — pick a low note, around `C-3`)
	- Track 3: melodic (use `Macrosynth` or `Wavsynth` preset — higher note, around `C-5`)
- [ ] In Phrase View: enter notes in column `N`, leave velocity `V` at default `64`, set instrument `I` to your instrument number.
- [ ] **Presets only.** No instrument editing this week.
- [ ] Save the project: Project View → `SAVE`.

## Thread 2: Synthesis fundamental — Oscillators

*Goal: train your ears to recognize the 5 fundamental wave shapes.*

- [ ] Open an empty instrument slot, set `TYPE` to `Wavsynth` (Wavsynth view, manual p.50).
- [ ] In Wavsynth, the `SHAPE` parameter cycles through wave types. Reference: Wavsynth Wave Table Index, p.82.
- [ ] Listen to each in isolation. Set envelope to default (Instrument Modulation View → MOD1 = `AHD ENVELOPE` with default values).
- [ ] Hit `[EDIT]+[PLAY]` to preview the instrument at each shape change.
- [ ] Mental notes (no need to write):
	- **Sine** — pure, sub-frequency, no harmonics
	- **Sawtooth** — bright, all harmonics, classic synth bass/lead
	- **Square** — hollow, only odd harmonics, "clarinet-y"
	- **Triangle** — mellow, mostly fundamental + weak harmonics
	- **Noise** — non-pitched, used for hats/snare/sweeps

## Thread 3: Arrangement principle — Identifying tension and release

*Goal: train your ear to spot what makes electronic tracks "arrive."*

- [ ] Pick 2–3 tracks you love (electronic, any genre — preferably tracks in your taste range).
- [ ] Listen to each once, fully. Identify the **single moment** everything was building toward.
- [ ] Note: it might be the full drop, a melodic entrance, a sudden silence, or a sound finally being unmuted. Could even be a *negative* arrival (everything drops out).
- [ ] Don't try to write one yet. Just notice.
- [ ] Reference (optional listening): [laamaa - seven weeks](https://laamaa.bandcamp.com/album/seven-weeks) — M8 album with source files. Notice how each track has a clear arc.

---

## 🎯 Deliverable

- [ ] Extend the 4-bar phrase into a 32-bar arrangement using **Chain View**. Each chain holds up to 16 phrases (manual p.12).
- [ ] Add basic dynamics: mute/unmute tracks across sections. Mute current track with `[OPTION]+[SHIFT]` from Song View.
- [ ] Render: navigate to Render View (manual p.47) and render the song to WAV.
- [ ] Save the WAV with today's date in the filename.
