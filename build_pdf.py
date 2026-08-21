"""
M8 Learning Plan — PDF builder.

Reads the markdown files in this directory and renders them into a single
professional PDF suitable for sharing in the M8 community.

Reading order:
  1. Title page (hardcoded — note from the producer)
  2. Table of contents (auto-computed page numbers)
  3. overview.md
  4. weeks/week-01.md through weeks/week-10.md
  5. reference/mixing.md, finalization.md, generative.md,
     timing.md, firmware.md, troubleshooting.md
  6. About this document (closing page)

Usage:
  python3 build_pdf.py [output_filename.pdf]

Defaults to writing M8_Learning_Plan.pdf in the script's directory.
"""

import sys
import re
from pathlib import Path

from markdown_it import MarkdownIt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)

# ---------- Color palette ----------
INK = HexColor("#1a1a1a")
MUTED = HexColor("#666666")
RULE = HexColor("#cccccc")
ACCENT = HexColor("#0066cc")
CODE_BG = HexColor("#f4f4f4")
CALLOUT_BG = HexColor("#fff8e1")
SECTION_BG = HexColor("#f0f4f8")

# ---------- Styles ----------
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=32, leading=38,
    textColor=INK, alignment=TA_LEFT, spaceAfter=8,
)
subtitle_style = ParagraphStyle(
    "SubtitleStyle", parent=styles["Normal"],
    fontName="Helvetica", fontSize=14, leading=20,
    textColor=MUTED, alignment=TA_LEFT, spaceAfter=20,
)
h1 = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontName="Helvetica-Bold", fontSize=22, leading=28,
    textColor=INK, spaceBefore=18, spaceAfter=12, keepWithNext=True,
)
h2 = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontName="Helvetica-Bold", fontSize=15, leading=20,
    textColor=INK, spaceBefore=14, spaceAfter=6, keepWithNext=True,
)
h3 = ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontName="Helvetica-Bold", fontSize=12, leading=16,
    textColor=INK, spaceBefore=10, spaceAfter=4, keepWithNext=True,
)
body = ParagraphStyle(
    "Body", parent=styles["BodyText"],
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=INK, alignment=TA_LEFT, spaceAfter=8,
)
bullet = ParagraphStyle(
    "Bullet", parent=body, leftIndent=14, bulletIndent=2, spaceAfter=4,
)
sub_bullet = ParagraphStyle(
    "SubBullet", parent=body, leftIndent=28, bulletIndent=14, spaceAfter=3,
)
task = ParagraphStyle(
    "Task", parent=body, leftIndent=16, bulletIndent=0, spaceAfter=3, leading=14,
)
sub_task = ParagraphStyle(
    "SubTask", parent=body, leftIndent=30, bulletIndent=14, spaceAfter=3, leading=14,
)
callout = ParagraphStyle(
    "Callout", parent=body, fontSize=10, leading=14, textColor=INK,
    spaceBefore=4, spaceAfter=4,
)
caption = ParagraphStyle(
    "Caption", parent=body, fontSize=9, textColor=MUTED, spaceAfter=4,
)


