"""
M8 Learning Plan — PDF builder.

Renders a source directory of Markdown into a single shareable PDF.

This script holds no prose and no per-language content. Everything a language
needs lives beside its Markdown in the source directory:

  front-matter.md   cover page: title, subtitle, note callout, summary lines
  strings.json      UI chrome: footer, "Contents", TOC group labels, output name
  overview.md       ) the plan itself, in the order given by SECTIONS below
  weeks/*.md        )
  reference/*.md    )
  about.md          closing page

Section titles in the table of contents are read from each file's own `#`
heading, so the TOC cannot drift out of sync with the pages it indexes.

Adding a language means adding translations/<lang>/ with those files. No code
change is required.

Usage:
  python3 build_pdf.py [output.pdf]
  python3 build_pdf.py --lang ru [output.pdf]
"""

import argparse
import json
import re
import unicodedata
from importlib import metadata
from pathlib import Path

from markdown_it import MarkdownIt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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

# ---------- Document structure ----------
# (key, path) renders a file; ("@name", None) is a TOC group label looked up in
# strings.json under "groups". Titles come from each file's own "#" heading.
SECTIONS = [
    ("overview", "overview.md"),
    ("@phase1", None),
    ("week-01", "weeks/week-01.md"),
    ("week-02", "weeks/week-02.md"),
    ("week-03", "weeks/week-03.md"),
    ("week-04", "weeks/week-04.md"),
    ("@phase2", None),
    ("week-05", "weeks/week-05.md"),
    ("week-06", "weeks/week-06.md"),
    ("week-07", "weeks/week-07.md"),
    ("@phase3", None),
    ("week-08", "weeks/week-08.md"),
    ("week-09", "weeks/week-09.md"),
    ("@optional", None),
    ("week-10", "weeks/week-10.md"),
    ("@references", None),
    ("ref-mixing", "reference/mixing.md"),
    ("ref-finalization", "reference/finalization.md"),
    ("ref-generative", "reference/generative.md"),
    ("ref-timing", "reference/timing.md"),
    ("ref-firmware", "reference/firmware.md"),
    ("ref-troubleshooting", "reference/troubleshooting.md"),
]

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
FONT_BOLD_ITALIC = "Helvetica-BoldOblique"
FONT_MONO = "Courier"

# Glyphs the prose fonts don't carry. Rather than rewriting the author's text,
# borrow the glyph from a base-14 font that does have it.
GLYPH_FALLBACK = {
    "\u2192": ("Symbol", "&#8594;"),        # right arrow
    "\u25a2": ("ZapfDingbats", "&#10065;"),  # empty checkbox
    "\u25a3": ("ZapfDingbats", "&#10063;"),  # ticked checkbox
}

# No font in the stack has emoji; drop them rather than emit .notdef boxes.
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]"
)

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
def _renderable_in_base14(text):
    """True if the base-14 fonts can render this text.

    They cover Latin-1 directly, and ReportLab substitutes from Symbol for the
    stray maths glyph, so the question that actually matters is whether the
    text uses *letters* from a script Helvetica doesn't have.
    """
    for char in text:
        if not unicodedata.category(char).startswith("L"):
            continue
        try:
            char.encode("cp1252")
        except UnicodeEncodeError:
            return False
    return True


def rendered_sources(source_dir):
    """The files that actually end up in the PDF."""
    paths = [source_dir / "front-matter.md", source_dir / "about.md"]
    paths += [source_dir / rel for _, rel in SECTIONS if rel]
    return paths


