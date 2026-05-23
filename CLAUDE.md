# Conventions for editing this plan

This file gives Claude Code context on how the M8 Learning Plan is structured and how to edit it consistently.

## What this is

A 9-week structured plan (+ optional Week 10) for a producer learning the Dirtywave M8 tracker. The plan also exists in Notion.

The plan was generalized for sharing in the M8 community on Telegram. **The markdown files are the generalized source that feeds the community-shareable PDF** — keep them clean of personal detail. **The Notion copy is the personal working version and can/should carry more personal phrasing** (first-person notes, references to the author's own history, etc.). The two therefore diverge in *voice* by design — that divergence is not "drift" to be flattened. Markdown is the source of truth for **facts, structure, and technique**; Notion owns **personal tone**.

## Conventions used throughout

### Task lists
Use markdown checkboxes for actionable tasks:
```
- [ ] Do this thing
- [ ] Then this thing
```

### Code formatting
- M8 commands, parameter names, and hex values: inline backticks. Examples: `PIT`, `TABLE TIC`, `TICFD`, `SLI01`, `C-4`, `00`.
- Keyboard shortcuts: bracket notation in bold or backticks. Examples: `[SHIFT]+[UP]`, `[EDIT]+[PLAY]`.
- File paths: backticks. Examples: `/Samples/`, `kick.wav`.
- Notation values (with arrows or em dashes): plain text is fine.

### Structure of each week
Every week page follows this template:

```markdown
# Week N — [Title]

**Goal:** One-sentence statement of what you'll achieve this week.
**Mindset:** (optional) the disposition needed for the week.
**Manual references:** Page numbers from the M8 manual.

---

## Thread 1: M8 technique — [Subject]
(Tasks)

## Thread 2: Synthesis fundamental — [Subject]
(Tasks)

## Thread 3: Arrangement principle — [Subject]
(Tasks)

---

## 🎯 Deliverable
(What's done at the end of the week)
```

Weeks 5 onwards may have different thread structures (mix sessions, library building, finalize sessions). Follow each week's existing structure.

### Reference page conventions

Reference pages (`reference/*.md`) have a different structure — more like documentation. They're consulted from week pages via links. Each reference page typically has:

- "What this is / What this is NOT" framing
- The core mental model (5 dimensions of a mix, 6 generative techniques, etc.)
- Concrete recipes with task lists
- Common failure modes
- Anti-perfectionism rules
- "When things fail" troubleshooting

### Cross-linking

- Week → Reference: link to `../reference/<name>.md` or use a section anchor like `[Mixing Reference](../reference/mixing.md)`.
- Reference → Reference: link via relative path.
- Both → Notion (for users who prefer that view): linked from the README, not from individual pages.

## Common edit patterns

### Adding a new technique to a week
1. Identify which thread it fits under (M8 technique / synthesis / arrangement / mix focus).
2. Add a `### Subheading` for the technique.
3. Lead with **Use case:** and **Recipe:** followed by a task list.
4. End with **Common failure mode:** so the reader knows why it might not click.

### Cross-referencing the Generative Toolkit
Many M8 techniques have a fuller treatment in the Generative Toolkit Reference. When adding a technique that's also in there, link to it:
```
*See [Generative Toolkit Reference](../reference/generative.md) → #N for full context.*
```

### Manual references
The M8 Operation Manual is the source of truth for M8 specifics. When adding factual claims about M8 behavior, include the manual page number: `(manual p.18)` or `(p.18)`. This keeps the plan trustworthy.

## What this plan is NOT

- It's not a manual replacement — the M8 manual is canonical for device behavior.
- It's not pro mixing/mastering tuition — the references are "functional mixing" / "finalization," not pro work.
- It's not a fixed gospel — the user is encouraged to ignore or adapt parts that don't fit.

## Things to watch out for when editing

- **Don't claim M8 features without manual verification.** If you're unsure whether a command exists or what its parameters are, verify it first via the `m8-agent` MCP tool (see below). Only fall back to "check the in-device Effect Command Help" when the index has no good answer — never invent specifics.
- **Hypersynth specifics are not fully documented in this plan.** The Hypersynth section in the Generative Toolkit Reference deliberately says "verify exact parameters in-device" because the manual section is dense and I didn't pull all details. Don't fabricate Hypersynth parameter values.
- **The "drum kit" loading approach in M8 is non-obvious.** Week 1 uses three separate Sampler instruments (one sound per instrument). Week 7 covers sliced kits using AUTO/SILENCE slice modes + chromatic playback via the SLICE parameter. Don't accidentally re-introduce the "load a kit" phrasing — M8 has no kit concept.
- **Time-boxes are structural defenses against perfectionism.** Every mix session has a 60-min hard limit; every master pass has a max-2-passes rule. Don't soften these even if it seems harsh — they're load-bearing.

## Verifying M8 facts: the m8-agent MCP tool

Before writing any factual claim about M8 behavior, search the local index via `mcp__m8-agent__search_m8`. It covers the official manual, The M8 Companion, the Open M8 Tips doc, and 144 community videos, and returns cited chunks with deep-link `citation_url`s. (`mcp__m8-agent__get_m8_stats` just reports index counts.)

- For device facts and page numbers, scope to the manual: `sources: ["manual"]`. Use the returned page for the `(p.X)` citation convention.
- Community sources (`companion`, `community_tips`, `video`) are good for technique and recipes — frame them as community knowledge, not device fact.
- If official and community sources conflict, describe both.

This is the first move for verification, and supersedes the older "point the user to in-device Effect Command Help" advice. The pdftotext workflow on the gitignored manual PDF still works for reading a full page, but `search_m8` is faster and returns a citable URL.

## Sync to Notion

**Rule: after every set of markdown edits in this repo, Claude must mirror the *substantive* change (facts, structure, tasks, page citations) to the corresponding Notion page via the `mcp__m8-guide__notion-*` MCP tools.** Do this as part of finishing the task — not as a separate step the user has to request. If the sync fails (auth, missing page, structural mismatch), surface the failure rather than silently dropping it.

**Preserve Notion's personal phrasing.** When the Notion passage you're editing has personal/first-person wording the generalized markdown lacks, fold the factual change *into* that wording — don't replace the personal voice with the generalized markdown text. (E.g. fix a wrong page number inside the personal sentence; don't swap the whole sentence for the neutral one.)

Page-ID mapping (markdown file → Notion page) lives in `notion-page-ids.txt`:
- `overview.md` → parent "Learning M8" page
- `weeks/week-0N.md` → Week N page
- `reference/<name>.md` → matching reference page
- `CLAUDE.md` and `README.md` are repo-local — no Notion counterpart.

Use targeted updates (`notion-update-page` with search-and-replace style content edits) for small changes. Reserve full-page replacement for structural rewrites. Don't run a blanket reconciliation in either direction to make the two identical — voice differences are intentional. Never copy Notion's personal phrasing back into the markdown (it feeds the shared PDF); only pull genuine structural/factual fixes that direction.

The PDF (`build_pdf.py` → `M8_Learning_Plan.pdf`) is a separate concern — only regenerate when the user asks or when the change is structural enough to warrant a refreshed share artifact.

## Generating the PDF

`build_pdf.py` reads all the markdown files and renders a single shareable PDF. The PDF visual style is intentionally clean/professional rather than retro/tracker-aesthetic — it has to render well on phone screens (Telegram users).

After editing markdown, run `python3 build_pdf.py` to regenerate. The TOC page numbers are computed automatically from the rendered output.
