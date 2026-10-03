> **2026-09-27 final disposition:** the exoplanet lead is retired. Official
> Gaia and SIMBAD TAP queries traced the host to a Gaia DR3 SB1 orbit; the exact
> queries and rows are recorded in
> `../../reports/lead-followup-2026-09-27/catalog_followup.json`. The derived
> mass function, conditional minimum companion mass and timing comparison are
> in `toi7610_sb1_results.json`. The separate cached-TPF reduction independently
> reproduced the failed S99 localization. See [REJECTION.md](REJECTION.md).
> The generated search log below remains the historical baseline.

<!-- [private Drive store] -->
# Search log: toi-7610-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 39 (9 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 20000 | 15906 | 2.50 | 24 | 3 |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 19922 | 11996 | 3.50 | 36 | 36 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
