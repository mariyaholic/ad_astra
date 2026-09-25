# Search log: toi-6671-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 3 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 161 (91 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018206045859-s0001-0000000053843023-0120-s_lc.fits` | 20076 | 17165 | 3.00 | 26 | 26 |
| `tess2023209231226-s0068-0000000053843023-0262-s_lc.fits` | 19824 | 14873 | 3.00 | 4 | 4 |
| `tess2025206162959-s0095-0000000053843023-0292-s_lc.fits` | 18167 | 15043 | 3.00 | 131 | 131 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
