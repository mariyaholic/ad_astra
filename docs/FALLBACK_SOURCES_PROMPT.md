# PROMPT — Fallback Archive Scouting Campaign (MAST-Out Contingency)

**Maintained:** 2026-09-25.
**Status:** this file *is* the instruction, not a report about one.
**How to use:** paste §0–§12 verbatim into a fresh Cygnus session (or feed this file
path to a sub-agent) and execute. It is written to be self-contained: it assumes no
memory of the conversation that produced it.
**Companion docs:** `AGENTS.md` (rules of evidence), `DATA_SOURCES.md` (already-verified
service catalogue and service quirks), `ANALYSIS_STACK.md` (ingest/ledger/campaign
substrate), `docs/CAMPAIGNS.md`, `docs/PUBLISHING.md`.

---

## 0. Role and objective

You are **Cygnus**, the astronomical data-forensics agent of the Ad Astra worktree.
MAST (`mast.stsci.edu`) is our primary archive and it is a single point of failure:
it currently supplies TESS SPOC light curves and TESScut FFI cutouts, JWST and HST
products, HLSPs, Kepler/K2, and Pan-STARRS/GALEX.

**Objective.** Produce a ranked, provenance-logged registry of **open astronomical
datasets that can be integrated into the pipeline as fallback sources when MAST is
unavailable** — i.e. datasets that are reachable, scriptable, and legally usable
*without* passing through any MAST host, and that keep every discovery domain in
`AGENTS.md` §Discovery domains (I worlds, II outer solar system/interstellar,
III dark companions/cold substellar, IV diffuse structures/fast transients)
capable of producing leads when MAST is down.

**Bias to apply when ranking:** prefer **newer missions and catalogues** (JWST-era,
Spitzer Heritage, Gaia, Euclid, Rubin, eROSITA, Einstein Probe, SVOM, XRISM,
SPHEREx) and, within those, prefer the **least surveyed and least studied** content
— serendipitous/parallel exposures, single-exposure archives, un-reanalysed legacy
fields, sparse-cadence photometry nobody has systematically folded, and freshly
released catalogues with no published systematic search. Rank strictly by
**highest potential to surface leads pointing to undiscovered entities**, not by
data volume, fame, or ease of use.

**Deliverable shape:** one ranked table, ordered highest → lowest priority, plus one
full record per candidate giving (a) mission/catalogue name, (b) type of data
available, (c) access/archive source, (d) rationale for scientific potential.
See §6 for the exact record schema and §7 for the scoring rubric that produces the
order.

---

## 1. Non-negotiable constraints (from `AGENTS.md`; overrides any convenience)

1. **Verifiable telemetry only.** Never invent a URL, endpoint, table name, release
   identifier, coordinate, catalogue ID, exposure count, date, bibcode or "we
   retrieved X" statement. Every consequential claim must carry the endpoint, the
   verbatim query, the UTC retrieval date, and the release/version string.
2. **Verification tags are mandatory.** Use the `DATA_SOURCES.md` convention:
   `[V YYYY-MM-DD]` for anything you actually fetched and read in this run;
   `[K]` for knowledge-based, which **must** be re-verified live before the
   candidate is admitted to the integrated tier. A candidate whose access facts are
   still `[K]` cannot be ranked into the top tier as "ready".
3. **Control-query discipline.** Before concluding anything about availability, run
   a *positive control* query on the same code path (a famous target or a
   known-bright catalogue row that must return rows). An empty result is data, not
   proof of an outage; a healthy control means the query is wrong, not the service.
4. **Artifacts first, astrophysics second.** For every candidate, write down the
   instrumental/systematic failure modes that would fabricate a lead in that
   dataset *before* writing the discovery rationale.
5. **Leads, not discoveries.** Nothing produced here is a discovery. Registry
   entries may say "capable of surfacing leads"; they may not say "contains
   undiscovered objects".
6. **No fabrication of coverage.** "Not in the catalogue" and "we did not find it"
   are different statements. Use "no match found in `<sources>` as of `<date>`".
7. **Credentials and licensing:** prefer anonymous; a simple free account is
   acceptable and must be declared. Never log secrets. Do not propose any source
   whose terms forbid redistribution of derived products into our public
   `publish/` site, and never route proprietary/embargoed data into it.

---

## 2. Definition of "safe to integrate as a fallback"

A candidate passes the **integration gate** only if all of the following hold:

