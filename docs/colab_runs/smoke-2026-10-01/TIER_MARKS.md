# Colab tier audit: smoke-2026-10-01

Source commit: `0cf74ece66982c00c080c8b66c1973b7353be0dc`; source UTC: 2026-09-30T21:20:15.378387+00:00.

Requested: 3; checkpointed: 3. **T2: 3**.

Tier means tools earned from the saved checks, not scientific confirmation or tools already executed.
This is a gate audit; draft review markers and evidence levels remain unchanged.

Verified 5/79 manifest files (tier inputs only).
Bulk products, light curves and the companion ledger were not verified or imported.

| Target | Tier earned | Starting tier | Run at | Outcome | Next-tier blockers |
| --- | --- | --- | --- | --- | --- |
| toi-224-01 | **T2** | T2 | T0 | lead | localization failed on defining events ['E1', 'E2', 'E3'] (T2 vet must pass first); calibrated null inconclusive: needs a passed result before heavy tools; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-2666-01 | **T2** | T2 | T0 | lead | event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
| toi-3500-02 | **T2** | T2 | T0 | lead | localization failed on defining events ['E1'] (T2 vet must pass first); blend census not passed; event-epoch null exceedance (k/N) not passed: run the event_null step at T2; spec lacks budget and discriminating_question (T3) |
