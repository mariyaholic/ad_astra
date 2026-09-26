<!-- [private Drive store] -->
# Search log: toi-7714-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 82 (33 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 41332 | 25144 | 2.50 | 68 | 58 |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | 18730 | 17489 | 3.50 | 18 | 18 |
| `tess2026192185000-s0106-0000000423785115-0308-s_lc.fits` | 20484 | 12331 | 2.50 | 6 | 6 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
