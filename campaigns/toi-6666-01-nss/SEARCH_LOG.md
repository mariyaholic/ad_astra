# Search log: toi-6666-01-nss

> Drafted by `python -m cygnus.multi report`; reviewed 2026-09-25 — see REPORT.md for the
> reviewer notes.

| Item | Value |
|---|---|
| Archive(s) | gaia, simbad (discovered via the archive adapters; formats csv) |
| Products fetched | 2 (kinds: table) |
| Selection | none — no light-curve product was retrieved, so nothing was screened |
| Veto | — |
| Catalogue services | — |
| Random seed | 20260925 |

## Products fetched (no screen)

No light curve was retrieved, so there are no rows, thresholds or entries to report:

- `gaia_cone_TOI-6666.01_r30as.csv` — gaia, table (Gaia DR3 cone r=30" (5 rows))
- `simbad_TOI-6666.01.csv` — simbad, table (SIMBAD cone r=30" (1 rows))

## Not searched / not tested

- No light curve was retrieved or screened: this campaign's questions are answered from catalogue tables alone, so transit photometry (depths, epochs, centroids) is not tested here.
- The ADS literature search (a declared check marked not_tested in the sky record). Proper-motion propagation to the Gaia epoch was not done by the runner (positions matched as given) but has since been computed in `reports/position-epoch-audit-01`: the TOI-table position is at epoch J2015.5, and the 0.5-yr offset to Gaia DR3 (2016.0) is 0.019″ against a 5″ match radius (check now `passed`).
