# Cloud Tier 2 batch execution — 2026-10-10

All 30 eligible targets from first-stage source `p02-b02-2026-10-02` were handled in one automatic batch. Two verified local checkpoints were imported and skipped; the remaining 28 were attempted on a CPU Colab runtime through the Codex in-app browser. The target-loop UI duration was 54 minutes. Final result: **19/30 checkpoints, 17 at T2, two closed, 11 incomplete**. No target currently passes the implemented T3 science gate or complete saved-spec eligibility.

Run `t2-p02-b02-2026-10-02-10deebcecc06` uses notebook commit `0c0a7f3e89351d7e9596f7a46b637377cd6365c7`, revision `t2-v1-c3f37cbbb62b`, science pin `05ba4f4ee6e2053c256240ab04f7fbb527e32afe`. Source manifest SHA256: `440b3780231eb6e05c69845fbfca201243889239d79d09cf891c34249c921f51`. Source commit: `9250aee3b91d7da7d664681195a250ec85d8c43d`. The source requested 100 targets, checkpointed 99, and yielded 30 eligible plus 70 excluded. Frozen specialist leads were excluded. All 30 exact source receipts were visible through the approved Drive mount; estimated LC inputs were 230.1 MB before pixel/neighbour products.

The 11 incomplete attempts all emitted `event null emitted no measured/covered defining event: not a completed T2 target`. Their extraction/coverage diagnostics were preserved in Drive `ATTEMPTS/`, distinct from completed campaigns. They are neither accepted events nor definitive disproof of objects. Inspect timestamps, masks, coverage and extraction before any retry; do not relax the guard to create checkpoints.

TOI-2191.01 and TOI-4880.01 received automated closed-route decisions for a failed known-variable/ephemeris collision check. Their original measurements remain retained. These gate closures need event-by-event scientific review before a canonical interpretation is reconciled; no candidate records or publication collections were changed. Other completed rows retain Unverified-lead evidence. A checkpoint certifies workflow completion and saved-file integrity, not successful scientific tests.


All 515 manifest-listed payload files verified after local archive download and extraction; companion ledger remains scratch-only.

Final archive hash and T3 eligibility outputs were visible in Colab. Screenshot unavailable. Original local execution provenance remains separate.
