<!-- [private Drive store] -->
# Search log: toi-447-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 309 (115 distinct events, 35 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 18730 | 17626 | 3.00 | 119 | 113 |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 18944 | 17391 | 2.50 | 54 | 54 |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 15678 | 14610 | 2.50 | 88 | 88 |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 41332 | 30336 | 3.50 | 54 | 54 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
