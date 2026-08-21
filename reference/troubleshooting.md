# Troubleshooting Reference — When the M8 is the problem

**What this is:** the short list of hardware and file-level failures that stop a session dead, with the official fix for each. Keep it findable — the moment you need it, you can't get to the manual on the device.

**What this is NOT:** musical troubleshooting. If the track sounds wrong rather than the *device* behaving wrong, you want the [Mixing Reference](mixing.md) or [Finalization Reference](finalization.md) instead.

**Manual references:** Troubleshooting appendix (manual p.66–67), the microSD Card section (manual p.4), Firmware Updates (manual p.8).

**Model note:** everything here applies to Model:02 unless a Model:01 difference is called out.

---

## The M8 is unresponsive after a firmware update

This is recoverable. The M8 has a hardware bootloader that survives a failed flash.

**Two things that cause most failures in the first place** (manual p.66, p.8): flashing through a **USB hub**, and using a **charge-only cable**. Use a direct port and a known-good data cable — the one that shipped with the M8 is marked with a `DW` logo on the end.

**Recovery procedure** (manual p.66–67):

- [ ] Hold the power button for **10 seconds** to be certain the M8 is off.
- [ ] Connect the M8 to your computer with a known-good data cable. Avoid a hub if at all possible.
- [ ] Open **TyUploader** (not TyCommander).
- [ ] Turn the M8 on by holding power for 2 seconds. Depending on its state it may make no sound, and the screen may stay blank — with or without the backlight on. This is expected.
- [ ] With a SIM ejector key or a paperclip, press and release the **internal reset button** in the hole on the back of the M8, once.
- [ ] Wait about 10 seconds. A device should appear in TyUploader labelled `HalfKay…`.
- [ ] Click **Upload** and select the correct `.hex` file for your model, from `Firmware/Model01` or `Firmware/Model02` in the unzipped firmware download.
- [ ] The flash takes 10–20 seconds, then the M8 reboots. The new firmware version appears in the bottom-left corner of Song View for a few seconds.

*The manual prints the bootloader name as "HalfKey"; the string TyUploader actually shows is `HalfKay`, after the Teensy bootloader.*

**Host-side gotchas** (community, not in the manual):

- **Windows:** install a current TyTools build, and make sure you're launching the new copy rather than an older install still sitting in a previous folder.
- **macOS:** move `TyUploader.app` into `/Applications` and grant it permission under Settings → Privacy & Security. On macOS 14 and later this is usually required before the app can see the device.
- **Windows 7:** the USB driver comes from Teensyduino, which must be installed separately.

---

## A brand-new M8 won't turn on

- [ ] Plug it into a standard USB charger or host computer with the supplied cable and switch it on (manual p.66).
- [ ] Check the supply actually delivers enough power — the M8 wants USB-standard 5V 500mA (manual p.67).
- [ ] If it's still unresponsive, contact `support@dirtywave.com`.

*Community note:* units ship in a battery ship mode that prevents accidental power-on in transit. Connecting power is what wakes them.

---

## MIDI won't reach an external device

The M8's MIDI is **3.5mm TRS Type A**, in and out (manual p.91). Use the adapter that came with the unit, or another Type A adapter. **Type B will not work** — it's the single most common MIDI failure here, and it fails silently.

## A USB MIDI keyboard won't play the M8

The M8 is a USB MIDI *device*, not a USB MIDI *host*. You cannot plug a class-compliant keyboard straight into it. You need a computer in between, or a standalone USB MIDI host box — or use the TRS MIDI input instead.

## USB audio, USB MIDI, TyUploader, or the remote display don't work

Almost always the cable. Use the one supplied with the M8, or another cable you know carries data — many USB cables are power-only (manual p.67).

## The M8 isn't charging

The port needs to supply USB-standard 5V 500mA (manual p.67).

---

## Samples

### "Failed to load"

All three must be true (manual p.67):

- [ ] The file is **8, 16, 24, or 32-bit**, mono or stereo.
- [ ] The format is **PCM** or **PCM Raw**. Compressed WAVs do not work.
- [ ] The **entire path** is **under 128 characters** — every folder and subfolder name plus the filename, not just the filename.

The path limit is the one that bites, and it bites hardest when you drag a sample-pack folder tree across wholesale. Flatten the folders rather than shortening names into unreadable abbreviations.

### Samples aren't listed in the browser

You're in the Instrument Preset view rather than the Sample Load view (manual p.67).

### The note range is limited above `C-4`

Notes above `C-4` are limited by the sample's bit depth and channel count. Drop the bit depth in the Sample Editor — **16-bit is the recommended sampler bit depth** (manual p.67).

---

## microSD card

Samples are **streamed from the card during playback**, not loaded into memory. That makes the card's *random-access* read speed critical — far more important than its capacity or its sequential speed rating (manual p.4). Most cards are optimised for reading one file sequentially and struggle with several samples at once.

- [ ] Use a card from the tested list at `dirtywave.com/sd`.
- [ ] Format with the SD Association's SD Memory Card Formatter (`sdcard.org/downloads/formatter`). Not required for a new card, but recommended the moment you see trouble (manual p.4).
- [ ] If it's the factory card, reseat it first. If it still fails, contact Dirtywave support (manual p.67).

### "CPU TOO BUSY"

Almost always the SD card being overworked, not the CPU (manual p.67). Convert stereo samples to mono where stereo isn't doing anything, and reduce how many samples stream simultaneously (manual p.4).

### The card is stuck

The slot can be slightly larger than the card, so a misaligned insertion can trap it (manual p.4). Tweezers usually free it. On **Model:01** only, loosening the two screws on the left side of the case with a #2 metric hex tool gives enough clearance (manual p.67).

---

## Anti-panic rule

None of the above is a broken M8. A device that won't boot after a flash, a card that won't read, a sample that won't load — all of these have a documented fix, and none of them cost you the song. Work the checklist, and if it's genuinely hardware, `support@dirtywave.com` exists. Don't spend a session's energy on it: note where you got to, and come back.
