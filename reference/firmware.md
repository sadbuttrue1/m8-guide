# Firmware Reference — What changed since 6.5.2

**What this is:** the changes in firmware **6.6.0** and **6.6.1** that affect exercises in this plan, plus the new on-device update path. The rest of this plan is written against the **6.5.2** manual, so this page is where the two meet.

**What this is NOT:** a changelog mirror. The full list lives at the [official Dirtywave changelog](https://github.com/Dirtywave/M8Firmware/blob/main/changelog.txt) and will always be more complete than this page. Only what changes what you *do* in a week is repeated here.

**Sources:** [Dirtywave M8 firmware changelog](https://github.com/Dirtywave/M8Firmware/blob/main/changelog.txt) and [firmware readme](https://github.com/Dirtywave/M8Firmware/blob/main/readme.txt). These describe firmware newer than the 6.5.2 manual, so page citations don't apply — verify parameter details in-device.

---

## Two fixes that make Week 7 recipes reliable

Week 7's Table `TIC` recipes and the Generative Toolkit's `TIC` section both depend on map modes behaving predictably. Two 6.6.0 fixes matter directly:

- **`TIC:FD` (Velocity Map) now retriggers on velocity changes, not note changes.** Before this it re-fired when the note changed, which is exactly backwards for a velocity-mapped drum. If you tried a velocity-mapped instrument on an older firmware and it behaved erratically, this was why.
- **`TIC:FE` (Note Map) and `TIC:FC` (Octave Map) no longer retrigger** merely because a volume value changed in a phrase, or because of a `TBX` command.

If you're on 6.6.0 or later, [Week 7 → Option A](../weeks/week-07.md) and [Generative Toolkit → #4](generative.md) do what they say. On 6.5.x, expect the wobble.

---

## Hypersynth gained a `SHAPE` parameter

6.6.0 adds a `SHAPE` parameter to Hypersynth with twelve options:

`SAW`, `SOFT SAW`, `DARK SAW`, `SQUARE SOFT`, `TRIANGLE`, `SINE`, `SINE 3X`, `SINE FB`, `SINE FOLD`, `SINE RING`, `SINE HALF`, `SINE ORGAN`

This splits a decision that used to be one knob: **the chord structure** and **the character of the source** are now chosen separately. When building a Hypersynth chord instrument in Week 7 or exploring it in the Generative Toolkit, pick the harmonic structure first, then audition shapes against it — a `DARK SAW` and a `SINE ORGAN` on the same voicing are different instruments.

6.6.0 also improves Hypersynth sub-oscillator interpolation.

---

## Faster command entry (6.6.1)

**Tapping `[EDIT]` on a parameter in Mixer View or Effect Settings captures its FX command.** Tapping `[EDIT]` in a Phrase or Table FX column then inserts it.

This is the same capture-and-paste idea that already worked for Instrument parameters, extended to the mixer and effects. In Week 2 it removes the hunt for the cutoff command; in Week 8 it speeds up writing effect automation. The in-device **Effect Command Help view** (manual p.48) is still how you confirm a command is valid for the current instrument type — capture tells you the name, not whether it applies.

---

## Song View arrangement tools

Three additions that matter in Week 8, when you're moving whole sections around:

- **Whole-row selection.** On Track 1, press `[LEFT]` twice to select the entire Song View row. `[PLAY]` queues that row; `[EDIT]+[UP/DOWN]` moves it, carrying its bookmark with it. (6.6.0)
- **Coloured row bookmarks.** With a row selected, `[OPT]+[LEFT/RIGHT]` or `[EDIT]+[LEFT/RIGHT]` cycles through theme colours and variants; `[OPT]+[EDIT]` clears. Use one colour for build, one for the arrival, one for release — Week 8's structural arc becomes visible at a glance. (6.6.0)
- **Third-level clone includes instruments.** In selection mode, applying `SELECT+EDIT` a third time clones the instruments used by the selection as well as the structure, including instruments called by `INS` and `NXT`. This is the safe way to make a variation of a section without editing the original section's instruments. (6.6.1)

---

## Mixing and rendering

- **`EQ View` has a spectrum analyser.** (6.6.0) Useful in Weeks 5 and 8 for *seeing* a 200–400Hz build-up or a kick/bass collision — but a graph shows you that energy is present, not whether it's musically wrong. Decide by ear, confirm on two systems. See [Mixing Reference](mixing.md). A 6.6.1 fix stops the spectrum graph from taking priority over sample playback under heavy sample load, so it's safer to leave open on sample-heavy projects.
- **`ModFX` gains a Comb filter type.** (6.6.0) Worth trying in Week 8's effects-as-sound-design thread. Small depth on percussion, plucks or noise; heavy feedback turns it into a pronounced tonal resonance fast.
- **Render fixes** (6.6.0) that matter for Week 10 stem exports: renders with many `TPO` tempo changes now line up correctly with a DAW's tempo grid, Quick Render length is no longer slightly off, and the messy initial transient on Quick Render with OTT enabled is fixed.
- **`ADSR ENV` same-instrument retrigger now resumes attack from the current envelope level** (6.6.0) rather than restarting from zero. Repeated notes and legato-style figures are smoother — relevant to the acid line in Week 3 and the retrigger work in Week 4.

---

## Updating from the microSD card

From 6.6 onward the M8 can flash itself from the card — no computer, no TyUploader.

**Prerequisite:** the M8 must already be running **6.6 or newer**. Getting *to* 6.6 from an older version is still a one-time USB update.

- [ ] Unzip the firmware download.
- [ ] Copy the correct `.bin` for your model from `Firmware/Model01` or `Firmware/Model02` to anywhere on the microSD card — via `USB-DRIVE` in Project View, or by taking the card out.
- [ ] If you used `USB-DRIVE`, eject it properly first.
- [ ] On the M8: `PROJECT` → `SYSTEM SETTINGS` → `FIRMWARE UPDATE`.
- [ ] Select the `.bin` and confirm.
- [ ] The M8 restarts and updates. **Do not remove the card while it runs.**

If it fails, fall back to the USB route — see [Troubleshooting Reference](troubleshooting.md#the-m8-is-unresponsive-after-a-firmware-update).

---

## Should you update mid-plan?

**Between projects, not during one.** A firmware update in the middle of Week 8 is a change of instrument, and this plan's whole structure is built on finishing things rather than re-tuning them. Finish the track, then update.

The exception is the `TIC:FD` fix — if you're heading into Week 7 and velocity mapping is misbehaving, that's a real bug you'd otherwise spend an hour blaming yourself for.
