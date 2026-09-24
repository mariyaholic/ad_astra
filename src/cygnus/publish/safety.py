"""Publication safety: path confinement, redaction, and output leak scanning.

Three independent guards, so one mistake is not enough to leak:

1. ``resolve_source`` confines every item source to an allowlisted worktree
   root (no absolute paths, no ``..``, no escaping symlinks, never ``state/``);
2. ``redact`` rewrites private locations in text that *is* published
   (docs mention the scratch root and the Drive remote by design);
3. ``scan_for_leaks`` runs over the finished site and fails the build if any
   private path, remote name, credential-shaped string or e-mail survived.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

from .schema import PublicationError

# kind -> worktree-relative roots its source may live under ("" = top-level files only)
ALLOWED_SOURCE_ROOTS: dict[str, tuple[str, ...]] = {
    "document": ("", "publish/pages", "docs", "campaigns", "reports"),
    "module_register": ("",),
    "campaign": ("campaigns",),
    "archive_manifest": ("publish/data",),
    "candidate": ("publish/candidates",),
    "file": ("publish/files", "reports", "campaigns", "docs"),
}

_FORBIDDEN_PARTS = {"state", ".git", ".env", "venv", ".venv", "scratch", "__pycache__"}


def resolve_source(worktree: Path, kind: str, source: str) -> Path:
    """Resolve an item source to a real file inside its allowed root, or raise."""
    if not source or "\x00" in source:
        raise PublicationError(f"empty or invalid source for {kind}")
    rel = PurePosixPath(source.replace("\\", "/"))
    if rel.is_absolute() or re.match(r"^[A-Za-z]:", source) or ".." in rel.parts:
        raise PublicationError(f"source {source!r} must be a relative path without '..'")
    if _FORBIDDEN_PARTS & set(rel.parts) or rel.name.startswith("."):
        raise PublicationError(f"source {source!r} touches a private location")
    worktree = worktree.resolve()
    target = (worktree / Path(*rel.parts)).resolve()
    for root in ALLOWED_SOURCE_ROOTS.get(kind, ()):
        if root == "":
            if target.parent == worktree:
                break
        else:
            base = (worktree / root).resolve()
            if target.is_relative_to(base):
                break
    else:
        allowed = ", ".join(r or "<worktree top level>" for r in ALLOWED_SOURCE_ROOTS.get(kind, ()))
        raise PublicationError(f"source {source!r} is outside the roots allowed for {kind}: {allowed}")
    if not target.is_file():
        raise PublicationError(f"source {source!r} does not exist")
    return target


# ------------------------------------------------------------------ redaction
_REDACTIONS: tuple[tuple[re.Pattern[str], str], ...] = (
    # rclone remote paths such as cygnus:Cygnus/data/tier1
    (re.compile(r"\bcygnus:(?:Cygnus)?[\w./\\-]*"), "[private Drive store]"),
    # Windows absolute paths (drive letter + separator), up to whitespace/quote/closer
    (re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s`'\"|<>()\[\]]*(?: [A-Z][\w-]*(?:[\\/][^\s`'\"|<>()\[\]]*)?)?"),
     "[private path]"),
    # POSIX home directories
    (re.compile(r"(?<![\w/])/(?:home|Users)/[^\s`'\"|<>()]+"), "[private path]"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[e-mail redacted]"),
)


def redact(text: str) -> str:
    """Replace private locations in text that is otherwise fit to publish."""
    for pattern, repl in _REDACTIONS:
        text = pattern.sub(repl, text)
    return text


# ----------------------------------------------------------------- leak scan
LEAK_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("windows-path", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/](?![/\\])")),
    ("scratch-root", re.compile(r"AO_Artifacts", re.I)),
    ("drive-remote", re.compile(r"\bcygnus:Cygnus")),
    ("rclone-config", re.compile(r"rclone\.conf|\[cygnus\]\s*\n\s*type\s*=")),
    ("credential", re.compile(r"(?i)(client_secret|refresh_token|access_token|api[_-]?key)\s*[\"':=]")),
    ("ledger-file", re.compile(r"ledger\.sqlite-(?:wal|shm|journal)")),
    ("email", re.compile(r"[\w.+-]+@[\w-]+\.(?:com|org|net|edu|io)\b")),
)

TEXT_SUFFIXES = {".html", ".json", ".csv", ".md", ".txt", ".yaml", ".yml", ".js", ".css", ".xml", ".svg"}


def scan_text(text: str) -> list[str]:
    return [name for name, pat in LEAK_PATTERNS if pat.search(text)]


def scan_for_leaks(out_dir: Path) -> list[str]:
    """Return 'relative/path: pattern' for every text output that leaks."""
    findings: list[str] = []
    for path in sorted(out_dir.rglob("*")):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="replace")
            for name in scan_text(text):
                findings.append(f"{path.relative_to(out_dir).as_posix()}: {name}")
    return findings
