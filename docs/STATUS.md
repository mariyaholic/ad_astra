# Project status and handoff

Last updated: 2026-09-25 (UTC). Read this after `AGENTS.md` when picking the project up. It records the current state, open decisions and known problems that are not obvious from the code. Update it when any of these change.

## Where things are

| Area | State | Docs |
|---|---|---|
| Science | One known-planet recovery and one residual screen (WASP-12, TESS S20/S43): **bounded null, no candidate**; at k = 5 the residual screen excludes only dips ≳ 1.5% deep. **`tess-mono-01` full declared pool completed 2026-09-25:** `target_queue.top` raised 20 → 100 and rebuilt to 76 members; all 76 targets are now run, reviewed and committed through the known-object loop (`docs/AGENT_RUNBOOK.md`), with ranks 37–76 handled in five batches of eight. Positive-control states: 32 passed, 22 failed, 12 inconclusive, 10 `not_tested`; failures are pipeline outcomes, not evidence against catalogued signals when their depths are below the measured completeness floors. Thirteen reports carry runner-flagged repeat events as **unverified leads**: TOI-2666.01, TOI-3500.02, TOI-5812.02, TOI-2318.01, TOI-6674.01, TOI-2065.01, TOI-6666.01, TOI-6695.01, TOI-225.01, TOI-1835.02, TOI-6667.01, TOI-7857.01 and TOI-7399.01. The reviews flag substantial shape/depth and artifact concerns for TOI-7857.01 and TOI-7399.01; neither has an established period. TOI-6650.04 also has an unresolved ~20.33-d, ~1% event train, escalated for multi-TOI / eclipsing-binary / blend checks; the runner did not assign it lead status. Earlier reviewer flags remain for TOI-790.03, TOI-2534.01 and TOI-3724.01. No candidate dossiers exist. **Lead vetting started and paused 2026-09-25** (`campaigns/tess-mono-01/LEAD_VETTING_LOG.md`; ledger runs #537–#545, #546–#547 aborted by the pause):
<br>• **Rejected:** TOI-5812.02 (a transit of the sibling WASP-134 b), TOI-2318.01 and TOI-6674.01 (systematics), TOI-2065.01 (scattered light), TOI-6666.01 (pointing common mode).
<br>• **Survived every test run:** TOI-2666.01; TOI-3500.02 event E1, whose events are spaced 700.62 d and 350.32 d apart.
<br>• **Not yet vetted:** six leads and three reviewer flags. **Resolved:** the ~20.33-d train of TOI-6650.04 is its sibling TOI-6650.01 (all six events within 0.5 h of a predicted transit). | `campaigns/`, `reports/`, their `sky_record.json` |
| Tier-1 baseline pack | 132 manifest rows from 8 archives, checksummed. Products live in private cloud storage (`cygnus:Cygnus/…`); the repo holds manifests only. Engineering baseline, not a scientific result. | `docs/tier1_pack/` |
| Public site | **Converted 2026-09-25 (user decision):** https://cygnus-sky.pages.dev serves the sky explorer at `/` (94 targets, including all 76 tess-mono-01 known-object tests with Gaia fields and survey images). The v1 generator's pages keep their paths, with its home page at `/about/`. `/preview/*` redirects to `/`. Leak scan clean; deployed by hand (steps in `docs/PUBLISHING.md`, deployment `9c27d9f6`), not connected to git. Still v1-styled: the repository pages (`/campaigns/`, `/log/`, …). There are no per-target pages or observing log in the explorer design yet. | `docs/PUBLISHING.md`, `design-system/mockups/README.md` |
| Sky records | Every analysis must leave `sky_record.json`; tests fail otherwise. | `docs/SKY_RECORDS.md` |
| Design system "Ad Astra" | Source in `design-system/project/`. A browsable copy exists as a private claude.ai artifact (only reachable from Claude). It still describes the **v1** look, not the explorer. | `design-system/project/README.md` |
| Pipeline autonomy | Campaigns run from YAML specs through a ledgered, resumable runner with calibration (sign-flip null, injection–recovery), catalogue cross-match and a ranked target queue; CI and a weekly public-archive queue job exist. Known-object tests are generated and run by any agent with five commands (`docs/AGENT_RUNBOOK.md`), with a positive control, grouped screen events and period aliases. **Lead vetting** (`python -m cygnus.campaign vet`, 2026-09-25) adds per event:
<br>• sibling-TOI ephemerides, box-fit shape against the reference transit, detrending alternatives and red-noise significance;
<br>• background, centroid and pointing shifts, quality flags, and a TPF difference-image centroid;
<br>• Gaia neighbours, same-CCD common mode, and stellar-density and secondary-eclipse limits on the aliases.

Not yet built: ADS and a full stellar-density period posterior. | `docs/CAMPAIGNS.md`, `docs/AUTONOMY_STUDY.md` |
| Repository | GitHub `mariyaholic/ad_astra`, branch `main`. Licence Apache-2.0; third-party data keep their own terms (see README). | `README.md` |

## Open decisions (ask the user; do not assume)

1. **Site, next steps** (the conversion itself was approved and done 2026-09-25): per-target pages and an observing log in the explorer design; restyle the repository pages; update `design-system/project/` to match.
2. **Publish the restricted source archive** in `publish/collections/cygnus-software-0-1-0.json`? It was withheld while no licence existed; the licence is now Apache-2.0, but nobody has decided to publish it.
3. **TOI-2666.01 lead.** Pursue the Sector 99 repeat (ExoFOP/SPOC DV check, difference-image centroids, alias follow-up)? Nothing is submitted anywhere without the user's authorisation.
4. **Logo.** Direction chosen and approved (2026-09-24): concept **D**, the Northern Cross badged with a transit chord at a seeded random angle (`design-system/brand/build_brand.py`, `transit_params`). Revised the same day to rigid four-point spike stars and a transit chord drawn as a double-ended blade that breaks through the rim, angle drawn from hard diagonals (25–65° or 115–155°). Still to pick: the seed (alternatives in `design-system/brand/index.html`). Then: final outlined SVGs, favicon set, explorer header, site and design system.
5. If the explorer's Gaia-derived files are published, Gaia's share-alike terms (CC BY-SA 3.0 IGO) apply to those files.

## Known problems (surface them; do not paper over)

- Ledger run #1 measurements cite product `tesscut-219.7570--80.5310-sec12`, but the ledger's product row is `…-sec12-cam3-ccd1`. The site shows it as unresolved.
- Ten `cygnus.ingest.tier1` runs left `open` by crashed processes were closed as `aborted` on 2026-09-24 with a note; new runs close themselves.
- The ledger (`state/ledger.sqlite`) is not in git and was being written by ingest jobs during the last session; ledger-derived pages are only as fresh as the last build on a machine that has it.
- `docs/TEST_ARCHITECTURE_PLAN_DRAFT.md` lists unaddressed safety gaps: MAST live-test scratch isolation, pack retirement verifying zero rows, ledger referential integrity.
- The residual screen is now calibrated (see its report addendum); pixel-level, centroid, independent-reduction and ADS literature checks remain not tested.
- The SIMBAD prior-art adapter failed with a proxy `Tunnel connection failed` for every target in the first (rank 1–20) batch run on 2026-09-25 (NASA Exoplanet Archive, TESS TOI and VSX answered normally). The catalogue cross-match check therefore reports `inconclusive` (3 answered, 1 errored) on those records; SIMBAD was not actually queried. Re-verify the SIMBAD path before treating a cross-match as complete. (The proxy was intermittent — see the later Exoplanet Archive failures below.)
- The full `python -m pytest -q` gate passed after each completed target batch on 2026-09-25; the final run returned **159 passed, 2 deselected**.
- **Colab access is not actually set up on this machine (checked 2026-09-25).** The network reaches Google (`colab.research.google.com` HTTP 200, `drive.google.com` 302, Google APIs responding), and `cygnus.analysis` imports locally, but there is **no Google identity, no mounted Drive and no rclone remote**: `rclone` is installed yet `~/.config/rclone/rclone.conf` is absent and `rclone listremotes` is empty, so the `cygnus:Cygnus/…` remote that hosts the Tier-1 pack does not exist here. No Google Drive for desktop / Drive File Stream is installed, and `docs/tier1_pack/` holds **manifests only** — no `01_mast/`…`08_legacy_survey/` directories and no `.fits` anywhere in the repo (the manifest's 132 rows are 115 `drive_only`, 14 `failed`, 3 `excluded`). `notebooks/cygnus_reanalysis_colab.ipynb` therefore cannot run here: cell 1 (`drive.mount`) needs an interactive Colab runtime with Google sign-in, and cell 2 requires a mounted `PACK_ROOT/'01_mast'` that is not present. The blockers are identity and data, not connectivity.
- The archive proxy is intermittent: on 2026-09-25 the SIMBAD adapter failed with `Tunnel connection failed` for every rank-1–20 target, then later the same day NASA Exoplanet Archive and TESS TOI failed the same way for TOI-6667.01 (SIMBAD and VSX answered). Any cross-match left `inconclusive` by this should be re-run before it is treated as complete.

## Environment notes

- Windows workstation originally; `.gitattributes` forces LF line endings.
- Private storage and scratch paths from `AGENTS.md` exist only on the original workstation. A cloud or other machine has no Drive access and no ledger; the test suite and both site builds still run (`python -m pytest -q`, `python -m cygnus.publish build`, `python design-system/mockups/build_explorer.py`).
- Never commit credentials, `rclone.conf`, FITS products, `state/` or `.env` (`.gitignore` covers them).
