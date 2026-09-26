<!-- cygnus:generated-draft -->
# Search log: toi-1114-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 1032 (180 distinct events, 123 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000409934330-0290-s_lc.fits` | 18862 | 16180 | 3.50 | 167 | 137 |
| `tess2019169103026-s0013-0000000409934330-0146-s_lc.fits` | 20479 | 17219 | 3.00 | 186 | 186 |
| `tess2020186164531-s0027-0000000409934330-0189-s_lc.fits` | 17546 | 14568 | 3.50 | 141 | 141 |
| `tess2023181235917-s0067-0000000409934330-0261-s_lc.fits` | 19987 | 14016 | 4.50 | 133 | 133 |
| `tess2025180145000-s0094-0000000409934330-0291-s_lc.fits` | 18620 | 15378 | 3.00 | 233 | 233 |
| `tess2026060005000-s0101-0000000409934330-0303-s_lc.fits` | 18814 | 15352 | 3.50 | 202 | 202 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
