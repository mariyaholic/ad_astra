<!-- cygnus:generated-draft -->
# Search log: toi-2108-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 264 (63 distinct events, 24 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000347538174-0223-s_lc.fits` | 17707 | 7646 | 3.00 | 12 | 0 |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 17602 | 11007 | 2.50 | 225 | 225 |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 13003 | 8607 | 2.50 | 21 | 21 |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 19542 | 12349 | 4.00 | 18 | 18 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
