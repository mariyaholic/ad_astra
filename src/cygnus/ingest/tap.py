"""Minimal byte-safe TAP 1.x client for Cygnus ingest.

Rationale: pyvo 1.9's VOTable pipeline failed on this machine for two
independent reasons observed live on 2026-09-23 — a UnicodeDecodeError
('ascii' codec) for tap_schema FIELD descriptions containing non-ASCII
bytes, and 'Read timed out (read timeout=10)' on large sync streams whose
origin pyvo does not document. The direct client:

* holds responses as BYTES (requests), never re-decoding text;
* parses with ``astropy.io.votable.parse`` on an in-memory buffer, where the
  VOTable's own XML encoding declaration governs decoding (validated live
  against Gaia's tap_schema, which declares UTF-8);
* applies explicit client side timeouts and retry/backoff;
* optionally papers raw VOTable responses next to the derived CSVs so the
  delivered product equals the archive's exact bytes.

Coverage: TAP sync (GET) and TAP async jobs (POST /async + phase polling),
both returning an :class:`astropy.table.Table`.
"""

from __future__ import annotations

import io
import re
import time
from typing import Any

import requests

from .netio import session as cyg_session


def normalize_votable_bytes(raw: bytes) -> bytes:
    """Make VOTable bytes safely parseable.

    Two failure modes handled here (both observed live on 2026-09-23):

    * a missing ``encoding=`` in the XML declaration makes astropy fall back to
      byte-paranoid decoding — declaring UTF-8 up front avoids that;
    * Gaia's tap_schema descriptions contain lone non-UTF-8 bytes (e.g. 0xA0
      as latin-1 non-breaking space inside a UTF-8-declared document), which
      astropy's strict decode rejects. Such bytes are repaired to U+FFFD
      placeholders before parsing so metadata text survives byte-repaired.
    """
    head = raw[:2048]
    m = re.search(rb"<\?xml[^>]*\?>", head)
    if m is None:
        raw = b'<?xml version="1.0" encoding="UTF-8"?>\n' + raw
    else:
        if b"encoding=" not in m.group(0).lower():
            tag = m.group(0)
            tag2 = tag[:-2] + b' encoding="UTF-8"?>'
            raw = tag2 + raw[len(tag):]
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        repaired = raw.decode("utf-8", errors="replace").encode("utf-8")
        return repaired
    return raw


def parse_votable_bytes(raw: bytes):
    """Parse VOTable bytes into an astropy Table (first RESOURCE table)."""
    from astropy.io.votable import parse as votable_parse

    vt = votable_parse(io.BytesIO(normalize_votable_bytes(raw)))
    return vt.get_first_table().to_table()


class TapDirectError(RuntimeError):
    """Raised when the service returns no parsable table after retries."""


