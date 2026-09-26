# Search log: toi-289-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 75 (28 distinct events, 11 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000201292545-0190-s_lc.fits` | 18182 | 12438 | 2.50 | 11 | 11 |
| `tess2020238165205-s0029-0000000201292545-0193-s_lc.fits` | 18864 | 14819 | 3.00 | 0 | 0 |
| `tess2023209231226-s0068-0000000201292545-0262-s_lc.fits` | 19824 | 13908 | 2.50 | 0 | 0 |
| `tess2023237165326-s0069-0000000201292545-0264-s_lc.fits` | 18569 | 14760 | 3.00 | 7 | 7 |
| `tess2025206162959-s0095-0000000201292545-0292-s_lc.fits` | 18167 | 15074 | 2.50 | 18 | 18 |
| `tess2025232030459-s0096-0000000201292545-0293-s_lc.fits` | 18487 | 14874 | 2.50 | 39 | 39 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
