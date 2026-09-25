"""Second-stage check for targets the DR3 audit could not classify ("inconsistent"), plus two controls.

For each name below, the spec position is compared directly (no propagation) with Gaia DR2
(gaiadr2.gaia_source, ref_epoch 2015.5) and Gaia DR1 (gaiadr1.gaia_source, ref_epoch 2015.0)
10-arcsec cone results. A TOI-table position copied from a Gaia release matches that release's
catalogue position to within the 1e-6 deg quantisation (<= ~2.5 mas).

  python reports/position-epoch-audit-01/check_outliers.py     -> gaia_dr2_check.json
"""

from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))

SERVICE = "https://gea.esac.esa.int/tap-server/tap"
NAMES = ("TOI-2318.01", "TOI-4319.01", "TOI-6663.01", "TOI-2666.01", "TOI-6666.01")  # last two: controls
TABLES = {"dr2": ("gaiadr2.gaia_source", "source_id, ra, dec, pmra, pmdec, ref_epoch, phot_g_mean_mag"),
          "dr1": ("gaiadr1.gaia_source", "source_id, ra, dec, ref_epoch, phot_g_mean_mag")}


def main() -> int:
    from cygnus.ingest.tap import TapDirect

    tap = TapDirect(SERVICE)
    audit = json.loads((HERE / "audit_results.json").read_text(encoding="utf-8"))
    targets = {}
    for r in audit["results"]:
        if r["name"] in NAMES:
            targets.setdefault(r["name"], r)
    out = {}
    for name in NAMES:
        r = targets[name]
        for rel, (table, cols) in TABLES.items():
            adql = (f"SELECT {cols} FROM {table} WHERE 1=CONTAINS(POINT('ICRS', ra, dec), "
                    f"CIRCLE('ICRS', {r['ra_deg']!r}, {r['dec_deg']!r}, {10 / 3600!r}))")
            when = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            try:
                tab, status = tap.sync_table(adql, timeout_s=120.0)
                err = None
                rows = [{c: (None if str(tab[c][i]) == "--" else tab[c][i].item()) for c in tab.colnames}
                        for i in range(len(tab))]
            except Exception as exc:  # noqa: BLE001 - recorded, never guessed
                status, err, rows = None, f"{type(exc).__name__}: {exc}", []
            for s in rows:
                c = math.cos(math.radians(s["dec"]))
                dra, dde = (r["ra_deg"] - s["ra"]) * c * 3.6e6, (r["dec_deg"] - s["dec"]) * 3.6e6
                s["spec_minus_catalogue_mas"] = [dra, dde, math.hypot(dra, dde)]
            rows.sort(key=lambda s: s["spec_minus_catalogue_mas"][2])
            out[f"{name}|{rel}"] = {"name": name, "release": rel, "query_utc": when, "adql": adql, "status": status,
                                    "error": err, "dr3_match": r["gaia_source_id"], "rows": rows}
            best = rows[0] if rows else None
            print(name, rel, err or (best["source_id"], best["ref_epoch"],
                                     [round(x, 2) for x in best["spec_minus_catalogue_mas"]]), flush=True)
            time.sleep(1.5)
    (HERE / "gaia_dr2_check.json").write_text(json.dumps({"service": SERVICE, "radius_arcsec": 10.0, "checks": out},
                                                          indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
