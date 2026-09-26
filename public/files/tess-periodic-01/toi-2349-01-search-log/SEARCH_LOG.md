<!-- [private Drive store] -->
# Search log: toi-2349-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 153 (20 distinct events, 19 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 18517 | 16007 | 2.50 | 37 | 27 |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 20745 | 19185 | 3.50 | 85 | 85 |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 19922 | 12398 | 3.50 | 41 | 41 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
