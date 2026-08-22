# M8 Learning Plan

A 9-week structured plan for Dirtywave M8 producers who want to ship tracks again. Built collaboratively with Claude (Anthropic).

Mirror of the [Notion source](https://www.notion.so/Learning-M8-3656d3b8eb1381d6a5b1f60287a33180?source=copy_link).

## Structure

```
.
├── README.md                          # this file
├── CLAUDE.md                          # conventions for editing with Claude Code
├── overview.md                        # parent page content: gaps, principles, anti-burnout, resources
├── weeks/
│   ├── week-01.md                     # Week 1 — Re-entry
│   ├── week-02.md                     # Week 2 — LFO to filter + envelopes
│   ├── week-03.md                     # Week 3 — Pitch slides, Tracking, filters
│   ├── week-04.md                     # Week 4 — Retriggers, arpeggios, LFO concept
│   ├── week-05.md                     # Week 5 — Mix Project 1
│   ├── week-06.md                     # Week 6 — Finalize and ship Project 1
│   ├── week-07.md                     # Week 7 — Starter instrument library
│   ├── week-08.md                     # Week 8 — Build Project 2
│   ├── week-09.md                     # Week 9 — Finalize and ship Project 2
│   └── week-10.md                     # Week 10 — Scope B mix + master (optional)
├── reference/
│   ├── mixing.md                      # Mixing Reference
│   ├── finalization.md                # Finalization Reference
│   ├── generative.md                  # Generative Toolkit Reference
│   ├── timing.md                      # Timing Reference
│   ├── firmware.md                    # Firmware Reference
│   └── troubleshooting.md             # Troubleshooting Reference
├── translations/
│   └── ru/                            # complete Russian edition
├── build_pdf.py                       # generate the shareable PDF from markdown
└── notion-page-ids.txt                # Notion page IDs for sync
```

## Plan navigation

**Phase 1 — Learn (Weeks 1–4):** pure technique, no finishing pressure
- [Week 1 — Re-entry](weeks/week-01.md)
- [Week 2 — LFO to filter + envelopes](weeks/week-02.md)
- [Week 3 — Pitch slides, Tracking, filters](weeks/week-03.md)
- [Week 4 — Retriggers, arpeggios, LFO concept](weeks/week-04.md)

**Phase 2 — Apply (Weeks 5–7):** Project 1 finish + library
- [Week 5 — Mix Project 1](weeks/week-05.md)
- [Week 6 — Finalize and ship Project 1](weeks/week-06.md)
- [Week 7 — Starter instrument library](weeks/week-07.md)

**Phase 3 — Polish (Weeks 8–9):** Project 2
- [Week 8 — Build Project 2](weeks/week-08.md)
- [Week 9 — Finalize and ship Project 2](weeks/week-09.md)

**Optional**
- [Week 10 — Scope B mix + master in Ableton](weeks/week-10.md)

**Reference pages**
- [Mixing Reference](reference/mixing.md) — used Week 5 onwards for balancing tracks
- [Finalization Reference](reference/finalization.md) — used Week 6, 9, 10 for mastering
- [Generative Toolkit Reference](reference/generative.md) — generative features woven into Weeks 2, 4, 7, 8
- [Timing Reference](reference/timing.md) — ticks, PPQ, groove, `MTT`
- [Firmware Reference](reference/firmware.md) — firmware 6.6.0/6.6.1 changes relevant to the plan
- [Troubleshooting Reference](reference/troubleshooting.md) — device-level failures and their official fixes

## How to use this with Claude Code

Open this folder in Claude Code. Claude will read `CLAUDE.md` automatically and learn the conventions. Then:

- **To edit a week:** `edit weeks/week-N.md` or ask Claude to make changes
- **To regenerate the PDF:** install `requirements.txt`, then run `python3 build_pdf.py`
- **To build the Russian PDF:** `python3 build_pdf.py --lang ru`
- **To find a specific topic across all weeks:** `grep -r "PIT" weeks/` or ask Claude

## Notion sync philosophy

This bundle and the Notion page are mirrors. Keeping them in sync is a manual commitment, not automated. Suggested workflow:

- **Small in-flight edits (ticking checkboxes, adding a note in passing):** edit Notion directly. Don't bother syncing to markdown unless it's a structural change.
- **Big rewrites or restructuring:** edit markdown first, then mirror to Notion. Markdown is easier to do structural work in.
- **Reconcile periodically:** when you notice drift, fetch all Notion pages and re-export to markdown, or push markdown changes back to Notion. Whichever direction has more recent work wins.

Page IDs for each Notion page are stored in `notion-page-ids.txt` for easy lookup when syncing.

## Generating the PDF

The PDF is what you share with the M8 community on Telegram/Discord. To regenerate after edits:

```bash
python3 build_pdf.py
```

Outputs `M8_Learning_Plan.pdf` in the same directory.

The complete [Russian edition](translations/ru/README.md) mirrors all 17 source
Markdown files. Build it with:

```bash
python3 build_pdf.py --lang ru
```

This writes `translations/ru/M8_Learning_Plan_RU.pdf`. Generated PDFs are ignored
by Git and are not stored in the repository.

## Credit

Created by Danielyan ([t.me/sadbuttrue1](https://t.me/sadbuttrue1)), built collaboratively with Claude (Anthropic). M8 by Dirtywave (Timothy Lamb). Free to share, adapt, remix.
