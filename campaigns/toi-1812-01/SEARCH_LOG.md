# Search log: toi-1812-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 21 (9 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020049080258-s0022-0000000207425167-0174-s_lc.fits` | 19579 | 17248 | 3.50 | 95 | 0 |
| `tess2020078014623-s0023-0000000207425167-0177-s_lc.fits` | 19279 | 13808 | 2.50 | 13 | 13 |
| `tess2020133194932-s0025-0000000207425167-0182-s_lc.fits` | 18489 | 17245 | 2.50 | 0 | 0 |
| `tess2022057073128-s0049-0000000207425167-0221-s_lc.fits` | 19331 | 13806 | 3.00 | 6 | 6 |
| `tess2022085151738-s0050-0000000207425167-0222-s_lc.fits` | 18896 | 10407 | 3.00 | 0 | 0 |
| `tess2022112184951-s0051-0000000207425167-0223-s_lc.fits` | 17707 | 11969 | 3.50 | 2 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
