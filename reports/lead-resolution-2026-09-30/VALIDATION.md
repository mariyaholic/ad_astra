# Verification record — 2026-09-30

## Resumed verification

The user resumed research with GPT-6 Luna High execution and primary-agent review. The cached spectrum rerun completed31/31uniqueinputs,29descriptive profiles/2retainedfailures, with exact source/input hashes and CCF input-output linkage. Source snapshot and partial pre-rerun files are retained as history. Original Errno22 cause remains unknown; atomic replacement repairs the partial-write exposure. Both fresh HARPS CCF-alignment precision comparisons still fail10m/s (R50G2 RMS10.9458m/s, K0 RMS10.8503m/s); these scientific failures do not conflict with software checks passing.

- Parent focused test command: `python -m pytest -q tests/test_lead_resolution.py` — **11passed in11.55s**, exit0.
- Ruff reconciliation check — **All checks passed**; canonical reconciliation completed as ledger run**4019**.
- Fresh full offline suite: `python -m pytest -q` — **655passed,37deselected in479.20s**, exit0; output preserved in `resume_pytest.log`. The37excluded tests were not run. This validates offline software/record consistency, not source localization, FEROS precision or orbital identity.
- Fresh local publication check: `python -m cygnus.publish check` — **dry build ok:569pages,577publicfiles**, exit0; output preserved in `resume_publish_check.log`. No deployment occurred.

After Keck-screen code completion, scoped Ruff passed again, offline `--mode koa-products-cached` regenerated all three parsed headers and calibration counts18/59/58 with zero network requests, and the focused suite passed **11tests in54.99s**, exit0. The1998stale parse error was moved to explicit history rather than treated as a current failure. The655-test gate above preceded final Keck-record reconciliation; targeted record/publication checks below verify those later metadata changes. No velocity or orbit extraction test has been performed for the Keck products.

Final canonical reconciliation is ledger run**4020**. `python -m pytest -q tests/test_candidate_record.py tests/test_skyrecord.py` passed **23tests in225.58s**, exit0, after final metadata reconciliation (`resume_record_tests.log`). A separate read-only assertion probe verified31unique spectrum inputs, exact CCF masked-input SHA linkage, all three parsed primary headers with no active parse error, and SHA-256 for each of the six cached prefix/list byte products. `git diff --check` passed (line-ending warnings only). These are provenance/schema checks, not acquired-component identification or calibration applicability tests.

The final publication check after run4020 also completed with exit0: **dry build ok:569pages,577publicfiles** (`resume_publish_check.log`). No deployment, observer contact, external submission or commit occurred. The executor finished both bounded phases; no scientific analysis is running. The app goal entry still reports `paused` despite the user's chat resume instruction; available goal tools have no active/resume status. Automatic goal continuation must be resumed by the user in the app. This tooling state does not imply scientific completion.

The pause validation below is historical. Research resumed at the user's request; full proof/disproof remains outstanding.

## Pause checkpoint validation

The fresh publication-check rerun was also interrupted before its dry-build completion; no fresh publish-pass is claimed. The earlier569-page/577-file successful dry build below remains historical. `git diff --check` returned exit0 (line-ending warnings only). A final filtered process inventory found no running `resolve_leads`, reconciliation, pytest or publication-check Python process. No deployment occurred.

The latest Ruff check passed for the scientific script, reconciliation script and11-test file. The focused synthetic suite passed **11 tests in2.73s** before the final KOA syntax repair; the repaired complete script parses and its five public metadata queries completed. All checkpoint JSON outputs parse. Canonical reconciliation completed as ledger run**4018**. The full-suite rerun was interrupted at approximately54percent to honor the safe-pause request; it did **not** complete and supplies no fresh full-suite pass. The652-pass result below is the earlier completed gate. The current code's final weighting refinement has no successfully saved real-data result; `PAUSE_CHECKPOINT.md` explicitly records that limit.

Scientific evidence and software validation are separate. At the historical pause all three event interpretations remained **Unverified leads**, and the goal was paused at the user's request; see `PAUSE_CHECKPOINT.md`. The resumed results above supersede the interrupted rerun status without promoting evidence.

| Check | Actual result | Scope |
|---|---|---|
| `python -m ruff check reports/lead-resolution-2026-09-30/resolve_leads.py reports/lead-resolution-2026-09-30/reconcile.py tests/test_lead_resolution.py` | All checks passed | New scientific/reconciliation code and controls |
| `python -m pytest -q tests/test_lead_resolution.py` | 8 passed in27.73s | Synthetic baseline/gap/flare/PRF/exposure/RV/spectral-shift controls |
| `python -m pytest -q` | **652 passed,37 deselected in224.03s; exit0** | Full default offline suite including candidate/campaign/sky-record validation;37 excluded tests were not run |
| `python -m cygnus.publish check` | **Dry build ok:569pages,577public files; exit0** | Local collection/build/leak validation; no deployment |
| Independent real-spectrum precision comparison | **Failed:167.945m/s RMS over5non-reference HARPS comparisons** | Exceeds declared10m/s requirement; synthetic passing does not validate real derivedRV |
| TOI2666 component spectral extraction | **Failed/inconclusive** | Two FEROS epochs have53.127km/s wavelength-block scatter; no component orbit |
| TOI3500 calibrated PRF source assignment | **Inconclusive** | Registration/model-floor sensitivity and excess static residuals |
| New TOI224 S107 localization | **Inconclusive** | Significant0.618arcsec/4.71bootstrap-ratio offset and unresolved calibration/component covariance |

Reconciliation: local ledger run4017 registers the updated evidence packet, canonical three candidate records, dated dossiers and sky records. Original campaign YAMLs and numerical runner outputs remain frozen; dated historical notices link to this packet. No evidence level was promoted. The sky-record `status:completed` describes this bounded evidence packet, not completion of the overall research goal.

The first full-suite attempt exposed a pre-existing schema defect in the already-retired TOI7610 sky record: evidence was the empty string rather than JSONnull. It was corrected to null without changing its retired `pipeline_check` outcome, original measurements or rejection interpretation; the fresh full suite then passed.

Owned new files were scanned for API-key/token/secret patterns; no matching credential pattern was found. Archive FITS and ancillary bundles remain in the designated scratch cache; no FITS or state files appear in the Git change inventory. No WORKSTACK.md exists; current open work and the smallest next actions are recorded in `docs/STATUS.md` and the report's execution queue. No memory was written. Changes remain reviewable in the worktree; no commit, observer contact, external submission or deployment occurred.

Unverified research gates: component/eclipse orbit identity for all three; activity and blend discrimination for the six-epoch HARPS hypothesis; valid instrument-specific FEROS extraction; calibrated new-event pointing/same-CCD/moving-object audit; search-wide noise/selection calibration. ProductHTTP401 limitations are retained as access failures, not scientific nondetections.
