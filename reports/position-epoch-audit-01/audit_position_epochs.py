"""Position-epoch audit of campaign target coordinates against Gaia DR3.

Question: at which epoch are the ``ra_deg``/``dec_deg`` values copied into ``campaigns/*.yaml``
(NASA Exoplanet Archive TOI table) actually valid? The specs label them ``epoch: J2000.0``.

Method (per target position found in a spec):
  1. Gaia DR3 cone search, 10 arcsec, gaiadr3.gaia_source, via the ESA Gaia TAP service
     (sync, CSV), one query per unique position, serialised with a pause between queries.
  2. For every returned source, propagate the DR3 position (epoch 2016.0) linearly with
     (pmra, pmdec) to 2015.5 and to 2000.0 in the tangent plane (pmra already includes cos dec).
  3. Pick the source whose smaller of the two residuals is smallest ("nearest match"); record
     whether it is also the brightest source in the cone.
  4. Classify:  J2015.5      if r(2015.5) <= TOL_MAS and r(2000.0) - r(2015.5) >= SEP_MAS
                J2000.0      if r(2000.0) <= TOL_MAS and r(2015.5) - r(2000.0) >= SEP_MAS
                undetermined if no match, no proper motion, or 16 yr x |PM| < MIN_SHIFT_MAS
                inconsistent otherwise (neither epoch fits; reported individually).

Usage:
  python reports/position-epoch-audit-01/audit_position_epochs.py            # query + classify
  python reports/position-epoch-audit-01/audit_position_epochs.py --offline  # reclassify from gaia_rows.json

Outputs (beside this script): gaia_rows.json (raw rows per position, with query text and UTC time),
audit_results.csv, audit_results.json.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
import time
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

SERVICE = "https://gea.esac.esa.int/tap-server/tap"
RADIUS_ARCSEC = 10.0
TOL_MAS = 5.0          # a residual this small is consistent with the TOI-table 1e-6 deg quantisation
SEP_MAS = 5.0          # the other epoch must be worse by at least this much ("clearly smaller")
MIN_SHIFT_MAS = 10.0   # 16 yr x |PM| below this cannot discriminate 2000.0 from 2015.5
PAUSE_S = 1.5
MAS_PER_DEG = 3.6e6

ADQL = ("SELECT source_id, ra, dec, pmra, pmdec, parallax, phot_g_mean_mag FROM gaiadr3.gaia_source "
        "WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra!r}, {dec!r}, {r!r}))")


def spec_targets() -> list[dict]:
    out = []
    for p in sorted((ROOT / "campaigns").glob("*.yaml")):
        spec = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for t in spec.get("targets") or []:
            if "ra_deg" in t and "dec_deg" in t:
                out.append({"spec": p.relative_to(ROOT).as_posix(), "name": t.get("name"), "tic": t.get("tic"),
                            "ra_deg": float(t["ra_deg"]), "dec_deg": float(t["dec_deg"]),
                            "frame": t.get("frame"), "epoch_label": t.get("epoch"),
                            "position_source": t.get("position_source"), "tmag": t.get("tmag")})
    return out


def _f(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(x) else x


def query_all(targets: list[dict]) -> dict:
    from cygnus.ingest.tap import TapDirect

    tap = TapDirect(SERVICE)
    rows: dict = {}
    for t in targets:
        key = f"{t['ra_deg']!r},{t['dec_deg']!r}"
        if key in rows:
            continue
        adql = ADQL.format(ra=t["ra_deg"], dec=t["dec_deg"], r=RADIUS_ARCSEC / 3600.0)
        when = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            tab, status = tap.sync_table(adql, timeout_s=120.0, max_retries=3)
            recs = [{c: (tab[c][i].item() if hasattr(tab[c][i], "item") else tab[c][i]) for c in tab.colnames}
                    for i in range(len(tab))]
            for r in recs:
                for c in list(r):
                    if isinstance(r[c], float) and math.isnan(r[c]):
                        r[c] = None
                    elif hasattr(r[c], "mask") or str(r[c]) == "--":
                        r[c] = None
            rows[key] = {"query_utc": when, "adql": adql, "status": status, "rows": recs, "error": None}
        except Exception as exc:  # noqa: BLE001 - recorded, never guessed
            rows[key] = {"query_utc": when, "adql": adql, "status": None, "rows": [], "error": f"{type(exc).__name__}: {exc}"}
        print(f"{t['name']}: {len(rows[key]['rows'])} rows {rows[key]['error'] or ''}", flush=True)
        time.sleep(PAUSE_S)
    return rows


def residual(t: dict, s: dict, epoch: float) -> tuple[float, float, float]:
    """Spec minus propagated Gaia position, in mas (RA*cos dec, Dec, total)."""
    dtyr = epoch - 2016.0
    cosd = math.cos(math.radians(s["dec"]))
    ra_p = s["ra"] + (s["pmra"] or 0.0) * dtyr / MAS_PER_DEG / cosd
    de_p = s["dec"] + (s["pmdec"] or 0.0) * dtyr / MAS_PER_DEG
    dra = (t["ra_deg"] - ra_p) * cosd * MAS_PER_DEG
    dde = (t["dec_deg"] - de_p) * MAS_PER_DEG
    return dra, dde, math.hypot(dra, dde)


def classify(t: dict, q: dict) -> dict:
    out = dict(t)
    out.update(query_utc=q["query_utc"], n_gaia=len(q["rows"]), query_error=q["error"])
    if q["error"] or not q["rows"]:
        out.update(epoch_class="undetermined", reason="query failed" if q["error"] else "no Gaia DR3 source in 10 arcsec")
        return out
    scored = []
    for s in q["rows"]:
        r15, r00 = residual(t, s, 2015.5), residual(t, s, 2000.0)
        scored.append((min(r15[2], r00[2]), s, r15, r00))
    scored.sort(key=lambda x: x[0])
    _, s, r15, r00 = scored[0]
    g = [x["phot_g_mean_mag"] for x in q["rows"] if x.get("phot_g_mean_mag") is not None]
    brightest = s.get("phot_g_mean_mag") is not None and s["phot_g_mean_mag"] <= min(g)
    pm = math.hypot(s["pmra"] or 0.0, s["pmdec"] or 0.0) if s.get("pmra") is not None else None
    shift = 16.0 * pm if pm is not None else None
    out.update(gaia_source_id=str(s["source_id"]), gaia_ra=s["ra"], gaia_dec=s["dec"], pmra=s["pmra"], pmdec=s["pmdec"],
               parallax=s["parallax"], g_mag=s["phot_g_mean_mag"], match_is_brightest=brightest,
               pm_total_masyr=pm, shift_16yr_mas=shift,
               res2015_ra_mas=r15[0], res2015_dec_mas=r15[1], res2015_mas=r15[2],
               res2000_ra_mas=r00[0], res2000_dec_mas=r00[1], res2000_mas=r00[2])
    if pm is None:
        out.update(epoch_class="undetermined", reason="matched source has no proper motion (2-parameter solution)")
    elif shift < MIN_SHIFT_MAS:
        out.update(epoch_class="undetermined", reason=f"16 yr x |PM| = {shift:.1f} mas < {MIN_SHIFT_MAS} mas")
    elif r15[2] <= TOL_MAS and r00[2] - r15[2] >= SEP_MAS:
        out.update(epoch_class="J2015.5", reason="")
    elif r00[2] <= TOL_MAS and r15[2] - r00[2] >= SEP_MAS:
        out.update(epoch_class="J2000.0", reason="")
    else:
        out.update(epoch_class="inconsistent", reason="neither epoch within tolerance, or not clearly separated")
    return out


COLS = ["spec", "name", "tic", "ra_deg", "dec_deg", "epoch_label", "position_source", "tmag", "query_utc", "n_gaia",
        "gaia_source_id", "gaia_ra", "gaia_dec", "pmra", "pmdec", "parallax", "g_mag", "match_is_brightest",
        "pm_total_masyr", "shift_16yr_mas", "res2015_ra_mas", "res2015_dec_mas", "res2015_mas",
        "res2000_ra_mas", "res2000_dec_mas", "res2000_mas", "epoch_class", "reason", "query_error"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="reuse gaia_rows.json instead of querying")
    a = ap.parse_args()
    targets = spec_targets()
    raw_path = HERE / "gaia_rows.json"
    if a.offline:
        rows = json.loads(raw_path.read_text(encoding="utf-8"))["positions"]
    else:
        rows = query_all(targets)
        raw_path.write_text(json.dumps({"service": SERVICE, "table": "gaiadr3.gaia_source", "radius_arcsec": RADIUS_ARCSEC,
                                        "positions": rows}, indent=1), encoding="utf-8")
    res = [classify(t, rows[f"{t['ra_deg']!r},{t['dec_deg']!r}"]) for t in targets]
    with (HERE / "audit_results.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for r in res:
            w.writerow({k: (f"{v:.3f}" if isinstance(v, float) and k.startswith(("res", "pm_", "shift")) else v)
                        for k, v in r.items()})
    counts: dict = {}
    for r in res:
        counts[r["epoch_class"]] = counts.get(r["epoch_class"], 0) + 1
    (HERE / "audit_results.json").write_text(json.dumps({
        "service": SERVICE, "table": "gaiadr3.gaia_source", "radius_arcsec": RADIUS_ARCSEC,
        "thresholds_mas": {"tol": TOL_MAS, "sep": SEP_MAS, "min_shift_16yr": MIN_SHIFT_MAS},
        "n_targets": len(res), "n_unique_positions": len(rows), "counts": counts, "results": res}, indent=1),
        encoding="utf-8")
    print(json.dumps(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
