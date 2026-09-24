# Search log: toi-2666-01

> Drafted by the runner's report command; reviewed 2026-09-24.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 3 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 59 (32 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000170889511-0205-s_lc.fits` | 17997 | 13613 | 10.00 | 6 | 0 |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 18312 | 15424 | 3.50 | 36 | 36 |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 19922 | 11992 | 5.00 | 23 | 23 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
