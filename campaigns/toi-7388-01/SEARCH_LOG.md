<!-- cygnus:generated-draft -->
# Search log: toi-7388-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 1283 (236 distinct events, 201 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 20745 | 17888 | 3.00 | 461 | 461 |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 17997 | 13675 | 2.50 | 421 | 421 |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 18517 | 15539 | 3.00 | 401 | 401 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
