# Full methods definitions

This is the complete public definition of the current Cygnus research and publication system. The [worktree specification](/documents/agents-spec/) is the governing operational contract; this page explains how that contract is implemented in the site-facing suite.

## Full analysis suite

Cygnus has two explicit ledgered runners. `cygnus.campaign` handles the original single-archive campaign specifications. `cygnus.multi` handles multi-archive specifications and is the runner used by the 78-record `suite2-2026-09-26` known-object batch. A spec must name its runner; validation rejects a `runner: cygnus.multi` spec anywhere else, so a result cannot silently come from the wrong path.

Both runners use the spec as the only source of campaign parameters. A run is a sequence of resumable ledger steps. Each step records its configuration hash, code version, seed, products and measurements, and ends as `completed`, `failed` or `aborted`. Re-running an unchanged completed step reuses its saved output. Pinned products must match their expected SHA-256; discovered products retain the checksum from retrieval. The sky record is regenerated from the spec's record block and the checks actually set by the steps.

The multi-archive runner accepts light-curve, image, table and text products from the registered archive adapters. Only time-series products enter the time-series screen. Catalogue-only products still contribute provenance and checks. A single-channel light curve is analysed with the declared red-noise systematics model; the suite does not pretend that two reductions are independent when only one channel exists. Reported event statistics include robust and parametric z values, Gaussian-tail and empirical p values, and trial-corrected false-alarm estimates. The red-noise inflation diagnostic is reported separately and is not silently applied.

The principal steps are:

1. `target_queue` records the ranked target pool, query and per-target rationale.
2. `fetch_products` discovers or retrieves products from the declared scratch/search locations and verifies them before analysis.
3. `calibrate_screen` uses sign-flip nulls and injection–recovery to set the screen calibration and completeness limits.
4. `residual_screen` searches declared reductions and baselines for negative excursions outside the known-signal veto.
5. `known_signal_recovery` is the positive control: the known catalogue signal must be recovered where coverage allows.
6. `period_aliases` tests repeat-event timing and raises only an **Unverified lead** when the record supports it.
7. `bls_recovery` supplies a bounded BLS and permutation diagnostic; it is not a calibrated discovery claim.
8. `event_null` is a T2 tool. It re-measures each repeat event, estimates the event-epoch empirical null as k/N, and runs injection–recovery at the measured depth. Uncovered windows are excluded from N rather than counted as misses.
9. `prior_art`, `source_checks`, `context_products` and `astrometric_vetting` audit catalogues, product integrity, archive context and Gaia NSS alternatives.
10. Where a spec declares it, `fetch_independent` obtains a second archive or epoch for the independent-repetition and ZTF checks; old records that predate the step remain historical until explicitly regenerated.

No step may turn an absent product into a failed scientific result: a catalogue-only campaign records a bounded null, while an outage or integrity error remains visible as a failure or inconclusive check according to the run record.

## Full tier definitions

Tiers are gates over named sky-record checks:

| Tier | Definition | Typical work |
| --- | --- | --- |
| T0 | Light screening and provenance baseline | Product integrity, calibrated residual screen, known-signal control, initial catalogue context |
| T1 | Repeat-event triage | Period aliases, event-time prior-art comparison, catalogue cross-match, null and moving-object checks |
| T2 | Pixel or FFI vetting | Per-event localization, blend/dilution census and calibrated event-epoch null; heavy vetting runs only after T2 is earned |
| T3 | Discriminating follow-up | A declared budget and question, independent data or a test that separates the competing explanations |
| T4 | Confirmation | Event-depth injection–recovery, an independent-sky check and evidence at least at the vetted level; spectral extraction stays behind the precision gate |

The transition rules are strict. T1 requires aliases, catalogue cross-match, event-time comparison against published ephemerides, null checks and moving-object checks. T2 requires localization passed for every defining event, no other localization failure, a passed blend census and a passed event-epoch k/N null. T3 requires the spec's budget and discriminating question. T4 requires event-depth injection–recovery and an independent sky check. A target may be **closed** when a known signal, catalogue collision, rejected event set or explicit rejection record resolves it.

