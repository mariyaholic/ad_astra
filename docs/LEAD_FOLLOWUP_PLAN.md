# Follow-up plan: the five vetted candidate dossiers (2026-09-26)

Working handoff for the pursuit phase after the 2026-09-26 lead vetting and dossier
creation. **Read `docs/STATUS.md` first**, then the five dossiers themselves — the
dossiers, not this file, are the evidence of record; this file only *sequences the
next work*. Maintain by hand; it is a private worktree document, not published to
the site.

## 0. Orientation for the picking-up agent

Read, in order:

1. `docs/STATUS.md` — "Current focus", open decisions 3/8 (resolved), known problems.
   Note two open maintainer items that affect tooling: the `colab-p01` queue's missing
   period column (self-match root cause) and the GitHub `ci` lane failing on
   Linux-only test bugs while the local gate is green.
2. The five dossiers and their backing artifacts (the per-campaign dossier carries
   every number cited below):
   - `campaigns/toi-224-01/DOSSIER.md`
   - `campaigns/toi-2666-01/DOSSIER.md`
   - `campaigns/toi-3500-02/DOSSIER.md`
   - `campaigns/toi-6695-01/DOSSIER.md`
   - `campaigns/toi-7610-01/DOSSIER.md`
3. `campaigns/tess-mono-01/LEAD_VETTING_LOG.md` and
   `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md` — the vetting narratives behind
   the audit tables, including why specific events and aliases were rejected.

Current evidence state: all five are **Unverified lead**. Photometric evidence and
catalog/blend forensics are exhausted; no independent epoch exists yet. Nothing has
been, or should be, submitted to any external catalogue or journal without explicit
user authorisation.

## 1. Standing operating rules

- Verifiable telemetry only (AGENTS.md §4): every consequential claim cites exact
  product IDs, query dates and versions; "(no match in services searched)" is the
  correct phrasing, never "uncatalogued".
- A run that silently did nothing is not a test. A service outage is `not_tested`,
  re-run it, then treat it as complete (the SIMBAD proxy precedent — see STATUS).
- Analyses run as campaigns: `python -m cygnus.multi run campaigns/<id>.yaml`,
  `python -m cygnus.campaign vet campaigns/<id>.yaml`. Keep every step ledgered.
