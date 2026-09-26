<!-- [private Drive store] -->
# Search log: toi-3491-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 786 (205 distinct events, 73 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 20707 | 15147 | 2.50 | 252 | 252 |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 18862 | 15826 | 3.00 | 134 | 134 |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 19064 | 17089 | 3.50 | 115 | 115 |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 17790 | 16113 | 2.50 | 173 | 173 |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 18969 | 15319 | 2.50 | 112 | 112 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
