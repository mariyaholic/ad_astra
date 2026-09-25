# Search log: toi-4509-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 156 (72 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000319610598-0204-s_lc.fits` | 18231 | 16767 | 3.00 | 0 | 0 |
| `tess2020238165205-s0029-0000000319610598-0193-s_lc.fits` | 18864 | 11750 | 2.50 | 3 | 3 |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 18730 | 17445 | 2.50 | 63 | 63 |
| `tess2020351194500-s0033-0000000319610598-0203-s_lc.fits` | 18609 | 17458 | 3.50 | 0 | 0 |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 18312 | 15257 | 2.50 | 57 | 57 |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 18517 | 15936 | 2.50 | 33 | 33 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