- Scratch (bulky downloads, seams of throwaway scripts): `D:\AO_Artifacts\cygnus_scratch\`.
  Do not commit scratch; no `*.fits`, no `state/` into git; no credentials anywhere.
- Google Drive remote (`cygnus:` where this harness has it, `gdrive:` elsewhere) sees
  `Cygnus/`; anything outside `Cygnus/` on Drive is off-limits. Resolve with
  `python -m cygnus.storage where`.
- Before committing: `python -m pytest -q` (last full gate at commit 3333372 read
  639 passed, 37 deselected; local CI on Windows is green, GitHub's `ci` lane is
  known red for a Linux-only test bug — not inherited from ledger work).
- Publishing uses `python -m cygnus.publish check` before `build`. Candidate
  evidence-level rules apply; no audit item may quietly upgrade.

## 2. Standing server / archive state as of the vetting day (2026-09-26)

- **ESO TAP** was down all day (every live probe timed out); the RV-bound step
  (`rv_bounds`, active in generated specs when ESO is declared) is `not_tested` for
  every survivor. Re-probe first thing: `python -m cygnus.multi archives --check all`
  (the L3 network lane). When ESO answers, run `rv_bounds` for all five in one pass;
  recorded archival RV points, even sparse, set a lower bound on K.
- Earthdata (`mast`/Kepler-10 style probes) gave a 403 from Google egress IPs at the
  last Colab archive health strip — likely to still fail from Colab; use the workstation.
- The workspace's Gaia cone sweep is complete; the vetting used those field files
  (`design-system/mockups/data/field_<cid>.csv`); DO NOT re-download neighbours.

## 3. Pursuit plan, ranked

### P1 — TOI-2666.01 (dossier `CYG-2026-09-TOI2666.01`) — RV is decisive and the host is the easiest target

Host HD 80133, V ≈ 7.0 (Tmag 6.99); too bright for Gaia RVS (absent), saturated in ZTF.
Two measured deep events: S35 BJD 2459259.1579 (15,215 ± 176 ppm, 1.16 h), S99
BJD 2461049.1644 (15,464 ± 181 ppm, 1.16 h), ΔT = 1790.006 d. 52 data-allowed aliases
(P ≥ 12.79 d) remain; every shorter claim SPOC made is refuted by its own predicted-
and-absent transit; P 36.53 d alias is parity-inconsistent.

- Next tests, in order of leverage:
  1. **Any archival RV scan** (ESO TAP is the registered free service): a stellar
     companion at any surviving alias gives K ~ km/s; a planet gives ≲ 100 m/s; a
     single visit already bounds a stellar companion. Record per-service query dates
     even for no-result.
  2. **Spot-variability guard** — the host varies 1–3.4 ppt at 2–61 h; subtract a
     spot model from the S99 residuals before any 0.5 ppt-scale secondary claim.
     The 316 ± 62 ppm phase-0.5 rows are the spot explanation, not a detection.
- Where the grazing EB reading would surface first: secondary-eclipse windows of
  the *long* aliases (P > 40 d) landing inside the TESS seasonal gaps at phase 0.5 —
  the alias family keeps these testable against any future sector.
- If RV finds nothing at ≲ 100 m/s resolution or the full K excursion never exceeds
  ~1 km/s: the planetary reading (R_p ≈ 1.1–1.4 R_Jup at b near 1) survives; upgrade
  the dossier only at an independent RV confirm or a second on-target transit at a
  new predicted epoch.

### P2 — TOI-224.01 (`CYG-2026-09-TOI224.01`) — the densest upcoming transit machine

M dwarf (0.49 R☉, 0.52 M☉), Tmag 11.14. Four events, all on-target, all shape-1.0
duration, depth ratios 0.93–0.98 of the reference: S29 BJD 2459092.1803, S69
2460197.4715, S96 2460923.7950, S106 2461239.5866; one harmonic family, P = 31.5798 d,
holds under all four spacings (n = 23/58/81/91). The catalogued TOI-row period
705.5845 d does NOT fit (705.58/31.58 = 22.34). Next ephemeris transit from E4:
**BJD ≈ 2461271.17**, and every +31.58 d after (22 of the next two years land inside
schedulable ground windows; compute exact UTs at claim time).

- RV: an M-dwarf host at Rp/R\* = 0.28 is a large K either way; the planetary reading
  gives K ≈ 8–13 km/s against the M-dwarf mass, high precision even at V = 11–13.
  One epoch inside a transit window is enough to *bound* M.
- Ground photometry at the next windows is the direct confirm: the reference is
  1.25 h; the candidate is deep (7.4–8.0 ppt), so a centimetre-class telescope with
  a decent CCD is sufficient in z/g.
- Residual caveats (recorded honestly in the dossier): E4's difference image is
  displaced 9.6″ (7.1σ) inside a heavily manual-exclude-flagged window — treat E4 as
  supporting, not proof; the same-CCD common-mode query at E1 never completed
  (MAST ChunkedEncodingError) — the neighbour-focused re-run is a cheap upgrade.
- The 31.58-d reading is falsifiable both ways: absence of a transit at BJD
  2461271.17 with ~2 mmag photometry would weaken it specifically, while a
  confirmed dip at that epoch excludes every incompatible alias at once.

### P3 — TOI-7610.01 (`CYG-2026-09-TOI7610.01`) — RV or photometry inform the SB\* label

TIC 121341000, Tmag 11.80; 0.74 R☉/0.74 M☉. Two clean events: S88 BJD 2460700.9701
(16,594 ± 529 ppm, 3.76 h), S99 BJD 2461066.3486 (15,757 ± 425 ppm, 3.76 h); ΔT =
365.379 d; 21 data-allowed aliases (P ≥ 10.44 d). The catalogued P 22.1441 d is not
an integer divisor (365.379/22.1441 = 16.5).

- **SIMBAD's SB\* label on UCAC4 433-048726 is the driving unknown**: if it is a
  spectroscopic binary at 0.3″ from the host, a grazing equal-mass EB becomes the
  more natural reading of two equal-depth 3-sigma-recognised events, and an RV scan
  settles it. Prefer the first RV slot here when scheduling: cheapest decisive test
  on the shortest orbit question.
- Diff image is on the flux core (2.9″/5.9σ); the +5.9σ MOM_CENTR2 excursion at
  E1 is the residual caveat — a pointing-slide reading that an independent
  difference-image rerun on new sector data would also disambiguate.
- Ground photometry at the 21 alias phases (shortest 10.44 d) is cheap; pick the
  two phases with the longest n.

### P4 — TOI-6695.01 (`CYG-2026-09-TOI6695.01`) — RV scan on a 1.15-M☉ host

TIC 118339710, Tmag 10.35. Reference S34 BJD 2459249.5428 (3,598 ± 162 ppm, 8.67 h),
E1 S61 BJD 2459973.5382 (3,494 ± 159 ppm, 6.93 h), 26 data-allowed aliases of
ΔT = 723.995 d (shortest compatible 20.69 d); no ≥4σ secondary at any covered
phase-0.5 window. Rejected E2 (S88) sits 12.0″ off-centroid at 14.7σ — an artifact
that defends clean reading of the reference family.

- Predicted ephemeris points depend on which alias is real; at the *shortest*
  density-compatible P = 20.69 d, from E1 the next transit is BJD ≈ 2459994.23
  (already past; compute the current next alias window at pursue time). Do **not**
  quote an uncomputed future UT date in the dossier before computing it.
- RV at v ~ 100 m/s precision separates Saturn-mass from stellar over one
  shortest-alias period, i.e. within ~3 weeks of any programme start.

### P5 — TOI-3500.02 (`CYG-2026-09-TOI3500.02`) — RV over the 2:1 reading

TIC 443666343, Tmag 10.83, host G 11.35 (RV-measurable). Reference S64
BJD 2460056.6957 (7,020 ± 282 ppm, 7.91 h), E1 S90 BJD 2460757.3199 (7,553 ± 277 ppm,
7.91 h), 2:1 spacing (700.6242 d), 16 data-allowed aliases of P = 700.62/n
(n = 2..18 excluding 18.44 d; P ≥ 35.03 d); **P = 350.31 d is the most economical
single reading**; next transit ≈ 2027-08 (compute the exact UT at pursue time).
E2 (S101) is rejected — an aperture-loss/pointing artifact that never content-free
supports a period.

- The 3.71″ co-moving neighbour is excluded *for E1* by the deficit direction and
  TPF-WCS mapping; the 43.2″ neighbour has no capable ZTF depth. Treat the blend
  as **disfavoured, not closed** — an archival high-res image (e.g. from a TPF or
  Local Survey 90-arcsec PSF) is a worthwhile second check when cheap.
- RV at ≲ 150 m/s over a 350-d baseline resolves planet-vs-grazing-EB.
- Ground photometry targeting the short aliases (35.03, 50.04, 58.39, 87.58, 100.09,
  116.77 … d) can disfavour subsets early; build the phase targets from the alias
  family, not the 2:1 reading alone.

## 4. Work sequencing suggestion (for the next session, not a mandate)

1. Re-probe archives (`python -m cygnus.multi archives --check all`). If ESO answers,
   run `rv_bounds` for all five campaigns that declared it; else record `not_tested`
   per campaign and move on without hiding it.
2. Re-run the E1 common-mode query for TOI-224.01 (the one MAST outage in the
   surviving set's audit) and re-run TOI-7610.01's difference-image table on any
   sector-108 product becoming available.
3. Draft ZTF phase-coverage tables per host at the alias phases (no new IRSA
   download is needed for the 3.71″ neighbour — it has zero rows; quoted per OID).
4. Only then consider external submission; **nothing moves without user
   authorisation** — see `docs/STATUS.md` open decisions.

## 5. Ledger and artefact conventions already in place

- Each dossier already has ledger `candidates` + `prior_art` rows (keyed by
  candidate_id `CYG-2026-09-…`) in `state/ledger.sqlite`; the collection
  `publish/collections/cygnus-candidates-2026-09.json` is published and deployed.
- On any evidence change (RV measured, transit detected, artifact identified):
  re-run the dossier builder script
  `D:\AO_Artifacts\cygnus_scratch\lead_vetting_2026-09-26\build_dossiers.py`
  and the standard publication flow (`publish check` → `build` → explorer
  unaffected → bundle → `push_site_branch`). Keep `commit` trailer
  "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".
- The committed sky records (`campaigns/<cid>/sky_record.json`) still carry
  `outcome: lead / evidence: Unverified lead`; they do not change until the
  evidence level does — the evidence rule in `cygnus/candidate_record.py`
  will refuse any upgrade while an audit item stays non-passed.
