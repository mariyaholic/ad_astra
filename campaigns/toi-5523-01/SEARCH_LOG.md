# Search log: toi-5523-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 5 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 3 (2 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021310001228-s0045-0000000443616612-0216-s_lc.fits` | 18089 | 16202 | 3.50 | 7 | 3 |
| `tess2021065132309-s0036-0000000443616612-0207-s_lc.fits` | 18066 | 15518 | 3.00 | 0 | 0 |
| `tess2021336043614-s0046-0000000443616612-0217-s_lc.fits` | 19542 | 16631 | 4.00 | 0 | 0 |
| `tess2023069172124-s0063-0000000443616612-0255-s_lc.fits` | 19107 | 17146 | 10.00 | 0 | 0 |
| `tess2023315124025-s0072-0000000443616612-0267-s_lc.fits` | 18292 | 12697 | 4.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
