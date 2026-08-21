# Week 1 — Re-entry

**Goal:** Remove cold-start friction. Rebuild muscle memory. No new techniques — prove the device still works for you.
**Mindset:** Deliberately low bar. Success = boot it, use it, render something.
**Manual references:** Getting Started (manual p.5), Navigation (manual p.6), Global Key Shortcuts (manual p.7), Loading a Demo Song (manual p.9), Song View (manual p.10), Chain View (manual p.12), Phrase View (manual p.14), Mixer View (manual p.31), Render View (manual p.47).

---

## Thread 1: M8 technique — Re-entry

### Boot and recall

- [ ] Charge M8 if battery low. Boot with power button (right side, 1 sec hold). Reference: Powering Up, p.3.
	- If it won't boot, a sample won't load, or the card misbehaves, the fix is almost certainly in the [Troubleshooting Reference](../reference/troubleshooting.md). Don't lose the session to it.
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
		- **Note on sliced kit files:** if you load a multi-hit drum chain into one Sampler with `SLICE 00OFF`, it just plays the whole file pitched by note — not what you want. To trigger slices chromatically you need slice markers (via the Sample Editor's `AUTO` or `SILENCE` modes) plus the `SLICE` parameter set to `FILE` in Instrument View. **Skip this for Week 1** — it's covered in Week 7.
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
- [ ] Enable `NOTE PREVIEW` in System Settings (manual p.40), then audition each shape in **Phrase view** (manual p.14): drop the instrument in a step and move the note with `[EDIT]+[LEFT/RIGHT]` (semitone) or `[EDIT]+[UP/DOWN]` (octave). `[EDIT]+[PLAY]` from the Instrument view also works but only previews at a fixed low pitch.
- [ ] Mental notes (no need to write):
	- **Sine** — pure, sub-frequency, no harmonics
	- **Sawtooth** — bright, all harmonics, classic synth bass/lead
	- **Square** — hollow, only odd harmonics, "clarinet-y" (on Wavsynth this is `PULSE 50%`; there's no shape literally labeled "Square")
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

Arrangement on the M8 happens in **Song View** — it stacks one chain per track down the rows, and each track's playhead runs through its chains independently (manual p.10). A chain is a sequence of up to 16 phrases (manual p.12). You'll turn your 4-bar loop into a short arrangement with real dynamics.

- [ ] **Get your loop into a chain per track.** In each track's Song column, place a chain that plays your 4-bar loop (the phrases you wrote this week). Keep every chain the same length so the tracks stay aligned — the manual recommends this explicitly (manual p.10).
- [ ] **Stack Song rows into ~32 bars with an arc.** Add rows in Song View until the song runs ~32 bars (e.g. eight rows of your 4-bar chain). Shape a simple arc by what's present each row: intro (drums only) → add bass → add melody → full → strip back.
- [ ] **Drop tracks out with empty-phrase chains — not mutes.** To silence a track for a section while keeping it locked to the others, put a chain of *empty* phrases in that track's cell for those rows. By convention this is chain `00` or `FE` (manual p.10); empty/no-note chains show grayed-out in Song View. This bakes the dynamics into the arrangement, so they survive a save and render correctly.
	- *Why not the mute button? Live mute/solo (`[OPTION]+[SHIFT]` / `[OPTION]+[PLAY]`, Mixer View, manual p.31) is a real-time performance control — it isn't stored in the song structure, so it's the wrong tool for composing sections. Use it to audition, not to arrange.*
	- *Optional, and it pays off as projects grow: **number by column.** Phrases and chains are a global pool shared across all 8 tracks (manual p.12), so the M8 gives you no hint about which column a chain belongs to — supply it yourself. Give each Song column its own range so the leading hex digit tells you which track a chain/phrase belongs to: column `00` → `00`–`0F`, column `01` → `10`–`1F`, and so on. Then a glance at a number confirms you're editing the right column. Keep empties (`FE`) and any shared/utility chains up in a high range so they sit outside the per-column blocks. Trade-off: this cuts against reusing one phrase/chain across tracks (the other strength of the global pool) — bend it when you deliberately want a shared element.*
- [ ] Render: navigate to Render View (manual p.47) and render the song to WAV.
- [ ] Save the WAV with today's date in the filename.
