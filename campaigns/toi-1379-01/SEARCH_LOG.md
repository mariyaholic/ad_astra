<!-- cygnus:generated-draft -->
# Search log: toi-1379-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 56 (11 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000252490659-0245-s_lc.fits` | 20712 | 17991 | 3.50 | 11 | 0 |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 20209 | 11028 | 3.50 | 47 | 47 |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | 18545 | 14755 | 2.50 | 9 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
