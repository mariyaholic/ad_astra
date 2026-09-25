# Search log: toi-5563-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 11 (10 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021310001228-s0045-0000000239198720-0216-s_lc.fits` | 18089 | 16473 | 2.50 | 50 | 10 |
| `tess2021336043614-s0046-0000000239198720-0217-s_lc.fits` | 19542 | 17099 | 3.00 | 0 | 0 |
| `tess2022027120115-s0048-0000000239198720-0219-s_lc.fits` | 20202 | 15159 | 4.00 | 1 | 1 |
| `tess2023315124025-s0072-0000000239198720-0267-s_lc.fits` | 18292 | 14722 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
