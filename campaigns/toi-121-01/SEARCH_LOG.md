<!-- cygnus:generated-draft -->
# Search log: toi-121-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 297 (91 distinct events, 30 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000207081058-0190-s_lc.fits` | 18182 | 12596 | 3.00 | 0 | 0 |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 20076 | 18059 | 2.50 | 84 | 84 |
| `tess2023209231226-s0068-0000000207081058-0262-s_lc.fits` | 19824 | 14944 | 3.00 | 0 | 0 |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 18167 | 15174 | 5.00 | 51 | 51 |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 19915 | 15170 | 2.50 | 70 | 70 |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 20484 | 11366 | 2.50 | 92 | 92 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
