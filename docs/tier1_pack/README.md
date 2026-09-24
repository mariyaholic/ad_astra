# CYGNUS — Tier-1 Baseline Data Pack

**Location:** `cygnus:Cygnus/data/tier1/` (Drive-hosted; local staging copies are deleted after MD5 verification per the user retention instruction of 2026-09-24).

**Contents:** 82 checksummed data products (1112.1 MB), 132 manifest rows (including probe/exclusion records), from all 8 anonymous-access deep-sky archives of `DATA_SOURCES.md` §1. Built by `cygnus.ingest.tier1` on 2026-09-23/24. Every data product above was MD5-verified against the Drive copy before its local staging copy was deleted.

**Provenance:** every product is checksummed (sha256 + md5), carries its exact endpoint URL and verbatim query, and is registered in the worktree ledger (`state/ledger.sqlite`; CSV export `PROVENANCE_ledger_products.csv`). Any product can be re-fetched from its recorded URL.

**Files in this folder:**

| Path | What it is |
| --- | --- |
| `MASTER_MANIFEST.csv` | every product row across services (checksums, endpoints, queries, states) |
| `SEARCH_LOG.md` | service summary, data gaps, and the collector machine log |
| `PROVENANCE_ledger_products.csv` | ledger `products` table export |
| `NAME_RESOLUTIONS.json` | CDS Sesame name-resolver results used for every coordinate |
| `RUN_CONFIG.json` | budgets, target lists, package versions, config hash |
| `01_mast/` … `08_legacy_survey/` | per-service data + `MANIFEST.json` / `MANIFEST.csv` |

## Service summary

| Pack dir | Archive | Data products (state counts) |
| --- | --- | --- |
| 01_mast | MAST (STScI) | (none) |
| 02_gaia | Gaia DR3 (ESA TAP+) | (none) |
| 03_skyview | SkyView (NASA GSFC) | (none) |
| 04_cds | CDS Strasbourg | (none) |
| 05_ned | NED (IPAC) | (none) |
| 06_eso | ESO Science Archive | (none) |
| 07_irsa | IRSA (IPAC) | (none) |
| 08_legacy_survey | Legacy Survey (LS DR9/DR10) | (none) |

See `SEARCH_LOG.md` for verified data gaps (they are recorded, never hidden) and `DATA_SOURCES.md` §0 for the live-verified service quirks this build relied on.

The separately developed read-only research pilot in `src/cygnus/analysis/` and
`notebooks/cygnus_reanalysis_colab.ipynb` is described in `docs/ANALYSIS_SUITE.md`.
It checks SHA-256 before loading a selected file and does not mount or inspect
Drive on its own. This document's product totals reflect the recorded pack
build, not a fresh Drive inventory; a Colab account's mount permissions must
be verified separately. The chosen targets are benchmark examples rather than
an exhaustive or previously unsurveyed sky sample.