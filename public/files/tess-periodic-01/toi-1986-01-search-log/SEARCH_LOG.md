<!-- [private Drive store] -->
# Search log: toi-1986-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 194 (60 distinct events, 28 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 17997 | 13816 | 3.50 | 22 | 22 |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | 18187 | 16518 | 4.00 | 10 | 10 |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 18900 | 15672 | 2.50 | 41 | 41 |
| `tess2021065132309-s0036-0000000468997317-0207-s_lc.fits` | 18066 | 16084 | 3.00 | 0 | 0 |
| `tess2023043185947-s0062-0000000468997317-0254-s_lc.fits` | 18517 | 17532 | 3.00 | 0 | 0 |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 19107 | 18353 | 2.50 | 121 | 121 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
