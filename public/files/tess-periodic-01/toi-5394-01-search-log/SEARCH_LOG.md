<!-- [private Drive store] -->
# Search log: toi-5394-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 96 (35 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021336043614-s0046-0000000061109252-0217-s_lc.fits` | 19542 | 17125 | 3.50 | 12 | 6 |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 18089 | 16505 | 3.50 | 18 | 18 |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 20202 | 15650 | 3.50 | 27 | 27 |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 18292 | 14905 | 3.50 | 45 | 45 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