# ---------- Helpers ----------
def callout_box(title, body_text, bg=CALLOUT_BG):
    inner = []
    if title:
        inner.append(Paragraph(f"<b>{title}</b>", callout))
    inner.append(Paragraph(body_text, callout))
    t = Table([[inner]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def on_page(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(MUTED)
    canvas_obj.drawString(
        2 * cm, 1.2 * cm,
        "M8 Learning Plan · Built collaboratively with Claude (Anthropic) · Free to share"
    )
    canvas_obj.drawRightString(
        A4[0] - 2 * cm, 1.2 * cm,
        f"{doc.page}"
    )
    canvas_obj.restoreState()


# ---------- Markdown → ReportLab inline conversion ----------

def md_inline_to_reportlab(text):
    """
    Convert Markdown inline syntax (bold, italic, code, links) to ReportLab
    paragraph markup. ReportLab uses HTML-like tags inside Paragraph.
    """
    # Escape ampersands first (but not entities)
    text = re.sub(r"&(?!\w+;)", "&amp;", text)
    # Escape angle brackets (but preserve them later for our tags)
    text = text.replace("<", "&lt;").replace(">", "&gt;")

    # Bold: **text** → <b>text</b>
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic: *text* → <i>text</i> (but not inside ** which we already handled)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    # Inline code: `text` → mono span with bg
    text = re.sub(
        r"`([^`]+)`",
        lambda m: f'<font face="Courier" size="9.5">{m.group(1)}</font>',
        text,
    )
    # Links: [text](url) → <link href="url" color="...">text</link>
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: (
            f'<link href="{m.group(2)}" color="#0066cc">{m.group(1)}</link>'
            if m.group(2).startswith("http")
            else m.group(1)  # local refs: just show the text
        ),
        text,
    )
    return text


# ---------- Markdown → flowables ----------

def parse_markdown_to_flowables(md_text):
    """
    Parse a markdown string into a list of ReportLab flowables.
    Handles: headings, paragraphs, bulleted lists (incl. nested),
    task checkboxes (- [ ] / - [x]), tables, blockquotes (as callouts),
    horizontal rules.
    """
    md = MarkdownIt("commonmark", {"html": False}).enable("table").enable("strikethrough")
    tokens = md.parse(md_text)

    flowables = []
    i = 0

    while i < len(tokens):
        tok = tokens[i]

        # Headings
        if tok.type == "heading_open":
            level = int(tok.tag[1])
            inline = tokens[i + 1].content
            style = {1: h1, 2: h2, 3: h3}.get(level, h3)
            flowables.append(Paragraph(md_inline_to_reportlab(inline), style))
            i += 3  # heading_open, inline, heading_close
            continue

        # Paragraphs
        if tok.type == "paragraph_open":
            inline = tokens[i + 1].content
            flowables.append(Paragraph(md_inline_to_reportlab(inline), body))
            i += 3
            continue

        # Bulleted/unordered lists
        if tok.type == "bullet_list_open":
            i = render_list(tokens, i, flowables, depth=0)
            continue

        # Horizontal rule
        if tok.type == "hr":
            flowables.append(Spacer(1, 4))
            t = Table([[""]], colWidths=[16 * cm], rowHeights=[1])
            t.setStyle(TableStyle([
                ("LINEABOVE", (0, 0), (-1, 0), 0.5, RULE),
            ]))
            flowables.append(t)
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Blockquote → callout
        if tok.type == "blockquote_open":
            i = render_blockquote(tokens, i, flowables)
            continue

        # Tables
        if tok.type == "table_open":
            i = render_table(tokens, i, flowables)
            continue

        # Code blocks (fenced)
        if tok.type == "fence":
            t = Table([[Paragraph(
                tok.content.replace("\n", "<br/>"),
                ParagraphStyle("CodeInner", parent=body,
                               fontName="Courier", fontSize=9.5, leading=13)
            )]], colWidths=[16 * cm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]))
            flowables.append(t)
            i += 1
            continue

        # Skip everything else (inline tokens already handled, close tokens skipped)
        i += 1

    return flowables


def render_list(tokens, start, flowables, depth=0):
    """
    Render a bullet_list. Returns the index after bullet_list_close.
    Handles nested lists by recursion.
    Task checkboxes ([ ] / [x]) are rendered with ▢ / ▣ prefix.
    """
    i = start + 1  # skip bullet_list_open
    while i < len(tokens) and tokens[i].type != "bullet_list_close":
        if tokens[i].type == "list_item_open":
            # Find the content of this list item
            j = i + 1
            item_content_paragraphs = []
            while tokens[j].type != "list_item_close":
                if tokens[j].type == "paragraph_open":
                    inline = tokens[j + 1].content
                    item_content_paragraphs.append(inline)
                    j += 3
                elif tokens[j].type == "bullet_list_open":
                    # Emit accumulated paragraphs first
                    for k, content in enumerate(item_content_paragraphs):
                        is_task, checked, stripped = parse_task(content)
                        bullet_style, task_style = pick_styles(depth)
                        if is_task:
                            mark = "▣" if checked else "▢"
                            flowables.append(Paragraph(
                                f"{mark}&nbsp;&nbsp;{md_inline_to_reportlab(stripped)}",
                                task_style
                            ))
                        else:
                            prefix = "•&nbsp;&nbsp;" if k == 0 else ""
                            flowables.append(Paragraph(
                                f"{prefix}{md_inline_to_reportlab(content)}",
                                bullet_style
                            ))
                    item_content_paragraphs = []
                    # Render nested list
                    j = render_list(tokens, j, flowables, depth=depth + 1)
                else:
                    j += 1

            # Emit any remaining paragraphs
            for k, content in enumerate(item_content_paragraphs):
                is_task, checked, stripped = parse_task(content)
                bullet_style, task_style = pick_styles(depth)
                if is_task:
                    mark = "▣" if checked else "▢"
                    flowables.append(Paragraph(
                        f"{mark}&nbsp;&nbsp;{md_inline_to_reportlab(stripped)}",
                        task_style
                    ))
                else:
                    prefix = "•&nbsp;&nbsp;" if k == 0 else ""
                    flowables.append(Paragraph(
                        f"{prefix}{md_inline_to_reportlab(content)}",
                        bullet_style
                    ))
            i = j + 1  # skip list_item_close
        else:
            i += 1
    return i + 1  # skip bullet_list_close


def parse_task(text):
    """
    Detect `[ ] something` or `[x] something` at the start.
    Returns (is_task, is_checked, stripped_text).
    """
    m = re.match(r"^\[([ xX])\]\s+(.*)$", text, re.DOTALL)
    if not m:
        return False, False, text
    checked = m.group(1).lower() == "x"
    return True, checked, m.group(2)


def pick_styles(depth):
    """Return (bullet_style, task_style) for a given nesting depth."""
    if depth == 0:
        return bullet, task
    return sub_bullet, sub_task


def render_blockquote(tokens, start, flowables):
    """Render a blockquote as a callout box. Returns index after close."""
    i = start + 1
    paragraphs = []
    while i < len(tokens) and tokens[i].type != "blockquote_close":
        if tokens[i].type == "paragraph_open":
            paragraphs.append(tokens[i + 1].content)
            i += 3
        else:
            i += 1
    body_text = "<br/><br/>".join(md_inline_to_reportlab(p) for p in paragraphs)
    flowables.append(callout_box(None, body_text, bg=SECTION_BG))
    return i + 1


def render_table(tokens, start, flowables):
    """Render a markdown table. Returns index after table_close."""
    i = start + 1
    rows = []
    current_row = []
    is_header_row = False
    in_header = False

    while i < len(tokens) and tokens[i].type != "table_close":
        tok = tokens[i]
        if tok.type == "thead_open":
            in_header = True
        elif tok.type == "thead_close":
            in_header = False
        elif tok.type == "tr_open":
            current_row = []
            is_header_row = in_header
        elif tok.type == "tr_close":
            rows.append((current_row, is_header_row))
        elif tok.type in ("th_open", "td_open"):
            # Find inline content
            j = i + 1
            if tokens[j].type == "inline":
                current_row.append(tokens[j].content)
        i += 1

    # Build the ReportLab table
    if not rows:
        return i + 1

    col_count = len(rows[0][0])
    col_widths = [16 * cm / col_count] * col_count

    table_data = []
    header_indices = []
    for idx, (row_cells, is_header) in enumerate(rows):
        cell_paragraphs = []
        for cell_text in row_cells:
            style = ParagraphStyle(
                "TableCell", parent=body, fontSize=9, leading=12,
                fontName="Helvetica-Bold" if is_header else "Helvetica",
            )
            cell_paragraphs.append(Paragraph(md_inline_to_reportlab(cell_text), style))
        table_data.append(cell_paragraphs)
        if is_header:
            header_indices.append(idx)

    t = Table(table_data, colWidths=col_widths)
    table_style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.3, RULE),
    ]
    for hi in header_indices:
        table_style.append(("BACKGROUND", (0, hi), (-1, hi), SECTION_BG))
    t.setStyle(TableStyle(table_style))
    flowables.append(t)
    flowables.append(Spacer(1, 10))

    return i + 1