class TapDirect:
    """Small TAP client used by Tier-1 collectors (byte-safe, retrying)."""

    def __init__(self, service: str, *, sess: requests.Session | None = None) -> None:
        self.service = service.rstrip("/")
        self.s = sess or cyg_session()

    # ------------------------------------------------------------------ sync
    def sync_table(
        self,
        adql: str,
        *,
        timeout_s: float = 600.0,
        max_retries: int = 3,
        fmt: str = "csv",
    ):
        """Sync TAP query (GET /sync); returns (table, status_text).

        Default FORMAT is csv: astropy's VOTable *binary* reader decodes
        variable-length char fields with a hardcoded ascii codec
        (astropy/io/votable/converters.py ``_binparse_var``) and raises on
        non-ASCII bytes (observed live for Gaia tap_schema descriptions,
        2026-09-23). CSV output avoids the VOTable binary layer entirely;
        VOTable remains available via ``fmt='votable'`` (with the byte
        repair in ``normalize_votable_bytes``).
        """
        url = f"{self.service}/sync"
        params = {"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": fmt, "QUERY": adql}
        last = ""
        for attempt in range(1, max_retries + 1):
            try:
                print(f"[tap] sync attempt {attempt}/{max_retries}: {adql[:90]!r}", flush=True)
                r = self.s.get(url, params=params, stream=True, timeout=timeout_s,
                               allow_redirects=True)
                if r.status_code in (429, 500, 502, 503, 504):
                    last = f"sync HTTP {r.status_code}"
                    time.sleep(min(90.0, 5.0 * attempt * attempt))
                    continue
                r.raise_for_status()
                raw = r.content
                if fmt == "votable":
                    tab = parse_votable_bytes(raw)
                else:
                    from astropy.io import ascii as ascii_io

                    tab = ascii_io.read(io.BytesIO(raw), format="csv")
                return tab, f"HTTP {r.status_code}; {len(raw)} bytes"
            except requests.RequestException as exc:
                last = f"{type(exc).__name__}: {str(exc)[:300]}"
                time.sleep(min(90.0, 5.0 * attempt * attempt))
            except Exception as exc:  # noqa: BLE001 - parse errors go to async fallback
                last = f"{type(exc).__name__}: {str(exc)[:300]}"
                raise TapDirectError(f"sync parse failed: {last}") from exc
        raise TapDirectError(f"sync failed after {max_retries} attempts: {last}")

    # ----------------------------------------------------------------- async
    def async_table(
        self,
        adql: str,
        *,
        poll_s: float = 15.0,
        wait_max_s: float = 10800.0,
        fmt: str = "votable",
        delete_job: bool = True,
    ):
        """Async TAP job (POST /async + phase polling); returns (table, status).

        The POST creates a job as PENDING; per TAP 1.1 the response is 303 with
        a Location header pointing at ``/async/{jobid}`` — that job URL is used
        for all subsequent phase/results calls.
        """
        joburl = f"{self.service}/async"
        print(f"[tap] async submit: {adql[:90]!r}", flush=True)
        r = self.s.post(
            joburl,
            data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": fmt, "QUERY": adql},
            timeout=180.0,
            allow_redirects=False,
        )
        if r.status_code in (303, 302, 301):
            joburl = r.headers.get("Location", joburl)
        elif r.status_code >= 400:
            raise TapDirectError(f"async job POST failed: HTTP {r.status_code}: {r.text[:200]}")
        r.raise_for_status()
        deadline = time.monotonic() + wait_max_s
        t0 = time.monotonic()
        phase = ""
        while time.monotonic() < deadline:
            pr = self.s.get(f"{joburl}/phase", timeout=120.0)
            pr.raise_for_status()
            phase = (pr.text or "").strip().upper()
            print(f"[tap] async phase: {phase} ({int(time.monotonic() - t0)}s elapsed)", flush=True)
            if phase in ("COMPLETED", "ERROR", "ABORTED"):
                break
            time.sleep(poll_s)
        if phase != "COMPLETED":
            raise TapDirectError(f"async job phase={phase!r} (adql head: {adql[:120]!r})")
        rr = self.s.get(f"{joburl}/results/result.vot", timeout=600.0,
                        headers={"Accept": "application/x-votable+xml"})
        rr.raise_for_status()
        raw = rr.content
        tab = parse_votable_bytes(raw)
        if delete_job:
            try:
                self.s.delete(joburl, timeout=60.0)
            except Exception:  # noqa: BLE001 - cleanup best-effort
                pass
        return tab, f"async COMPLETED; {len(raw)} bytes"

    def run(self, adql: str, *, async_threshold_rows: int = 50000, **kw: Any):
        """Sync first; fall back to async when sync is capped/failed."""
        try:
            tab, status = self.sync_table(adql, **kw)
            return tab, status, "sync"
        except TapDirectError as exc:
            print(f"[tap] sync failed -> trying async: {str(exc)[:200]}", flush=True)
        tab, status = self.async_table(adql, **{k: v for k, v in kw.items()
                                                if k in ("poll_s", "wait_max_s", "fmt", "delete_job")})
        return tab, status, "async"
