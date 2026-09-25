# Search log: toi-2435-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 46 (23 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 17765 | 14618 | 3.00 | 3 | 3 |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 18757 | 15589 | 2.50 | 41 | 41 |
| `tess2020049080258-s0022-0000000298164705-0174-s_lc.fits` | 19579 | 16948 | 3.00 | 0 | 0 |
| `tess2020078014623-s0023-0000000298164705-0177-s_lc.fits` | 19279 | 13854 | 3.00 | 1 | 1 |
| `tess2022057073128-s0049-0000000298164705-0221-s_lc.fits` | 19331 | 13824 | 3.50 | 0 | 0 |
| `tess2024058030222-s0076-0000000298164705-0271-s_lc.fits` | 19502 | 13496 | 3.00 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
