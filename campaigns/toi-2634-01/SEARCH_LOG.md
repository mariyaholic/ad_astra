# Search log: toi-2634-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 3 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 82 (37 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020294194027-s0031-0000000318812447-0198-s_lc.fits` | 18314 | 16176 | 3.00 | 42 | 0 |
| `tess2023263165758-s0070-0000000318812447-0265-s_lc.fits` | 18339 | 15521 | 3.00 | 0 | 0 |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 18677 | 15339 | 2.50 | 82 | 82 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
