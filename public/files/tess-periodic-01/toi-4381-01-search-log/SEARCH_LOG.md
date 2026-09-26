<!-- [private Drive store] -->
# Search log: toi-4381-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 530 (92 distinct events, 40 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 20126 | 19336 | 2.50 | 51 | 42 |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 19064 | 16128 | 2.50 | 181 | 181 |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 18814 | 16085 | 2.50 | 173 | 173 |
| `tess2026086090000-s0102-0000000305767364-0304-s_lc.fits` | 17790 | 15493 | 8.00 | 2 | 2 |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 18969 | 15271 | 3.00 | 132 | 132 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
