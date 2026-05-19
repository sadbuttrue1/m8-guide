# Conventions for editing this plan

This file gives Claude Code context on how the M8 Learning Plan is structured and how to edit it consistently.

## What this is

A 9-week structured plan (+ optional Week 10) for a producer learning the Dirtywave M8 tracker. The plan also exists in Notion. Both should stay roughly in sync.

The plan was generalized for sharing in the M8 community on Telegram. The PDF version is the deliverable people download; the markdown files are the source of truth for editing.

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

- **Don't claim M8 features without manual verification.** If you're unsure whether a command exists or what its parameters are, point the user to the in-device Effect Command Help view rather than inventing specifics.
- **Hypersynth specifics are not fully documented in this plan.** The Hypersynth section in the Generative Toolkit Reference deliberately says "verify exact parameters in-device" because the manual section is dense and I didn't pull all details. Don't fabricate Hypersynth parameter values.
- **The "drum kit" loading approach in M8 is non-obvious.** Week 1 uses three separate Sampler instruments (one sound per instrument). Week 7 covers sliced kits using AUTO/SILENCE slice modes + chromatic playback via the SLICE parameter. Don't accidentally re-introduce the "load a kit" phrasing — M8 has no kit concept.
- **Time-boxes are structural defenses against perfectionism.** Every mix session has a 60-min hard limit; every master pass has a max-2-passes rule. Don't soften these even if it seems harsh — they're load-bearing.

## Sync to Notion

After editing markdown, you can mirror changes to Notion using its MCP integration. Page IDs are in `notion-page-ids.txt`. The Notion API uses the `update_content` command with `content_updates` (search-and-replace) for targeted edits. Whole-page replacement is also possible via `replace_content`.

Reverse direction (Notion → markdown): use the `notion-fetch` MCP tool to retrieve a page's content, then write back to the corresponding markdown file.

## Generating the PDF

`build_pdf.py` reads all the markdown files and renders a single shareable PDF. The PDF visual style is intentionally clean/professional rather than retro/tracker-aesthetic — it has to render well on phone screens (Telegram users).

After editing markdown, run `python3 build_pdf.py` to regenerate. The TOC page numbers are computed automatically from the rendered output.