# ---------- Two-pass build (to compute real TOC page numbers) ----------

def build_story(toc_data=None):
    """
    Build the full story (list of flowables). If toc_data is None, use
    placeholder page numbers (this is pass 1, to discover real positions).
    If toc_data is provided, use those page numbers in the TOC.
    """
    here = Path(__file__).resolve().parent
    story = []

    # --- Title page ---
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph("M8 Learning Plan", title_style))
    story.append(Paragraph(
        "A 9-week structured plan for M8 producers<br/>"
        "who want to ship tracks again.",
        subtitle_style
    ))
    story.append(Spacer(1, 1 * cm))
    story.append(callout_box(
        "A note before you read",
        "I built this for myself with Claude (Anthropic) after realizing I had a "
        "drawer full of trackers, grooveboxes and samplers but no recent finished "
        "tracks. The diagnosis was simple: I kept buying new gear to spark ideas "
        "instead of going deeper into the tools that already worked for me. M8 was "
        "the one that produced finished work in the past, so I built a plan to "
        "rebuild fluency, close my real gaps (instrument tables, sound design, "
        "arrangement, mixing, mastering), and ship tracks again.<br/><br/>"
        "Sharing it here in case it helps anyone else stuck in the same loop. "
        "It's generalized — no personal references — but the structure and the "
        "specific corrections are real. Take what's useful, ignore the rest.",
        bg=SECTION_BG,
    ))
    story.append(Spacer(1, 1.5 * cm))
    story.append(Paragraph(
        "<b>What this plan covers:</b> M8 technique, synthesis fundamentals, "
        "arrangement, on-device mixing, on-device finalization, optional Ableton "
        "post-production. Verified against M8 firmware 6.5.2.",
        body
    ))
    story.append(Paragraph(
        "<b>Time commitment:</b> 2–3 focused sessions per week, ~60 min each. "
        "~20 hours total over Weeks 1–9. Optional Week 10 adds ~3 hours.",
        body
    ))
    story.append(Paragraph(
        "<b>Outcome:</b> Two shipped tracks in ~9 weeks. After that, ~4–5 weeks "
        "per release-ready track sustainably.",
        body
    ))
    story.append(PageBreak())

    # --- Table of contents ---
    story.append(Paragraph("Contents", h1))
    toc_items = [
        ("Overview & operating principles", "overview"),
        ("    Resources", "resources"),
        ("Phase 1 — Learn (Weeks 1–4)", None),
        ("    Week 1 — Re-entry", "week-01"),
        ("    Week 2 — LFO to filter + envelopes", "week-02"),
        ("    Week 3 — Pitch slides, Tracking, filters", "week-03"),
        ("    Week 4 — Retriggers, arpeggios, LFO concept", "week-04"),
        ("Phase 2 — Apply (Weeks 5–7)", None),
        ("    Week 5 — Mix Project 1", "week-05"),
        ("    Week 6 — Finalize and ship Project 1", "week-06"),
        ("    Week 7 — Starter instrument library", "week-07"),
        ("Phase 3 — Polish (Weeks 8–9)", None),
        ("    Week 8 — Build Project 2", "week-08"),
        ("    Week 9 — Finalize and ship Project 2", "week-09"),
        ("Optional", None),
        ("    Week 10 — Scope B mix + master in Ableton", "week-10"),
        ("References", None),
        ("    Mixing Reference", "ref-mixing"),
        ("    Finalization Reference", "ref-finalization"),
        ("    Generative Toolkit Reference", "ref-generative"),
        ("    Timing Reference", "ref-timing"),
        ("    Firmware Reference", "ref-firmware"),
        ("    Troubleshooting Reference", "ref-troubleshooting"),
    ]
    toc_rows = []
    for title, key in toc_items:
        page_num = ""
        if key and toc_data:
            page_num = str(toc_data.get(key, ""))
        is_section = key is None
        # Convert leading 4-space indent to &nbsp; so it renders
        display_title = title.replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;", 1)
        if is_section:
            toc_rows.append([Paragraph(f"<b>{display_title}</b>", body), ""])
        else:
            toc_rows.append([
                Paragraph(display_title, body),
                Paragraph(page_num, body),
            ])
    toc_table = Table(toc_rows, colWidths=[14 * cm, 2 * cm])
    toc_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    # --- Overview ---
    section_anchors = {}  # key → flowable index
    section_anchors["overview"] = len(story)
    overview_md = (here / "overview.md").read_text()
    # The overview file starts with "# M8 Learning Plan — Overview".
    # We rewrite it to "Overview & operating principles" since that's what the
    # TOC and traditional document structure expect.
    overview_md = overview_md.replace(
        "# M8 Learning Plan — Overview",
        "# Overview & operating principles",
        1
    )
    story.extend(parse_markdown_to_flowables(overview_md))
    # Note: "Resources" is part of overview.md, lives in the same file at "## Resources"
    # The TOC entry for "Resources" maps to the same section - we'll mark it at
    # the right point during rendering. For simplicity, point it to overview.
    section_anchors["resources"] = section_anchors["overview"]

    # --- Weeks ---
    for i in range(1, 11):
        story.append(PageBreak())
        section_anchors[f"week-{i:02d}"] = len(story)
        week_md = (here / "weeks" / f"week-{i:02d}.md").read_text()
        story.extend(parse_markdown_to_flowables(week_md))

    # --- References ---
    for name, key in [
        ("mixing", "ref-mixing"),
        ("finalization", "ref-finalization"),
        ("generative", "ref-generative"),
        ("timing", "ref-timing"),
        ("firmware", "ref-firmware"),
        ("troubleshooting", "ref-troubleshooting"),
    ]:
        story.append(PageBreak())
        section_anchors[key] = len(story)
        ref_md = (here / "reference" / f"{name}.md").read_text()
        story.extend(parse_markdown_to_flowables(ref_md))

    # --- Closing page ---
    story.append(PageBreak())
    story.append(Spacer(1, 6 * cm))
    story.append(Paragraph("About this document", h1))
    story.append(Paragraph(
        "This plan was built collaboratively between a producer and Claude "
        "(Anthropic) over an extended conversation. The producer brought the gear "
        "history, the personal weaknesses, the priorities, and the corrections. "
        "Claude pulled references from the M8 manual (firmware 6.5.2) and the "
        "<font face=\"Courier\">awesome-m8</font> community list, structured the "
        "plan into phases and weeks, and helped enforce time-boxes and "
        "anti-perfectionism rules.",
        body
    ))
    story.append(Paragraph(
        "It's been generalized for sharing. The structure is real; the framing is "
        "real; the anti-perfectionism rules are real. The personal details have "
        "been removed.",
        body
    ))
    story.append(Paragraph(
        "<b>License:</b> free to share, adapt, remix. If it helps you finish "
        "tracks, that's the point.",
        body
    ))
    story.append(Paragraph(
        "<b>Credit:</b> Created by Danielyan "
        "(<a href=\"https://t.me/sadbuttrue1\">t.me/sadbuttrue1</a>), built "
        "collaboratively with Claude (Anthropic). M8 by Dirtywave (Timothy Lamb).",
        body
    ))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "<i>If you build a track using this plan, consider sharing it back to the "
        "M8 community. The point isn't the plan, it's finished music.</i>",
        body
    ))

    return story, section_anchors


