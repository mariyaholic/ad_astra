<!-- [private Drive store] -->
# Search log: toi-764-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 321 (60 distinct events, 36 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 18900 | 14874 | 2.50 | 70 | 53 |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 18066 | 15534 | 2.50 | 48 | 48 |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 18249 | 15560 | 3.00 | 39 | 39 |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 19107 | 17719 | 2.50 | 62 | 62 |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 20105 | 18651 | 3.00 | 55 | 55 |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 19922 | 14076 | 2.50 | 64 | 64 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
