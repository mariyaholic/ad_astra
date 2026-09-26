<!-- cygnus:generated-draft -->
# Search log: toi-1124-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 819 (299 distinct events, 58 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023181235917-s0067-0000000128790976-0261-s_lc.fits` | 19987 | 13273 | 3.00 | 110 | 103 |
| `tess2019169103026-s0013-0000000128790976-0146-s_lc.fits` | 20479 | 17213 | 3.50 | 154 | 154 |
| `tess2020186164531-s0027-0000000128790976-0189-s_lc.fits` | 17546 | 13469 | 2.50 | 163 | 163 |
| `tess2025180145000-s0094-0000000128790976-0291-s_lc.fits` | 18620 | 15332 | 2.50 | 255 | 255 |
| `tess2026164183000-s0105-0000000128790976-0307-s_lc.fits` | 19915 | 15265 | 3.50 | 144 | 144 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
