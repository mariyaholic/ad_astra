# Search log: toi-6674-01

> Reviewed 2026-09-25; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 75 (26 distinct events, 9 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019306063752-s0018-0000000452920657-0162-s_lc.fits` | 17554 | 15104 | 2.50 | 93 | 74 |
| `tess2020106103520-s0024-0000000452920657-0180-s_lc.fits` | 19074 | 15750 | 3.00 | 0 | 0 |
| `tess2022302161335-s0058-0000000452920657-0247-s_lc.fits` | 19962 | 18337 | 2.50 | 1 | 1 |
| `tess2024300212641-s0085-0000000452920657-0282-s_lc.fits` | 18357 | 12057 | 3.50 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
