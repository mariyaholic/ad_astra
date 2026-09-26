<!-- cygnus:generated-draft -->
# Search log: toi-1861-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 93 (35 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | 19527 | 11701 | 3.00 | 16 | 16 |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 20119 | 14347 | 2.50 | 6 | 6 |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 20479 | 17222 | 2.50 | 13 | 13 |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 19226 | 18118 | 3.00 | 17 | 17 |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 20126 | 19334 | 3.00 | 40 | 40 |
| `tess2023124020739-s0065-0000000323295479-0259-s_lc.fits` | 20085 | 19514 | 3.50 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
