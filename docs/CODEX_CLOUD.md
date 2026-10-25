# Cygnus in Codex Cloud

Updated 2026-10-25 (Asia/Manila). This is an environment and task handoff,
not a completed cloud science run. Read `AGENTS.md` and `docs/STATUS.md` first.

**One command.** After setup, a cloud task runs a whole tier batch with
`.venv/bin/python -m cygnus.tier cycle cloud/workflow.yaml --env cloud-agent`. It covers preflight,
plan, run, report, pack, delivery and in-place ingest, and is resumable by rerunning it. The result is
a verified handback in `docs/handbacks/<plan-id>/` plus `reports/handback-<plan-id>/`. The local
repository re-verifies it with `python -m cygnus.tier ingest docs/handbacks/<plan-id>`.
Contracts, rejection rules and failure classes are in [TIERS.md](TIERS.md). The step-by-step
commands below remain valid for inspection and debugging.

The repository moved from `mapsugui/ad_astra` to `mariyaholic/ad_astra` on 2026-10-25. The hosted
environment observed below was created for the old path. Whether it follows the transfer is
unverified; if it does not, recreate it for `mariyaholic/ad_astra` with the same settings.

## Create the environment

### Hosted setup observed 2026-10-17

The private `ad_astra` environment was created and published for `mapsugui/ad_astra`
through the hosted setup UI. Its Python 3.12 onboarding reported 734 passed,
one skipped and 37 deselected tests, all 1,283 campaign specifications validated,
and passing site/explorer builds, bundle leak scan and local HTTP checks.
These results cover the existing GitHub checkout, not the newer uncommitted
cloud controller and scouting files in this workstation. Those files must reach
the selected GitHub branch before the full workflow can be verified in cloud.

The configured install script creates `.venv`, installs `.[test,site,campaign]`
and runs `pip check`. The start skill uses explicit `.venv/bin/python`, requires
the workflow files and preflight before research, preserves notebook provenance
and enforces the one-target pilot and native gates. Five variables below were
accepted. The UI rejected `PYTHONUNBUFFERED` as platform-reserved; use `python -u`
when unbuffered command output is needed. Privacy is **Only me**, with no network
secrets. Package managers plus 20 explicit astronomy hosts were configured.
Live archive access, model availability and a hosted science pilot remain
unverified. The first snapshot publish attempt failed with the UI message
"Couldn't publish environment; your settings are saved." One retry succeeded;
the configuration panel subsequently showed **Published**. This publishes a
private reusable environment snapshot, not a scientific result or website.

1. Make the reviewed workflow files available on the GitHub branch you will use
   in `mariyaholic/ad_astra`. A cloud checkout does not receive this workstation's
   uncommitted files, ignored scratch, SQLite ledger or personal skills.
2. In Codex, choose **Work in > Cloud > Select environment > Create environment**
   (or **Settings > Codex Cloud > Environments**). Select `mariyaholic/ad_astra`.
3. Paste the setup request below into the environment setup conversation. Review
   its actual commands, configuration and test results before selecting **Publish**.
4. Start a new task in that published environment. Select **Luna** and **xhigh**
   in the model/effort controls. The intended current model is `gpt-6-luna`;
   account-specific cloud availability is not verified here. If it is unavailable,
   report that rather than silently substituting another model. A prompt or a
   repository file does not select the model for the hosted task.
5. Paste the launch request from the end of this document. Keep the first science
   task to one target; review its outputs before scaling.

### Setup conversation: paste this

```text
Prepare mariyaholic/ad_astra for CPU-only Cygnus campaigns. Read AGENTS.md,
docs/STATUS.md and docs/CODEX_CLOUD.md. Use Python 3.12, matching Linux CI.
Use the repository root as the working directory, including on future tasks.
Record `python3.12 tools/setup_cloud.py` as the install command. It creates/reuses
.venv and installs the existing [test,site,campaign] extras without an upgrade sweep.
Use .venv/bin/python explicitly for every subsequent Python command.
Keep full Git history: notebook provenance tests need historical revisions.
If shallow, run git fetch --unshallow origin; otherwise fetch missing historical
revisions only when a provenance test identifies them. Do not change notebook pins.
Set the non-secret environment variables listed in docs/CODEX_CLOUD.md.
Enable internet with the Package managers preset and the listed archive hosts.
Use existing proxy/CA settings; do not bypass network policy or disable TLS checks.
No credentials, Google Drive, GPU, Windows scheduler or research run is needed
to prepare this environment.
Run .venv/bin/python tools/setup_cloud.py --check, .venv/bin/python -m pytest -q,
and .venv/bin/python -m cygnus.cloud --help. Inspect all exit codes.
Record start instructions to repeat the preflight in new tasks. Repository
refresh does not automatically reinstall changed dependencies: rerun install and
checks, then republish when pyproject.toml or this setup tool changes.
Report the Python version, Git revision/history state, dependency check, test
counts and any blockers. Stop before research or publication. Leave the final
environment Publish action for my review.
```

