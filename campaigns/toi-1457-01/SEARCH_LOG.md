<!-- cygnus:generated-draft -->
# Search log: toi-1457-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 613 (205 distinct events, 38 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 18545 | 16711 | 3.00 | 220 | 201 |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 18012 | 13125 | 2.50 | 318 | 318 |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 20712 | 17987 | 3.00 | 94 | 94 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
