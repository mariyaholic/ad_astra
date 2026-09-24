"""Central path and environment configuration.

See ``AGENTS.md`` ('Data, compute, and Google Drive policy'):

* worktree root: holds code, docs, small reproducibility metadata only;
* scratch root: bulky downloads/intermediates, nonsynced, safe to delete
  (default ``D:/AO_Artifacts/cygnus_scratch``, override via ``CYGNUS_SCRATCH``);
* ledger: SQLite provenance DB under ``<worktree>/state``
  (override via ``CYGNUS_LEDGER``).

Credentials are never stored in code or config files here; they live in
uncommitted environment files only.
"""

from __future__ import annotations

import os
from pathlib import Path

WORKTREE = Path(__file__).resolve().parents[2]
_STATE_DIR = WORKTREE / "state"


def scratch_dir(subdir: str | None = None) -> Path:
    """Resolve (and create) a directory under the scratch root."""
    root = Path(os.environ.get("CYGNUS_SCRATCH", "D:/AO_Artifacts/cygnus_scratch"))
    path = root / subdir if subdir else root
    path.mkdir(parents=True, exist_ok=True)
    return path


def state_dir() -> Path:
    """Resolve (and create) the worktree-local state directory."""
    _STATE_DIR.mkdir(parents=True, exist_ok=True)
    return _STATE_DIR


def ledger_path() -> Path:
    """Default SQLite provenance-DB path (env ``CYGNUS_LEDGER`` overrides)."""
    env = os.environ.get("CYGNUS_LEDGER")
    return Path(env) if env else state_dir() / "ledger.sqlite"
