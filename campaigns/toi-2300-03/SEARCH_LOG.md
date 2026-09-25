# Search log: toi-2300-03

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 74 (25 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021175071901-s0040-0000000280031353-0211-s_lc.fits` | 20309 | 19611 | 3.00 | 142 | 0 |
| `tess2019226182529-s0015-0000000280031353-0151-s_lc.fits` | 18757 | 13244 | 3.00 | 16 | 16 |
| `tess2019253231442-s0016-0000000280031353-0152-s_lc.fits` | 17765 | 11370 | 3.50 | 0 | 0 |
| `tess2020106103520-s0024-0000000280031353-0180-s_lc.fits` | 19074 | 18216 | 4.00 | 0 | 0 |
| `tess2020133194932-s0025-0000000280031353-0182-s_lc.fits` | 18489 | 17245 | 2.50 | 49 | 49 |
| `tess2021204101404-s0041-0000000280031353-0212-s_lc.fits` | 19149 | 18322 | 2.50 | 9 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
