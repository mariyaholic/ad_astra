# Search log: toi-225-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 91 (38 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000047525799-0121-s_lc.fits` | 19737 | 17844 | 3.00 | 62 | 0 |
| `tess2020238165205-s0029-0000000047525799-0193-s_lc.fits` | 18864 | 14866 | 2.50 | 33 | 33 |
| `tess2023237165326-s0069-0000000047525799-0264-s_lc.fits` | 18569 | 14715 | 5.00 | 0 | 0 |
| `tess2025232030459-s0096-0000000047525799-0293-s_lc.fits` | 18487 | 14390 | 2.50 | 58 | 58 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