The script installs only the existing CI extras, constrained on Linux CPython 3.12 by the
resolved pins in `cloud/constraints-linux-py312.txt` (a uv resolution dated in its header, not yet
a tested hosted install). `mast`, `timing`, `imaging` and
`moving` are optional additions for tasks that actually need their extra tools;
do not install every science package for routine queue screening. Record actual
package versions for each run; dependency lower bounds are not a lockfile.

### Environment configuration

| Variable | Value | Purpose |
| --- | --- | --- |
| `CYGNUS_REQUIRE_SITE` | `1` | Fail if publication dependencies are missing. |
| `MPLBACKEND` | `Agg` | Render plots without a desktop. |
| `OMP_NUM_THREADS` | `1` | Avoid CPU oversubscription. |
| `OPENBLAS_NUM_THREADS` | `1` | Keep numerical work within the VM budget. |
| `MKL_NUM_THREADS` | `1` | Same limit for MKL environments. |

Do not add `PYTHONUNBUFFERED` in the hosted variable editor: the platform reserves
that name (observed 2026-10-17). Use `.venv/bin/python -u` for commands that need
immediate progress output.

Leave `CYGNUS_SCRATCH` unset to use `~/.cache/cygnus/scratch` on Linux.
Leave `CYGNUS_LEDGER` unset to use this task's `state/ledger.sqlite`.
Do not copy a Windows drive-letter path into Linux settings. Each new task has
its own working files; a fresh ledger cannot prove a previous campaign completed.
Do not set `CYGNUS_MULTI_ROOT` for the normal production campaign route.

The preflight writes a version-only package inventory and readiness checks to
ignored `state/cloud/environment.json`. It never dumps environment values,
pip credential/index settings, remote URLs or secret files. `--check` uses the
interpreter invoking it and never installs packages. A nonzero exit means stop
and inspect the named failed check. Preflight is offline and does not certify
archive access, cloud configuration or scientific correctness.

### Network configuration

Choose **Allow Codex to access internet**, **Package managers**, and add the
hosts needed by the campaign. These initial hosts come from repository adapter
endpoints and the documented archive routes, not a successful cloud probe:

```text
mast.stsci.edu
exoplanetarchive.ipac.caltech.edu
gea.esac.esa.int
simbad.cds.unistra.fr
tapvizier.cds.unistra.fr
vizier.cds.unistra.fr
cdsarc.cds.unistra.fr
irsa.ipac.caltech.edu
vo.imcce.fr
ssp.imcce.fr
ned.ipac.caltech.edu
skyview.gsfc.nasa.gov
www.legacysurvey.org
legacysurvey.org
portal.nersc.gov
koa.ipac.caltech.edu
archive.eso.org
ssd.jpl.nasa.gov
ssd-api.jpl.nasa.gov
data.minorplanetcenter.net
```

TAP and MAST queries may use POST even for read-only searches. If using the legacy
HTTP-method controls, allow the methods required by those clients as well as
GET/HEAD/OPTIONS. For Gaia async queries, include the TAP job lifecycle methods
if that task needs them. Record blocked requests as unavailable/inconclusive;
do not reinterpret them as empty sky or circumvent the proxy.

Additional domains, redirects and catalogue mirrors must be tested at runtime.
Add the exact host only when the selected workflow needs it. Specialist work
may require `koa.ipac.caltech.edu`, `archive.eso.org`, `skyview.gsfc.nasa.gov`,
literature hosts or product-storage hosts. Consult `DATA_SOURCES.md`; update its
dated access evidence only after an actual probe. The default setup never runs
an all-archive health sweep or downloads FITS.

