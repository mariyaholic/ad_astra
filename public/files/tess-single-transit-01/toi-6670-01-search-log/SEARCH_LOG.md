# Search log: toi-6670-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 239 (125 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000126797048-0207-s_lc.fits` | 18066 | 16084 | 3.00 | 359 | 84 |
| `tess2019032160000-s0008-0000000126797048-0136-s_lc.fits` | 17755 | 13178 | 3.00 | 0 | 0 |
| `tess2021039152502-s0035-0000000126797048-0205-s_lc.fits` | 17997 | 13731 | 3.00 | 7 | 7 |
| `tess2023043185947-s0062-0000000126797048-0254-s_lc.fits` | 18517 | 17532 | 3.00 | 8 | 8 |
| `tess2023069172124-s0063-0000000126797048-0255-s_lc.fits` | 19107 | 18358 | 3.00 | 81 | 81 |
| `tess2025042113628-s0089-0000000126797048-0286-s_lc.fits` | 20745 | 20257 | 2.50 | 59 | 59 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