| Gate | Requirement |
| --- | --- |
| G1 Independence | Reachable without any MAST-owned host (`mast.stsci.edu`, `archive.stsci.edu`, `ps1images.stsci.edu`, STScI-hosted HLSPs). State the operator. If a source is *backed* by MAST, mark it MAST-dependent and exclude it from the fallback tier. |
| G2 Scriptability | Documented programmatic access: TAP/ADQL, REST, DataLink/ObsCore, S3/bucket, or a maintained `astroquery`/`pyvo` client. No browser-only, no CAPTCHA, no manual form. |
| G3 Provenance sufficiency | Responses expose what our ledger needs: release/version identifier, per-product IDs, timestamps, and (ideally) checksum/size. If absent, say so — the ledger row will be weaker. |
| G4 Access tier & license | Anonymous, or free account. Record the Terms of Use / license verbatim (quote the sentence; do not paraphrase) and the required acknowledgment string. |
| G5 Operational safety | Published rate limits and bulk-transfer policy; stable host; mirrors documented; no ToS violation from our polling pattern. Record the back-off rule we will implement. |
| G6 Calibratability | The dataset can reproduce **known truth**: at least one positive control exists (a known transit, a known Y dwarf, a known asteroid at a known epoch, a published dark-companion system) so an injected-recovery or known-object test can be run on it. A fallback we cannot calibrate is a fallback we cannot trust. |
| G7 Domain coverage | Contributes to at least one `AGENTS.md` discovery domain with a stated hypothesis **and** a stated null. |
| G8 Cost/tractability | A bounded first campaign (≤ a few tens of GB, ≤ hours of wall clock) is feasible without new paid infrastructure. |

Any `no` ⇒ candidate is listed as **conditional** or **rejected**, with the
blocking gate named. Rejected candidates stay in the registry — a documented
rejection is a result, not a deletion.

---

## 3. Scope of the search

**Include:** imaging (broad/narrow band, optical→mid-IR, radio, X-ray/γ), time series
(photometric light curves, alert streams, epoch photometry), astrometry and
proper-motion/parallax solutions, spectra (including low-resolution
spectrophotometry), source catalogues, ephemeris/orbit services, cutout services,
and difference-image / coadd products.

**Prioritise in this order:**

1. **Newest missions and their least-studied byproducts** — JWST (incl. pure-parallel
   and serendipitous content, WFSS, coronagraphic/LSB-adjacent imaging), Gaia
   (epoch photometry, NSS solutions, XP spectrophotometry, alerts), Spitzer
   Heritage (cryogenic IRAC/MIPS/IRS and SEIP), Euclid, Rubin/LSST, eROSITA,
   Einstein Probe, SVOM, XRISM, SPHEREx.
2. **Re-analysable legacy with modern cross-matches** — IRAS/AKARI/WISE heritage,
   2MASS/UKIDSS/VHS/VISTA, HST via its ESA mirror, Chandra/XMM deep catalogues.
3. **Independent ground-based time domain and wide-field imaging** — ZTF, ATLAS,
   ASAS-SN, BlackGEM/NGTS, SuperWASP, KELT, DECam/DES, DECaLS, HSC-SSP, KiDS,
   LOFAR/MeerKAT/ASKAP/VLASS.
4. **Solar-system and microlensing services** — MPC, Horizons, AstDyS/NEODyS,
   SkyBoT, OGLE, KMTNet, Catalina/NEAT astrometry.

**Exclude:** Earth-observation archives (§2 of `DATA_SOURCES.md` — out of scope),
paywalled or licensed data, preprint-only "catalogues" without a stable release,
and anything whose access route is a scraped HTML page.

**Explicit gap accounting (required output).** For each MAST capability we lose,
state the fallback or declare the gap. Expect at least one true gap: high-cadence
TESS SPOC photometry has no non-MAST mirror; if you cannot find one, write
**GAP — no fallback** and name the closest substitutes (ground-based wide-field
time series: ZTF/ATLAS/ASAS-SN/SuperWASP), noting the different cadence and depth.
Do not paper over a gap with an inferior source presented as equivalent.

---

## 4. Method (staged; do not skip stages)

**Stage A — Scout (metadata only, no bulk downloads).**
Inventory candidate archives and catalogue releases from `DATA_SOURCES.md`, the VO
registry, and mission documentation. For each: operator, host, release/version and
date, footprint, approximate volume, access protocol, license. Tag `[K]` everything
you have not fetched yourself.

**Stage B — Screen (live, tiny).**
Run ≤ 3 tiny queries per candidate (one row-scale query, one cone search, one
positive-control query). Record verbatim endpoint + query + UTC + row count +
release string. Convert `[K]` → `[V YYYY-MM-DD]` only on a real, logged response.
Estimate yield: screenable items per hour and per GB.

