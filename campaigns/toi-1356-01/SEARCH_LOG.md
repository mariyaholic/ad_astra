<!-- cygnus:generated-draft -->
# Search log: toi-1356-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 245 (85 distinct events, 16 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 20079 | 19610 | 3.00 | 26 | 21 |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 19562 | 18882 | 3.00 | 28 | 28 |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 20712 | 17990 | 3.50 | 13 | 13 |
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | 19947 | 19473 | 3.00 | 8 | 8 |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 19502 | 19025 | 2.50 | 93 | 93 |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 20209 | 12873 | 3.50 | 82 | 82 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
