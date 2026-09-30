# Native-support gaps from the 2026-09-30 lead-resolution campaign

Source: `reports/lead-resolution-2026-09-30/` (REPORT, SEARCH_LOG, VALIDATION, PRIOR_ART_AUDIT, CHIRON_ACCESS_AUDIT, PAUSE_CHECKPOINT, RESUME_PROGRESS), `resolve_leads.py` (about 2,650 lines, 40+ functions), `reconcile.py`, `tests/test_lead_resolution.py`, and the diffs to `DATA_SOURCES.md` and `docs/STATUS.md`.

**Attribution caveat.** The repo does not label work by model. STATUS.md records only that GPT-6 Luna High executed the resumed phase (persistence repair, the cached spectrum rerun, the Keck screen) under primary-agent review. Nothing in the repo names a "6.1 Sol" or "5.6 Luna" run. This inventory therefore covers the packet as a whole, not per-model work.

**Why this exists.** All of the packet's analysis lives in one hard-coded script: `resolve_leads.py` reads `config.json` and the three lead slugs. AGENTS.md says known-object work should need "no new analysis code". This campaign broke that rule because the runner had nothing for the steps below. Each item is a candidate for a `cygnus.campaign` / `cygnus.multi` step, an `analysis/` primitive, or an `archives/` adapter.

## A. Analysis primitives (move into `src/cygnus/analysis/`)

| # | What the packet hand-rolled (`resolve_leads.py`) | Native form | Existing overlap |
|---|---|---|---|
| A1 | `box_measure`: joint baseline + box fit, exposure-integrated box for coarse cadence, missing event window reported as *not tested* rather than a null, positive flares cannot become dips. Tests: `test_joint_baseline_*`, `test_missing_event_window_*`, `test_box_does_not_turn_positive_flare_into_dip`, `test_exposure_integrated_box_*` | `analysis.events.measure_event(time, flux, t0, dur, baseline_variants, exposure)`, returning depth in ppm plus a coverage flag | The `residual_screen` finds events but does not re-measure a predicted epoch |
| A2 | `photometry`: a null-window and fixed-epoch injection harness over 4 variants per product. It ran 19,200 null windows and 4,800 injections and kept covered-null counts. | An `event_null_and_injection` step that reports exceedances as counts/N with finite resolution, as AGENTS.md requires | `calibrate_screen` does a sign-flip null and box injection, but not at a fixed predicted epoch with a coverage gate |
| A3 | `coarse_alias_test`: for each period alias, predict the event window, check coverage on a new sector, and flag as excluded only when the window is covered. Result: 0 of 52 excluded on S8, because coverage was poor. | Extend `period_aliases` to accept later sectors and FFI cutouts, and to output "predicted but uncovered" separately from "absent" | `period_aliases` handles only SPOC light curves |
| A4 | `cutouts` + `ffi_photometry`: TESScut 7x7 pixel cubes, apertures, outer-pixel background, and 300 residual-block centroid bootstrap. Shifts of 0.618 arcsec / 4.71 block-bootstrap were still called *inconclusive*. | A pixel-level localization step wired to `analysis/pixels.py` (`aperture_counterfactuals`, `event_control_centroid`). Add the block bootstrap, and a rule that centroid excursion at a given sigma means localization failed. | `analysis/pixels.py` exists, but no campaign step calls it, and it has no TESScut fetch |
| A5 | `fetch_prfs` + `sample_prf` + `calibrated_prf`: official TESS UPDATED_2.0 PRF bracketing, position-propagated fits with registration profiling and 1/3/5% model floors (2,646 trials). Test: `test_prf_sampling_recovers_known_subpixel_shift`. | `analysis/prf.py`: fetch the PRF for the camera/CCD, sample it, and fit a two-source model with a registration grid and model floors. Output: source preference vs. floor, and whether preference flips. | None. This is the main gap for blended pairs such as TOI-3500 A/B (0.18 pixel). |
| A6 | `rv_template` + `rv_linear_fit` + `harps_profiles`: transit-tied circular RV model (zero velocity at transit), weighted fit in km/s, nuisance and jitter variants, RV vs. FWHM correlation. 136 fits. Tests: `test_weighted_rv_orbit_*`, `test_circular_transit_tied_rv_*` | `analysis/rv.py`: `fit_transit_tied_orbit(rv, sigma, alias_periods, nuisance, jitter)`, with unit checks and the FWHM-correlation flag. Uses the mass function already in `analysis/nss.py`. | `analysis/nss.py` covers Gaia NSS only, not epoch RVs |
| A7 | `spectral_shift` / `relative_spectra` / `validate_relative_spectra`: relative shifts between spectra, with a mandatory precision gate against HARPS pipeline RVs. It **failed** (167.9 m/s RMS vs. a 10 m/s gate). | `analysis/spectra.py`, with the gate built in. A derived shift may not be labelled an RV until the gate passes, and a failed gate is stored as a negative result. | None |
| A8 | `integrated_mask_ccf`, `fit_mask_ccf`, `relative_ccf_shift`, `covered_mask_lines`, `ccf_alignment`: gap-aware line-mask CCF. Detector gaps are excluded, not filled. Tests: `test_integrated_line_mask_*`, `test_line_mask_excludes_detector_gap_*`, `test_relative_ccf_alignment_preserves_static_asymmetry`. Still failed 10 m/s (10.85 to 10.95 m/s RMS). | Same module as A7. Mask files come with a pinned-commit manifest and licence. | None |
| A9 | `barycentric_audit`: recompute the barycentric correction from exact Gaia astrometry and UTC start/mid/end. Discrepancies of -103 to +173 m/s versus the pipeline's applied value. Nothing applied. | `analysis/timing.py`: `bary_audit(header, gaia_row)`, which returns the delta but never overwrites | None. AGENTS.md already warns against assuming BJD_TDB or J2000. |

