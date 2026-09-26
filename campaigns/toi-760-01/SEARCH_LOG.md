<!-- cygnus:generated-draft -->
# Search log: toi-760-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 209 (65 distinct events, 14 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 18900 | 14394 | 3.00 | 29 | 10 |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | 18066 | 15467 | 3.00 | 4 | 4 |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 18249 | 15120 | 3.00 | 25 | 25 |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 19107 | 17117 | 2.50 | 57 | 57 |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 20105 | 18346 | 3.00 | 61 | 61 |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 19922 | 14076 | 2.50 | 52 | 52 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
