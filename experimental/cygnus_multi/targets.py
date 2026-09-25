"""Target queue: a ranked list drawn from a declared pool, with the ranking rule and each target's
rationale recorded (AGENTS.md: "maintain a ranked target/lead queue and explain why each lead was
prioritized").

The ranking is a transparent heuristic, not a measurement. The default for single-transit pools is

    score = depth_ppm × sqrt(duration_h) × 10^(−0.2 (Tmag − 10))

i.e. deeper, longer transits on brighter stars (photon noise ∝ flux^−½) rank higher. Sector count
would be a natural extra factor, but the archive's TOI ``sectors`` column was empty for every row
when checked (2026-09-24), so it is not used.
"""

from __future__ import annotations

import csv
import io
import math

EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
TOI_COLUMNS = ("toi", "tid", "tfopwg_disp", "ra", "dec", "st_tmag", "pl_trandep", "pl_trandurh", "pl_tranmid",
               "pl_orbper", "sectors", "toi_created", "rowupdate")
DEFAULT_FORMULA = "depth_ppm * sqrt(duration_h) * 10**(-0.2*(tmag-10))"


def _fetch(adql: str) -> list[dict]:
    import requests

    r = requests.post(EXO_TAP, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
                      headers={"User-Agent": "cygnus-targets/0.1"}, timeout=120)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):
        raise RuntimeError(f"TAP error: {r.text[:300]}")
    return list(csv.DictReader(io.StringIO(r.text)))


def _f(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def score_toi(row: dict) -> tuple[float | None, str]:
    depth, dur, tmag = _f(row.get("pl_trandep")), _f(row.get("pl_trandurh")), _f(row.get("st_tmag"))
    if None in (depth, dur, tmag):
        return None, "not ranked: depth, duration or Tmag missing in the TOI table"
    s = depth * math.sqrt(dur) * 10 ** (-0.2 * (tmag - 10))
    return s, f"depth {depth:.0f} ppm, duration {dur:.2f} h, Tmag {tmag:.2f} → score {s:.0f}"


def build_queue(params: dict, fetch=_fetch) -> dict:
    """``params``: ``source`` (only ``nasa_exoplanet_archive.toi``), ``where`` (ADQL condition),
    ``top`` (queue length)."""
    if params.get("source", "nasa_exoplanet_archive.toi") != "nasa_exoplanet_archive.toi":
        raise ValueError(f"unsupported pool source {params.get('source')!r}")
    where = params.get("where", "pl_orbper IS NULL AND tfopwg_disp IN ('PC','APC')")
    adql = f"SELECT {', '.join(TOI_COLUMNS)} FROM toi WHERE {where}"
    rows = fetch(adql)
    ranked, unranked = [], []
    for r in rows:
        s, why = score_toi(r)
        entry = {"name": f"TOI-{r['toi']}", "tic": int(float(r["tid"])), "ra_deg": _f(r["ra"]), "dec_deg": _f(r["dec"]),
                 "tmag": _f(r["st_tmag"]), "depth_ppm": _f(r["pl_trandep"]), "duration_h": _f(r["pl_trandurh"]),
                 "t0_bjd": _f(r["pl_tranmid"]), "disposition": r.get("tfopwg_disp") or "",
                 "toi_rowupdate": r.get("rowupdate"), "score": s, "rationale": why}
        (ranked if s is not None else unranked).append(entry)
    ranked.sort(key=lambda e: (-e["score"], e["name"]))
    for i, e in enumerate(ranked, 1):
        e["rank"] = i
    top = int(params.get("top", 20))
    return {"query": adql, "endpoint": EXO_TAP, "pool_size": len(rows), "unranked": [(e["name"], e["rationale"]) for e in unranked],
            "ranking": {"formula": DEFAULT_FORMULA, "note": "heuristic for ordering work, not a measurement"},
            "queue": ranked[:top]}