## B. Archive adapters and access rules (move into `src/cygnus/multi/archives/` and `DATA_SOURCES.md`)

1. **ESO**: exact-name `ivoa.ObsCore` selection (spatial cone queries timed out at 45 s; exact name answered), DATALINK VOTable `#this` (science) vs. `#auxiliary` (pipeline bundles), a positive-control query, and an HTTP 401 ledger (18 HARPS + 6 FEROS products). New adapter with three rules: metadata visibility is not public eligibility; a timeout is not absence; a 401 is recorded, not bypassed.
2. **HARPS bundles**: G2 target-fibre CCF extraction (corrected RVC, NOISE, BJD, FWHM), from the six public bundles. Some FEROS bundles are gzip inside a TAR, so HTTP Range parsing fails. The reader must sniff the format before ranging.
3. **KOA/HIRES**: anonymous TAP at `koa.ipac.caltech.edu/TAP/sync`, plus the PyKOA raw route (`nph-getKOA`) and calibration-list route (`nph-getCaliblist`). The server ignores Range and returns HTTP 200, so the client must cap and close the stream itself. Do not host-prefix `filehand`. Association lists are not calibration suitability.
4. **TESScut** FFI cutout retrieval with sha256, headers and byte size in a manifest. Headers are TDB but keep the CCD-centre barycentric correction, so they are not target BJD_TDB.
5. **Gaia exact-source refresh**: RUWE, RV quality, `rv_amplitude_robust`, and `nss_two_body_orbit`. Zero NSS rows is a bounded null, not "not binary". `multi.nss` covers the NSS cross-match only. Extend it to the RV-quality columns.
6. **NASA TOI exact-row refresh** by TIC. AGENTS.md now requires this at claim time.
7. **MAST control queries**: strict, loosened and cone selections, with a known-answer control (TIC 261136679 returned 50 rows), and a rule that a local query error must not be read as an outage.
8. **FEROS release-description caveats** attached to the product (already-applied barycentric correction, dummy NaN ERR, no simultaneous-reference drift calibration), so a downstream step cannot treat a public product as precision-RV valid.

## C. Campaign-runner behaviors (fix in `src/cygnus/campaign/` and `multi/`)

