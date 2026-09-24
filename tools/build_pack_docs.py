"""Aggregate the staged service manifests into the Drive-level pack documents.

Reads every staged 0X_*/MANIFEST.json, produces:
  * MASTER_MANIFEST.csv   (every product row, across services)
  * PROVENANCE_ledger_products.csv (ledger products table export)
  * SEARCH_LOG.md (human-readable narrative + machine log excerpt)
  * README.md (pack guide for the Drive folder)
Also prints a summary table. Files land in the staging pack root and are then
copied to cygnus:Cygnus/data/tier1/.
"""

from __future__ import annotations

import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, r"D:\Ad Astra\src")

from cygnus.config import ledger_path  # noqa: E402
from cygnus.ingest.pack import ledger_products_csv  # noqa: E402
from cygnus.ledger import Ledger  # noqa: E402

PACK_ROOT = r"D:\AO_Artifacts\cygnus_scratch\tier1_pack"
OUT_ROOT = r"D:\Ad Astra\docs\tier1_pack"

SERVICES = [
    ("01_mast", "MAST (STScI)", "TESS SPOC 2-min light curves; TESS FFI cutouts; Kepler LCs; JWST + HST samples"),
    ("02_gaia", "Gaia DR3 (ESA TAP+)", "gaia_source cones; NSS two-body orbits + acceleration; vari_rrlyrae / eclipsing binaries / summary; xp_summary"),
    ("03_skyview", "SkyView (NASA GSFC)", "DSS2 Blue + 2MASS-K cutouts of three test fields; GALEX NUV (M44, Omega Cen)"),
    ("04_cds", "CDS Strasbourg", "TAPVizieR watchlist extracts (VSX, GCVS, Byurakan, ...); SIMBAD benchmark objects"),
    ("05_ned", "NED (IPAC)", "Object queries for the benchmark target list"),
    ("06_eso", "ESO Science Archive", "HARPS ObsCore metadata + two reduced spectra via DATALINK"),
    ("07_irsa", "IRSA (IPAC)", "AllWISE source-catalog cones; ZTF light curves at four anchors"),
    ("08_legacy_survey", "Legacy Survey (LS DR9/DR10)", "Brick listings + DR9 tractor catalogs; DR9/DR10 cutouts; unWISE cutout"),
]

FIELDS = ["service", "pack_dir", "product_id", "dest_rel", "state", "bytes",
          "sha256", "md5", "retrieved_utc", "url", "endpoint", "query",
          "license", "truncated", "extra_json", "note"]


