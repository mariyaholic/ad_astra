<!-- [private Drive store] -->
# Search log: toi-668-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 735 (179 distinct events, 37 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 18066 | 15113 | 2.50 | 184 | 174 |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 18187 | 15674 | 2.50 | 128 | 128 |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 19107 | 18358 | 2.50 | 282 | 282 |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 20105 | 16524 | 3.50 | 89 | 89 |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 19922 | 14077 | 2.50 | 62 | 62 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
