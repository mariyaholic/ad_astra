<!-- [private Drive store] -->
# Search log: toi-1351-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 342 (60 distinct events, 38 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 19132 | 13749 | 2.50 | 63 | 53 |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 20309 | 18358 | 3.00 | 79 | 79 |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 19149 | 18322 | 4.00 | 56 | 56 |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 19544 | 15526 | 3.50 | 69 | 69 |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 20202 | 14147 | 2.50 | 43 | 43 |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 19331 | 10701 | 3.50 | 42 | 42 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
