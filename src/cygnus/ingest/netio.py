"""Resumable, bounded HTTP retrieval for Cygnus ingest.

Grounds:

* data is streamed to scratch on disk — no multi-GB buffers in memory;
* interrupted downloads resume via HTTP Range on a ``.part`` file, then are
  atomically renamed into place, so runs are idempotent;
* an optional per-product byte cap can truncate instead of fail (the manifest
  row then records ``truncated=True`` so nothing is silently misrepresented);
* transient 429/5xx errors back off exponentially. Credentials are never
  handled here — all Tier-1 endpoints used by the pack retriever live
  anonymously.

The exact endpoint calls and their provenance are recorded by the callers
(``pack.PackBuilder``) in the ledger and manifests.
"""

from __future__ import annotations

import hashlib
import os
import time
from pathlib import Path
from typing import Any

import requests

USER_AGENT = (
    "cygnus/0.1.0 (astronomical data forensics; provenance-logged archive "
    "retrieval; python-requests)"
)

DEFAULT_TIMEOUT_S = 90.0
_RETRY_STATUS = {429, 500, 502, 503, 504}


def session() -> requests.Session:
    """A requests session with the Cygnus user agent."""
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def sha256_file(path: str | Path) -> str:
    """Streaming SHA-256 (matches ledger.file_sha256)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def md5_file(path: str | Path) -> str:
    """Streaming MD5 — used to compare uploads against the rclone/Drive mirror."""
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


class ByteCapReached(Exception):
    """Raised internally when the optional per-product cap is hit."""


def fetch_to_file(
    url: str,
    dest: str | Path,
    *,
    method: str = "GET",
    params: dict[str, Any] | None = None,
    data: dict[str, Any] | bytes | None = None,
    json_: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout_s: float = DEFAULT_TIMEOUT_S,
    max_bytes: int | None = None,
    max_retries: int = 5,
    sess: requests.Session | None = None,
) -> dict[str, Any]:
    """Stream ``url`` to ``dest`` via GET or POST, resumable and bounded.

    Writes to ``dest + '.part'`` (reusing an existing partial via Range when
    the server honours it) and atomically renames on success. Returns a dict:

    ``url, path, bytes, resumed, truncated, http_status, note``.

    Raises :class:`requests.RequestException` after ``max_retries`` attempts.
    """
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.parent / (dest.name + ".part")
    sess = sess or session()
    from ..throttle import wait

    wait(url)                      # parallel batch jobs share a per-host request rate

    headers = dict(headers or {})
    resumed = part.exists() and part.stat().st_size > 0 and method.upper() == "GET"
    done_bytes = part.stat().st_size if resumed else 0
    if max_bytes is not None and done_bytes >= max_bytes:
        # A previous run capped this file; do not resume past the cap.
        os.replace(part, dest)
        return {
            "url": url,
            "path": str(dest),
            "bytes": done_bytes,
            "resumed": False,
            "truncated": True,
            "http_status": 0,
            "note": "existing .part already at byte cap; finalized",
        }
    if resumed:
        headers["Range"] = f"bytes={done_bytes}-"

    total = done_bytes
    status = 0
    note = ""
    trunc = False
    for attempt in range(1, max_retries + 1):
        try:
            with sess.request(
                method.upper(),
                url,
                params=params,
                data=data,
                json=json_,
                headers=headers,
                stream=True,
                timeout=timeout_s,
            ) as resp:
                status = resp.status_code
                if status in _RETRY_STATUS:
                    time.sleep(min(90.0, 3.0 * attempt * attempt))
                    continue
                resp.raise_for_status()
                if status == 206:
                    mode = "ab"  # Range honoured; append to the partial
                else:
                    mode = "wb"  # full restart (Range ignored/cleared)
                    total = 0
                with open(part, mode) as fh:
                    for chunk in resp.iter_content(chunk_size=512 * 1024):
                        if not chunk:
                            continue
                        if max_bytes is not None and total + len(chunk) > max_bytes:
                            keep = max_bytes - total
                            if keep > 0:
                                fh.write(chunk[:keep])
                                total = max_bytes
                            else:
                                break
                            note = "per-product byte cap reached; file truncated at cap"
                            trunc = True
                            break
                        fh.write(chunk)
                        total += len(chunk)
                if trunc:
                    os.replace(part, dest)
                    return {
                        "url": url,
                        "path": str(dest),
                        "bytes": total,
                        "resumed": resumed,
                        "truncated": True,
                        "http_status": status,
                        "note": note,
                    }
                if total == 0:
                    note = "zero-byte response body (kept for the record if useful)"
                os.replace(part, dest)
                return {
                    "url": url,
                    "path": str(dest),
                    "bytes": total,
                    "resumed": resumed,
                    "truncated": False,
                    "http_status": status,
                    "note": note,
                }
        except ByteCapReached:  # pragma: no cover - defensive
            raise
        except (requests.RequestException, OSError) as exc:
            if attempt >= max_retries:
                raise
            time.sleep(min(90.0, 3.0 * attempt * attempt))
    raise requests.RequestException(
        f"fetch failed after {max_retries} attempts: url={url!r} last_status={status} note={note!r}"
    )
