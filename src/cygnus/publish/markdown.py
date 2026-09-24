"""Small, escape-first Markdown renderer for the project's own documents.

Supports what the worktree docs use: ATX headings (with anchors), paragraphs,
nested bullet/numbered lists, pipe tables, fenced code, block quotes, rules,
and inline code/bold/italic/links/autolinks. Raw HTML is always escaped —
published Markdown can never inject markup or script.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field

_INLINE_CODE = re.compile(r"`([^`]+)`")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_AUTOLINK = re.compile(r"(?<![\"'=>])\bhttps?://[^\s<>()\"'`]+[^\s<>()\"'`.,;:]")
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<![*\w])\*(?!\s)([^*]+?)(?<!\s)\*(?![*\w])")
_SAFE_URL = re.compile(r"^(https?://|/|#|\.{0,2}/?[\w.-]+)", re.I)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_]+", "-", text)[:80] or "section"


def _safe_href(url: str) -> str | None:
    url = html.unescape(url)
    if url.lower().startswith(("javascript:", "data:", "vbscript:")):
        return None
    return url if _SAFE_URL.match(url) else None


def inline(text: str, unlink_relative: bool = False) -> str:
    """Render inline Markdown on escaped text; code spans are protected first."""
    stash: list[str] = []

    def keep(fragment: str) -> str:
        stash.append(fragment)
        return f"\x00{len(stash) - 1}\x00"

    text = _INLINE_CODE.sub(lambda m: keep(f"<code>{html.escape(m.group(1))}</code>"), text)
    text = html.escape(text, quote=False)

    def link(m: re.Match[str]) -> str:
        href = _safe_href(m.group(2))
        label = m.group(1)
        if href is None:
            return label
        if (unlink_relative or _UNLINK) and not href.startswith(("http://", "https://", "/", "#")):
            return label  # repository-relative path: not a page on the published site
        ext = ' rel="noopener" class="ext"' if href.startswith("http") else ""
        return keep(f'<a href="{html.escape(href)}"{ext}>{label}</a>')

    text = _LINK.sub(link, text)
    text = _AUTOLINK.sub(
        lambda m: keep(f'<a href="{m.group(0)}" rel="noopener" class="ext">{m.group(0)}</a>'), text
    )
    text = _BOLD.sub(r"<strong>\1</strong>", text)
    text = _ITALIC.sub(r"<em>\1</em>", text)
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)
    return text


@dataclass
class Rendered:
    html: str
    title: str | None
    toc: list[tuple[int, str, str]] = field(default_factory=list)  # (level, id, text)


def _split_row(line: str) -> list[str]:
    line = line.strip().strip("|")
    cells, buf, in_code = [], [], False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    cells.append("".join(buf).strip())
    return cells


_LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def _render_list(lines: list[str]) -> str:
    """Render a (possibly nested) list block from raw lines."""
    out: list[str] = []
    stack: list[tuple[int, str]] = []  # (indent, tag)
    for raw in lines:
        m = _LIST_RE.match(raw)
        if not m:  # continuation line of the previous item
            if out:
                out[-1] = out[-1].removesuffix("</li>") + " " + inline(raw.strip()) + "</li>"
            continue
        indent, marker, body = len(m.group(1)), m.group(2), m.group(3)
        tag = "ol" if marker[0].isdigit() else "ul"
        while stack and indent < stack[-1][0]:
            out.append(f"</{stack.pop()[1]}></li>")
        if not stack or indent > stack[-1][0]:
            if stack and out:
                out[-1] = out[-1].removesuffix("</li>")
            stack.append((indent, tag))
            out.append(f"<{tag}>")
        out.append(f"<li>{inline(body)}</li>")
    while stack:
        tag = stack.pop()[1]
        out.append(f"</{tag}>" + ("</li>" if stack else ""))
    return "\n".join(out)


def render(md: str, *, demote_h1: bool = False, unlink_relative: bool = False) -> Rendered:
    global _UNLINK
    _UNLINK = unlink_relative
    try:
        return _render(md, demote_h1=demote_h1)
    finally:
        _UNLINK = False


_UNLINK = False


def _render(md: str, *, demote_h1: bool = False) -> Rendered:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    title: str | None = None
    used: set[str] = set()
    i = 0
    para: list[str] = []

    def flush() -> None:
        if para:
            out.append(f"<p>{inline(' '.join(s.strip() for s in para))}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            lang = stripped[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            cls = f' class="lang-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            i += 1
            continue
        if not stripped:
            flush()
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", stripped)
        if h:
            flush()
            level = len(h.group(1))
            text = h.group(2)
            if level == 1 and title is None:
                title = re.sub(r"[`*]", "", text)
                if demote_h1:
                    i += 1
                    continue
            anchor = slugify(text)
            base, n = anchor, 2
            while anchor in used:
                anchor, n = f"{base}-{n}", n + 1
            used.add(anchor)
            if level in (2, 3):
                toc.append((level, anchor, re.sub(r"[`*]", "", text)))
            out.append(
                f'<h{level} id="{anchor}">{inline(text)}'
                f'<a class="anchor" href="#{anchor}" aria-label="Link to this section">#</a></h{level}>'
            )
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{3,}", lines[i + 1].strip()):
            flush()
            header = _split_row(stripped)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            thead = "".join(f'<th scope="col">{inline(c)}</th>' for c in header)
            body = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows
            )
            out.append(
                f'<div class="table-wrap" tabindex="0" role="region" aria-label="Table">'
                f"<table><thead><tr>{thead}</tr></thead><tbody>{body}</tbody></table></div>"
            )
            continue
        if stripped.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(buf))}</p></blockquote>")
            continue
        if _LIST_RE.match(line):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip() and (
                _LIST_RE.match(lines[i]) or lines[i].startswith((" ", "\t"))
            ):
                buf.append(lines[i])
                i += 1
            out.append(_render_list(buf))
            continue
        para.append(line)
        i += 1
    flush()
    return Rendered(html="\n".join(out), title=title, toc=toc)
