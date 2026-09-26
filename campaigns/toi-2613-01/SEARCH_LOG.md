<!-- cygnus:generated-draft -->
# Search log: toi-2613-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 374 (52 distinct events, 46 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 19824 | 15268 | 3.00 | 94 | 48 |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 18569 | 14671 | 3.00 | 130 | 130 |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 18167 | 15170 | 3.00 | 115 | 115 |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 18487 | 14770 | 2.50 | 81 | 81 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
