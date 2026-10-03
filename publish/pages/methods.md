# How Cygnus investigates a signal

Cygnus searches for credible, independently testable leads in observations that a standard survey pipeline may set aside: isolated transits, faint moving sources, unseen companions, diffuse structure and short-lived events. A surprising residual is a lead for review, never proof of a new object.

The **Compact** view is the operational summary. Use **Full definitions** above it for the complete runner, tier, evidence and publication rules. The two views are generated from separate maintained source files so a short landing page does not replace the detailed contract.

## Current public reading

The current candidate collection contains three **Unverified leads**: [TOI-224.01](/candidates/CYG-2026-09-TOI224.01/), [TOI-2666.01](/candidates/CYG-2026-09-TOI2666.01/) and [TOI-3500.02](/candidates/CYG-2026-09-TOI3500.02/). TOI-6695.01 and TOI-7610.01 are retracted pipeline checks with their rejection records preserved. No planet, component orbit or established discovery is claimed.

The October 2 Colab export is a separate metadata audit: 99 of 100 checkpoints were saved, with 68 earned T0, one T1, 30 T2 and one missing. The marks describe saved sky-record checks, not bulk-product review or scientific confirmation. The [operations collection](/collections/operations-2026-10/) carries the export and scheduler record.

## Analysis suite

The production suite is the ledgered `cygnus.multi` runner. A campaign spec declares its target, archive products, thresholds, vetoes and record checks; the runner discovers or verifies products, executes resumable steps, writes measurements and regenerates a `sky_record.json`. The older single-archive `cygnus.campaign` runner remains valid for its existing specs. The runner name is explicit so the two systems cannot be confused.

The suite starts with a light T0 screen and only spends heavier work on targets that earn it. In compact form the path is **T0 screen → T1 repeat-event triage → T2 pixel/FFI vetting → T3 discriminating follow-up → T4 confirmation**. A tier is an earned gate from recorded checks, not a claim about the object.

## Investigation protocol

Every target follows the same eight checks: provenance and access; data health; baseline; signal extraction; artifact audit; catalogue and literature audit; competing models; and an independent check with the next discriminating test. Missing work is recorded as `not_tested`, and a negative result remains in the search log.

## Evidence states

`passed` means a check ran and the signal survived. `failed` means it did not. `inconclusive` means the check ran but could not decide. `not_tested` means it was unavailable or not run; it never counts as passed. Evidence levels are **Unverified lead**, **Vetted candidate**, **Independently supported candidate** and **Established object / phenomenon**. The toolkit cannot promote a record to established on its own.

## Publication boundary

The site is a curated export. Only items named by a published collection manifest appear here. Private paths, credentials, ledgers and bulky archive products stay out of the build; public documents replace private locations with placeholders. Each build runs a leak scan, and published files carry their recorded checksums and source provenance.

## What this site does not do

Cygnus does not submit candidates to external catalogues, alert streams, journals or observers, and it does not turn a high nominal sigma value or a missing catalogue match into a discovery claim. Read the [full definitions](/documents/analysis-suite/) and the source-linked campaign records for the assumptions, checks and limits behind each result.
