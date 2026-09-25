# Search log: toi-4319-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 5 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 339 (154 distinct events, 20 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000157115010-0204-s_lc.fits` | 18231 | 16833 | 3.00 | 87 | 87 |
| `tess2018349182500-s0006-0000000157115010-0126-s_lc.fits` | 15678 | 14612 | 2.50 | 76 | 76 |
| `tess2019006130736-s0007-0000000157115010-0131-s_lc.fits` | 17612 | 16329 | 2.50 | 131 | 131 |
| `tess2020351194500-s0033-0000000157115010-0203-s_lc.fits` | 18609 | 17458 | 2.50 | 44 | 44 |
| `tess2024353092137-s0087-0000000157115010-0284-s_lc.fits` | 19370 | 15677 | 4.00 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
