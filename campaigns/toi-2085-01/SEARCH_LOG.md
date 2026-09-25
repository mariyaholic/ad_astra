# Search log: toi-2085-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 116 (58 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019357164649-s0020-0000000103633672-0165-s_lc.fits` | 18954 | 17632 | 2.50 | 27 | 16 |
| `tess2019198215352-s0014-0000000103633672-0150-s_lc.fits` | 19337 | 18422 | 3.00 | 47 | 47 |
| `tess2020020091053-s0021-0000000103633672-0167-s_lc.fits` | 19694 | 18758 | 3.00 | 15 | 15 |
| `tess2021175071901-s0040-0000000103633672-0211-s_lc.fits` | 20309 | 19313 | 2.50 | 35 | 35 |
| `tess2021204101404-s0041-0000000103633672-0212-s_lc.fits` | 19149 | 18322 | 3.00 | 0 | 0 |
| `tess2021364111932-s0047-0000000103633672-0218-s_lc.fits` | 19544 | 16480 | 3.00 | 3 | 3 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
