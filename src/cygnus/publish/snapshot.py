"""Import pack manifests from scratch into sanitized, versioned worktree snapshots.

Scratch is disposable, so the site never reads it directly. An operator runs
``python -m cygnus.publish snapshot`` to copy an allowlisted subset of each
``<pack>/MANIFEST.json`` into ``publish/data/<name>/<pack>.json``:

* fields outside ``SNAPSHOT_FIELDS`` are dropped (``dest_rel`` etc.);
* free text is passed through ``redact`` (notes cite Drive paths);
* upload-verification notes are reduced to a neutral public sentence;
* the source manifest's sha256 and mtime are recorded for traceability.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .safety import redact
from .sources import mtime_utc

SNAPSHOT_FIELDS = (
    "service", "pack_dir", "product_id", "state", "bytes", "sha256", "md5",
    "retrieved_utc", "url", "endpoint", "query", "license", "truncated",
)
_EXTRA_DROP = {"dest_rel", "pack_dir", "local_path", "path"}
_VERIFIED = re.compile(r"verified_md5@\S+;\s*local_deleted@(\S+)")


def _public_note(note: str | None) -> str | None:
    if not note:
        return None
    m = _VERIFIED.search(note)
    if m:
        return f"Upload verified by MD5 against the manifest; local staging copy removed {m.group(1)}."
    return redact(note)


def sanitize_row(row: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in SNAPSHOT_FIELDS:
        val = row.get(key)
        if val in ("", None):
            out[key] = None
        elif key == "bytes":
            out[key] = int(val)
        else:
            out[key] = redact(str(val))
    try:
        extra = json.loads(row.get("extra_json") or "{}")
    except json.JSONDecodeError:
        extra = {}
    out["extra"] = {k: redact(json.dumps(v)) if not isinstance(v, (str, int, float, bool, type(None))) else
                    (redact(v) if isinstance(v, str) else v)
                    for k, v in sorted(extra.items()) if k not in _EXTRA_DROP}
    out["note"] = _public_note(row.get("note"))
    return out


def snapshot_pack(pack_root: Path, dest_dir: Path, *, snapshot_utc: str) -> list[Path]:
    """Write one sanitized snapshot per ``*/MANIFEST.json``; returns written paths."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for manifest in sorted(pack_root.glob("*/MANIFEST.json")):
        raw_bytes = manifest.read_bytes()
        rows = json.loads(raw_bytes.decode("utf-8"))
        pack_dir = manifest.parent.name
        services = sorted({r.get("service") for r in rows if r.get("service")})
        snap = {
            "service": services[0] if len(services) == 1 else ", ".join(services) or None,
            "pack_dir": pack_dir,
            "source_manifest": f"{pack_dir}/MANIFEST.json",
            "source_sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "source_modified_utc": mtime_utc(manifest),
            "snapshot_utc": snapshot_utc,
            "rows": [sanitize_row(r) for r in rows],
        }
        out = dest_dir / f"{pack_dir}.json"
        out.write_text(json.dumps(snap, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append(out)
    return written
