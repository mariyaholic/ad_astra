<!-- cygnus:generated-draft -->
# Search log: toi-5149-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 122 (33 distinct events, 12 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 19562 | 18882 | 2.50 | 32 | 15 |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | 19149 | 18320 | 3.00 | 15 | 15 |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 20079 | 19612 | 2.50 | 19 | 19 |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | 19947 | 19474 | 3.00 | 16 | 16 |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 19502 | 19025 | 2.50 | 40 | 40 |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 18619 | 18137 | 3.00 | 17 | 17 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