Use the runtime's environment-status capability when available and inspect
`/etc/codex/network-policy.json` if present before network work. Desired settings
and observed readiness are separate. Keep configured proxy/CA handling intact.
No API key is required to use the public campaign services or to run an already
selected Codex model. Personal connectors and rclone configuration do not
automatically transfer from this workstation.

## Start instructions for each task

Run from the repository root:

```bash
.venv/bin/python tools/setup_cloud.py --check
.venv/bin/python -m pytest -q
```

Stop if either fails. Do not repeatedly run the full suite without a change or
new failure to investigate. If dependencies changed since setup, run
`python3.12 tools/setup_cloud.py` and recheck; update and republish the reusable
environment separately. Do not solve missing packages by weakening tests.
Run verification commands sequentially. `cygnus.publish check` performs a dry
site build under scratch `site_check/`; concurrent checks sharing that scratch
root can delete or lock one another's output. Use separate scratch roots for
independent tasks.

For a coding-only task, follow the explicit task request. For a science task,
use [the gated task brief](prompts/cloud-task.md) and `cloud/workflow.yaml`.
The controller selects a finite batch from the repaired queue, refreshes exact
source rows, runs the native T0/T1 campaign, and continues eligible targets to
native T2 vet/null checks and supported T3 diagnostics. No tier override or
scientific evidence promotion is used.

## Gated execution and resume

For fresh multi-archive scouting and downloads before T0, use
[`CLOUD_SCOUTING.md`](CLOUD_SCOUTING.md) and `cloud/scout.yaml`. The commands
`sources`, `scout` and `acquire` inventory actual capabilities, gather finite
catalogue/field samples and retrieve bounded public products. Pass the resulting
verified `ACQUISITION.json` to `plan --acquisition` to reuse eligible TESS inputs.
This adds source discovery; it does not apply transit tests to images/spectra.

```bash
.venv/bin/python -m cygnus.cloud plan cloud/workflow.yaml
# Use the PLAN.json path printed above:
.venv/bin/python -m cygnus.cloud run state/cloud_runs/<id>/PLAN.json
.venv/bin/python -m cygnus.cloud status state/cloud_runs/<id>/PLAN.json
.venv/bin/python -m cygnus.cloud report state/cloud_runs/<id>/PLAN.json
```

`plan` performs bounded exact-row metadata queries and records every selected,
excluded, duplicate, frozen, already-claimed and lookup-failed row. It downloads
no light curves. Queue rank is a dated heuristic. The refreshed ephemeris goes
into the generated campaign, including the periodic veto. No stale-row fallback
is allowed. The pilot has `limit: 1`; increase it for later finite batches.
Reservations are local to a checkout, so separate cloud tasks need disjoint
assignments. The fresh-source age limit is checked before starting a screen.

`run` uses a serial worker and the existing native methods:

| Stage | Execution | Continuation gate |
| --- | --- | --- |
| `screen` (native T0/T1) | Calibrated light-curve screen, positive control, aliases, context and prior art. | A completed verified record must earn T2; a failed covered positive control stops for review. |
| `T2` | Pinned source light curves/events; native pixel/neighbour/sibling vetting; event nulls and injection recovery. | Every defining event must pass localization, with passed blend, calibrated-null and event-null checks; the recipe must supply a budget and question. |
| `T3` | Requested supported diagnostics, with per-test `ran` and scientific `state`. | All requested diagnostics must run to complete the stage. Missing inputs stay `not_tested`. No automatic T4 or evidence promotion. |

Earned tier is derived with `campaign.tiers`. `run_at` records the highest
verified executed stage (`screen`, `T2`, or `T3`). A target can earn T3 eligibility
while its last executed stage is T2. Completing an inconclusive diagnostic means
it executed; the scientific result remains inconclusive.

All native per-event T2 checks remain in the sky record. Failed dip, detrending,
red-noise, pointing/background or common-mode checks additionally stop automatic
continuation for review. This interlock preserves the canonical earned tier;
it does not relabel a failed check or treat an unavailable check as passed.
Conditional shape, duration and secondary-eclipse interpretations remain
available for model comparison rather than automatic artifact rejection.

The controller reuses the reviewed notebook's pure product-pin, defining-event
and conservative vet-merge helpers from `notebooks/higher_tiers/workflow.py`.
That source is included in the code hash. The notebook and its pinned-history
artifacts are unchanged. Cloud capsules have their own schema and do not claim
to be Colab notebook exports.