The October 2 Colab export uses the same tier language but is a separate post-run audit. Its 68 T0, one T1 and 30 T2 marks were derived from 101 manifest-verified tier inputs across 99 saved checkpoints; the bulk products and companion ledger were not imported. The marks therefore describe earned software gates, not completed pixel science or candidate confirmation.

## Full investigation protocol

For every target, coordinate pair and product, the record must identify the archive, release, product ID, access state, instrument, bandpass, cadence or exposure, timestamp standard, coordinate frame and epoch. Data health covers gaps, saturation, backgrounds, detector position, nearby sources and quality masks. Original inputs remain distinct from derived products.

The baseline is physically and instrumentally reasonable and is compared with alternate detrending, sky, PSF or variability treatments. Extraction reports amplitude, position, duration, uncertainty, units and a statistic matched to the noise. For transit depths, records use ppm and show the conversion when displayed as ppt or percent (`1 ppt = 1,000 ppm = 0.1%`).

The artifact audit tests pointing and centroid correlation, cosmic rays and detector defects, scattered light, blending, calibration discontinuities, time-system mistakes, quality flags, background structure and image-subtraction failures as applicable. An unavailable test is `not_tested` or `inconclusive`, never `passed` by implication. Catalogue and literature checks state the service, release, query date, search radius, epoch propagation and coverage limit. A position-only match does not clear an event: every measured event time is compared against the target and sibling ephemerides, confirmed planets, individual published transit times and plausible timing variations.

Competing models remain explicit. For a dark-companion interpretation, an astrometric or radial-velocity mass function is a conditional constraint, not a measured mass. For a single transit, a period is a family of aliases conditional on coverage and stellar properties. For a diffuse or fast transient signal, detector structure, background, PSF, moving-object contamination and independent-epoch persistence are tested before an astrophysical label.

## Full evidence definitions

The record states both the evidence level and its bottom line. **Unverified lead** means a reproducible feature remains after the available first-pass checks but the artifact audit or key alternatives are incomplete. **Vetted candidate** requires the available artifact tests to pass while relevant alternatives remain. **Independently supported candidate** requires corroboration from an independent epoch, instrument, reduction or archive. **Established object / phenomenon** requires sufficient support including published or community confirmation; the toolkit alone cannot create that state.

Every check uses one of four states: `passed`, `failed`, `inconclusive` or `not_tested`. A check that is absent from the runner is not evidence that the signal survived it. Empirical nulls are reported as finite k/N counts; 0/N is not zero probability. Search-wide trial counts, selection effects, correlated pixels, red noise, incomplete coverage and look-elsewhere effects remain part of the interpretation.

## Full provenance and reproducibility

Each campaign report points to its spec, source products, checksums, code version, configuration hash, package versions, random seed and generated sky record. Archive queries and retrieval dates are retained. Large products stay in designated scratch or Drive locations and are never silently copied into the public site. Google Drive routes are resolved through the storage command and recorded under the `Cygnus/` boundary; credentials and tokens never enter records.

The reproducible entry points are `python -m cygnus.campaign check|run|report` for campaign specs and the corresponding `python -m cygnus.multi` commands for multi-archive work. The offline test gate, campaign-record validation, site build and leak scan are separate checks. A green software gate does not certify archive completeness, false-alarm calibration or a physical discovery.

## Full publication boundary

Content becomes public only through `publish/collections/*.json`. The builder resolves sources inside the allowed worktree paths, redacts private locations, refuses restricted downloads, reads the local ledger read-only and scans the finished output for private paths, storage remotes, credentials and email addresses. External archive products are linked to their source archives unless redistribution is explicitly recorded. Withdrawn collections retain a dated tombstone so a citation resolves to an explanation.

The public candidate index currently contains TOI-224.01, TOI-2666.01 and TOI-3500.02 as Unverified leads. TOI-6695.01 and TOI-7610.01 remain preserved retractions. Historical batch pages keep their original run counts and provenance, but their current-status notes point back to the candidate index and operations collection so an old batch snapshot is not mistaken for the present queue.
