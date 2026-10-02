<!-- cygnus:generated-draft -->
# Search log: toi-3628-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.4945148, 't0_bjd': 2459879.231564, 'veto_phase': 0.0457, 'depth_ppm': 8254.0, 'duration_h': 2.555, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 31), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:58Z (rowupdate 2025-09-19 12:04:41)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 153 (112 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 20712 | 17991 | 2.50 | 335 | 79 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 18545 | 15966 | 2.50 | 232 | 23 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 18357 | 10683 | 3.00 | 100 | 51 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