Each completed stage is bound to the plan, exact output file set/hashes,
re-derived decision, target identity/ephemeris, and upstream checkpoint. The
supervisor commits a checkpoint only after the worker exits and final resource
checks pass. A changed/extra file, stale source/runtime, altered tier label or
changed upstream checkpoint stops resume. Incomplete attempts do not count as
done. Retry history stays in ignored state. An interrupted final journal append
is preserved as history; corrupt complete/interior journal rows fail closed.

Resume the same PLAN.json in the same task. A new plan is a new selection with
fresh source provenance. `status` is read-only; `report` needs the plan writer
lock. Do not run a second writer or an unbounded retry loop.

The capsule under `docs/handbacks/<id>/` contains the ranked board, selection/
search logs, scientific stage records/reports, source/runtime `LINEAGE.json`,
checkpoint receipts and `MANIFEST.sha256`. Raw FITS and SQLite stay outside it.
It retains negative results and incomplete work, without publishing or uploading.
Plan/ledger/attempt state is under `state/cloud_runs/<id>/`; preserve it for
same-task resume. Cross-task state import is not automated.

## T3 input contracts and limits

`archive_metadata` runs bounded KOA/ESO metadata queries, retaining exact
endpoints, queries, retrieval times, responses and errors. A spatial match or
empty response does not clear source identity or certify RV precision. It does
not download raw spectra. Allow the selected archive hosts in network settings.

`rv_fit` and `prf_source_fit` use optional packets in
`t3.inputs.<campaign-slug>.<test-name>`. Without usable data/quality receipts,
they stay `not_tested` and T3 cannot complete. A packet requires:

- `path`: repository-relative or `scratch:<relative>`; exact lowercase
  `sha256`; `target` and integer `tic` matching the refreshed source.
- `event_label` and `event_bjd`: matching a **measured defining event** from
  native T2 vetting. RV fits never silently use the catalogue planet's epoch.
- `provenance`: `archive`, `product_id`, public HTTPS `url`, timezone-aware
  `retrieved_utc`, and the extraction/table `method`.
- `validation`: `{path: ..., sha256: ...}` for a quality JSON containing matching
  `target`/`input_sha256`, `state: passed`, and nonempty `checks`, each with
  `state: passed` and an inspectable `source`. The controller verifies receipt
  integrity and declared state; scientific adequacy still requires review.

RV CSV columns: `time_bjd_tdb,rv_kms,sigma_kms`. Declare
`time_standard: BJD_TDB`, `velocity_unit: km/s`, `rv_frame: barycentric`,
`periods_days` and optional `jitters_kms`. At least six finite distinct epochs
and positive uncertainties are required. The native fit is conditional on the
event/orbit, one velocity zero point and supplied noise model. It does not choose
a period, establish a companion mass or exclude every alias. Use a validated,
consistently calibrated series; multi-instrument offsets, SB2 extraction and
uncalibrated browse spectra are not solved by this adapter. CSVs are capped at
8 MiB and 10,000 rows.

PRF NPZ arrays: `difference`, `sigma`, `prf`, without pickle. Declare
`instrument: TESS`, `pixel_unit: cutout_pixel`, `flux_unit: electron/s`,
`positions: {<target-name>: [x,y], <competitor>: [x,y]}`, `shifts: [[dx,dy], ...]`
and positive `floors`. The native sampler assumes its 117×117, nine-samples-per-
pixel UPDATED_2.0 layout; inputs must match that assumption. Correct detector/
epoch association, registration, uncertainties and model validation belong in
the quality receipt. Compressed/decompressed size and grids are bounded. Stable
preference remains a conditional `inconclusive` result, never an automatic
on-target pass or independent-sky check.

Raw spectral extraction, calibration association, empirical PRF construction,
primary-literature/TTV clearance and T4 are not automated. Do not invent quality
packets to make an eligible target finish T3.

## Data and completion

- Inspect disk space and product metadata before downloads. The recipe uses one
  CPU worker/target, a 1 GiB managed scratch quota, at least 1 GiB free, 30 minutes
  per worker stage and 60 minutes per `run` invocation. The supervisor samples
  scratch/time and checks completion before checkpointing. One request can
  overshoot between samples; occupancy is not total network bytes. A budget stop
  leaves an incomplete attempt, never a scientific null result.
