<!-- [private Drive store] -->
# Search log: toi-1976-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 674 (229 distinct events, 48 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021118034608-s0038-0000000329888006-0209-s_lc.fits` | 19226 | 18491 | 2.50 | 226 | 168 |
| `tess2023124020739-s0065-0000000329888006-0259-s_lc.fits` | 20085 | 19408 | 2.50 | 212 | 212 |
| `tess2026060005000-s0101-0000000329888006-0303-s_lc.fits` | 18814 | 16415 | 2.50 | 143 | 143 |
| `tess2026086090000-s0102-0000000329888006-0304-s_lc.fits` | 17790 | 15723 | 2.50 | 151 | 151 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
