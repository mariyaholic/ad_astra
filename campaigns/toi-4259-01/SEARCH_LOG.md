<!-- cygnus:generated-draft -->
# Search log: toi-4259-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 8.9612626, 't0_bjd': 2459963.456678, 'veto_phase': 0.02, 'depth_ppm': 11333.9389745, 'duration_h': 1.8325932, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 28), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:45Z (rowupdate 2024-09-06 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 49 (29 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | 18312 | 15775 | 3.50 | 18 | 0 |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 18517 | 16510 | 3.00 | 70 | 29 |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 20000 | 18032 | 2.50 | 84 | 20 |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | 20745 | 20256 | 3.00 | 41 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
