# Search log: toi-790-03

> Reviewed 2026-09-25; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 219 (83 distinct events, 19 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 18569 | 15045 | 3.00 | 288 | 19 |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 20076 | 18278 | 4.00 | 7 | 7 |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 18684 | 14407 | 3.00 | 35 | 35 |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 17755 | 12981 | 3.00 | 20 | 20 |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 18187 | 16170 | 2.50 | 136 | 136 |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | 18900 | 14973 | 3.00 | 2 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
