<!-- [private Drive store] -->
# Search log: toi-450-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 147 (38 distinct events, 17 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 18730 | 17629 | 2.50 | 70 | 54 |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | 18944 | 17198 | 5.00 | 15 | 15 |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 15678 | 14529 | 5.00 | 30 | 30 |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 41332 | 30044 | 7.00 | 30 | 30 |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | 20484 | 12115 | 5.00 | 18 | 18 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
