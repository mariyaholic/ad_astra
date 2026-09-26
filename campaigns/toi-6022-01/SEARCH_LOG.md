<!-- cygnus:generated-draft -->
# Search log: toi-6022-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 609 (108 distinct events, 93 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000455947620-0245-s_lc.fits` | 20712 | 17990 | 3.00 | 108 | 102 |
| `tess2019279210107-s0017-0000000455947620-0161-s_lc.fits` | 18012 | 15115 | 5.00 | 121 | 121 |
| `tess2024114025118-s0078-0000000455947620-0273-s_lc.fits` | 13003 | 12676 | 2.50 | 109 | 109 |
| `tess2024274222008-s0084-0000000455947620-0281-s_lc.fits` | 18545 | 16716 | 2.50 | 125 | 125 |
| `tess2024300212641-s0085-0000000455947620-0282-s_lc.fits` | 18357 | 16644 | 2.50 | 152 | 152 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
