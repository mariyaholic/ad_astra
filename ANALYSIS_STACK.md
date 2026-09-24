# CYGNUS ANALYSIS STACK — Design & Status

Maintained: 2026-09-23 (UTC). Companion docs: `AGENTS.md` (spec), `DATA_SOURCES.md` (verified service catalog).

## Purpose

Layer 2 is the purpose-built forensics layer: the programs we *create* to find
subtleties that standard survey pipelines discard, under the falsification-first
discipline of `AGENTS.md`. Layers:

1. **Layer 1 — off-the-shelf science libraries** (use, don't rebuild):
   `lightkurve`, `astroquery`, `astropy`, TLS (`transitleastsquares`),
   `wotan`, `celerite2`, `batman`, `pyLIMA`, `photutils`/`sep`/`astroscrappy`,
   `skyfield`/JPL Horizons, `emcee`/`dynesty`, `stingray`.
2. **Layer 2 — custom forensics modules** (this package, `src/cygnus/`).
3. **Layer 3 — deliberately *not* built:** full LSST/Gaia-DPAC-style pipelines;
   we consume their outputs and test them with our independent reductions.

## Substrate (built first; shared by every module)

- **`ledger.py`** — SQLite provenance database: `products`, `runs`,
  `measurements`, `candidates`, `prior_art`. Every measurement must reference a
  logged run and product rows; every dossier section must trace to ledger rows.
  Enforces AGENTS.md rules 4/5 mechanically instead of by memory.
- **`candidate_record.py`** — standard output of every detector. Audit states
  limited to `passed|failed|inconclusive|not_tested`; any non-`passed` state pins
  the record to `unverified_lead`; rendering never invents values (absent fields
  render "(none recorded)"); strict validation refuses empty provenance/audit.
- **`instruments.py`** — per-instrument profiles (plate scale, cadence, quirks).
  PSF size is **not** preloaded as a universal cutoff: `psf_fwhm_px=None` forces
  measurement or a library value per campaign — "no universal pixel-width cuts"
  per AGENTS.md Domain IV and falsification-matrix discipline.
- **`config.py`** — single source of truth for paths: worktree (`D:\Ad Astra`),
  scratch root (`D:\AO_Artifacts\cygnus_scratch`, env `CYGNUS_SCRATCH`,
  nonsynced/disposable), ledger DB (`state/ledger.sqlite`, env `CYGNUS_LEDGER`).
  Credentials never enter code/config; they live in uncommitted env files.
- **`ingest/`** — thin archive clients (MAST/`Tesscut`, later IRSA/Gaia/ESO/
  Horizons). Idempotent by checksum, cached in scratch, every product logged to
  the ledger. Lazy heavy imports: unit tests run without the science stack
  (pyproject extras install it: `pip install "cygnus[mast]"` etc.).
- **`priorart.py`** — Known-Object Gate (§ below).
- **`reporting/`** — dossier renderer + leads board, driven *only* by ledger
  and candidate records.

## Layer-2 module register (build status)

| Module | Function | Status |
| --- | --- | --- |
| `ledger.py` | provenance DB, checksums, runs/measurements | **implemented (scaffold)** |
| `candidate_record.py` | standard detector output + invariant rules | **implemented (scaffold)** |
| `instruments.py` | instrument profiles, no-universal-cutoff policy | **implemented (scaffold)** |
| `config.py` | paths (worktree/scratch/state), env overrides | **implemented (scaffold)** |
| `ingest/scratch.py` | scratch resolve + safe cleanup inside scratch root | **implemented (scaffold)** |
| `ingest/mast.py` | MAST SPOC LC search+download, TESScut cutouts | **implemented; live-verified 2026-09-23** (astroquery 0.4.11; TESScut pi Men: sector 12, 5×5×1289 cadences, ledgered) |
| `priorart.py` | Known-Object Gate; service adapters w/ not_tested defaults | **implemented (scaffold; adapters stub)** |
| `reporting/dossier.py` | dossier markdown emission (never invents) | **implemented (scaffold)** |
| `reporting/leads_board.py` | evidence-level ranked table | **implemented (scaffold)** |
| `cli.py` | `doctor`, `dossier` commands | **implemented (scaffold)** |
| `publish/` | public repository site: curated manifests → static site, leak-scanned (`docs/PUBLISHING.md`) | **implemented 2026-09-24** |
| `analysis/` | bounded, in-memory reanalysis pilots: reduction disagreements, pixel controls, imaging residuals, epoch-aware crossmatches, Gaia NSS triage; read-only manifest/FITS adapter | **implemented research utilities; synthetic tests only — see `docs/ANALYSIS_SUITE.md`** |
| `domains/timeseries/detrend_lab.py` | multi-recipe detrending robustness score | designed — Sprint 1 |
| `domains/timeseries/singletransit.py` | monotransit posteriors, coverage constraints | designed — Sprint 1 |
| `domains/timeseries/ttvs.py` | per-transit O–C with GP noise floor | designed — Sprint 1 |
| `domains/imaging/zogydiff.py` | PSF-matched difference imaging (ZOGY-style) | designed — Sprint 2 |
| `domains/imaging/blendmap.py` | difference-image centroids, BEB verdicts | designed — Sprint 1 |
| `domains/imaging/lsblab.py` | Background2D + masked extraction, SB limits | designed — Sprint 2 |
| `domains/auditing/jitterwatch.py` | pointing/centroid/quaternion correlation | designed — Sprint 1 |
| `domains/auditing/crwatch.py` | PSF-profile + streak/cosmic-ray discrimination | designed — Sprint 2 |
| `domains/moving/mover.py` | parallax-aware multi-epoch linking | designed — Sprint 3 |
| `domains/moving/orbitfit.py` | multi-epoch LSQ orbit + error propagation | designed — Sprint 3 |
| `domains/modeling/massfunction.py` | dark-companion M2 posteriors vs alternatives | designed — Sprint 3 |
| `domains/validate/injection_recovery.py` | detection-efficiency curves per method | minimal version — Sprint 1 |
| `domains/validate/nulllab.py` | empirical nulls → calibrated FAPs | Sprint 1–3 |

Sprint order: **S0** substrate (this scaffold) → **S1** monotransit campaign
minimum (detrend/singletransit/blendmap/jitterwatch, minimal injection
recovery, prior-art gate hardening) → **S2** imaging campaigns → **S3** movers
and dark companions.

## Bounded reanalysis suite (implemented research utilities, not domain pipelines)

`src/cygnus/analysis/` now offers in-memory reduction-disagreement ranking,
small TESScut aperture/centroid counterfactuals, cutout model-residual islands,
epoch-aware optical–IR matching and Gaia NSS control/mass-function triage. A
NumPy-only nearest-control ML ranker and checksum-gated, read-only Tier-1/FITS
adapters support a **manually mounted** Colab pilot. All outputs are descriptive
and either inconclusive or explicitly limited; no archived-data calibration,
credible FAP, full survey discovery, Gaia orbit posterior or completed Known-
Object Gate is supplied. Synthetic tests live in `tests/test_analysis_*.py`;
methods, data prerequisites and limits are specified in `docs/ANALYSIS_SUITE.md`.
The designed `domains/...` register above remains designed, not implemented by
these pilots. A Colab mount or verified pack file alone is not a vetting step.

## Execution pattern

Campaigns are declarative YAML in `campaigns/` (see `campaigns/tess-mono-01.yaml`);
a runner executes them as a resumable DAG keyed by config hash (Sprint 1).
Every step is idempotent; interrupt/resume recomputes nothing already ledgered.
Bulk data stays in scratch; curated outputs and reports go to Drive
`cygnus:Cygnus/` via rclone (see `DATA_SOURCES.md`).

## Prior-Art / Known-Object Gate

Goal: never brand a rediscovery as new. Three leak paths, three kill mechanisms:

1. **Watchlists first (Gate 1):** per-domain known-object registries collected
   and *pinned with versions* at campaign start, before screening:
   - planetary: NASA Exoplanet Archive (TOI/KOI/K2), ExoFOP, SPOC per-sector DV
     reports, Villanova Kepler EB catalog;
   - variables: VSX, GCVS, ASAS-SN variable catalog, ZTF periodic catalogs;
   - dark companions: `gaiadr3.nss_two_body_orbit` TAP queries **plus** ADS sweep
     of papers analyzing that table (Gaia BH1/BH2/BH3 came from DR3 data);
   - brown dwarfs: UltracoolSheet-style compilations, Montreal WD DB, Y-dwarf
     lists; SSOs: MPC + SkyBoT per-epoch (via `astroquery.imcce`) + NEOCP;
   - microlensing/FFP: OGLE EWS, KMTNet; transients: TNS (free acct), ATel,
     ALeRCE, Gaia alerts.
2. **Epoch-aware matching (Gate 2):** propagate Gaia proper motion/parallax to
   the observation epoch before any position match; no-match without epoch
   propagation is recorded `not_tested`, never `passed`.
3. **Event-aware matching (Gate 3):** transits are checked against known
   transits that could masquerade through blending (`blendmap.py` feeds inputs);
   moving objects are matched against ephemeris at each image epoch.
4. **Recorded literature sweep (Gate 4):** ADS/bulletin queries stored verbatim
   in the ledger's `prior_art` table; claims use "not found in sources searched
   as of <date>", never bare "uncataloged".
5. **Ambiguity escalation (Gate 5):** partial matches block advancement with a
   `known ?` working label; silent dismissal is forbidden; rejected leads stay
   in the search log.

**Claim rule:** new = full artifact audit + gates 1–4 (pinned) + ambiguity check.
Lead evidence caps: any gate `not_tested` ⇒ at most `unverified_lead` at emission.
Publication lag/embargo means novelty can never be *guaranteed* — only a dated,
reproducible record of no contradiction when checked. Cross-campaign dedupe runs
inside `prior_art` against our own past candidates.

## Testing culture

- Tiny synthetic fixtures for units; published monotransit recoveries as
  end-to-end calibration targets (we quote our recovery rate on known truth).
- `injection_recovery.py` runs early (even rough) so leads tables cite
  completeness curves, not bare sigma.
- Modules with `not_tested` items cannot raise evidence level past
  `unverified_lead` — enforced in `candidate_record.py`.
- Loud failures over silent drops (AGENTS.md); pytest markers: `not network` by
  default, explicit `-m network` for archive smoke tests.

## Environment & verification record

- Python 3.13 venv: `D:/AO_Artifacts/cygnus_scratch/venv` (disposable; recreate
  with `python -m venv` plus the extras groups from `pyproject.toml`).
- Historical record (2026-09-23): `python -m pytest` reported 27 offline
  unit tests; extras plus live MAST probes reported 30 passed. These figures
  describe that earlier checkout, not the present suite.
- Current development verification of the reanalysis additions:
  `python -m pytest -q -m 'not network'` reported **132 passed, 2 deselected**.
  This was an offline synthetic/integration run; no Colab mount, Drive inventory,
  real-product science calibration or live archive smoke was performed.
- Live probe record (`tests/probe_data_check.py`): TESScut pi Men (ra 219.757,
  dec −80.531): sector 12 camera 3 ccd 1; 1289 FFI cadences over ~27.9 d; FLUX
  finite fraction 1.000; product checksummed + ledgered with 2 measurements;
  run closed `completed`. astroquery >=0.4.11 API notes:
  `Tesscut.get_cutouts(coordinates, size, product, sector)`; sector resolved
  live from `get_sectors`; a requested sector not covering the position raises
  loudly instead of returning empty data.