- `state/cloud/environment.json`, ledger, raw data and caches remain local to
  the task. Keep scientific product IDs, hashes, exact queries, versions, seeds,
  report, search log and valid `sky_record.json` in reviewable small artifacts.
  Retain the task ledger and state for same-task resume; do not commit SQLite.
- Before leaving a task, copy the relevant version inventory into its small
  reproducibility packet, excluding private machine paths. Record the exact Git
  revision and relevant working changes. Reopening the same task is the first
  resume route; a new task must verify/import its inputs and provenance anew.
- If bulky inputs need durable retention, resolve the route with
  `.venv/bin/python -m cygnus.storage where`. Only `Cygnus/` is authorized on
  Drive. Follow `docs/STORAGE.md` and verify uploads before claiming retention.
  If no route is configured, report that explicitly and leave the cloud-task
  scratch intact; never claim a Drive backup or delete the only input copy.
- End with actual test outcomes, retained artifacts, incomplete work and the
  highest-value next test. No automatic scientific evidence promotion,
  publication, catalogue submission, observer contact, scheduler, commit or push
  is included in the default launch brief.

## Local handoff gap at preparation time

The starting local HEAD was `0c0a7f3`. The workstation also held uncommitted
`DATA_SOURCES.md`, `WORKSTACK.md`, `docs/STATUS.md`, `storage/locations.jsonl`,
October 10 Colab audit/run folders, and October 10–11 research report folders.
They are existing work, outside this setup change. `.worktrees/` is also local;
never stage it wholesale. A cloud task must name its checkout revision and read
what is actually present rather than assume it has those newer findings.

The actual workstation preflight imports the new controller and required
packages but returns nonzero because the shared global interpreter has Gradio
dependency conflicts with its installed Pillow/Pydantic versions. Its offline
suite including scouting passed 788 tests (37 deselected, three warnings; 118.94 s), and changed
Python files passed Ruff. Those results do not certify dependency readiness.
The earlier fresh Windows
venv installation was stopped at its local time budget and remains incomplete.
Use the isolated cloud Python 3.12 venv and require a clean `--check` there;
do not copy or certify either workstation environment as the hosted setup.

For fresh queue screening, the existing committed runner can be used after its
gates pass. For continuing the specialist leads or T2 lineage, first transfer
the reviewed latest status/results and verified input receipts through the
authorized repository/storage route. Never reconstruct absent measurements or
rerun frozen lead specs to fill that gap.

## Launch request: paste into a new cloud task

```text
Use the selected Luna model at xhigh. Read AGENTS.md, docs/STATUS.md,
docs/CODEX_CLOUD.md and docs/prompts/cloud-task.md. Verify the environment, then
use cloud/scout.yaml with sources/scout/acquire before cloud/workflow.yaml.
Gather finite public catalogue/product samples and pass verified eligible
inputs through plan --acquisition. Run the native methods through earned tiers,
up to T3. Return other data types as review queues. Keep gates
and thresholds unchanged. Return the reports, board, sky records and manifest,
including failed/inconclusive/not-tested states. Missing validated T3 inputs
are a blocker, not permission to fabricate data or passes. Resume the same plan
when appropriate. Do not commit, push, publish, contact anyone, run T4 or start
a scheduler.
```

## Older environment screen

If your environment uses legacy **Setup script / Maintenance script** fields,
use `python3.12 tools/setup_cloud.py` for setup and dependency refresh, and
`.venv/bin/python tools/setup_cloud.py --check` for an offline readiness check.
Set persistent variables in environment settings; setup-shell exports do not
persist into the agent. Do not apply legacy setup-only-secret assumptions to
the current environment's variable/network-secret system.

## Official references

Verified against official documentation on 2026-10-17:

- [Current cloud environment setup, installation, startup and network configuration](https://learn.chatgpt.com/docs/environments/cloud-environments).
- [Legacy cloud setup and maintenance scripts](https://learn.chatgpt.com/docs/environments/cloud-environment).
- [Legacy internet and HTTP-method settings](https://learn.chatgpt.com/docs/cloud/internet-access).
- [GPT-6 Luna and supported reasoning efforts](https://developers.openai.com/api/docs/models/gpt-6-luna).

Local preparation evidence is recorded in `WORKSTACK.md`. A real Linux cloud
setup, its archive probes and hosted model selection must still be verified
in the environment setup and first task.
