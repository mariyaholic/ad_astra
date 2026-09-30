"""Durable output writes and history preservation shared by every step."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import date
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_write_text(path: Path | str, text: str) -> Path:
    """Flushed temp file + os.replace: a failed write never exposes a partial file."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="\n", dir=target.parent,
                                         prefix=f".{target.name}.", suffix=".tmp", delete=False) as s:
            tmp = Path(s.name)
            s.write(text)
            s.flush()
            os.fsync(s.fileno())
        os.replace(tmp, target)
    finally:
        if tmp is not None and tmp.exists():
            tmp.unlink()
    return target


def atomic_write_json(path: Path | str, payload, *, inputs: dict | None = None) -> Path:
    """Write JSON atomically. ``inputs`` maps a label to a file whose SHA-256 is linked in ``_provenance``."""
    if inputs:
        payload = dict(payload)
        payload["_provenance"] = {"input_sha256": {k: sha256_file(Path(v)) for k, v in inputs.items()}}
    return atomic_write_text(path, json.dumps(payload, indent=2, allow_nan=False, ensure_ascii=False) + "\n")


def archive_previous(path: Path | str, reason: str, *, today: str | None = None) -> Path | None:
    """Rename an existing output to ``<stem>_history_<date>_<reason>.<ext>``; never overwrites history."""
    p = Path(path)
    if not p.exists():
        return None
    slug = "".join(c if c.isalnum() else "_" for c in reason).strip("_")
    base = f"{p.stem}_history_{today or date.today().isoformat()}_{slug}"
    dest, n = p.with_name(base + p.suffix), 1
    while dest.exists():
        n += 1
        dest = p.with_name(f"{base}_{n}{p.suffix}")
    os.replace(p, dest)
    return dest
