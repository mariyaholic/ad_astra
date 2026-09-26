<!-- cygnus:generated-draft -->
# Search log: toi-3312-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 658 (144 distinct events, 66 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 20707 | 16438 | 3.00 | 158 | 158 |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 18862 | 16325 | 3.00 | 239 | 239 |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 19167 | 16487 | 3.00 | 261 | 261 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
