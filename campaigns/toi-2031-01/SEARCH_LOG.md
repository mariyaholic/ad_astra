<!-- cygnus:generated-draft -->
# Search log: toi-2031-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 205 (43 distinct events, 29 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 19962 | 18695 | 2.50 | 39 | 27 |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 17602 | 16748 | 2.50 | 46 | 46 |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 17992 | 17305 | 2.50 | 42 | 42 |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 19029 | 16048 | 3.00 | 30 | 30 |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 18494 | 12406 | 3.00 | 39 | 39 |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 19337 | 11420 | 3.00 | 21 | 21 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