def get_page_for_flowable_index(doc_path, section_anchors):
    """
    Render the PDF once, then walk the rendered pages to find which page
    each section actually starts on. Uses pypdf to read back.
    """
    from pypdf import PdfReader
    reader = PdfReader(doc_path)

    # Heuristic: scan the rendered PDF for each section's title text.
    # We use a mapping from anchor key → expected title prefix.
    title_map = {
        "overview": "Overview & operating principles",
        "resources": "Resources",
        "week-01": "Week 1 — Re-entry",
        "week-02": "Week 2 — LFO to filter",
        "week-03": "Week 3 — Pitch slides",
        "week-04": "Week 4 — Retriggers",
        "week-05": "Week 5 — Mix Project 1",
        "week-06": "Week 6 — Finalize and ship Project 1",
        "week-07": "Week 7 — Starter instrument library",
        "week-08": "Week 8 — Build Project 2",
        "week-09": "Week 9 — Finalize and ship Project 2",
        "week-10": "Week 10 — Scope B mix + master",
        "ref-mixing": "Mixing Reference",
        "ref-finalization": "Finalization Reference",
        "ref-generative": "Generative Toolkit Reference",
        "ref-timing": "Timing Reference",
        "ref-firmware": "Firmware Reference",
        "ref-troubleshooting": "Troubleshooting Reference",
    }
    result = {}
    for key, title in title_map.items():
        for i, page in enumerate(reader.pages):
            if i < 2:
                # Skip title page and TOC page
                continue
            text = page.extract_text()
            # Strip the footer prefix to isolate page-body content.
            # Footer looks like: "M8 Learning Plan · ... · Free to share\nNN\n<body>"
            body_start = text.find("Free to share")
            if body_start == -1:
                continue
            # Skip past "Free to share\n" + page number + "\n"
            body = text[body_start + len("Free to share"):].lstrip()
            # Skip the page-number line
            if "\n" in body:
                body = body.split("\n", 1)[1]
            # Now body starts with the actual page content. The heading is
            # the very first thing on a section-start page.
            if body.startswith(title):
                result[key] = i + 1
                break
    return result


