# Search log: toi-6667-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 93 (31 distinct events, 11 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 18182 | 14250 | 2.50 | 120 | 12 |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 19824 | 14941 | 2.50 | 23 | 23 |
| `tess2025206162959-s0095-0000000161169240-0292-s_lc.fits` | 18167 | 15209 | 3.00 | 1 | 1 |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | 17790 | 15094 | 3.00 | 3 | 3 |
| `tess2026111101500-s0103-0000000161169240-0305-s_lc.fits` | 18969 | 15079 | 3.50 | 0 | 0 |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 19167 | 15995 | 3.00 | 54 | 54 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