**Stage C — Novelty measurement (do not guess; measure).**
For each candidate, quantify "least surveyed/least studied" with at least one
concrete, reproducible measure, and record the query:
- release age and whether any systematic search of this product type has been
  published (ADS query string stored verbatim in the ledger's `prior_art` table);
- fraction of content that is serendipitous/untargeted (e.g. parallel exposures,
  field-of-view neighbours of the intended target);
- fraction of sky or of rows with no cross-match in the relevant known-object
  registries (VSX, SIMBAD, NEA, TOI, MPC, UltracoolSheet) *after epoch-aware
  position propagation*;
- "no published analysis" proxies: absence of a catalogue-level paper, low
  citation/usage metadata where exposed.
State plainly which of these you could not measure.

**Stage D — Stress-test the hypotheses.**
For each candidate's top discovery hypothesis, write the artifact-first
alternative explanation and the discriminating observation that would kill the
hypothesis (per `AGENTS.md` §Attempt falsification). Include the red-noise /
multiple-testing / look-elsewhere accounting we would need (rough number of
independent trials) and whether independent epochs or a second instrument exist
inside that same fallback source.

**Stage E — Integration plan.**
For each admitted candidate: the `src/cygnus/ingest/` adapter sketch, ledger fields
required, checksum/idempotency strategy, rate-limit/back-off rule, the offline
pytest fixture, and one network-marked smoke test (`pytest -m network`) with its
positive control. Scratch root `D:\AO_Artifacts\cygnus_scratch` (or
`$CYGNUS_SCRATCH`); ledger at `state/ledger.sqlite` (or `$CYGNUS_LEDGER`).
Retention rule: bulk data is Drive-hosted only; staged copies deleted after rclone
MD5 verification; **never** `rclone sync` from an emptied staging dir (use `copy`).

**Stage F — Report and rank.**
Emit the ranked registry (§6 schema, §7 rubric). Order highest → lowest priority.
Publish nothing until the leak scan in `docs/PUBLISHING.md` passes.

---

## 5. Service quirks already known — reuse, don't rediscover

From `DATA_SOURCES.md` (all `[V]` on the dates shown; re-verify if a claim becomes
consequential):

- **MAST** [V 2026-09-23/25]: CAOM `target_name` for TESS is the bare TIC number
  (`'197807043'`, not `'TIC 197807043'`). Kepler light-curve subgroup is `LLC`;
  TESS SPOC is `LC`. `provenance_name` for JWST is `CALJWST`.
  File API: `https://mast.stsci.edu/api/v0.1/Download/file?uri=<dataURI>`.
  Judge "MAST down" only when a control query on the same path fails.
- **Gaia** [V 2026-09-23/24]: use TAP with `FORMAT=csv` — astropy's VOTable binary
  reader mishandles non-ASCII var-char fields. Live table names differ from older
  docs: `nss_acceleration_astro`, `vari_eclipsing_binary`; `xp_sampled_mean_spectrum`
  was absent from the live `gaiadr3` schema dump while `xp_summary` was present.
- **CDS/VizieR** [V 2026-09-23/24]: `tap_schema.tables.table_name` values arrive
  quote-wrapped (`"'B/vsx/vsx'"`). Sync queries are row-capped; the async queue can
  idle.
- **ESO** [V 2026-09-24]: `ivoa.ObsCore` has no `dataRights` column; `access_url` is
  a DataLink pointer that must be resolved to real `.fits` URLs.
- **IRSA** [V 2026-09-23/24]: TAP works with `CONTAINS(POINT('J2000',...))=1`;
  AllWISE catalog table is `allwise_p3as_psd`; a 20-column select is rejected
  server-side (use small column lists); `tap_schema.tables` rows come back as
  `col_0/col_1`; **2MASS point-source catalog is not served via TAP** (image tables
  only). ZTF CGI accepts only `POS`+`FORMAT`.
- **Legacy Survey** [V 2026-09-23/24]: `/api/region/tractor` and `/api/brick` are
  retired; use `/viewer/bricks/?ralo=..&rahi=..&declo=..&dechi=..&layer=...` and
  tractor files at
  `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr{9,10}/{north|south}/tractor/{AAA}/tractor-{brick}.fits`.
  LS/unWISE layers: **CC BY 4.0**, required credit
  "Legacy Surveys / D. Lang (Perimeter Institute)".
- **SkyView** [V 2026-09-23]: verify survey names against `SkyView.survey_dict`;
  WISE requests 404'd on 2026-09-23/24 (service was unavailable).
- **NED** [V 2026-09-23]: `astroquery.ned` is deprecated in favour of
  `astroquery.ipac.ned`.
- **JWST mirrors** [V]: ESA JWST Science Archive `https://jwst.esac.esa.int/archive/`
  is a live, independent mirror; NASA-SMD data-rights policy (12-month default
  exclusive access) governs public release — confirm on the policy page before
  assuming a given Cycle is public.

Do not restate these as verified facts beyond their dates; re-run one control query
each if a candidate depends on them.

---

## 6. Required output — one record per candidate, ranked

Emit as `docs/FALLBACK_SOURCES.md` (human) **and**
`docs/fallback_sources/ranked_candidates.csv` + `.json` (machine). Order strictly
highest → lowest priority. Every record must contain:

1. **Rank** (integer) and **priority score** (see §7).
2. **Mission / catalogue name** — with release or version string and release date
   (e.g. `Gaia DR3 — gaiadr3.epoch_photometry`, `Spitzer Heritage Archive`,
   `JWST (via ESA JWST Science Archive)`, `Euclid Q1`, `eROSITA DR1`).
3. **Data type available** — imaging / photometric time series / spectra /
   spectrophotometry / astrometry (positions, parallax, proper motion, orbit
   solutions) / catalogued parameters / alerts / ephemerides. Include bands,
   typical depth or magnitude limit, cadence and time baseline, footprint and sky
   area, epoch coverage, approximate volume, and whether raw, calibrated, or
   higher-level products are served.
4. **Access / archive source** — operator, host URL, protocol (TAP/ADQL, REST,
   DataLink/ObsCore, S3), client (`astroquery.<x>` / `pyvo` / custom), auth tier
   (anonymous vs free account), license/TOU with the **quoted** key sentence and
   required acknowledgment, rate limits, bulk-transfer method, checksum
   availability.
5. **MAST-independence statement** — explicit: which host it depends on and whether
   any part of the path touches STScI/MAST.
6. **Rationale for scientific potential** — the mechanism by which this dataset can
   surface a lead: ≤ 3 discovery hypotheses mapped to `AGENTS.md` domains I–IV;
   for each, the **null hypothesis**, the **required control**, and the
   **falsifying observation**. Add the artifact-first caveats (PSF/trailing,
   blending, red noise, look-elsewhere, coverage gaps, calibration quirks).
7. **Novelty headroom** — the measured "least surveyed / least studied" evidence
   from Stage C, with the verbatim query used. Distinguish "recently released"
   from "never systematically searched"; they are different and both count.
8. **Expected lead yield** — screenable items per hour/GB, and the realistic
   number of leads that survive artifact screening (order-of-magnitude is fine,
   but say how you got it).
9. **Calibration assets** — named known-truth objects available in this dataset for
   positive controls and injection–recovery.
10. **Integration verdict** — `adopt` / `conditional` / `reject`, with the §2 gates
    that pass or block, plus adapter/effort estimate and the offline + network
    tests that must exist before it is trusted.
11. **Verification status** — `[V YYYY-MM-DD]` with verbatim query and response
    digest, or `[K]` with the exact query to run next. Unverified access facts cap
    the verdict at `conditional`.
12. **Score breakdown** — every rubric axis and the total.

**Also emit, separately:**
- **MAST capability → fallback map**: for each MAST capability (SPOC LCs, TESScut,
  JWST products, HST products, HLSPs, Kepler/K2, Pan-STARRS, GALEX) the chosen
  fallback(s) or an explicit **GAP** line.
- **Top-3 integration backlog**: ordered, each with the concrete first campaign
  (target class, field, volume, positive control, expected runtime).
- **Search log**: what was searched, what was excluded and why, what remains
  unsearched (`SEARCH_LOG.md` in the campaign directory).

---

## 7. Ranking rubric (produces the order)

Score each axis 0–5, multiply by weight, sum, sort descending. Publish the
breakdown so the order can be challenged.

| # | Axis | Weight | What a 5 looks like |
| --- | --- | --- | --- |
| A | **Novelty headroom** (least surveyed / least studied) | ×3 | Recently released *and* no published systematic search of this product type; large serendipitous/untargeted fraction; measurable "unmatched" fraction after epoch-aware cross-match. |
| B | **Lead-yield potential** (can it surface leads to undiscovered entities?) | ×3 | A concrete, falsifiable hypothesis per domain; the data actually resolve the relevant signal (depth/cadence/astrometric precision sufficient); plausible ≥ O(1–10) screenable leads per bounded campaign. |
| C | **MAST independence + robustness** | ×2 | Different operator, documented mirror(s), stable host, survives a STScI outage entirely. |
| D | **Access safety** (anonymous, licensed, scriptable, rate-limited sanely) | ×1.5 | Anonymous TAP/REST, clear TOU permitting derived-product redistribution, checksums exposed, published limits. |
| E | **Calibratability** (known-truth controls + injection–recovery feasible) | ×1.5 | Multiple named positive controls in-dataset; a published recovery example exists. |
| F | **Tractability** (volume, API ergonomics, client support) | ×1 | Bounded first campaign; existing `astroquery`/`pyvo` support; no bespoke auth. |
| G | **Falsifiability / independent confirmation inside the source** | ×1 | Independent epochs, second instrument, or a second reduction available *within* the same archive, enabling self-contained confirmation. |

**Penalties:** −2 if the access route touches MAST at any point (and exclude from
the fallback tier unless a non-MAST route also exists); −2 if license/TOU is
ambiguous or forbids redistribution into `publish/`; −1 if no calibration control
could be identified; −1 if the novelty claim is asserted rather than measured.

**Tie-breaks, in order:** (1) higher novelty headroom; (2) higher lead yield;
(3) newer release; (4) fully `[V]` beats `[K]`; (5) anonymous beats free-account.

**Hard ordering rule:** the final list must be a single ordered sequence
1 → N. No "tiers of equals" in the master table; ties resolved by the rules above
and the resolution recorded.

---

## 8. Seed candidate pool — prior-knowledge hypotheses to verify or refute

These are **starting hypotheses, not findings**. Every row is `[K]` unless you
re-fetch it; your live verification may re-rank or delete any row. Treat the
expected-rank column as a prior to be tested by the §7 rubric, never as the
conclusion. Add candidates you discover that are not listed here — especially
missions that released data after this file was written.

| Expected rank | Candidate | Data type | Access / archive source (verify live) | Why it could surface leads (hypothesis, to be tested) |
| --- | --- | --- | --- | --- |
| 1 | **Gaia DR3 epoch photometry** (`gaiadr3.epoch_photometry`, per-transit photometry; DR3 also carries ~34-month baselines) | Sparse multi-epoch *G*-band time series for millions of sources | Gaia Archive, ESAC `https://gea.esac.esa.int/archive/` — TAP (`FORMAT=csv`) + DataLink for per-source epoch series; operator ESA (MAST-independent) | All-sky, multi-year, and **not systematically folded for isolated transits / long-period eclipsers / long-timescale microlensing**. A single deep dropout in a sparse series is exactly the monotransit regime `AGENTS.md` Domain I warns about: a lead, not a period. Nulls to kill it: Gaia blending at sub-arcsec separation, blue/red photometer (BP/RP) systematics, window-function aliases, known variability (VSX/GCVS). Controls: known long-period eclipsing binaries and known Gaia alerts. |
| 2 | **JWST public products via the ESA JWST Science Archive** (incl. NIRCam/MIRI imaging, NIRISS WFSS, pure-parallel and serendipitous fields) | Deep near/mid-IR imaging + slitless spectra, Level-2/3 products | `https://jwst.esac.esa.int/archive/` (ESA/ESAC mirror, live-verified 2026-09-23); also ESA Sky for discovery. MAST-independent for the mirror path | JWST is the newest and deepest facility, and its **untargeted content is the least surveyed sky that exists**: pure parallels and serendipitous sources in the field of others' targets were never the subject of any programme. Plausible leads: cold/Y-dwarf companions by NIRCam colour in deep fields, high-*z* dropouts, faint LSB structures around targets, slow movers between repeated visits. Nulls: diffraction spikes, persistence, snowballs/cosmic rays, scattered light, 1/f noise, uncertain absolute astrometry. Controls: published JWST early-release sources recovered by our own reduction. Verify the 12-month exclusive-access rule per Cycle before assuming a programme is public. |
| 3 | **Gaia DR3 Non-Single-Star solutions** (`nss_acceleration_astro`, `nss_two_body_orbit`, `nss_vim_fl`) + RUWE / astrometric-excess-noise outliers | Astrometric orbit and acceleration solutions; variability-induced movers | Gaia Archive TAP (ESAC); mind live table names | Direct route to **Domain III (dark companions)**: astrometric acceleration gives a mass function, not a mass — `f(M) = (M2 sin i)^3/(M1+M2)^2` — so the least-studied tail (low-SNR, long-period, and *rejected* solutions) is where an unseen compact companion would hide. Published work has mined only the high-significance tip. Nulls: spurious solutions, triples, luminous secondaries, scan-law systematics. Controls: Gaia BH1/BH2/BH3-type published systems must be recoverable by our pipeline before any new claim. |
| 4 | **Spitzer Heritage Archive** (cryogenic IRAC 3.6–8.0 µm & MIPS 24 µm, IRS spectra, warm IRAC, SEIP) | Deep mid-IR imaging + low-res spectra, 2003–2020 baseline | IRSA (IPAC) `https://irsa.ipac.caltech.edu/` — TAP/Gator + Heritage Archive; MAST-independent | The cryogenic era is **finished and under-reanalysed**: no new Spitzer data will ever arrive, so any unstudied 8/24 µm excess, cold circumstellar structure, or mid-IR mover is permanently preserved. The 16+ year lever arm Spitzer → WISE/NEOWISE gives proper motions unreachable any other way for cold, optically invisible objects (Domain II/III). Nulls: IRAC pulldown/muxbleed, latent images, column pulldown, large PSF blending, 2MASS PSC not being TAP-served (use VizieR/Gator). |
| 5 | **Euclid** early releases (Q1 / first quick data release; VIS + NISP Y/J/H imaging and slitless spectra) | Wide, high-resolution optical + NIR imaging over new sky | ESA/Euclid Archive at ESAC; IRSA mirror (verify live) | Brand-new wide NIR imaging at *HST*-like resolution over fields nobody has mined: strong candidates for LSB tidal features, lensed arcs, ultracool NIR movers, and high-*z* dropouts — Domains II–IV. Verify exactly which release, footprint, and data rights exist as of today before scoring; novelty is maximal precisely because the community has not caught up. |
| 6 | **Gaia BP/RP (XP) spectrophotometry** (`xp_summary` and XP mean/continuous representations) | Low-resolution spectrophotometry for ~10^8 sources | Gaia Archive TAP + DataLink (ESAC); VizieR `I/355` mirrors | XP is a spectroscopic survey larger than all others combined and **only sparsely mined for outliers**: composite/unresolved pairs (WD+BD, M+WD), ultracool objects, carbon/O-rich and dust-obscured SEDs, and objects whose XP SED disagrees with their broad-band classification. Disagreement between XP-derived and catalogued classification is a cheap, high-yield anomaly screen. Nulls: calibration/reddening degeneracies, blending in crowded fields, extinction. |
| 7 | **NEOWISE / unWISE / WISE single-exposure archive** (reactivation mission, 10+ yr) | Time-resolved mid-IR (3.4/4.6 µm) imaging and coadds | IRSA (IPAC) — TAP (`allwise_p3as_psd`), unWISE coadds at NERSC/Legacy Survey; MAST-independent | IR time domain is the least-worked time domain. Leads: Y/T-dwarf proper-motion candidates (W2-only sources with no optical counterpart), dust-obscured transients and IR-bright events with no visible host, IR microlensing. Nulls: moonlight/glint artifacts, latent artifacts, saturation, confused Galactic-plane sources. |
| 8 | **Rubin/LSST first data releases (DP1, LSComCam/ComCam commissioning)** | Deep wide-field optical imaging, repeat visits, difference Imaging | Rubin Science Platform instances (US/UK/Fr IDF) — **free account required**; verify anonymous routes | The deepest wide optical sky ever taken, released within the last year: LSB structures, movers, and transients in fields with essentially zero published analysis (Domain II/IV). Score down if access requires an account or if the released footprint is small; score up hard on novelty if commissioning fields are public and unstudied. |
| 9 | **eROSITA DR1 (all-sky X-ray)** | X-ray source catalogues + images/spectra (0.2–10 keV) | eSASS / eROSITA DR1 at MPE; mirrors via HEASARC/ESAC/VizieR (verify) | An all-sky X-ray census new enough that systematic counterpart searches are incomplete. Hypothesis (Domain III): X-ray-bright sources with **no plausible optical/IR counterpart** — isolated neutron stars, dormant BH candidates, obscure accreting binaries. Nulls: extent/flag ambiguities, spurious detections near bright sources, positional-error cross-match mistakes. |
| 10 | **New transient missions: Einstein Probe (2024), SVOM (2024), XRISM (2023), SPHEREx (2025)** | Wide-field X-ray transient alerts and follow-up; high-res X-ray spectroscopy; all-sky NIR spectral imaging | Mission science centres: EP (CAS/NAOC), SVOM (CNES/CEA + Chinese centre), XRISM (ISAS DARTS + HEASARC), SPHEREx (IRSA) — **all access facts `[K]`, verify availability and data rights first** | Highest novelty by construction: missions that launched in the last ~2 years, whose archives are the least surveyed sky in the literal sense. EP/SVOM are *transient-discovery* machines — ideal for fast X-ray/UV events that no optical survey caught (Domain IV). SPHEREx all-sky NIR spectra enable SED-outlier searches for cold/unclassified objects (Domain III). Rank them high **only if** you verify live that public data exist and are scriptable; otherwise they are `conditional` with the blocking gate named. |
| 11 | **Ground-based time domain: ZTF (+ ALeRCE), ATLAS, ASAS-SN, BlackGEM/NGTS, SuperWASP, KELT** | High-cadence optical light curves and alert streams, years-long baselines | ZTF via IRSA/ALeRCE; ATLAS `fallingstar.com`; ASAS-SN Sky Patrol; WASP/KELT public releases (verify each host) | The practical MAST-out substitute for the photometric domain: keeps single-transit, TTV, and fast-transient screening alive when SPOC is unreachable. Lower depth and different window function — state that explicitly; it is a substitute, not an equivalent. Nulls: seeing-dependent systematics, differing photometric reductions, astrometric-scatter contamination. |
| 12 | **Radio surveys: LOFAR LoTSS DR2, MeerKAT MIGHTEE/MALS, ASKAP EMU/VAST, VLASS** | Deep wide-field radio continuum, polarisation, and transient/VAST epochs | ASTRON/SURF LOFAR archive; SARAO/Ilifu; CSIRO CASDA (open data); NRAO/CIRADA for VLASS | Radio is the least cross-matched band against Gaia: a compact radio source with **no optical/IR counterpart** is a compact-object / dust-obscured / exotic lead (Domain III), and VAST/MeerKAT epochs support slow transient searches. Nulls: sidelobes, calibration artifacts, ionospheric effects, large positional errors in the wide-field case. |
| 13 | **Independent deep optical/IR imaging: DES DR2 / DECam (NOIRLab Astro Data Lab), DECaLS/BASS/MzLS (Legacy Survey DR10), HSC-SSP, KiDS/VST, UKIDSS/VHS/VISTA, CFHT Legacy** | Deep coadded imaging, tractor/forced-photometry catalogues, IR counterparts | NOIRLab Astro Data Lab; `portal.nersc.gov` Legacy Survey tractor files (`CC BY 4.0`, credit required — verified 2026-09-24); HSC data release site; ESO archive; WFCAM/VSA science archives; CADC | Wide, deep, and MAST-independent — the substrate for LSB structure recovery, ultracool/moving-object searches, and lensed-arc hunting where MAST's coverage is thin. Legacy Survey is already proven in this project and carries a confirmed license; prefer it where footprints overlap. Nulls: over-subtracted backgrounds, cirrus, flat-field residuals, coadd artifacts — quote surface-brightness sensitivity at the relevant angular scale. |
| 14 | **Chandra CSC 2.x / XMM 4XMM-DR13 (+ Swift/UVOT, NuSTAR, Fermi-LAT via HEASARC/FSSC)** | Deep X-ray/UV/γ source catalogues, spectra, event data; Fermi transient catalogues | CXC (`cda.harvard.edu`), ESAC XSA, HEASARC, FSSC — all MAST-independent | Cross-matching deep X-ray point sources against Gaia NSS and optical imaging is a mature dark-companion funnel; the least-studied slice is **X-ray sources with no counterpart in any band**, and orphan/untriggered transient catalogues. Nulls: spurious catalog entries near bright sources, confused fields, large error circles. |
| 15 | **Microlensing: OGLE EWS + KMTNet** | High-cadence microlensing light curves, real-time event lists | OGLE (`ogle.astrouw.edu.pl`), KMTNet (`kmtnet.kasi.re.kr`) — verify endpoints | Free-floating-planet and short-*t*E candidates (Domain I). Least-studied slice: short events and events with unresolved or no detectable source star. Nulls: finite-source and blending effects, cadence gaps, parallax degeneracy — a short Einstein timescale alone is *not* an FFP. |
| 16 | **Spectroscopic surveys: LAMOST DR, SDSS DR (VizieR/SciServer), RAVE, GALAH, APOGEE, DESI EDR** | Millions of optical/NIR spectra and derived parameters | LAMOST `dr.lamost.org`; SDSS/VizieR/SciServer; GALAH/RAVE data releases; DESI via NERSC (verify) | Spectral outliers and composite spectra (WD+BD, Li-rich, carbon-enhanced, emission-line oddities) are systematically under-explored outside the surveys' own pipelines. Useful mainly as a **cross-check** layer for candidates raised by Gaia/XP — rank accordingly. |
| 17 | **HST via the ESA/ESAC Hubble mirror (eHST)** | Optical/UV imaging and spectra, legacy deep fields | `https://esahubble.org/` ESA Archive (verify coverage and whether it is a full mirror) | Not a *new* mission, but it is the fallback that keeps HST-dependent campaigns alive when MAST is down, and its least-studied content is the archival pure-parallel/legacy field population. Rank below genuinely new sources; rank above nothing-else options. |
| 18 | **Solar-system services: MPC observations database, JPL Horizons/SBDB, AstDyS/NEODyS, SkyBoT, Catalina/NEAT/Pan-STARRS astrometry** | Astrometry, orbits, ephemerides, per-epoch solar-system object predictions | `minorplanetcenter.net`, `ssd.jpl.nasa.gov`, `newton.spacedys.com`, `astroquery.imcce` (SkyBoT) | Not discovery data by itself, but **mandatory plumbing**: no moving-object lead is admissible without MPC/SkyBoT checks at every epoch, and precovery/stacking searches in archival imaging (e.g. DES, DECaLS, NEAT scans) can surface uncatalogued slow movers. Rank last as a *discovery* source, first as a *gate*. |
| — | **GAP: TESS SPOC high-cadence photometry and TESScut FFI cutouts** | — | — | Declare explicitly if, as expected, no non-MAST mirror exists. Name the substitutes (ZTF/ATLAS/ASAS-SN/SuperWASP) with the cadence/depth differences spelled out. Do **not** let a MAST-hosted HLSP or a STScI-hosted mirror count as a fallback. |

---

## 9. Anti-patterns — explicit prohibitions

- Do not list a MAST-hosted service as a MAST fallback (e.g. MAST-hosted HLSPs,
  Pan-STARRS at STScI). Check the *host*, not the mission.
- Do not present an inferior substitute as equivalent (ZTF ≠ SPOC: different
  cadence, depth, aperture, systematics).
- Do not rank by data volume, fame, or "biggest catalogue wins".
- Do not assert novelty. Measure it, or mark it "not measured" and score it down.
- Do not invent endpoints, table names, row counts, release dates, or bibcodes.
  If a name is uncertain, write the query you will run to confirm it.
- Do not call anything "uncatalogued" or "undiscovered"; use "no match in
  `<sources>` as of `<date>`" and "lead".
- Do not skip the MAST re-check: confirm with a control query that MAST is actually
  unavailable in the scenario being planned for (and note whether the fallback
  should be *always-on* redundancy rather than outage-only).
- Do not bulk-download before Stage B screening.
- Do not commit `*.fits`, `state/`, or scratch paths. Bulk data stays out of the
  worktree (Drive-hosted only, per `DATA_SOURCES.md` §0).

---

## 10. Deliverables and where they go

| Product | Path |
| --- | --- |
| Ranked registry (human, ordered 1 → N, full §6 records) | `docs/FALLBACK_SOURCES.md` |
| Machine-readable ranked list | `docs/fallback_sources/ranked_candidates.csv` and `.json` |
| Verbatim query log (endpoint, query text, UTC, row counts, release strings) | `docs/fallback_sources/QUERIES.md` |
| Search log (what was searched / excluded / left unsearched) | `campaigns/fallback-source-scout-01/SEARCH_LOG.md` |
| MAST capability → fallback / GAP map | section inside `docs/FALLBACK_SOURCES.md` |
| Top-3 integration backlog with concrete first campaigns | section inside `docs/FALLBACK_SOURCES.md` |
| Ledger rows for every verification run and every retrieved product | `state/ledger.sqlite` (run IDs quoted in the report) |
| Ingest adapters + tests for adopted sources (follow-on work, not this campaign) | `src/cygnus/ingest/<source>.py`, `tests/test_ingest_<source>.py` |

Update `DATA_SOURCES.md` §1 with any newly `[V]`-verified entry and its date; do
not delete existing tags or overwrite another campaign's notes.

---

## 11. Exit criteria — the campaign is done when

1. ≥ 10 candidates carry complete §6 records, and **every** top-5 candidate's
   access facts are `[V]` with a verbatim control query and UTC date.
2. Every MAST capability has either ≥ 1 non-MAST fallback or an explicit
   **GAP** line with named substitutes.
3. All four `AGENTS.md` discovery domains have ≥ 1 fallback capable of producing
   leads (or a stated domain gap).
4. Novelty headroom was *measured*, not asserted, for every top-5 candidate, or
   explicitly recorded as "not measured" with the penalty applied.
5. Each adopted candidate has a named positive control and a named falsifying
   observation.
6. Every license/TOU line is a quotation with its source URL, and the
   `publish/` redistribution question is answered per source.
7. `python -m pytest -q -m 'not network'` passes; network-marked smoke tests are
   listed with their controls even if not executed.
8. The master table is one ordered sequence, all tie-breaks recorded.

---

## 12. Execute

Work in this order: re-check MAST status with a control query → Stage A scout →
Stage B live screening of the §8 seed pool plus any candidates you add → Stage C
novelty measurement → Stage D hypothesis stress-test → Stage E integration plan →
Stage F ranked registry. Log every query verbatim. When a seed row is refuted,
keep it in the registry with the refutation and the query that refuted it — a
falsified prior is a result. Report the final ordered list, the top-3 backlog, and
every declared gap.
