<!-- cygnus:generated-draft -->
# Search log: toi-3751-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.9157041, 't0_bjd': 2459910.877562, 'veto_phase': 0.0723, 'depth_ppm': 12630.0, 'duration_h': 3.375, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 65), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:30Z (rowupdate 2026-08-06 12:03:27)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 26 (12 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 19029 | 16203 | 2.50 | 185 | 10 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 17804 | 15576 | 2.50 | 165 | 0 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 17466 | 16214 | 2.50 | 50 | 1 |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 18339 | 15243 | 3.00 | 22 | 15 |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 18677 | 15263 | 3.00 | 7 | 0 |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 19132 | 10600 | 3.50 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
