# Search log: toi-1301-02

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 79 (57 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020133194932-s0025-0000000356867115-0182-s_lc.fits` | 18489 | 17246 | 3.00 | 6 | 6 |
| `tess2019198215352-s0014-0000000356867115-0150-s_lc.fits` | 19337 | 18422 | 2.50 | 52 | 52 |
| `tess2019226182529-s0015-0000000356867115-0151-s_lc.fits` | 18757 | 15783 | 3.00 | 3 | 3 |
| `tess2019253231442-s0016-0000000356867115-0152-s_lc.fits` | 17765 | 14905 | 2.50 | 15 | 15 |
| `tess2019279210107-s0017-0000000356867115-0161-s_lc.fits` | 18012 | 12941 | 3.00 | 2 | 2 |
| `tess2019306063752-s0018-0000000356867115-0162-s_lc.fits` | 17554 | 14194 | 3.00 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
