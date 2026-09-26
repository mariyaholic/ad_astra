# Search log: toi-6695-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 279 (75 distinct events, 34 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000118339710-0204-s_lc.fits` | 18231 | 16821 | 2.50 | 233 | 52 |
| `tess2021039152502-s0035-0000000118339710-0205-s_lc.fits` | 17997 | 13644 | 2.50 | 15 | 15 |
| `tess2023018032328-s0061-0000000118339710-0250-s_lc.fits` | 18312 | 15378 | 3.50 | 25 | 25 |
| `tess2025014115807-s0088-0000000118339710-0285-s_lc.fits` | 20000 | 15491 | 2.50 | 187 | 187 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