def configure_fonts(source_dir):
    """Embed a Unicode prose font only if the source actually needs one.

    English stays on the base-14 fonts, so its PDF is unchanged by the
    multi-language support. A source written in Cyrillic (or any other script
    Helvetica lacks) gets Roboto for prose instead. Code spans keep the
    monospace font either way -- see code_font().
    """
    global FONT_REGULAR, FONT_BOLD, FONT_ITALIC, FONT_BOLD_ITALIC

    sources = rendered_sources(source_dir)
    if all(_renderable_in_base14(f.read_text(encoding="utf-8")) for f in sources):
        return

    distribution = metadata.distribution("font-roboto")
    font_dir = Path(distribution.locate_file("font_roboto/files"))
    for name, filename in {
        "M8Sans": "Roboto-Regular.ttf",
        "M8Sans-Bold": "Roboto-Bold.ttf",
        "M8Sans-Italic": "Roboto-Italic.ttf",
        "M8Sans-BoldItalic": "Roboto-BoldItalic.ttf",
    }.items():
        pdfmetrics.registerFont(TTFont(name, str(font_dir.joinpath(filename))))
    pdfmetrics.registerFontFamily(
        "M8Sans", normal="M8Sans", bold="M8Sans-Bold",
        italic="M8Sans-Italic", boldItalic="M8Sans-BoldItalic",
    )
    FONT_REGULAR = "M8Sans"
    FONT_BOLD = "M8Sans-Bold"
    FONT_ITALIC = "M8Sans-Italic"
    FONT_BOLD_ITALIC = "M8Sans-BoldItalic"

    for style in (subtitle_style, body, bullet, sub_bullet, task, sub_task,
                  callout, caption):
        style.fontName = FONT_REGULAR
    for style in (title_style, h1, h2, h3):
        style.fontName = FONT_BOLD


def code_font(code_text):
    """Monospace for code, falling back to the prose font for scripts Courier
    can't render (e.g. a Cyrillic word inside a keycap span)."""
    return FONT_MONO if _renderable_in_base14(code_text) else FONT_BOLD


def substitute_glyphs(text):
    """Borrow glyphs the prose font lacks from a base-14 font that has them,
    and drop emoji. The author's text is never rewritten into different
    characters -- only wrapped so it renders."""
    text = EMOJI_RE.sub("", text)
    for glyph, (face, entity) in GLYPH_FALLBACK.items():
        if glyph in text:
            text = text.replace(glyph, f'<font face="{face}">{entity}</font>')
    return text


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


def make_on_page(footer):
    def on_page(canvas_obj, doc):
        canvas_obj.saveState()
        canvas_obj.setFont(FONT_REGULAR, 8)
        canvas_obj.setFillColor(MUTED)
        canvas_obj.drawString(2 * cm, 1.2 * cm, footer)
        canvas_obj.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"{doc.page}")
        canvas_obj.restoreState()

    return on_page


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
        lambda m: f'<font face="{code_font(m.group(1))}" size="9.5">{m.group(1)}</font>',
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
    # M8 button notation. This also handles combined keycaps such as
    # [UP/DOWN] and [LEFT/RIGHT], not only single-key brackets.
    key = r"(?:SHIFT|OPTION|OPT|EDIT|PLAY|UP|DOWN|LEFT|RIGHT|DIRECTION|SELECT)"
    text = re.sub(
        rf"\[(?:{key})(?:/(?:{key}))*\]",
        lambda m: f'<font face="{FONT_BOLD}" color="#006666">{m.group(0)}</font>',
        text,
    )
    return substitute_glyphs(text)


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
                               fontName=FONT_MONO, fontSize=9.5, leading=13)
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
                            mark = substitute_glyphs("▣" if checked else "▢")
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
                    mark = substitute_glyphs("▣" if checked else "▢")
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
                fontName=FONT_BOLD if is_header else FONT_REGULAR,
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


# ---------- Source loading ----------

def load_language(lang):
    """Resolve a language to its source directory and UI strings."""
    here = Path(__file__).resolve().parent
    source_dir = here if lang == "en" else here / "translations" / lang
    strings_path = source_dir / "strings.json"
    if not strings_path.is_file():
        raise SystemExit(f"No strings.json in {source_dir} — is '{lang}' a translation?")
    return source_dir, json.loads(strings_path.read_text(encoding="utf-8"))


def available_languages():
    here = Path(__file__).resolve().parent
    langs = ["en"]
    translations = here / "translations"
    if translations.is_dir():
        langs += sorted(
            d.name for d in translations.iterdir()
            if (d / "strings.json").is_file()
        )
    return langs


