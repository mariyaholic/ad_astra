# Batch colab-p01

Updated 2026-09-26T11:40:03Z. Specs: 100; finished: 100; failed: 0; not yet run: 0; to review first: 64.

Nothing here is reviewed. Every finished campaign still needs the review in `docs/AGENT_RUNBOOK.md` before its draft marker is removed; start with the escalations.

## Escalations (review these first)

| Campaign | Why |
|---|---|
| `campaigns/toi-224-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-588-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1986-01.yaml` | positive control failed on data covering the epoch |
| `campaigns/toi-573-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1356-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6806-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log; Variable-catalogue collision (VSX) failed: TOI-6806.01: KELT KS29C20599                EA                             P=23.24895 at 2.3" (collides with alias 46.4967 d) |
| `campaigns/toi-890-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-447-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1433-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4543-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1059-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-585-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-340-01.yaml` | positive control failed on data covering the epoch |
| `campaigns/toi-1976-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-668-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-3501-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1124-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-173-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1019-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4597-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-2137-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-630-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log; Object-class guard (SIMBAD) failed: TOI-630.01: BD-19  1337 otype EB* (eclipsing_or_ellipsoidal) at 0.1" |
| `campaigns/toi-5149-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1229-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-450-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6650-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1455-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-7714-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-2108-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-760-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-5379-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4494-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-3157-01.yaml` | positive control failed on data covering the epoch; Variable-catalogue collision (VSX) failed: TOI-3157.01: Gaia DR3 5869860717491400320   E                              P=2.08874 at 4.3" |
| `campaigns/toi-706-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-2613-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-3241-01.yaml` | Variable-catalogue collision (VSX) failed: TOI-3241.01: Gaia DR3 6070306978593207424   E                              P=0.87645 at 3.1" |
| `campaigns/toi-6022-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-5394-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1192-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6564-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-621-01.yaml` | Variable-catalogue collision (VSX) failed: TOI-621.01: KELT KS34C003047               EA                             P=3.112338 at 1.0" |
| `campaigns/toi-3460-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-7464-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1351-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-764-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1149-01.yaml` | positive control failed on data covering the epoch |
| `campaigns/toi-4381-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-2349-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-3972-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-527-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-768-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6036-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6568-01.yaml` | positive control failed on data covering the epoch |
| `campaigns/toi-7610-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4422-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1114-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1528-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-6106-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4427-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1709-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-4398-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-2031-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1461-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |
| `campaigns/toi-1457-01.yaml` | repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log |

## Finished

| Campaign | Status | Outcome | Positive control | Cross-match |
|---|---|---|---|---|
| `campaigns/toi-224-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-588-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1986-01.yaml` | completed | pipeline_check | failed | passed |
| `campaigns/toi-573-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1356-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-850-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-6806-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-671-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-890-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-447-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-352-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-1433-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-4543-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1059-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-585-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1656-01.yaml` | completed | pipeline_check | passed | passed |
| `campaigns/toi-340-01.yaml` | completed | pipeline_check | failed | passed |
| `campaigns/toi-1976-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-316-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-121-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-5575-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-911-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-668-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3501-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1124-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1379-01.yaml` | completed | pipeline_check | passed | passed |
| `campaigns/toi-173-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1949-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-1019-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-4597-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2137-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-630-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3487-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-5149-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1229-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-450-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6650-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3223-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3716-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3491-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-1455-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-7714-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2108-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-760-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2183-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-7780-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-5379-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-4494-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3157-01.yaml` | completed | pipeline_check | failed | passed |
| `campaigns/toi-706-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2613-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-7018-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3241-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-1861-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-6022-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-5670-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-5394-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1192-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6564-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3012-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-621-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-7814-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-6815-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3460-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-7464-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1351-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2645-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-764-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6798-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-1149-01.yaml` | completed | pipeline_check | failed | passed |
| `campaigns/toi-4381-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3048-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-2349-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-162-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3972-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-527-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-768-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-7420-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3531-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-6036-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6568-01.yaml` | completed | pipeline_check | failed | passed |
| `campaigns/toi-7388-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-7610-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-4422-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1114-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3586-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-1528-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6106-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2782-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-4427-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1709-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-6137-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-830-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-5861-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-3312-01.yaml` | completed | pipeline_check | not_tested | passed |
| `campaigns/toi-4398-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-2031-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-1461-01.yaml` | completed | lead | passed | passed |
| `campaigns/toi-3098-01.yaml` | completed | pipeline_check | inconclusive | passed |
| `campaigns/toi-1457-01.yaml` | completed | lead | passed | passed |
