<!-- cygnus:generated-draft -->
# Search log: toi-2645-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 674 (115 distinct events, 111 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 19107 | 17695 | 3.00 | 149 | 149 |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 20085 | 17078 | 3.00 | 122 | 122 |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 20707 | 12974 | 2.50 | 94 | 94 |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 18569 | 14682 | 3.00 | 97 | 97 |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 20105 | 15195 | 2.50 | 109 | 109 |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 18862 | 14742 | 2.50 | 103 | 103 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
