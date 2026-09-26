<!-- cygnus:generated-draft -->
# Search log: toi-3012-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 423 (90 distinct events, 69 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 18517 | 16759 | 3.00 | 42 | 41 |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 19107 | 18358 | 3.00 | 23 | 23 |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 20745 | 20257 | 2.50 | 183 | 183 |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 20105 | 19273 | 2.50 | 176 | 176 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
