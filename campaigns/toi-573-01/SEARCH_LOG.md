<!-- cygnus:generated-draft -->
# Search log: toi-573-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 83 (28 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | 17755 | 12989 | 4.50 | 13 | 7 |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 17997 | 13619 | 4.00 | 48 | 48 |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | 18517 | 16025 | 3.50 | 12 | 12 |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | 19922 | 12392 | 3.00 | 16 | 16 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
