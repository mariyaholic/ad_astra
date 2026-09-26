<!-- cygnus:generated-draft -->
# Search log: toi-830-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 264 (110 distinct events, 15 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 18900 | 15545 | 2.50 | 90 | 90 |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 19527 | 11701 | 2.50 | 70 | 70 |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 20119 | 14346 | 2.50 | 62 | 62 |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 18609 | 17457 | 2.50 | 14 | 14 |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 18066 | 15444 | 3.00 | 24 | 24 |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | 18249 | 15720 | 3.00 | 4 | 4 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