def read_heading(path):
    """The document title a file declares in its own leading '#' heading."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise SystemExit(f"{path} has no '# ' heading to use as its title.")


def section_titles(source_dir, strings):
    """key → title, derived from each file's own heading. The overview keeps a
    dedicated PDF title because its Markdown heading names the whole plan."""
    titles = {}
    for key, rel_path in SECTIONS:
        if rel_path is None:
            continue
        titles[key] = (
            strings["overview_title"] if key == "overview"
            else read_heading(source_dir / rel_path)
        )
    titles["resources"] = strings["resources_title"]
    return titles


def render_front_matter(source_dir):
    """Render front-matter.md into the cover page.

    Format (see any front-matter.md):
      # title
      ## subtitle line          (consecutive '##' lines join with a break)
      > ### callout title       (a blockquote becomes the highlighted note box;
      > callout body            blank '>' lines separate its paragraphs)
      body paragraphs
    """
    lines = (source_dir / "front-matter.md").read_text(encoding="utf-8").splitlines()
    title, subtitle, quote, paragraphs = "", [], [], []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
        elif stripped.startswith("## "):
            subtitle.append(stripped[3:].strip())
        elif stripped.startswith(">"):
            quote.append(stripped[1:].strip())
        elif stripped:
            paragraphs.append(stripped)

    note_title, note_parts, current = "", [], []
    for line in quote:
        if line.startswith("### "):
            note_title = line[4:].strip()
        elif line:
            current.append(line)
        elif current:
            note_parts.append(" ".join(current))
            current = []
    if current:
        note_parts.append(" ".join(current))

    flowables = [Spacer(1, 4 * cm), Paragraph(md_inline_to_reportlab(title), title_style)]
    if subtitle:
        joined = "<br/>".join(md_inline_to_reportlab(s) for s in subtitle)
        flowables.append(Paragraph(joined, subtitle_style))
    flowables.append(Spacer(1, 1 * cm))
    if note_parts:
        flowables.append(callout_box(
            md_inline_to_reportlab(note_title),
            "<br/><br/>".join(md_inline_to_reportlab(x) for x in note_parts),
            bg=SECTION_BG,
        ))
        flowables.append(Spacer(1, 1.5 * cm))
    for paragraph in paragraphs:
        flowables.append(Paragraph(md_inline_to_reportlab(paragraph), body))
    flowables.append(PageBreak())
    return flowables, title


# ---------- Two-pass build (to compute real TOC page numbers) ----------

def build_story(source_dir, strings, toc_data=None):
    """
    Build the full story (list of flowables). If toc_data is None, use
    placeholder page numbers (this is pass 1, to discover real positions).
    If toc_data is provided, use those page numbers in the TOC.
    """
    story, doc_title = render_front_matter(source_dir)
    titles = section_titles(source_dir, strings)

    # --- Table of contents ---
    story.append(Paragraph(strings["contents"], h1))
    toc_items = []
    for key, rel_path in SECTIONS:
        if key.startswith("@"):
            toc_items.append((strings["groups"][key[1:]], None))
            continue
        toc_items.append((f"    {titles[key]}", key))
        if key == "overview":
            toc_items.append((f"    {titles['resources']}", "resources"))

    toc_rows = []
    for title, key in toc_items:
        page_num = ""
        if key and toc_data:
            page_num = str(toc_data.get(key, ""))
        is_section = key is None
        # Convert leading 4-space indent to &nbsp; so it renders
        display_title = title.replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;", 1)
        display_title = md_inline_to_reportlab(display_title)
        if is_section:
            toc_rows.append([Paragraph(f"<b>{display_title}</b>", body), ""])
        else:
            toc_rows.append([
                Paragraph(display_title, body),
                Paragraph(f"<font color='#666666'>{page_num}</font>", body),
            ])
    toc_table = Table(toc_rows, colWidths=[14.5 * cm, 1.5 * cm])
    toc_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    # --- Body sections ---
    section_anchors = {}
    for index, (key, rel_path) in enumerate(SECTIONS):
        if rel_path is None:
            continue
        if index:
            story.append(PageBreak())
        section_anchors[key] = len(story)
        md_text = (source_dir / rel_path).read_text(encoding="utf-8")
        if key == "overview":
            # The overview file's own heading names the whole plan; inside the
            # PDF this section is the plan's opening chapter instead.
            md_text = md_text.replace(
                f"# {read_heading(source_dir / rel_path)}",
                f"# {titles['overview']}",
                1,
            )
            # Resources is an H2 inside the overview, not a file of its own.
            section_anchors["resources"] = section_anchors[key]
        story.extend(parse_markdown_to_flowables(md_text))

    # --- Closing page ---
    story.append(PageBreak())
    story.append(Spacer(1, 6 * cm))
    story.extend(parse_markdown_to_flowables(
        (source_dir / "about.md").read_text(encoding="utf-8")
    ))

    return story, section_anchors, doc_title


def resolve_section_pages(doc_path, titles, footer_marker):
    """
    Render the PDF once, then walk the rendered pages to find which page
    each section actually starts on. Uses pypdf to read back.
    """
    from pypdf import PdfReader
    reader = PdfReader(doc_path)

    result = {}
    for key, title in titles.items():
        if key == "resources":
            continue
        for i, page in enumerate(reader.pages):
            if i < 2:
                # Skip title page and TOC page
                continue
            body_text = page_body(page, footer_marker)
            if body_text is None:
                continue
            # A long heading can wrap in the PDF and extract with an inserted
            # newline, so compare normalized whitespace rather than raw lines.
            if " ".join(body_text.split()).startswith(" ".join(title.split())):
                result[key] = i + 1
                break
    return result


def page_body(page, footer_marker):
    """Strip the running footer and page number from an extracted page."""
    text = page.extract_text()
    start = text.find(footer_marker)
    if start == -1:
        return None
    rest = text[start + len(footer_marker):].lstrip()
    return rest.split("\n", 1)[1] if "\n" in rest else rest


def find_resources_page(doc_path, titles, page_map, footer_marker):
    """Resources is an H2 inside the overview, so locate it by scanning the
    overview's pages for the heading."""
    from pypdf import PdfReader
    reader = PdfReader(doc_path)
    first = page_map.get("overview", 3)
    last = page_map.get("week-01", len(reader.pages) + 1)
    needle = " ".join(titles["resources"].split())
    for i, page in enumerate(reader.pages):
        if i + 1 < first:
            continue
        if i + 1 >= last:
            break
        body_text = page_body(page, footer_marker)
        if body_text and needle in " ".join(body_text.split()):
            return i + 1
    return first