1. **Atomic writes with input/output hash linkage.** A direct JSON overwrite failed (Errno 22, cause still unknown) and lost the final weighting rerun. The fix was flushed temp-file plus `os.replace`, and linking each output to its source and input hashes. Make this the default for every step output.
2. **History preservation.** Superseded outputs are renamed `*_history_2026-09-30_<reason>.json` (four such files this run). A runner-level `archive_previous(output, reason)` would replace the by-hand renaming.
3. **Frozen comparison vs. fresh extraction.** The four-lead exception in AGENTS.md needs a spec flag (`frozen: true`, fresh work in a new campaign ID) so a rerun cannot overwrite the frozen numbers.
4. **Per-item access-state table.** Each attempted product gets one of `ok / http_401 / timeout / format_error / not_tried`, with error text. The manifest must never drop failures (`spectra_manifest.json` does this by hand).
5. **Resumability keyed to actual inputs** (as `campaign` already does), extended to the bulky scratch cache. The 31 unique spectra (108.6 MB) and 8 PRFs were re-verified by hand.
6. **Budget and resource log**: bytes transferred, per-archive query counts and timeouts, scratch path and cleanup policy. This was written into the search log by hand.

## D. Reporting, reconciliation and gates (`src/cygnus/reporting/`, `skyrecord`, `candidate_record`, `publish`)

1. **`reconcile.py` to `cygnus.campaign reconcile`.** It updates the canonical campaign result, sky record, report, search log, dossier, candidate JSON, ledger and publication collection together (ledger run 4019). AGENTS.md already demands this whole set, but only a script supplied it.
2. **Dossier generation from the sky record** so `toi-*-DOSSIER.md` and `campaigns/*/DOSSIER.md` stop being hand-copied. `reporting/dossier.py` exists at 99 lines and needs the artifact-audit and untested-check sections.
3. **Historical annotation** of frozen campaign outputs (the three-line additions to REPORT/DOSSIER/SEARCH_LOG in the diff): a standard "superseded by" footer.
4. **A prior-art step that stores per-paper event-time match results** (yes/no/none published) and separates *companion exists* from *event source identified*. This was the central distinction in `PRIOR_ART_AUDIT.md`, and today it is prose only. `priorart.py` does cone matches only.
5. **A checklist-as-data for the lead-promotion gate**: units (ppm), `sqrt(depth) x R*`, null counts as k/N, and the centroid-failure rule. `test_lead_resolution.py` tests the science primitives, but the gate has no automated check.
6. **A publish check for stale claims.** Three dossiers changed today, so `publish check` should fail if a candidate record's evidence text contradicts its sky record.

## E. Findings the pipeline should encode as defaults (recurring failure modes)

- A public archive product is not automatically precision-grade: FEROS has no drift calibration, and an independent HARPS comparison failed every gate today.
- **A failed precision gate blocks promotion.** It should be enforced in code, not left to a caveat in prose.
- A binary detection does not identify the eclipsing component. Store `companion_exists` and `event_source_identified` as separate fields.
- Coarse alias exclusion needs a coverage test. 0 of 52 excluded on S8 came from unstable baselines, not from clean nulls.
- A source-preference flip under allowed PRF floors is *inconclusive*. Store the flip itself as the result.
- Query timeouts, HTTP 401s and cache misses are logged access limits, never absence.

## Suggested order (highest reuse first)

1. C1 + C2 (atomic writes, history), since they prevent data loss.
2. D1 (`reconcile` as a CLI step), since every future falsified lead needs it.
3. A5 (`prf.py`) and A4 (FFI localization step), the largest missing science capability.
4. B1 + B2 (ESO/HARPS adapter), then A6 (`rv.py`).
5. A7 + A8 + A9 (spectra, CCF and barycentric tools), with the precision gate built in.
6. B3 (KOA) and the remaining adapters.

Every item above should ship with its synthetic-injection test, following the pattern already in `tests/test_lead_resolution.py`. That file's 11 tests would move into the native test modules unchanged.