def main() -> None:
    pack = Path(PACK_ROOT)
    out = Path(OUT_ROOT)
    out.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for dirname, label, _ in SERVICES:
        mf = pack / dirname / "MANIFEST.json"
        if not mf.exists():
            print(f"[warn] missing manifest: {mf}")
            continue
        svc_rows = json.loads(mf.read_text(encoding="utf-8"))
        for r in svc_rows:
            r.setdefault("service", label)
            r.setdefault("pack_dir", dirname)
        rows.extend(svc_rows)

    # master CSV
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows:
        clean = dict(r)
        clean["query"] = str(clean.get("query", "")).replace("\n", " ").replace("\r", " ")
        clean["url"] = str(clean.get("url", "")).replace("\n", " ")
        w.writerow({k: clean.get(k, "") for k in FIELDS})
    (out / "MASTER_MANIFEST.csv").write_text(buf.getvalue(), encoding="utf-8")

    # ledger export
    led = Ledger(ledger_path())
    try:
        ledger_products_csv(led, out / "PROVENANCE_ledger_products.csv")
        n_ledger = len(led.products())
    finally:
        led.close()

    # stats
    per_svc: dict[str, dict[str, int]] = {}
    for r in rows:
        st = r.get("state", "?")
        svc = r.get("pack_dir", "?")
        d = per_svc.setdefault(svc, {})
        d[st] = d.get(st, 0) + 1
    # data products = rows with a real md5 and a local/drive_only state
    # (md5-less drive_only rows are tracking records; failed/excluded are probes)
    data_rows = [r for r in rows if r.get("md5") and r.get("state") in ("local", "drive_only")]
    total_local = len(data_rows)
    total_bytes = sum(int(r["bytes"]) for r in data_rows
                      if r.get("bytes") not in ("", None))

    # machine search log excerpt: each service's tail
    mlog = (pack / "SEARCH_LOG.md").read_text(encoding="utf-8")

    lines = []
    lines.append("# CYGNUS Tier-1 Data Pack — Search Log")
    lines.append("")
    lines.append(f"Generated: 2026-09-24 (UTC). Pack contents live on Drive at "
                 f"`cygnus:Cygnus/data/tier1/` and are hosted there only "
                 f"(local staging copies deleted after MD5 verification per the "
                 f"user retention instruction).")
    lines.append("")
    lines.append(f"Aggregate: {total_local} data products, {total_bytes/1e6:.1f} MB, "
                 f"{len(rows)} manifest rows (including probes/exclusions), "
                 f"across 8 archives. Every product carries sha256+md5 checksums, "
                 f"the exact endpoint, and the verbatim query used to retrieve it.")
    lines.append("")
    lines.append("## Service summary")
    lines.append("")
    lines.append("| Pack dir | Archive | Products (state counts) |")
    lines.append("| --- | --- | --- |")
    for dirname, label, what in SERVICES:
        d = per_svc.get(dirname, {})
        counts = ", ".join(f"{k}={v}" for k, v in sorted(d.items()))
        lines.append(f"| {dirname} | {label} | {counts} |")
    lines.append("")
    lines.append("## What each directory contains")
    lines.append("")
    for dirname, label, what in SERVICES:
        lines.append(f"- **{dirname}** — {label}: {what}.")
    lines.append("")
    lines.append("## Volume vs. request (as-built, 2026-09-24)")
    lines.append("")
    lines.append(f"The as-built verified pack is **{total_bytes/1e6:.1f} MB across {total_local} checksummed "
                 "data products**, below the 5–10 GB size range chosen at scope time. The shortfall is a "
                 "property of the queried products, not of missing coverage: every service is represented. "
                 "Scaling notes for a later round (recorded so they are not rediscovered): TESS SPOC LC files "
                 "are ~2 MB each (a 5 GB TESS-only pack needs ~2500 files); the NGC 6819 Kepler cluster stars "
                 "have ~0.2–0.5 MB quarter LCs (cluster targets are faint); the TAP row caps (Gaia sync, "
                 "TAPVizieR, IRSA) bound single-query extracts; and the largest single lever remains larger "
                 "TESScut cubes (30 px cubes already yield 23–198 MB each — 60 px cubes would give ~1 GB "
                 "per sector but must be guarded against memory limits).")
    lines.append("")
    lines.append("## Verified data gaps and limitations (recorded, not hidden)")
    lines.append("")
    lines.append("- **MAST** — 'GJ 1214' has no SPOC 2-min series in the searched cone "
                 "(probe recorded); several `_a_fast` observations hold no LC subgroup. "
                 "JWST/HST samples are single-observation picks, not survey coverage.")
    lines.append("- **SkyView** — 'WISE 12' returned HTTP 404 for all three fields "
                 "(SkyView's WISE service unavailable on 2026-09-23/24); GALEX NUV and "
                 "SDSS g have no coverage for Pleiades in the served footprint. "
                 "Recorded per-field as failed/excluded rows.")
    lines.append("- **Gaia** — `xp_sampled_mean_spectrum` is absent from the live "
                 "`tap_schema` dump (2026-09-24); `xp_summary` was retrieved instead. "
                 "`nss_acceleration` and `vari_eb` do not exist by those names; the live "
                 "schema names `nss_acceleration_astro` and `vari_eclipsing_binary` were used.")
    lines.append("- **CDS** — VSX table id is `B/vsx/vsx` (live-verified); the probe "
                 "fallback name `B/vsx` does not resolve in TAPVizieR. Extracts are "
                 "TOP 20000 row samples of watchlist catalogs, not full catalogs.")
    lines.append("- **ESO** — `ivoa.ObsCore` has no `dataRights` column (400 observed); "
                 "HARPS products were resolved through the DATALINK service. Two reduced "
                 "spectra retrieved (smallest by access_estsize among the TOP 100 metadata rows).")
    lines.append("- **IRSA** — the 20-column AllWISE query is rejected server-side "
                 "(async phase=ERROR); the six-column list was used. 2MASS point-source "
                 "catalog is not served via IRSA TAP (image-metadata tables only) — "
                 "recorded as an exclusion.")
    lines.append("- **Legacy Survey** — the old `/api/region/tractor` service is retired "
                 "(nginx 404s); access now goes through `/viewer/bricks/` + the NERSC "
                 "portal DR9 layout. Omega Centauri (NGC 5139) has no DR9 bricks listed "
                 "and only a near-empty DR9 cutout (out of footprint); DR9 fits-cutouts "
                 "for NGC 5139 and Pleiades failed while DR10 worked for Omega Cen. "
                 "These gaps are recorded, not worked around.")
    lines.append("")
    lines.append("## Machine log (collector stdout, chronological)")
    lines.append("")
    lines.append("```")
    lines.append(mlog[:200000])
    lines.append("```")
    (out / "SEARCH_LOG.md").write_text("\n".join(lines), encoding="utf-8")

    print("rows:", len(rows), "| data products:", total_local, f"| bytes: {total_bytes/1e6:.1f} MB")
    print("ledger rows:", n_ledger)
    print("wrote:", out / "MASTER_MANIFEST.csv", out / "SEARCH_LOG.md")

    # README for the Drive folder
    rd = []
    rd.append("# CYGNUS — Tier-1 Baseline Data Pack")
    rd.append("")
    rd.append("**Location:** `cygnus:Cygnus/data/tier1/` (Drive-hosted; local staging copies are deleted after MD5 verification per the user retention instruction of 2026-09-24).")
    rd.append("")
    rd.append(f"**Contents:** {total_local} checksummed data products ({total_bytes/1e6:.1f} MB), "
              f"{len(rows)} manifest rows (including probe/exclusion records), from all 8 anonymous-access deep-sky archives "
              f"of `DATA_SOURCES.md` §1. Built by `cygnus.ingest.tier1` on 2026-09-23/24. "
              f"Every data product above was MD5-verified against the Drive copy before its local staging copy was deleted.")
    rd.append("")
    rd.append("**Provenance:** every product is checksummed (sha256 + md5), carries its exact endpoint URL and "
              "verbatim query, and is registered in the worktree ledger (`state/ledger.sqlite`; CSV export "
              "`PROVENANCE_ledger_products.csv`). Any product can be re-fetched from its recorded URL.")
    rd.append("")
    rd.append("**Files in this folder:**")
    rd.append("")
    rd.append("| Path | What it is |")
    rd.append("| --- | --- |")
    rd.append("| `MASTER_MANIFEST.csv` | every product row across services (checksums, endpoints, queries, states) |")
    rd.append("| `SEARCH_LOG.md` | service summary, data gaps, and the collector machine log |")
    rd.append("| `PROVENANCE_ledger_products.csv` | ledger `products` table export |")
    rd.append("| `NAME_RESOLUTIONS.json` | CDS Sesame name-resolver results used for every coordinate |")
    rd.append("| `RUN_CONFIG.json` | budgets, target lists, package versions, config hash |")
    rd.append("| `01_mast/` … `08_legacy_survey/` | per-service data + `MANIFEST.json` / `MANIFEST.csv` |")
    rd.append("")
    rd.append("## Service summary")
    rd.append("")
    rd.append("| Pack dir | Archive | Data products (state counts) |")
    rd.append("| --- | --- | --- |")
    for dirname, label, what in SERVICES:
        d = per_svc.get(dirname, {})
        counts = ", ".join(f"{k}={v}" for k, v in sorted(d.items())) or "(none)"
        rd.append(f"| {dirname} | {label} | {counts} |")
    rd.append("")
    rd.append("See `SEARCH_LOG.md` for verified data gaps (they are recorded, never hidden) "
              "and `DATA_SOURCES.md` §0 for the live-verified service quirks this build relied on.")
    (out / "README.md").write_text("\n".join(rd), encoding="utf-8")
    print("wrote:", out / "README.md")


if __name__ == "__main__":
    main()