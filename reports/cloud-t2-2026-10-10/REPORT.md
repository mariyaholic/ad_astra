# Cloud Tier 2 batch execution — 2026-10-10

All 30 eligible targets from first-stage source `p02-b02-2026-10-02` were handled in one automatic batch. Two verified local checkpoints were imported and skipped; the remaining 28 were attempted on a CPU Colab runtime through the Codex in-app browser. The target-loop UI duration was 54 minutes. Final result: **19/30 checkpoints, 17 at T2, two closed, 11 incomplete**. No target currently passes the implemented T3 science gate or complete saved-spec eligibility.

Run `t2-p02-b02-2026-10-02-10deebcecc06` uses notebook commit `0c0a7f3e89351d7e9596f7a46b637377cd6365c7`, revision `t2-v1-c3f37cbbb62b`, science pin `05ba4f4ee6e2053c256240ab04f7fbb527e32afe`. Source manifest SHA256: `440b3780231eb6e05c69845fbfca201243889239d79d09cf891c34249c921f51`. Source commit: `9250aee3b91d7da7d664681195a250ec85d8c43d`. The source requested 100 targets, checkpointed 99, and yielded 30 eligible plus 70 excluded. Frozen specialist leads were excluded. All 30 exact source receipts were visible through the approved Drive mount; estimated LC inputs were 230.1 MB before pixel/neighbour products.

The 11 incomplete attempts all emitted `event null emitted no measured/covered defining event: not a completed T2 target`. Their extraction/coverage diagnostics were preserved in Drive `ATTEMPTS/`, distinct from completed campaigns. They are neither accepted events nor definitive disproof of objects. Inspect timestamps, masks, coverage and extraction before any retry; do not relax the guard to create checkpoints.

TOI-2191.01 and TOI-4880.01 received automated closed-route decisions for a failed known-variable/ephemeris collision check. Their original measurements remain retained. These gate closures need event-by-event scientific review before a canonical interpretation is reconciled; no candidate records or publication collections were changed. Other completed rows retain Unverified-lead evidence. A checkpoint certifies workflow completion and saved-file integrity, not successful scientific tests.

## Per-target status and follow-up priorities

This table retains the source queue order rather than inventing a new statistical ranking. Priority is diagnostic: inspect closed-route artifact evidence, then defining-event localization/blend/null blockers on completed leads, then incomplete coverage. No candidate merits T3 compute yet. Coordinates, product IDs, epochs and measured statistics reside in the linked native records and full reports; counts here are not independent discoveries or search-wide significance.

| Target | Result | Evidence | Next-tier blockers / concern |
| --- | --- | --- | --- |
| toi-1938-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2'] (T2 vet must pass first); blend census not passed; spec lacks budget and discriminating_question (T3) |
| toi-2191-01 | closed | Unverified lead |  |
| toi-2557-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-2629-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2', 'E3'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-2939-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-2952-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-2956-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-2995-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-3100-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-3431-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-3533-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2', 'E3'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-3576-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2', 'E3'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-4880-01 | closed | Unverified lead |  |
| toi-4945-01 | T2 | Unverified lead | localization failed on defining events ['E1', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E2', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-5263-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-5330-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-5615-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-5699-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); spec lacks budget and discriminating_question (T3) |
| toi-5937-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-6224-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-6370-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-6374-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-6410-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-6480-01 | T2 | Unverified lead | localization failed on defining events ['E1', 'E2', 'E3'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-6521-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-6609-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1', 'E2', 'E3', 'E4'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-6614-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-6769-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-6831-01 | incomplete: no measured/covered defining event | no completed record | no shipped sky record |
| toi-917-01 | T2 | Unverified lead | localization inconclusive on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |

## Tier 3 eligibility

The implemented gate requires passed localization for every nonrejected defining event and no failed other localization, a passed blend census, passed calibrated null, and passed event-epoch null exceedance. A runnable T3 spec also requires both a budget and discriminating question. None of these rows passes all scientific requirements even when the budget/spec check is omitted. Injection recovery, independent-sky support and a Vetted-candidate evidence label additionally gate T4; passing the tier code would still not clear all scientific alternatives or primary-literature/TTV review.

## Reproduction, integrity and limits

Open the shipped [notebook](https://colab.research.google.com/github/mapsugui/ad_astra/blob/0c0a7f3e89351d7e9596f7a46b637377cd6365c7/notebooks/cygnus_higher_tiers_colab.ipynb). Use CPU, source `p02-b02-2026-10-02`, and the saved lineage. The scientific cells were unchanged. Operational additions imported two hash-verified checkpoints, audited T3 eligibility, preserved incomplete attempts and packaged the output. Defaults: n_null=300, n_inject=100, min_n=100; per-target specs, seeds, versions and product hashes are retained in the capsule. Completed checkpoints skip on resume, failures retry.

Drive output: `Cygnus/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/`, [owner folder](https://drive.google.com/drive/folders/1oAzRWrOHtb9GbzQ43UOG4DX51c3RqEUF). `FINAL_EXPORT.zip` is a separate archival copy outside the payload manifest, 17,294,340 bytes, SHA256 `61f91cc4d229bb6edcf48ecbfee61ad43ea6aa6d65750470873a57e11dab4283`; its own contents contain the manifest. Copy and hash readback were verified in the Colab UI. All 515 manifest-listed payload files verified after local archive download and extraction; companion ledger remains scratch-only.

The original local capsule and its environment remain preserved separately. Cloud copy: `docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/cloud/`; [tier marks](../../docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/TIER_MARKS.md) list verified record blockers. Full native measurements must be read with failed/inconclusive checks, selection effects and finite null resolution intact. No zero-exceedance count is promoted to zero probability or Gaussian significance; artifact-rejected events supply no period preference.

The pinned Colab setup completed its checked software gate; its exact pytest count was not captured. No T3/T4 scientific adapter ran, independent confirmation was not established, no evidence was promoted, and the companion ledger was not merged. The batch has finished; the retained Colab runtime is idle. Browser screenshot capture was unavailable, so the visible text output and downloaded metadata are the retained execution evidence.

Repository validation after retaining the cloud artifacts: `python -m pytest -q` completed with **735 passed, 37 deselected, two warnings in 152.59 seconds**. The warnings concern an empty plot legend and an all-NaN centroid diagnostic; neither is scientific confirmation. The operational retention helper passed Ruff fatal-error checks, the retained repository manifest was independently rechecked (516 files; no FITS or SQLite), and `git diff --check` passed. These checks validate software/artifact consistency, not the astronomical interpretation.