# ---------- Main ----------

def main():
    parser = argparse.ArgumentParser(description="Build the M8 Learning Plan PDF.")
    parser.add_argument("output", nargs="?", help="Output PDF path (optional).")
    parser.add_argument("--lang", choices=available_languages(), default="en",
                        help="Source language (default: en).")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    source_dir, strings = load_language(args.lang)
    configure_fonts(source_dir)

    output_path = Path(args.output) if args.output else source_dir / strings["output"]
    if not output_path.is_absolute():
        output_path = here / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(".tmp.pdf")

    footer = strings["footer"]
    footer_marker = footer.split("·")[-1].strip()
    page_callback = make_on_page(footer)
    titles = section_titles(source_dir, strings)

    # Pass 1: render without page numbers in TOC
    story, _, doc_title = build_story(source_dir, strings, toc_data=None)
    doc = SimpleDocTemplate(
        str(tmp_path),
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title=doc_title,
        author=strings["author"],
    )
    doc.build(story, onFirstPage=page_callback, onLaterPages=page_callback)

    # Discover real page numbers for headings
    page_map = resolve_section_pages(str(tmp_path), titles, footer_marker)
    page_map["resources"] = find_resources_page(
        str(tmp_path), titles, page_map, footer_marker
    )

    # Pass 2: rebuild with the real page numbers in the TOC
    story, _, doc_title = build_story(source_dir, strings, toc_data=page_map)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title=doc_title,
        author=strings["author"],
    )
    doc.build(story, onFirstPage=page_callback, onLaterPages=page_callback)
    tmp_path.unlink(missing_ok=True)

    from pypdf import PdfReader
    pages = len(PdfReader(str(output_path)).pages)
    print(f"Built {output_path} ({pages} pages, lang={args.lang})")


if __name__ == "__main__":
    main()
