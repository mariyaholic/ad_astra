<!-- cygnus:generated-draft -->
# Search log: toi-3787-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.8163162, 't0_bjd': 2459604.335042, 'veto_phase': 0.0465, 'depth_ppm': 15809.0676843, 'duration_h': 3.5830779, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 30), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:55Z (rowupdate 2024-09-08 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 19544 | 16477 | 3.00 | 12 | 0 |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 18494 | 12597 | 3.00 | 25 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
