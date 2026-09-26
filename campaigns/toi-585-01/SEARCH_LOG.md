<!-- cygnus:generated-draft -->
# Search log: toi-585-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 117 (37 distinct events, 12 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 18517 | 16642 | 3.00 | 36 | 30 |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 18187 | 16414 | 2.50 | 32 | 32 |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 20745 | 20253 | 2.50 | 55 | 55 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
