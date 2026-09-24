# Project Cygnus / Astraea

An astronomical data-forensics worktree: tools and records for re-examining public archive data (TESS, Kepler, Gaia, WISE, ZTF, Legacy Surveys and others) for signals that standard pipelines may have missed, and for trying hard to explain them away before calling anything a lead.

Nothing here is a discovery. As of 2026-09-24 the project has run one known-planet recovery test and one bounded residual screen (WASP-12, TESS Sectors 20 and 43; null result). There are no candidate dossiers. The monotransit campaign `tess-mono-01` is a draft.

## Start here

| Read | For |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | The governing specification: principles, investigation protocol, evidence levels, dossier schema. Agents must follow it. |
| [`docs/STATUS.md`](docs/STATUS.md) | Current state, open decisions and known problems: the handoff note. Read second. |
| [`ANALYSIS_STACK.md`](ANALYSIS_STACK.md) | Architecture and the module register (what is built vs. designed). |
| [`DATA_SOURCES.md`](DATA_SOURCES.md) | Verified free archives and access tiers. |
| [`docs/ANALYSIS_SUITE.md`](docs/ANALYSIS_SUITE.md) | Scope and limits of `src/cygnus/analysis/`. |
| [`docs/TEST_ARCHITECTURE_PLAN_DRAFT.md`](docs/TEST_ARCHITECTURE_PLAN_DRAFT.md) | Working-draft test plan and known gaps. |
| [`docs/PUBLISHING.md`](docs/PUBLISHING.md) | The public repository site and its publication boundary. |
| [`docs/AUTONOMY_STUDY.md`](docs/AUTONOMY_STUDY.md) | What runs by itself today, what is manual or only designed, and the next steps. |
| [`docs/CAMPAIGNS.md`](docs/CAMPAIGNS.md) | Campaign specs and the runner: how analyses are run, ledgered and calibrated. |
| [`docs/SKY_RECORDS.md`](docs/SKY_RECORDS.md) | The `sky_record.json` every analysis must leave (enforced by tests). |
| [`design-system/mockups/README.md`](design-system/mockups/README.md) | The interactive sky explorer prototype: build, run, rules. |
| [`design-system/project/README.md`](design-system/project/README.md) | The Ad Astra design system (site look and copy rules). |

## Layout

```
src/cygnus/          Python package: ledger, candidate records, ingest, analysis, reporting, publish (site)
tests/               pytest suite (offline by default; `-m network` for live archive probes)
campaigns/           campaign specs and small campaign runs
reports/             campaign reports, search logs and derived outputs
docs/tier1_pack/     Tier-1 baseline pack manifests, name resolutions, search log
publish/             curated publication manifests for the public site
design-system/       Ad Astra design system source and redesign mockups
notebooks/           Colab reanalysis pilot (not run against real products)
```

## Setup

```bash
python -m venv .venv
.venv/bin/python -m pip install -e ".[test,site]"
.venv/bin/python -m pytest -q
```

Science extras: `mast`, `timing`, `imaging`, `moving`, `analysis` (see `pyproject.toml`).

## What is not in this repository

Bulk archive data, the SQLite provenance ledger (`state/`), scratch downloads and credentials are deliberately excluded (`.gitignore`). The Tier-1 data products live in private cloud storage; this repository holds their manifests and checksums, so each product can be re-fetched from its public archive. Build outputs (`build/`) are regenerated with `python -m cygnus.publish build`.

Licensed under the Apache License 2.0 (see [`LICENSE`](LICENSE)). Third-party data keep their own terms: Gaia-derived files (ESA/Gaia/DPAC) are CC BY-SA 3.0 IGO; Pan-STARRS1, 2MASS, MAST/TESS and NASA Exoplanet Archive material require the acknowledgements recorded in `design-system/mockups/data/PROVENANCE.json` and in each report.
