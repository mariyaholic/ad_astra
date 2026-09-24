# Search log — TESS WASP-12 residual screen

**Campaign:** `tess-wasp12-residual-01`  
**Run date:** 2026-09-24 UTC (runtime date)  
**Outcome:** bounded null; no candidate dossier. No external submission.

## Falsifiable test

For TIC 86396382 (WASP-12), screen two checksum-verified TESS SPOC 120-s light curves (Sectors 20 and 43) for negative flux excursions at least 5 robust-MAD sigmas below local median baselines, lasting at least two consecutive cadences, and outside a conservative ±0.08 orbital-phase window around the known WASP-12 b transit. The result would be a lead only if repeated by reasonable baseline scales/reductions and not explained by quality flags or known transits. The -5 MAD threshold is a descriptive screen, not a calibrated false-alarm probability.

## Access and provenance

- Archive: MAST public product downloads; source URLs and product dataURIs are in `docs/tier1_pack/MASTER_MANIFEST.csv`; transfer used the existing scoped `cygnus:Cygnus/data/tier1/01_mast/` Drive location, one file at a time with `rclone copyto` (not sync). Scratch is `D:\AO_Artifacts\cygnus_scratch\campaign_wasp12\` and is disposable; no originals altered.
- Sector 20 product `tess2019357164649-s0020-0000000086396382-0165-s_lc.fits`: 1,926,720 bytes; manifest SHA-256 `bf74a16f6e0c40b693a66de922e142d446cb44cee5bb7f26843062e436957f63`; recomputed local SHA-256 matched.
- Sector 43 product `tess2021258175143-s0043-0000000086396382-0214-s_lc.fits`: 1,811,520 bytes; manifest SHA-256 `e3d5c6f76884014ec1dec1eb60f04eaf734330a7abd8eef99141f49df03b2493`; recomputed local SHA-256 matched.
- Both files are TESS SPOC light-curve FITS products (120 s in manifest). Sector 20 primary header: `PROCVER=spoc-5.0.96-20230729`, `DATA_REL=73`; Sector 43: `PROCVER=spoc-5.0.45-20211006`, `DATA_REL=62`. Header object TIC 86396382; header RA/Dec 97.6366528°, +29.6722962° (frame realization not independently verified). FITS table records `TIMESYS=TDB`, `BJDREFI=2457000`, `BJDREFF=0`; stored TIME is BJD−2457000 days, not a UTC date.
- Sector 20 UTC header dates: 2019-12-25 to 2020-01-20; usable stored TIME 1842.509510–1868.827130 (BJD-like 2458842.509510–2458868.827130). Sector 43 UTC dates: 2021-09-16 to 2021-10-11; TIME 2474.171742–2498.125471 (BJD-like 2459474.171742–2459498.125471).
- Runtime: Python 3.13.3; NumPy 2.5.3, SciPy 1.18.1, Astropy 8.0.1. Random seed 20260924 is declared in YAML; no stochastic computation was used.

## Catalog and literature gate

- NASA Exoplanet Archive live `pscomppars` snapshot queried 2026-09-24 for WASP-12 (`format=json`; no separately versioned release identifier was exposed in this query): `select pl_name,pl_orbper,pl_tranmid,pl_trandur,disc_refname from pscomppars where hostname='WASP-12'`. Returned WASP-12 b, period 1.09141890100 d, transit midpoint 2457607.51930500, duration 3.001 h, reference Hebb et al. 2009. Source URL: <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select%20pl_name,pl_orbper,pl_tranmid,pl_trandur,disc_refname%20from%20pscomppars%20where%20hostname%3D%27WASP-12%27&format=json>.
- The transit phase is calculated from that archive period/midpoint, but may not model long-baseline transit timing/period evolution. ±0.08 phase was deliberately broad (±2.1 h), not a precision ephemeris fit.
- Web-search requests on 2026-09-24: `WASP-12b transit ephemeris period 1.0914 TESS Sector 20 2019` and `WASP-12 TESS Sector 20 unusual transit event light curve 2019 paper`. Configured generic search service returned HTTP 402 (insufficient balance); these searches did not return results. No ADS, ExoFOP, VSX, or other literature/watchlist query succeeded in this run; those checks are **not tested**, not passed. The target is already a known transiting-planet host, so no novelty claim is in scope.

## Screening and exclusions

| Product | Rows | QUALITY=0 and finite nonzero TIME/SAP/PDCSAP | Excluded from extraction | -5 robust-MAD excursion entries | Entries outside phase window |
|---|---:|---:|---:|---:|---:|
| Sector 20 | 18,954 | 16,551 | 2,403 | 835 (overlapping recipe/reduction entries) | 0 |
| Sector 43 | 17,804 | 15,577 | 2,227 | 464 (overlapping recipe/reduction entries) | 0 |

Excluded cadences include nonzero QUALITY and/or nonfinite/zero flux/time; exact per-reason breakdown was not performed. For each product, flux measured by SAP and PDCSAP separately at centered 1-, 2-, and 3-day running-median scales. Event snippets recur only in the broad known-transit phase window; no threshold crossing survived outside it in any of the six reduction/scale combinations. Counts are not independent events, not trials-corrected, and not detections. No individual excursion is retained as a lead.

Off-transit same-light-curve control (`phase` between 0.08 and 0.92; phase computed from archive ephemeris) contained 13,926 Sector-20 and 13,071 Sector-43 cadences. Robust fractional scatter (SAP, PDCSAP): S20 0.002145, 0.001957; S43 0.001935, 0.001911. These are descriptive noise controls; they are not a calibrated null distribution.

## Artifact checks and omissions

- **Performed:** quality-zero cadence selection; parallel SAP/PDCSAP and three baseline-window comparison; centroid columns MOM_CENTR1/2 were present and their values retained with screen rows; two temporally separated sectors; known transit phase veto.
- **Not tested:** cadence-level centroid/event correlation (centroid columns only retained, no correlation statistic); pixel-level localization, background/scattered light, pointing systematics, cosmic rays/hot pixels, nearby blends/background eclipsing binaries, independent pipeline/reduction or instrument, injection–recovery, calibrated correlated-noise false-alarm rates, current ADS/literature and ExoFOP/watchlist sweep.

## Rejections and null results

1. All -5 MAD snippets were rejected from lead status because they lay inside the deliberately broad phase window for cataloged WASP-12 b transits. This is not evidence for additional objects. Any transit-shape or timing claim would require current transit timing, pixel/centroid auditing, and independent reduction.
2. The proposed target/hypothesis is retained only as a documented bounded null: no out-of-window excursion met the declared threshold in these two SPOC sectors. Other sectors, cadences, targets, filters, and all other phenomena were not searched.

## Reproduction

From repository root with the recorded scratch files and Python environment:

```text
D:\AO_Artifacts\cygnus_scratch\venv\Scripts\python.exe tools\analyze_tess_residual.py D:\AO_Artifacts\cygnus_scratch\campaign_wasp12\tess2019357164649-s0020-0000000086396382-0165-s_lc.fits --out reports\tess-wasp12-residual-01\sector20
D:\AO_Artifacts\cygnus_scratch\venv\Scripts\python.exe tools\analyze_tess_residual.py D:\AO_Artifacts\cygnus_scratch\campaign_wasp12\tess2021258175143-s0043-0000000086396382-0214-s_lc.fits --out reports\tess-wasp12-residual-01\sector43
```

The script enforces exact product basenames, byte lengths, and SHA-256 before reading FITS. Both selected products were successfully processed, producing `screen.json` and `normalized_series.csv` in each derived-output directory. Offline project regression test run from the worktree: `python -m pytest -q -m 'not network'` → **132 passed, 2 deselected** (these are general project tests, not a calibration validation of this real-product screen). Source data remain only in scratch and may be deleted; downloaded source products are not checked into the repository.
