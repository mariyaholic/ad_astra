# Handoff: Colab connectivity for Cygnus batches

> **Historical connectivity brief. Current note, 2026-10-03:** mount-written
> exports have since been read through a verified workstation route; scope and
> visibility remain harness-specific, dated observations. Resolve the route with
> `python -m cygnus.storage where`. Use [COLAB_SYNC.md](COLAB_SYNC.md) for current
> export auditing and the one canonical scheduler; do not implement a second
> sync from the proposal below. Companion-ledger and provenance rules still apply.

Written 2026-09-26 for the next agent. **Status: pilot done by another harness; see `docs/STATUS.md` and `docs/STORAGE.md` for the verified outcome and the storage standard.** Read `AGENTS.md`, `docs/STATUS.md` and `docs/AGENT_RUNBOOK.md` (*Batches*) first. This file is a brief, not a design: decide the details, test them, then record the outcome in `docs/STATUS.md` and `DATA_SOURCES.md`.

## Goal

Let `python -m cygnus.batch` run campaigns on a **Google Colab** runtime so that large batches (hundreds to thousands of targets) are not limited by this workstation's disk, and bring the results back into the repository with full provenance, identical to a local run.

## Why (measured 2026-09-26)

- A known-object campaign costs about **1 min** wall time at 3 parallel jobs, about **14 MB** of ignored intermediates under `campaigns/<id>/` and about **20 MB** of archive products in scratch. Only ~170 KB per campaign is committed.
- `D:` has **55 GB free (95 % full)**. About 1,000 targets fit; 5,000 do not.
- The bottleneck is **disk and archive rate limits, not CPU**. Nothing in the pipeline needs a GPU.

## Resources and constraints from the user

- **Colab Pro, about 80 compute units left.** Use a **CPU-only** runtime; never pick GPU or TPU for this work. Check the current burn rate in Colab's *Resources* panel before a long run and report the actual units used afterwards. Do not quote a rate you have not seen.
- The user signs in to Google; you never enter their password (see the safety rules). If you drive Colab through the in-app browser, the user must be signed in there already or sign in themselves.
- **Do not tunnel SSH, remote desktops or reverse shells into Colab.** Colab's terms restrict them, and they would be a security hole. The notebook runs the batch itself.
- Nothing is published, submitted or deployed from Colab.

## What exists now

- `notebooks/cygnus_reanalysis_colab.ipynb`: a **read-only single-product reanalysis pilot**. It mounts Drive, expects hand-edited `REPO_ROOT`/`PACK_ROOT`/`PRODUCT_ID`, installs `[analysis]` and compares SAP and PDCSAP for one product. It does not run campaigns or batches. Keep it; build a separate batch notebook.
- The repository is public (`https://github.com/mariyaholic/ad_astra`, transferred from `mapsugui` on 2026-10-25; checked 2026-09-26), so a runtime can `git clone` it without credentials.
- `cygnus.config.scratch_dir()` honours `CYGNUS_SCRATCH`. Set it to a VM path such as `/content/scratch` (never the Drive mount; FITS reads over the mount are slow).
- The batch driver takes `--spec`, `--jobs`, `--redo` and `--timeout`, keeps a journal under `state/batches/<id>/`, and holds one lock per ledger (`state/ledger.sqlite`).
- Live archive health check: `python -m cygnus.multi archives --check all` (run it first on the Colab VM; Google's egress IPs may be treated differently from this workstation's).

## Known problems you must resolve or document

1. **The Drive remote does not match the docs.** *Resolved 2026-09-26 by the user's decision: remote names are per-harness (`gdrive:` here, `cygnus:` in another harness), so nothing shared may name one. Locations are recorded in `storage/locations.jsonl` and resolved with `python -m cygnus.storage` (`docs/STORAGE.md`).*
2. **Scope mismatch.** The token's `drive.file` scope only sees files **rclone itself created**. Files a Colab `drive.mount()` writes are invisible to it. Choose one path and verify it both ways:
   - **Option A (recommended to evaluate first):** run rclone **inside Colab** with the same remote config supplied through **Colab Secrets** (`google.colab.userdata`). Uploads are then made by the same client and are visible locally. The user adds the secret themselves; never paste, log, print or commit the config or its token.
   - **Option B:** use `drive.mount()` in Colab and download locally through a different route. Confirm the local side can actually see the files before relying on it.
