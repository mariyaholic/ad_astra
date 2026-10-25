# Project status and handoff

<!-- cygnus:colab-sync:t2-p02-b02-2026-10-02-10deebcecc06:start -->

**Colab sync t2-p02-b02-2026-10-02-10deebcecc06:** T2: 17, closed: 2, missing: 11; 19/30 checkpointed. Post-run tiers derived from manifest-verified sky records; saved starting board is historical. Bulk products and scientific interpretations remain unreviewed. [Tier marks](colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/TIER_MARKS.md).

<!-- cygnus:colab-sync:t2-p02-b02-2026-10-02-10deebcecc06:end -->


<!-- cygnus:colab-sync:smoke-2026-10-01:start -->

**Colab sync smoke-2026-10-01:** T2: 3; 3/3 checkpointed. Post-run tiers derived from manifest-verified sky records; saved starting board is historical. Bulk products and scientific interpretations remain unreviewed. [Tier marks](colab_runs/smoke-2026-10-01/TIER_MARKS.md).

<!-- cygnus:colab-sync:smoke-2026-10-01:end -->


<!-- cygnus:colab-sync:p02-b02-2026-10-02:start -->

**Colab sync p02-b02-2026-10-02:** T0: 68, T1: 1, T2: 30, missing: 1; 99/100 checkpointed. Post-run tiers derived from manifest-verified sky records; saved starting board is historical. Bulk products and scientific interpretations remain unreviewed. [Tier marks](colab_runs/p02-b02-2026-10-02/TIER_MARKS.md).

<!-- cygnus:colab-sync:p02-b02-2026-10-02:end -->


Last updated: 2026-10-08 (Asia/Manila). Read after `AGENTS.md`.

## Current state

Three event interpretations remain **Unverified leads**: TOI-224.01,
TOI-2666.01 and TOI-3500.02. No established discovery, component orbit or
proved planet is claimed. TOI-6695.01 and TOI-7610.01 remain retracted pipeline
checks; their rejection notes and original measurements are preserved.
Canonical candidate records are `publish/candidates/*.json`. The latest bounded
follow-up and validation of the specialist spectral work are in [the 2026-09-30 packet](../reports/lead-resolution-2026-09-30/VALIDATION.md).
The newer [2026-10-11 advancement packet](../reports/lead-advancement-2026-10-11/REPORT.md)
completes native event-null/injection checks on retained epochs and adds official
S107 SPOC pixels plus a public HIRES red-order/QA pilot. All three remain
conservative T2 and Unverified leads: source/orbit gates are unresolved.
S107 official pixel localization fails the new diagnostic; February2021 HIRES
red orders pass browse QA but May red orders fail; the recovered CHIRON thesis
explicitly has no orbit. Original frozen campaigns remain historical comparisons.

The recovered spectrum rerun accounted for 31 unique cached inputs (29 profiles
and two retained failures). Relative CCF comparisons reached 10.9458 / 10.8503
m/s RMS for the R50 G2 / K0 reductions, both failing the 10 m/s requirement.
FEROS precision remains unvalidated. Three HIRES primary headers support the
intended TOI-2666 target identity; calibration association lists do not establish
applicable calibrations or an extracted component velocity. The older failed
write and pause checkpoint are history, superseded by the recovered outputs.
Scientific proof/disproof remains unfinished; no research process is implied
between chats by these notes.

## Batch state and next work

- Specialist advancement 2026-10-11: exact source rows refreshed; eight retained/reference
  event rows plus S107 conditional epoch pass configured local null/injection tests.
  These are not original-search FAP calibration. Current-check records and bounded
  archival findings are in the new advancement packet. Next: resolve224/3500 source
  assignment and obtain precision-validated2666 component series; do not promote
  a browse spectrum, failed-QA epoch or a periodogram label into an orbit.

- Cloud higher-tier batch on 2026-10-10 finished through the Codex browser:
  two verified local checkpoints reused, all 28 remaining targets attempted.
  Final result: 19/30 checkpoints, 17 T2, two closed routes (TOI-2191.01,
  TOI-4880.01), 11 incomplete event-coverage guard failures. None passes the
  implemented T3 scientific gate or full saved-spec eligibility. No evidence
  promotion or canonical candidate replacement. Review native diagnostics;
  do not bypass the coverage guard. [Cloud report](../reports/cloud-t2-2026-10-10/REPORT.md).
  The local entry below preserves the earlier execution history.

- Local higher-tier execution on 2026-10-10: source `p02-b02-2026-10-02`
  yielded 30 eligible and 70 excluded. Two targets have verified T2 checkpoints
  (TOI-1938.01, TOI-2629.01); TOI-2557.01 failed the event-null coverage guard;
  27 targets could not enter science because exact source receipts were missing.
  The shared rclone client returned HTTP 403 `RATE_LIMIT_EXCEEDED`, including
  a bounded later retry. This was a local CPU run, not Google Colab execution.
  Both checkpointed targets retain Unverified-lead labels and have inconclusive
  localization; other scientific checks include failures. Resume the same lineage
  when source access returns, then review the outputs before any promotion.
  [Execution report and retained diagnostics](../reports/local-t2-2026-10-10/REPORT.md).

