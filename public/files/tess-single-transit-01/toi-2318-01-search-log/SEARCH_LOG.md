# Search log: toi-2318-01

> Reviewed 2026-09-25; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 213 (89 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020160202036-s0026-0000000088840705-0188-s_lc.fits` | 17909 | 16941 | 3.00 | 88 | 47 |
| `tess2020133194932-s0025-0000000088840705-0182-s_lc.fits` | 18489 | 17245 | 4.00 | 8 | 8 |
| `tess2022138205153-s0052-0000000088840705-0224-s_lc.fits` | 17602 | 16643 | 3.00 | 20 | 20 |
| `tess2022164095748-s0053-0000000088840705-0226-s_lc.fits` | 17992 | 17302 | 2.50 | 81 | 81 |
| `tess2024142205832-s0079-0000000088840705-0274-s_lc.fits` | 19542 | 19073 | 3.00 | 15 | 15 |
| `tess2024170053053-s0080-0000000088840705-0275-s_lc.fits` | 19047 | 18555 | 2.50 | 42 | 42 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
