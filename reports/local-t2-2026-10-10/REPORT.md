# Local Tier 2 notebook execution — 2026-10-10

Run `t2-p02-b02-2026-10-02-10deebcecc06`. Source `p02-b02-2026-10-02`. Completed verified checkpoints: **2/30**; 28 targets have explicit errors. This is a partial live local run, not a Google Colab run or a completed 30-target batch.

The notebook selected 30 eligible targets and excluded 70 from 100 requested first-stage targets (99 checkpointed; earned tiers 68 T0, one T1, 30 T2, one missing). Targets use the same T2 route; input availability determined execution order, not a new scientific ranking. No specialist/frozen lead was rerun.

Drive returned HTTP 403 RATE_LIMIT_EXCEEDED from the shared rclone Google client. The first-stage identity/manifest/sky records were verified. Partial transfer yielded some receipts; every usable receipt was checked against that manifest. Missing receipts were not reconstructed or substituted. The 27 unexecuted targets remain retryable.

## Executed measurements and limits

TOI-1938.01 completed native pixel/neighbour vetting and event-null/injection work. Its E1 box fit is 1245 ± 204 ppm near BJD 2460075.1009383. Localization remains inconclusive; alternative detrending, reference-shape and red-noise checks include failures. Event-null exceedances are 0/190, 0/210 and 0/202, each with resolution 1/N; these are selection-touched local diagnostics, not zero probability or a search-wide significance. Injection recovery is 54/62, 64/71 and 58/69, failing for two source event rows. Three source event rows map into two native event groups; counts are not independent discoveries. Evidence remains Unverified lead.

TOI-2557.01 generated native vetting but no valid completed checkpoint: event-null coverage is 0.606 and 0.539, and neither source event row was measured under the coverage requirement. Its box-fit diagnostic is 1397 ± 479 ppm near BJD 2459254.0438; the native tool marks no significant dip. This is an incomplete/negative follow-up diagnostic, not a validated event or a period determination.

TOI-2629.01 completed a checkpoint, with three native event groups across sectors 94–96. Localization is inconclusive for all three; the sector-94 event has failed background and common-mode checks (two of five neighbouring light curves also dip). Covered event-null rows have 59/246 and 18/249 exceedances and both fail the configured gate. Injection recovery is 50/87 and 64/82 and also fails. This result supplies strong reasons to challenge the source lead, not promote it. Artefact-flagged events supply no period preference; the native alias tables are retained as diagnostics only.

No candidate dossiers, canonical evidence levels, publication collections or companion ledgers were promoted/merged. Both checkpointed source leads retain their inherited Unverified-lead label pending scientific review. The operational checkpoint means the tool sequence and saved-file checks completed, not that scientific checks passed.

| Target | Execution result | Evidence artifact |
| --- | --- | --- |
| toi-1938-01 | completed T2 checkpoint; evidence unchanged | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/campaigns/toi-1938-01/REPORT.md) |
| toi-2191-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-2191-01.json) |
| toi-2557-01 | attempted; failed coverage/completion guard | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/attempts/toi-2557-01/vetting/VETTING.md) |
| toi-2629-01 | completed T2 checkpoint; evidence unchanged | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/campaigns/toi-2629-01/REPORT.md) |
| toi-2939-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-2939-01.json) |
| toi-2952-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-2952-01.json) |
| toi-2956-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-2956-01.json) |
| toi-2995-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-2995-01.json) |
| toi-3100-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-3100-01.json) |
| toi-3431-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-3431-01.json) |
| toi-3533-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-3533-01.json) |
| toi-3576-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-3576-01.json) |
| toi-4880-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-4880-01.json) |
| toi-4945-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-4945-01.json) |
| toi-5263-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-5263-01.json) |
| toi-5330-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-5330-01.json) |
| toi-5615-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-5615-01.json) |
| toi-5699-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-5699-01.json) |
| toi-5937-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-5937-01.json) |
| toi-6224-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6224-01.json) |
| toi-6370-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6370-01.json) |
| toi-6374-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6374-01.json) |
| toi-6410-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6410-01.json) |
| toi-6480-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6480-01.json) |
| toi-6521-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6521-01.json) |
| toi-6609-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6609-01.json) |
| toi-6614-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6614-01.json) |
| toi-6769-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6769-01.json) |
| toi-6831-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-6831-01.json) |
| toi-917-01 | not run; missing manifest-bound source receipt | [output](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/errors/toi-917-01.json) |

## Reproduction

Canonical science code: `notebooks/cygnus_higher_tiers_colab.ipynb`, revision `t2-v1-c3f37cbbb62b`, pinned science commit `05ba4f4ee6e2053c256240ab04f7fbb527e32afe`. The local setup replaces only the Colab mount/install operation; configuration/helpers/target loop/readout use the shipped notebook cells. Discovery uses the source commit for exact campaign specifications. Default null parameters: n_null=300, n_inject=100, min_n=100. Per-target seed, product hashes, source links, environment and specifications are retained in the output capsule.

Local resumable setup/entry point: `scratch:higher_tier_local/run_notebook.py --run`; verified completed checkpoints skip and failed targets retry. The companion SQLite ledger and bulky FITS remain in designated disposable scratch. This local capsule is not registered as an uploaded Drive batch. The notebook export prints a Drive write message and records a Colab-mount writer label even on this local adapter; `LOCAL_EXECUTION.json` explicitly records actual local execution.

Verification: full repository suite 735 passed / 37 deselected / two warnings; notebook/sync checks 61 passed / one warning; pinned native setup gate 58 passed. The saved export was re-audited through cygnus.colab_sync.audit, and small retained output files were copied with SHA-256 comparison. No live Colab mount, T3/T4 adapters, independent confirmation or primary-literature/TTV clearance was established.

Next tests: restore source-receipt access and resume the remaining targets; review per-event localization, detrending and coverage before pursuing any astrophysical interpretation. Primary-literature/TTV comparisons and independent observations remain separate requirements.
