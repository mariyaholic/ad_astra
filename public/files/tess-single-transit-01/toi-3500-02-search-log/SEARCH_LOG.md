# Search log: toi-3500-02

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 185 (44 distinct events, 21 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 19385 | 17402 | 3.00 | 117 | 14 |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 18249 | 14333 | 2.50 | 29 | 29 |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 20105 | 18273 | 3.00 | 91 | 91 |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 18814 | 15406 | 2.50 | 51 | 51 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
