# Search log: toi-2087-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 160 (64 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 19337 | 18423 | 2.50 | 41 | 39 |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 18757 | 14831 | 2.50 | 51 | 51 |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 18954 | 17632 | 2.50 | 31 | 31 |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 19694 | 18606 | 2.50 | 37 | 37 |
| `tess2020049080258-s0022-0000000219462190-0174-s_lc.fits` | 19579 | 16718 | 3.00 | 2 | 2 |
| `tess2021175071901-s0040-0000000219462190-0211-s_lc.fits` | 20309 | 19610 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
