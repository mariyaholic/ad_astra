<!-- cygnus:generated-draft -->
# Search log: toi-3437-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.9873145, 't0_bjd': 2459967.078218, 'veto_phase': 0.0294, 'depth_ppm': 16931.1672966, 'duration_h': 2.3425677, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 21), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:09Z (rowupdate 2024-09-10 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 31 (14 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 18312 | 15554 | 4.00 | 0 | 0 |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 18517 | 16726 | 2.50 | 52 | 21 |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 20000 | 18695 | 2.50 | 10 | 10 |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 20745 | 20257 | 4.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
