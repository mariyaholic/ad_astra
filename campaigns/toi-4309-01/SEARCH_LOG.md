# Search log: toi-4309-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 5 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 138 (78 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 18187 | 15036 | 3.00 | 7 | 7 |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | 17997 | 13687 | 3.00 | 5 | 5 |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 18517 | 15780 | 2.50 | 97 | 97 |
| `tess2025042113628-s0089-0000000056662591-0286-s_lc.fits` | 20745 | 19194 | 3.00 | 2 | 2 |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 19064 | 16625 | 3.50 | 27 | 27 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
