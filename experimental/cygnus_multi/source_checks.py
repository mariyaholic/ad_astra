"""Per-source checks for fetched products.

Each archive exposes different things, so each adapter answers a different
question about its own products. These helpers implement the checks that are
meaningful per product kind and are reused by adapters:

* :func:`table_checks` — catalogue row counts, nearest match to the target, and
  (optionally) star-specific astrometric flags.
* :func:`image_checks` — image shape, finite-pixel fraction and a robust
  background estimate (an image full of NaNs or one constant value fails).
* :func:`lightcurve_checks` — cadence, time span and the time standard as stored.
* :func:`text_checks` / :func:`json_checks` — context payloads parse.

Every check returns a :class:`~cygnus_multi.archives.base.SourceCheck` with one of
the four audit states. A check that cannot be evaluated is ``not_tested`` or
``inconclusive``; it is never reported as ``passed``.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from .archives.base import SourceCheck


def _sep_arcsec(ra1, dec1, ra2, dec2) -> float:
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c)))) * 3600


def _f(v: Any) -> float | None:
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def table_checks(path: Path, target, *, kind: str = "catalog") -> list[SourceCheck]:
    """Row count and nearest-match separation for a catalogue product."""
    from .readers import read_product

    try:
        tab = read_product(path, fmt="csv" if path.suffix.lower() == ".csv" else "votable")
    except Exception as exc:  # noqa: BLE001
        return [SourceCheck(f"{kind} table readable", "failed", f"{type(exc).__name__}: {str(exc)[:160]}")]
    rows = tab.get("rows", [])
    cols = tab.get("columns", [])
    out = [SourceCheck(f"{kind} rows", "passed" if rows else "inconclusive",
                       f"{len(rows)} row(s); columns {', '.join(str(c) for c in cols[:10])}")]
    if not rows or target is None:
        return out
    racol = next((c for c in ("ra", "RAJ2000", "ra_deg") if c in cols), None)
    deccol = next((c for c in ("dec", "DEJ2000", "dec_deg") if c in cols), None)
    if racol and deccol:
        seps = []
        for r in rows:
            ra, dec = _f(r.get(racol)), _f(r.get(deccol))
            if ra is not None and dec is not None:
                seps.append(_sep_arcsec(target.ra_deg, target.dec_deg, ra, dec))
        if seps:
            out.append(SourceCheck(f"{kind} nearest match", "passed" if min(seps) <= 5.0 else "inconclusive",
                                   f"nearest row {min(seps):.2f}″ from the target (n={len(seps)})"))
    return out


def gaia_checks(path: Path, target=None) -> list[SourceCheck]:
    """Astrometric fidelity flags for a Gaia cone product."""
    from .readers import read_product

    checks = table_checks(path, target, kind="Gaia")
    try:
        rows = read_product(path, fmt="csv")["rows"]
    except Exception:  # noqa: BLE001 - table_checks already recorded the failure
        return checks
    ruwe = [_f(r.get("ruwe")) for r in rows if _f(r.get("ruwe")) is not None]
    nss = [_f(r.get("non_single_star")) for r in rows if _f(r.get("non_single_star")) is not None]
    px = [_f(r.get("parallax")) for r in rows if _f(r.get("parallax")) is not None]
    if ruwe:
        bad = sum(1 for v in ruwe if v > 1.4)
        checks.append(SourceCheck("Gaia RUWE", "passed" if bad == 0 else "inconclusive",
                                  f"{bad} of {len(ruwe)} source(s) with RUWE > 1.4 (astrometry may be compromised)"))
    if nss:
        flagged = sum(1 for v in nss if v and v > 0)
        checks.append(SourceCheck("Gaia non-single-star flag", "passed" if flagged == 0 else "inconclusive",
                                  f"{flagged} of {len(nss)} source(s) flagged non_single_star"))
    if px:
        checks.append(SourceCheck("Gaia parallax", "passed",
                                  f"{len(px)} parallax value(s), range {min(px):.3f}..{max(px):.3f} mas"))
    return checks


def image_checks(path: Path, *, source: str = "image") -> list[SourceCheck]:
    """Shape, finite fraction and background for a FITS image."""
    import numpy as np

    from .readers import read_image

    try:
        img = read_image(path)
    except Exception as exc:  # noqa: BLE001
        return [SourceCheck(f"{source} image readable", "failed", f"{type(exc).__name__}: {str(exc)[:160]}")]
    data = np.asarray(img["data"], float)
    finite = np.isfinite(data)
    frac = float(finite.mean()) if finite.size else 0.0
    out = [SourceCheck(f"{source} image shape", "passed", f"{img['shape']}")]
    out.append(SourceCheck(f"{source} finite pixels", "passed" if frac >= 0.5 else "failed",
                           f"{frac:.3f} of pixels finite"))
    if finite.any():
        med = float(np.nanmedian(data[finite]))
        mad = float(np.nanmedian(np.abs(data[finite] - med)))
        out.append(SourceCheck(f"{source} background", "passed" if mad > 0 else "inconclusive",
                               f"median {med:.4g}, robust sigma {1.4826 * mad:.4g}"))
    return out


def lightcurve_checks(path: Path, *, fmt: str, source: str = "light curve") -> list[SourceCheck]:
    """Cadence, baseline and stored time metadata for a time series."""
    from .readers import read_lightcurve

    try:
        lc = read_lightcurve(path, fmt=fmt)
    except Exception as exc:  # noqa: BLE001
        return [SourceCheck(f"{source} readable", "failed", f"{type(exc).__name__}: {str(exc)[:160]}")]
    finite = lc.usable(lc.channels[0])
    n = int(finite.sum())
    out = [SourceCheck(f"{source} usable cadences", "passed" if n >= 10 else "inconclusive",
                       f"{n} of {lc.time.size} cadence(s) usable in channel {lc.channels[0]}")]
    if n >= 2:
        span = float(lc.time[finite].max() - lc.time[finite].min())
        out.append(SourceCheck(f"{source} baseline", "passed", f"{span:.3f} d as stored"))
    if lc.time_scale:
        out.append(SourceCheck(f"{source} time standard", "passed", f"TIMESYS={lc.time_scale} as supplied"))
    else:
        out.append(SourceCheck(f"{source} time standard", "not_tested", "no TIMESYS in the product header"))
    if lc.bjdref:
        out.append(SourceCheck(f"{source} time reference", "passed", f"BJDREF {lc.bjdref}"))
    return out


def text_checks(path: Path, *, source: str = "text", min_bytes: int = 1) -> list[SourceCheck]:
    try:
        body = Path(path).read_text(encoding="utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return [SourceCheck(f"{source} readable", "failed", f"{type(exc).__name__}: {str(exc)[:160]}")]
    ok = len(body) >= min_bytes
    return [SourceCheck(f"{source} payload", "passed" if ok else "failed",
                        f"{len(body)} character(s); head {body.strip()[:80]!r}")]


def json_checks(path: Path, *, source: str = "json", required_keys: tuple[str, ...] = ()) -> list[SourceCheck]:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [SourceCheck(f"{source} parse", "failed", f"{type(exc).__name__}: {str(exc)[:160]}")]
    out = [SourceCheck(f"{source} parse", "passed", f"{type(data).__name__} payload")]
    if required_keys:
        missing = [k for k in required_keys if not (isinstance(data, dict) and k in data)]
        out.append(SourceCheck(f"{source} required keys", "passed" if not missing else "failed",
                               "all present" if not missing else f"missing {', '.join(missing)}"))
    return out