# Project status and handoff

Last updated: 2026-09-25 (UTC). Read this after `AGENTS.md` when picking the project up. It records the current state, open decisions and known problems that are not obvious from the code. Update it when any of these change.

## Where things are

| Area | State | Docs |
|---|---|---|
| Science | One known-planet recovery test and one residual screen (WASP-12, TESS S20/S43): **bounded null, no candidate**; calibration shows the screen at k = 5 only excludes dips ≳ 1.5 % deep. **`tess-mono-01` queue exhausted 2026-09-25:** all 20 queued targets (of the 73-member pool) have been run and reviewed through the known-object loop (`docs/AGENT_RUNBOOK.md`). Positive control: 12 recovered, 6 `not_tested` (no retrieved sector covers the catalogue epoch), 1 inconclusive, 1 failed. Five records carry a repeat candidate as an **unverified lead** — TOI-2666.01, TOI-3500.02, TOI-5812.02, TOI-2318.01, TOI-6674.01; the reviewer notes judge TOI-5812.02 the most transit-like and TOI-2318.01 / TOI-6674.01 likely systematics. Reviewer flags (not leads) also raised for TOI-790.03, TOI-2534.01 and TOI-3724.01. No candidate dossiers exist. | `campaigns/`, `reports/`, their `sky_record.json` |
| Tier-1 baseline pack | 132 manifest rows from 8 archives, checksummed. Products live in private cloud storage (`cygnus:Cygnus/…`); the repo holds manifests only. Engineering baseline, not a scientific result. | `docs/tier1_pack/` |
| Public site (v1) | Static generator working, leak scan clean. Deployed to Cloudflare Pages (https://cygnus-sky.pages.dev, explorer at `/preview/explorer/`) by hand: `python tools/build_pages_bundle.py` then `npx wrangler pages deploy build/pages --project-name cygnus-sky --branch main`; not connected to git. | `docs/PUBLISHING.md` |
| Site redesign | User found v1 too plain. An interactive **sky explorer prototype** is built and the direction approved; **converting the real site is not yet approved.** | `design-system/mockups/README.md` |
| Sky records | Every analysis must leave `sky_record.json`; tests fail otherwise. | `docs/SKY_RECORDS.md` |
| Design system "Ad Astra" | Source in `design-system/project/`. A browsable copy exists as a private claude.ai artifact (only reachable from Claude). It still describes the **v1** look, not the explorer. | `design-system/project/README.md` |
| Pipeline autonomy | Campaigns run from YAML specs through a ledgered, resumable runner with calibration (sign-flip null, injection–recovery), catalogue cross-match and a ranked target queue; CI and a weekly public-archive queue job exist. Known-object tests are generated and run by any agent with five commands (`docs/AGENT_RUNBOOK.md`), with a positive control, grouped screen events and period aliases. Detrending families, difference-image centroids, pointing audits, stellar-density period posteriors and ADS are still not built. | `docs/CAMPAIGNS.md`, `docs/AUTONOMY_STUDY.md` |
| Repository | GitHub `mariyaholic/ad_astra`, branch `main`. Licence Apache-2.0; third-party data keep their own terms (see README). | `README.md` |

## Open decisions (ask the user; do not assume)

1. **Convert the published site to the explorer design?** The plan: the explorer as the home page, one page per target and an observing log. After that, update `design-system/project/` to match.
2. **Publish the restricted source archive** in `publish/collections/cygnus-software-0-1-0.json`? It was withheld while no licence existed; the licence is now Apache-2.0, but nobody has decided to publish it.
3. **TOI-2666.01 lead.** Pursue the Sector 99 repeat (ExoFOP/SPOC DV check, difference-image centroids, alias follow-up)? Nothing is submitted anywhere without the user's authorisation.
4. **Logo.** Direction chosen and approved (2026-09-24): concept **D**, the Northern Cross badged with a transit chord at a seeded random angle (`design-system/brand/build_brand.py`, `transit_params`). Revised the same day to rigid four-point spike stars and a transit chord drawn as a double-ended blade that breaks through the rim, angle drawn from hard diagonals (25–65° or 115–155°). Still to pick: the seed (alternatives in `design-system/brand/index.html`). Then: final outlined SVGs, favicon set, explorer header, site and design system.
5. **tess-mono-01 queue.** Approved 2026-09-24 to be worked target by target by other agents via the runbook; **exhausted 2026-09-25** (all 20 targets run and reviewed). Next decision: extend it (raise `target_queue.top` in the spec, or take the weekly job's refreshed pool) or pursue the five lead records and the three reviewer flags above.
6. If the explorer's Gaia-derived files are published, Gaia's share-alike terms (CC BY-SA 3.0 IGO) apply to those files.

## Known problems (surface them; do not paper over)

- Ledger run #1 measurements cite product `tesscut-219.7570--80.5310-sec12`, but the ledger's product row is `…-sec12-cam3-ccd1`. The site shows it as unresolved.
- Ten `cygnus.ingest.tier1` runs left `open` by crashed processes were closed as `aborted` on 2026-09-24 with a note; new runs close themselves.
- The ledger (`state/ledger.sqlite`) is not in git and was being written by ingest jobs during the last session; ledger-derived pages are only as fresh as the last build on a machine that has it.
- `docs/TEST_ARCHITECTURE_PLAN_DRAFT.md` lists unaddressed safety gaps: MAST live-test scratch isolation, pack retirement verifying zero rows, ledger referential integrity.
- The residual screen is now calibrated (see its report addendum); pixel-level, centroid, independent-reduction and ADS literature checks remain not tested.
- The SIMBAD prior-art adapter failed with a proxy `Tunnel connection failed` for every target run on 2026-09-25 (NASA Exoplanet Archive, TESS TOI and VSX answered normally). The catalogue cross-match check therefore reports `inconclusive` (3 answered, 1 errored) on all of them; SIMBAD was not actually queried. Re-verify the SIMBAD path before treating a cross-match as complete.
- The `python -m pytest -q` gate in the runbook could not be run in the 2026-09-25 session environment: the sandbox blocked pytest's temporary-directory cleanup as a bulk delete. The per-target test gate is therefore unmet for the eight targets run that day and should be re-run where pytest is allowed.

## Environment notes

- Windows workstation originally; `.gitattributes` forces LF line endings.
- Private storage and scratch paths from `AGENTS.md` exist only on the original workstation. A cloud or other machine has no Drive access and no ledger; the test suite and both site builds still run (`python -m pytest -q`, `python -m cygnus.publish build`, `python design-system/mockups/build_explorer.py`).
- Never commit credentials, `rclone.conf`, FITS products, `state/` or `.env` (`.gitignore` covers them).