3. **The shared rclone client ID is being retired during 2026** (rclone prints a notice on every call). If authorisation errors appear, tell the user; creating their own client ID is their action.
4. **The ledger does not merge.** `state/ledger.sqlite` is local and uncommitted. A Colab run writes its own ledger, and nothing today imports runs from one ledger into another. Pick one:
   - (a) the Colab ledger becomes a named, archived companion ledger for that batch (ship it back beside the batch journal and record its path and SHA-256 in `docs/STATUS.md`);
   - (b) build a tested import tool that copies runs, measurements and products with their IDs remapped and provenance kept.
   Records cite ledger `run_id`s, so whichever you choose must keep every committed `run_id` resolvable. Tests first.
5. **Session limits.** Colab sessions end on idle and at a maximum lifetime. The batch driver is resumable (journal plus runner step reuse). Make the notebook re-entrant: clone or pull, restore the batch state and ledger from Drive, run, and push the state back at intervals, not only at the end.
6. **Rate limits.** *Resolved 2026-09-26: a cross-process rate limiter (one limit per archive host) is wired into the adapters and the product download path (commit `8cf091b`).* Colab and a local batch may overlap within its limits; the Colab stress run used `--jobs 7` on 8 vCPU without throttle errors. Keep `--jobs` near the core count and watch for `AdapterUnavailable`/timeout bursts.

## Suggested shape (adjust as you see fit)

A new `notebooks/cygnus_batch_colab.ipynb`:

1. CPU runtime check; `git clone` a **pinned commit** (record the SHA); `pip install -e .[test,mast]`; `python -m pytest -q` must pass before anything else runs.
2. `CYGNUS_SCRATCH=/content/scratch`; restore `state/` (ledger, batch journal) from Drive if present.
3. `python -m cygnus.multi archives --check all` and save the output.
4. `python -m cygnus.batch run --batch <id> --jobs 3 --spec ...` (specs come from the repo; queue and claim happen locally and are committed first).
5. Periodically and at the end: upload `state/batches/<id>/`, the ledger, and each finished `campaigns/<id>/` (committed files only; see `.gitignore`) to `Cygnus/colab_runs/<batch>/` with a manifest of SHA-256s. Archive products stay on the VM and are discarded: their checksums are already in the records, and L2 replay re-verifies on re-download.
6. Locally: download, verify every checksum, copy the campaign outputs in, run `python -m cygnus.batch status`, `python -m pytest -q`, review as usual (`docs/AGENT_RUNBOOK.md`), commit.

## Acceptance

- **Equivalence:** a pilot of 3 committed campaigns (e.g. `toi-2666-01`, `toi-1301-02`, `toi-2003-01`) run on Colab gives the same science values as the committed local outputs (screen entries, k\*, completeness, aliases, check states). Use `tests/test_replay_l2.py` as the model for the comparison. Differences are explained or fixed, not waved through.
- Round trip works in both directions with the `drive.file` token, verified by listing and checksumming, never assumed.
- No credentials in the notebook, its outputs, logs or commits (clear outputs before committing the notebook).
- `docs/STATUS.md`, `DATA_SOURCES.md` and `AGENTS.md` updated (remote name, Colab route, compute units actually used, limits found).
- Only then propose a larger Colab batch to the user, with an estimate of compute units and time taken from the pilot's actual numbers.

## Out of scope

GPU work, publishing, submitting leads anywhere, and changing science thresholds. A local disk-retention step (deleting scratch products and ignored intermediates after the record is written) is a separate, cheaper option for the disk problem. Mention it to the user if Colab turns out to be awkward; it is not this task.
