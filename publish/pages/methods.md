# How Cygnus investigates a signal

Cygnus looks for things standard survey pipelines may have set aside: isolated transits, faint moving sources, unseen companions, low-surface-brightness structure and short-lived events. The aim is **credible, independently testable leads**, not a target number of discoveries. A surprising residual is treated as a lead, never as proof of a new object.

The full rules are in the [worktree specification](/documents/agents-spec/). This page summarises them for readers.

## Operating principles

- **The pipeline is not the sky.** Automated cuts trade completeness for convenience, so discarded data and residuals are worth a second look — but rejected data are not presumed astrophysical.
- **Model, subtract, inspect, challenge.** Every signal is compared against explicit models of the source, background, variability and instrument, and the result is re-tested under alternative reasonable choices.
- **Artifacts are the first hypothesis.** Detector effects, cosmic rays, scattered light, pointing jitter, blending, calibration jumps and time-system mistakes are examined before any astrophysical explanation.
- **Account for the search itself.** Red noise, multiple testing and incomplete coverage are handled explicitly. A nominal sigma value alone is not confirmation.
- **Attempt falsification.** Each interpretation is recorded with the observation that would refute it.

## The investigation protocol

Every dataset, target or candidate goes through the same eight steps:

1. **Provenance and access** — archive, release, product ID, instrument, timestamps and their time scale, coordinate frame and epoch.
2. **Data health** — gaps, saturation, backgrounds, noise, nearby sources; exclusions are recorded and inputs kept unaltered.
3. **Baseline** — a physically and instrumentally reasonable model, compared with alternatives.
4. **Extraction** — morphology, amplitude, position, duration, uncertainty, and a detection statistic suited to the noise.
5. **Artifact audit** — each relevant test recorded as passed, failed, inconclusive or not tested.
6. **Catalog and literature audit** — known-object services and publications searched, with dates, radii and epoch propagation recorded.
7. **Competing models** — astrophysical and non-astrophysical explanations compared, with degeneracies stated.
8. **Independent check and next test** — another epoch, instrument or reduction, and the observation that best separates the hypotheses.

A negative result is reported, not dropped.

## Evidence levels

| Level | Meaning |
| --- | --- |
| Unverified lead | A feature was observed; the artifact audit is incomplete. |
| Vetted candidate | Reproducible, and survives every available artifact test; alternatives remain. |
| Independently supported candidate | Independent data, epochs, instruments or reductions corroborate it. |
| Established object / phenomenon | Sufficiently supported identification, including community confirmation where relevant. |

These levels describe **evidence, not importance**. The toolkit enforces two rules mechanically: any audit test that is not `passed` holds a record at *unverified lead*, and *established* cannot be reached from the toolkit alone.

## Audit states

- `passed` — the test ran and the signal survived it.
- `failed` — the test ran and the signal did not survive it.
- `inconclusive` — the test ran but could not decide.
- `not_tested` — the test was unavailable or not run. It never counts as passed.

## Identifiers

Candidate identifiers beginning `CYG-` are **local working identifiers**. They are not official designations and do not imply that an object is new. A missing catalog match is reported as "not found in the services searched as of a date", never as "uncatalogued".

## Provenance

Every archive product is registered in a provenance ledger with its archive, product ID, retrieval time and checksum. Every measurement cites the run that produced it (script, code version, configuration hash, seed) and the products it used. Dossiers are generated from the ledger and candidate records only; a field with no evidence renders as "none recorded" rather than a plausible-looking value.

Original archive data and derived products are kept apart: bulky downloads live in disposable staging storage, curated outputs in persistent project storage, and neither is served directly by this site.

## Publication boundary

This site is a curated export, not a window onto the project's storage.

- **Nothing is public by default.** Material appears only when an operator lists it in a published collection manifest. The ledger, staging storage, the project's cloud store and credentials are never exposed.
- **Documents** are published as maintained, with private storage locations replaced by placeholders.
- **Third-party archive products** are described and linked to their source archive. They are not re-hosted unless their redistribution terms have been checked and recorded.
- **Ledger material** appears only as specific runs or run logs chosen for publication, with allowlisted fields. The site reports ledger totals but never exports the ledger wholesale.
- **Withdrawn collections** keep their address with a dated notice and no files, so citations resolve to an explanation.
- **Every build is scanned** for private paths, storage remote names, credential-shaped strings and e-mail addresses; any hit aborts the build.

The machine-readable [publication catalog](/data/catalog.json) lists every published collection, item and file with its checksum.

## What this site does not do

It does not submit anything to external catalogs, alert streams, journals or observers, and it does not accept uploads. Publishing is a reviewed change to the collection manifests followed by a rebuild.
