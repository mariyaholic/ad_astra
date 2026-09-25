# Search log: toi-6692-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 106 (44 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000324609409-0210-s_lc.fits` | 20126 | 19337 | 3.00 | 105 | 3 |
| `tess2023153011303-s0066-0000000324609409-0260-s_lc.fits` | 20707 | 15535 | 3.50 | 0 | 0 |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 19987 | 14701 | 2.50 | 28 | 28 |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 18862 | 15564 | 2.50 | 11 | 11 |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 18620 | 15078 | 2.50 | 20 | 20 |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 18814 | 15160 | 2.50 | 44 | 44 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