- Reusable T2 follow-up notebook built: `notebooks/cygnus_higher_tiers_colab.ipynb`.
  It discovers first-stage exports, derives eligible targets and keeps
  source/revision-bound resume state; no manually copied target list. The
  initial shipped-cell and sync tests passed, but independent review found four
  integrity/completion gaps. Corrections and regression checks now pass, and
  focused independent re-review cleared the four gaps and stale closure receipt.
  Real CPU Colab/live-archive execution is now recorded in the cloud report above.
  [Operation and limits](HIGHER_TIERS_COLAB.md).
- `p02-b02-2026-10-02`: 99/100 saved checkpoints, executed at T0. Derived earned
  tiers are 68 T0, one T1 and 30 T2; one target is missing. These marks audit
  manifest-verified metadata, not the full bulk products or scientific conclusions.
- TOI-3941.01 has no shipped checkpoint or sky record. Inspect the notebook's
  failure evidence before retrying; the NaN serialization repair is committed.
- TOI-4280.01 remains T1 because the moving-object check is `not_tested` for one
  unanswered event epoch. Of the 30 eligible T2 targets, 19 now have follow-up
  checkpoints and 11 remain incomplete. Scientific review is still
  required before any evidence promotion.
- `p02-b01`: 98 completed but unreviewed, with 41 escalations including 35
  outcome-lead repeat candidates. Retain draft markers until runbook review.
- The legacy `tess-periodic-01` queue lacks usable periods for the current suite.
  Use repaired `tess-periodic-02` (300 targets with live periods). Preserve old
  specs as historical comparisons rather than rerunning them on current defaults.

For established leads, next tests remain component-aware localization and
phase-spanning binary RVs for TOI-224, an SB2/eclipse orbit for TOI-2666, and
validated empirical PRF or resolved photometry for TOI-3500. The [pursuit plan](LEAD_PURSUIT_PLAN_2026-09-27.md)
and [runbook](AGENT_RUNBOOK.md) govern fresh campaigns and event-identity checks.
Historical campaign numeric outputs must not be overwritten.

## Automation ownership

Windows `\Cygnus-Colab-Sync` is the **one canonical Colab sync task**, daily
09:00 UTC+08:00. Codex heartbeat `cygnus-colab-tier-sync` is PAUSED. Agents must
inspect/update the existing Windows task; do not create per-batch or redundant
schedules. [COLAB_SYNC.md](COLAB_SYNC.md) records registration, logs and limits.

The task discovers new exports, verifies tier inputs, updates separate marks,
managed blocks above and `storage/locations.jsonl`. It runs with Codex closed
while Windows remains signed in, including a locked session. Physical waking
from sleep is untested. It performs no science, commit, push or publication.
All Python/rclone launches suppress console windows. The corrected scheduled
run completed on 2026-10-03 with result 0 and no export errors.

## Repository and website

The offline gate, curated site build, explorer and whole-bundle leak scan are
the checks required before deployment; fresh outcomes are recorded in
[WORKSTACK.md](../WORKSTACK.md). Website content is selected only through
`publish/collections/*.json`; [PUBLISHING.md](PUBLISHING.md) describes the
existing `site` branch / Cloudflare Pages deployment route.

The 2026-10-03 cleanup separates current instructions from historical status,
corrects the notebook and access descriptions, and keeps local editor/browser
artifacts ignored. It includes the reviewed tier-sync implementation and its
regressions. Scientific records, rejected leads and source products are preserved.
Publishing the exported tier audit does not import the companion ledger or
replace the canonical campaign records with the Colab copy.

## Decisions still requiring the user

- Release of the restricted software source archive remains undecided. A general
  site update does not remove that collection item's restriction.
- Explorer per-target/log design, repository-page restyling and final logo seed
  remain design choices; they do not block rebuilding the current site.
- Separate publication of the two NSS campaigns remains undecided. Their
  inconclusive results may not be promoted into cleared companion checks.
- Observer contact, catalogue submission and journal submission require explicit
  authorization. None is part of a repository or website update.

Fleet recomputation, periodic campaign publication and survivor dossiers were
already authorized and completed in the dated history; do not ask again or
repeat them merely because an older note lists them as open.

## Known limits

- The reviewed T2 notebook is delivered as a local attachment. Its Drive kit
  was listed under `Cygnus/batches/higher-tiers-t2-v1-c3f37cbbb62b/`, but a
  shared rclone-client quota error (HTTP 403 `RATE_LIMIT_EXCEEDED`) blocked
  byte read-back and LOCATION registration. Treat that cloud copy as uncertified
  until verified; the storage index records partial staging. This does not claim
  a Colab mount or live archive failure.
- Evidence promotion requires scientific review; software tests and tier gating
  do not validate astrophysical interpretations.
- Empirical null exceedances retain finite sample resolution and dependence;
  zero exceedances never mean zero probability or Gaussian significance.
- Position-only catalogue matches cannot clear event-time prior art. Depths are
  stored in ppm; `1 ppt = 1,000 ppm = 0.1%`.
- Archive availability and token visibility are dated observations, not permanent
  promises. Resolve Drive through `cygnus.storage`; only `Cygnus/` is authorized.
- Companion Colab ledgers remain separate. Bulk hashes are outside the current
  post-run tier audit scope.

## Historical record

[STATUS_HISTORY_2026-10-02.md](STATUS_HISTORY_2026-10-02.md) preserves the previous
handoff, including its old five-lead claims, errata, resolved decisions and
superseded pause instructions. It is not a current task queue. Dated reports,
search logs, rejections and campaign measurements remain in their original paths.
