# Independent verification request: `experimental/cygnus_multi`

Maintained: 2026-09-25 (UTC). Author: Cygnus (agent), on the user's instruction.
Status: **open** — no verifier assigned yet.

## Purpose

The worktree contains an experimental multi-archive campaign pipeline under
`experimental/cygnus_multi/` (with adapters in `experimental/cygnus_multi/archives/`).
It is a *copy* of the production runner in `src/cygnus/campaign/` with the
product discovery/fetch/read path generalised to 24 public archives, a
single-channel screening mode, a red-noise systematics model, per-source
integrity checks and a Gaia DR3 NSS astrometric-vetting step.

The user wants the pipeline's genuinely new parts (and any parts that should
replace production code) **independently verified before they are merged into
the official pipeline**. This file is the verification request and the acceptance
contract. It is not a claim that the pipeline is correct.

**Independence requirement.** The verifier must not be the author of the
experimental code and must not accept the author's summaries as evidence. Every
consequential claim below must be checked against the code, the ledger and the
actual archive responses, and the verifier must attempt to falsify each one. A
nominal pass of the existing test suite is necessary but not sufficient.

## Where things are

| Item | Path |
| --- | --- |
| Pipeline package | `experimental/cygnus_multi/` |
| Archive adapters | `experimental/cygnus_multi/archives/` |
| Offline tests (36) | `experimental/tests/` |
| Sandbox root | `CYGNUS_MULTI_ROOT`, default `experimental/` |
| Sandbox ledger | `<root>/state/ledger.sqlite`, namespace `cygnus_multi:<id>:<step>` |
| Production code reused read-only | `src/cygnus/{ledger,config,skyrecord}.py`, `src/cygnus/ingest/netio.py`, `src/cygnus/analysis/nss.py` |
| Promotion helper (this request's tool) | `experimental/promote.py` |
| Promotion procedure | this file, "Promotion" section |

Run the sandbox (from the repository root; nothing writes outside the root):

```bash
python -m experimental.cygnus_multi --help
python -m experimental.cygnus_multi archives                 # 24 adapters + capabilities
python -m experimental.cygnus_multi archives --check gaia --target "TOI-2666.01" --ra 325.003248 --dec 69.086612
python -m experimental.cygnus_multi run  experimental/campaigns/<id>.yaml
python -m experimental.cygnus_multi report experimental/campaigns/<id>.yaml
python -m pytest experimental/tests -q
python -m pytest tests -q                                    # production gate must stay green
```

## Claims to verify

Each claim is falsifiable and must be reported as **verified**, **refuted**, or
**inconclusive** with the evidence (command, output, ledger run id, query date).

### A. Isolation and provenance

1. A sandbox run writes **only** under `CYGNUS_MULTI_ROOT` (specs, outputs,
   `state/ledger.sqlite`); it does not create or modify `campaigns/`, `reports/`
   or `state/` at the worktree root. Verify by running with a fresh temporary
   `CYGNUS_MULTI_ROOT` and diffing the worktree (`git status`) before/after.
2. Ledger runs from the sandbox use the script namespace
   `cygnus_multi:<campaign_id>:<step>` and `generated_by: cygnus_multi campaign
   runner`; no sandbox run can be mistaken for, or reused by, a production run.
   Verify in `experimental/tests/test_multi_cli.py` and by inspecting the
   sandbox ledger after a real run.
3. `vet` refuses non-MAST-SPOC products with a clear message rather than
   crashing; the CLI exits `0` success / `1` run error / `2` spec error with no
   traceback. Verify each exit code by hand.

### B. Science-bearing code (highest priority)

4. **Mass function.** `nss.mass_function_msun` implements
   `f(M) = P K1^3 (1 - e^2)^1.5 / (2 pi G)` with `P` in days, `K1` in km/s and
   `G` in km^3 Msun^-1 s^-2. Re-derive at least three values independently
   (including one high-eccentricity case) and compare to the function.
   Confirm that no minimum companion mass is claimed anywhere in the report
   text without an adopted primary mass and inclination.
5. **NSS interpretation.** A significant NSS solution must be labelled as
   *refuting a new unseen companion for that target*, not as a mass measurement;
   an empty NSS result must be `inconclusive`, never `passed` (Gaia sensitivity
   is incomplete). Verify in `nss.py`, `steps.step_astrometric_vetting` and in
   the promoted TOI-2666.01 report.
6. **Red-noise model.** `systematics.py`'s event significance and FAP
   (parametric and empirical) must be reproducible from the written series.
   Recompute one event's statistic from the saved `normalized_series.csv` +
   `screen.json` and confirm the reported value and the single-channel caveat
   (`independent=False` when `sap == pdc`, `channel_mode: single`).
7. **Aggregation semantics.** A check that was not run is `not_tested`; an
   unavailable archive or reader is never silently `passed`; the state order is
   `failed > inconclusive > not_tested > passed`; an empty target list yields
   `not_tested`, not `passed`. Verify `steps._aggregate_state` and at least one
   end-to-end case.
8. **Single-channel screening.** When an archive supplies only one flux column,
   the screen must run once (no SAP-vs-PDCSAP comparison), say so in the record,
   and must not report a false independent-channel agreement.

### C. Adapters and readers

9. For each of the 24 adapters, the registered `capabilities`, `source_checks`
   and `kind_for_format` match what the adapter actually implements, and an
   unreachable service raises `AdapterUnavailable` rather than returning an
   empty success. At minimum, exercise one adapter per file (`astronomy.py`,
   `solar_system.py`, `earth_obs.py`, `observing.py`) plus `mast`, `gaia`,
   `vizier`, `simbad`, `horizons`, `sbdb`, `mpc`.
10. `readers.py` dispatches real products to `LightCurve` / `Image` / `Table`
    correctly, and a product of an unsupported format produces an explicit
    `not_tested`/note rather than an exception that aborts the campaign.
11. The MPC adapter uses the reachable host `data.minorplanetcenter.net`
    (`/api/get-obs`, JSON body) and not the main site that was timing out.
    Confirm the endpoint and query from a live call, and record the date.

### D. Differential parity with production

12. For a step implemented by both runners (e.g. `fetch_products`,
    `calibrate_screen`, `residual_screen`), the experimental step produces the
    same science outputs as `src/cygnus/campaign/` for the same inputs and
    parameters. Run both on one pinned product and diff the JSON.
13. The experimental spec format is compatible with production
    (`schema: cygnus.campaign/1`); the production runner's `load_spec` rejects
    experimental-only steps with a clear message (it must not silently ignore
    them). Document any incompatibility found.
14. `cygnus.analysis.nss` (production) and `experimental/cygnus_multi/nss.py`
    must agree on the mass function and on the "no solution = inconclusive"
    rule, or the differences must be listed explicitly.

### E. Operational

15. Steps are resumable: a completed step with an unchanged config hash is
    skipped; `--force` recomputes; `--until` stops cleanly. Verify with the
    ledger and the `RUN_SUMMARY.json`.
16. Two campaigns can run concurrently **only if they are different campaigns**;
    concurrent writers to the same campaign are not safe (no file locks). The
    verifier must confirm this limitation is documented in
    `experimental/README.md` and must not assume it away.
17. `python -m pytest tests -q` (production gate) and
    `python -m pytest tests experimental/tests -q` both pass on a clean
    checkout, with no network access required for the offline tests.

## Known gaps the verifier must test, not assume

- `runner.write_record` does **not** call `cygnus.skyrecord.validate`; the
  production test gate does not scan `experimental/`. Sandbox records are
  therefore not schema-checked by any test today.
- The red-noise model is per-light-curve; it does not fit an orbit.
- The NSS step consumes published Gaia solutions; it does not fit one.
- Adapter availability depends on third-party services and rate limits;
  availability on the verification date must be recorded.
- The experimental tests are outside the production `testpaths` gate by design.

## Required verifier deliverables

Write the verification as a normal worktree analysis so it is collectable and
publicable with the rest of the project:

1. A report at `reports/<verification-id>/REPORT.md` with a claim-by-claim
   verdict table (verified / refuted / inconclusive), exact commands, ledger run
   ids, query dates and any counterexamples.
2. `reports/<verification-id>/SEARCH_LOG.md` with the services, releases,
   queries, thresholds and exclusions used.
3. `reports/<verification-id>/sky_record.json` (`schema:
   "cygnus.sky_record/1"`, `kind` e.g. "pipeline verification", `status:
   completed`, `outcome: pipeline_check`, checks mapping each claim above to a
   state). Run `python -m pytest -q` and confirm the production gate accepts it.
4. A recommendation: **promote as-is**, **promote with changes** (listed), or
   **do not promote**, with the smallest change set that would change the
   verdict.
5. If the verifier writes code, it must not modify `src/cygnus/`; independent
   checks belong in `experimental/tests/` or the verification report's own
   directory. Never submit anything to an external catalogue or observer.

## Promotion

Once (and only once) the verification recommendation is **promote as-is** or the
listed changes are applied, individual results move into the official pipeline
via the no-code-change path implemented in `experimental/promote.py`:

```bash
python -m experimental.promote --campaign <sandbox-id> --as <production-id> \
    --note "independent verification: reports/<verification-id>/REPORT.md"
```

The helper validates the sandbox record against `cygnus.skyrecord.validate`,
refuses to overwrite existing production content, copies the spec, report,
search log, record and runner outputs into `campaigns/<production-id>/`,
rewrites the record's paths, writes `PROMOTED.md` with provenance, and creates a
**draft** collection in `publish/collections/`. Publication and deployment
remain the user's decision (`docs/PUBLISHING.md`); the helper never deploys.

## Sign-off

| Role | Name/agent | Date | Verdict |
| --- | --- | --- | --- |
| Author | Cygnus (agent) | 2026-09-25 | request opened |
| Verifier | _(unassigned)_ | | |
| User (accept/reject) | | | |