# ---------- Main ----------

def main():
    output_filename = sys.argv[1] if len(sys.argv) > 1 else "M8_Learning_Plan.pdf"
    output_path = Path(__file__).resolve().parent / output_filename
    tmp_path = output_path.with_suffix(".tmp.pdf")

    # Pass 1: render without page numbers in TOC
    story, _ = build_story(toc_data=None)
    doc = SimpleDocTemplate(
        str(tmp_path),
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="M8 Learning Plan",
        author="Danielyan (t.me/sadbuttrue1)",
    )
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    # Discover real page numbers for headings
    page_map = get_page_for_flowable_index(str(tmp_path), {})

    # Special case: Resources is a sub-section inside overview.md.
    # Find the page where "Resources" appears as an H2 within the overview.
    from pypdf import PdfReader
    reader = PdfReader(str(tmp_path))
    overview_page = page_map.get("overview", 3)
    for i, page in enumerate(reader.pages):
        if i + 1 < overview_page:
            continue
        # Stop searching once we hit Week 1 (overview is done)
        text = page.extract_text()
        if "Week 1 — Re-entry" in text:
            body_start = text.find("Free to share")
            if body_start != -1:
                body = text[body_start + len("Free to share"):].lstrip()
                if "\n" in body:
                    body = body.split("\n", 1)[1]
                if body.startswith("Week 1 — Re-entry"):
                    break
        # Look for "Resources" as a heading (appears bolded, after a blank-ish line)
        # In extracted text, headings appear on their own line.
        if "\nResources\n" in text:
            page_map["resources"] = i + 1
            break

    # Pass 2: render with real page numbers
    tmp_path.unlink()
    story, _ = build_story(toc_data=page_map)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="M8 Learning Plan",
        author="Danielyan (t.me/sadbuttrue1)",
    )
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    print(f"Built {output_path.name} ({doc.page} pages)")


if __name__ == "__main__":
    main()
