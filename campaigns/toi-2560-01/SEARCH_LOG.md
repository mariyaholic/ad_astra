<!-- cygnus:generated-draft -->
# Search log: toi-2560-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.5511203, 't0_bjd': 2458348.918997, 'veto_phase': 0.0464, 'depth_ppm': 19660.0, 'duration_h': 2.634, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 25), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:28Z (rowupdate 2021-10-29 12:59:15)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 167 (38 distinct events, 24 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 19824 | 14437 | 3.50 | 2 | 0 |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 18167 | 14912 | 2.50 | 81 | 81 |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 20484 | 12909 | 2.50 | 86 | 86 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
