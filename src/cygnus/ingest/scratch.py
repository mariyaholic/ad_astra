"""Scratch-directory helpers (nonsynced, disposable)."""

from __future__ import annotations

import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

from ..config import scratch_dir


def resolve_scratch(subdir: str | None = None) -> Path:
    """Directory under the designated scratch root, created on demand.

    Per AGENTS.md: bulky downloads/intermediates live here — never in the
    worktree root, never merged with curated Drive data, safe to delete.
    """
    return scratch_dir(subdir)


def cleanup_scratch(target: str | Path | None = None, older_than_days: float | None = None) -> int:
    """Delete scratch *contents* (never the root itself).

    Refuses any path outside the scratch root. With ``older_than_days``, files
    newer than the cutoff are preserved. Returns the number of entries removed.
    """
    base = scratch_dir().resolve()
    p = (Path(target).resolve() if target is not None else base)
    if p != base and base not in p.parents:
        raise ValueError(f"cleanup refused: {p} is outside the scratch root {base}")

    cutoff: float | None = None
    if older_than_days is not None:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=older_than_days)).timestamp()

    removed = 0
    for child in sorted(p.iterdir(), reverse=True):
        if cutoff is not None and child.stat().st_mtime > cutoff:
            continue
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
        removed += 1
    return removed
