<!-- [private Drive store] -->
# Search log: toi-352-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 59 (17 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000047423120-0264-s_lc.fits` | 18569 | 15025 | 3.00 | 7 | 7 |
| `tess2025232030459-s0096-0000000047423120-0293-s_lc.fits` | 18487 | 14065 | 3.00 | 17 | 17 |
| `tess2026192185000-s0106-0000000047423120-0308-s_lc.fits` | 20484 | 12904 | 2.50 | 35 | 35 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
