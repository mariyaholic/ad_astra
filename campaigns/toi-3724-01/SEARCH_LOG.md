# Search log: toi-3724-01

> Reviewed 2026-09-25; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 3 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 146 (42 distinct events, 17 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000143642240-0248-s_lc.fits` | 19029 | 16692 | 2.50 | 71 | 71 |
| `tess2023341045131-s0073-0000000143642240-0268-s_lc.fits` | 19337 | 11368 | 3.00 | 57 | 57 |
| `tess2024326142117-s0086-0000000143642240-0283-s_lc.fits` | 19132 | 11790 | 3.50 | 18 | 18 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
