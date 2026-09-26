<!-- cygnus:generated-draft -->
# Search log: toi-6806-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 229 (69 distinct events, 19 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 18569 | 14533 | 2.50 | 77 | 71 |
| `tess2023209231226-s0068-0000000144327080-0262-s_lc.fits` | 19824 | 14164 | 3.50 | 11 | 11 |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 18487 | 14739 | 2.50 | 91 | 91 |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | 18969 | 14561 | 3.00 | 18 | 18 |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 19167 | 16117 | 2.50 | 12 | 12 |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 19915 | 15025 | 3.00 | 26 | 26 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
