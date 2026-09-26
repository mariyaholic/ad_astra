<!-- [private Drive store] -->
# Search log: toi-4427-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 164 (37 distinct events, 22 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 18494 | 12712 | 2.50 | 35 | 23 |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 20309 | 17077 | 2.50 | 51 | 51 |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 19544 | 16429 | 3.00 | 24 | 24 |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 17992 | 17304 | 3.00 | 47 | 47 |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 19232 | 12111 | 3.50 | 19 | 19 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
