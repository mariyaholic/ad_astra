### CYGNUS CANDIDATE DOSSIER

**Working identifier:** CYG-2026-09-TOI3500.02 (local working ID — not an official designation)
**Evidence level:** unverified_lead
**Bottom line:** S64/S90 dips persist, but official UPDATED_2.0 TESS PRFs do not assign the deficit robustly between the0.18-pixel-separated Gaia A/B pair. Source preference reverses with allowed registration and1/3/5-percent model floors; static PRF residuals exceed nominal interpolation accuracy. S101 remains rejected and supplies no period preference. All16 baseline aliases remain open; Gaia RV summaries provide no orbit or companion-mass bound. Unverified lead. Six public HARPS epochs span111.785days with87.507m/s corrected-RV range. A conditional circular50.0446-day fit gives signedK about39m/s but six epochs, line-width correlation and unresolved source identity prevent confirmation or alias rejection. Eighteen further HARPS and six FEROS products returnHTTP401. A relative-spectrum attempt on23 FEROS and6 HARPS spectra fails the independent HARPS precision check (168m/s RMS); derived shifts are not accepted orbital velocities. A completed31-input line-mask rerun gives HARPS CCF-alignment disagreement RMS10.9458m/s (R50G2) and10.8503m/s (K0), both failing the10m/s requirement. FEROS midpoint barycentric replacement deltas are roughly-103 to+173m/s; release products also lack simultaneous-reference drift correction and usable ERR arrays. FEROS profile shifts remain unvalidated.

#### 1. Provenance

- **2026-09-30 follow-up:** reports/lead-resolution-2026-09-30/REPORT.md; exact queries/checksums in companion JSON outputs
- **archive:** MAST (TESS SPOC 120-s light curves, TPF difference images; NASA Exoplanet Archive TOI table for target metadata)
- **campaign:** campaigns/toi-3500-02.yaml and campaigns/toi-3500-02; vetting artifacts campaigns/toi-3500-02/../vetting/ (vetting.json, VETTING.md, figures)
- **position:** RA 186.816884 deg, Dec -29.832996 deg (ICRS; TOI-table position at Gaia DR2 epoch J2015.5 — reports/position-epoch-audit-01)
- **products:** `tess*-s0064-00000000443666343-*-s_lc.fits`, `...s0090-...`, `...s0101-...`
- **sectors:** S64 (reference), S90 (E1); S101 (E2) rejected
- **target:** TOI-3500.02 (TIC 443666343), Tmag 10.83
- **time_standard:** BJD_TDB (SPOC light-curve timestamps)
- **vetting:** python -m cygnus.campaign vet, 2026-09-26; per-lead reading in campaigns/tess-{mono-01,periodic-01}/LEAD_VETTING_LOG.md
- **worktree_commit:** 6a3aa66

Prior-art gate results (ledger-pinned):

- catalog/NASA_Exoplanet_Archive: no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T08:20:55Z (as of 2026-09-26T08:20:55Z)
- catalog/SIMBAD: 1 match(es) in SIMBAD within 30" as of 2026-09-26T08:21:03Z: UCAC2  19403154 (PM*) (as of 2026-09-26T08:21:03Z)
- catalog/TESS_TOI: 2 match(es) in TESS_TOI within 30" as of 2026-09-26T08:20:58Z: TOI-3500.01 (TIC 443666343, disposition PC); TOI-3500.02 (TIC 443666343, disposition PC) (as of 2026-09-26T08:20:58Z)
- catalog/VSX: no match in VSX within 30" as of 2026-09-26T08:21:01Z (as of 2026-09-26T08:21:01Z)

#### 2. Measured signal

- **E1_S90:** value=BJD 2460757.3199, depth 7553 +/- 277 ppm (box fit), shape ratio 1.08 +/- 0.06, duration ratio 1.00
- **E2_S101_rejected:** value=BJD 2461107.6407, difference-image centroid 6.74 arcsec off at 11.5 sigma, POS_CORR2 +28.9 sigma, depth 1614-7796 ppm across detrendings — an aperture-loss/pointing artifact; supports no period
- **HARPS descriptive RV range:** value=0.08750691315560033; unit=km/s; method=six pipeline RVC epochs; range is not orbitalK or mass
- **alias_family_16_aliases:** value=P = 700.62, 350.31, 233.54, 175.16, 140.12, 116.77, 100.09, 87.58, 77.85, 70.06, 63.69, 58.39, 53.89, 50.04, 36.88, 35.03 d (density limit excludes 18.44 d)
- **delta_T_reference_to_E1:** value=700.6242; unit=d; method=reference S64 to accepted E1 S90; allowed aliases P = ΔT/n, including 350.31 d
- **no_secondary_E1:** value=with E2 excluded, phase-0.5 windows are clean at all covered aliases (e.g. P 35.03: -80 +/- 186; 50.04: +313 +/- 167 ppm)
- **red_noise_significance_E1:** value=local robust statistic 36.0 relative to 300 random epochs; zero exceedances, search-wide false-alarm rate not estimated
- **reference_depth:** value=7020; unit=ppm; uncertainty=+/-282; method=PDCSAP median residual (catalogue depth for TOI-3500.02: 8095 ppm)
- **reference_duration:** value=7.91; unit=h; method=box fit
- **reference_transit_S64_bjd:** value=2460056.6957; unit=BJD_TDB; method=box fit
- **stellar_priors:** value=1.10 Rsun, 0.94 Msun host (density limit), host G 11.35 — RV-measurable; sibling TOI-3500.01 (P 7.3436 d, PC) transit is not the signal
- **superseded_bottom_line_2026-09-27:** value=Two repeat dips remain in the TIC 443666343 aperture (the S90 event E1 and the S64 reference; S101 E2 is rejected as an aperture-loss/pointing artifact). Their depth, duration and shape agree, and their difference images lie near the target. A 2026-09-27 two-source Gaussian-PSF sensitivity grid usually prefers the target over the 3.71-arcsec co-moving neighbour, but the preference reverses under plausible PSF/registration perturbations because the sources are only 0.184 TESS pixel apart. Localization therefore remains inconclusive. Sixteen aliases P = 700.6242/n over 35.03–700.62 d remain; search-wide false alarms, calibrated PRF localization, RV and phase coverage are incomplete. Unverified lead.; method=historical narrative; superseded by2026-09-30 follow-up; original measurements retained

#### 3. Artifact audit

| test | state |
| --- | --- |
| 2026-09-30 SAP/PDCSAP baseline persistence | passed |
| 2026-09-30 fixed-epoch injection sensitivity | passed |
| 2026-09-30 search-wide false-alarm calibration | not_tested |
| FEROS precision calibration | inconclusive |
| Gaia neighbours able to mimic the depth (E1) | inconclusive |
| HARPS six-epoch pipeline RV retrieval | passed |
| Line-mask CCF precision validation | failed |
| RV (host G 11.35) | not_tested |
| RV orbit and activity discrimination | inconclusive |
| Relative-spectrum precision validation | failed |
| ZTF light curve (3.71 arcsec neighbour) | not_tested |
| ZTF phase coverage (host) | not_tested |
| alternative detrending (E1) | passed |
| background/centroid/pointing (E1) | passed |
| background/centroid/pointing (E2) | failed |
| blend blame (3.71 arcsec neighbour) | inconclusive |
| blend test (43.2 arcsec neighbour) | not_tested |
| box fit (E1; E2) | passed |
| calibrated two-source PRF2026-09-30 | inconclusive |
| difference-image centroid (E1) | passed |
| difference-image centroid (E2) | failed |
| future-sector alias test (P = 350.31 d epemeris next transit ~2027-08) | not_tested |
| independent cached TPF localization (2026-09-27) | failed |
| quality flags and coverage (E1) | passed |
| red-noise significance (E1; E2) | inconclusive |
| same-CCD common mode (E1; E2) | passed |
| secondary eclipse at phase 0.5 | inconclusive |
| shape vs reference (E1) | passed |
| stellar-density duration limit on aliases | passed |
| two-source Gaussian-PSF sensitivity grid (2026-09-27) | inconclusive |

(States: passed | failed | inconclusive | not_tested — 'not_tested' never supports an evidence upgrade.)

#### 4. Catalog and literature audit

- **2026-09-30 primary literature and exact-source refresh:** reports/lead-resolution-2026-09-30/PRIOR_ART_AUDIT.md; archive_refresh.json. Companion/binary evidence is not an event-time matched orbit.
- **Gaia DR3 cone:** 3.71 arcsec co-moving neighbour (parallax 5.21 mas = host's, G 14.07); 43.2 arcsec neighbour (G ~14.5)
- **NASA Exoplanet Archive (pscomppars, 30 arcsec):** no match within 30 arcsec (as of 2026-09-26T08:20:55Z)
- **SIMBAD (30 arcsec):** UCAC2 19403154 (PM*) — no eclipsing-binary class
- **TESS_TOI (30 arcsec):** TOI-3500.01 (PC, sibling known candidate, P 7.3436 d) and TOI-3500.02 (PC) — the phase-0.5 sibling-vs-lead relation checked through the sibling ephemeris in vet
- **VSX (30 arcsec):** no match (as of 2026-09-26T08:21:01Z)

#### 5. Competing explanations

- Transiting planet or eclipsing companion under any of the 16 allowed aliases. At 7 ppt on an assumed 1.10 Rsun host, the central undiluted sqrt(depth) radius scale is about 10 Earth radii; grazing, dilution and unresolved multiplicity make this illustrative only. RV would constrain mass.
- Long-period grazing eclipsing binary: secondary can hide in the seasonal gaps of the long aliases; equal depth and equal shape currently constrain it — RV is decisive.
- Contamination by the 3.71-arcsec co-moving neighbour remains unresolved. The reviewable Gaussian-PSF grid favors the target in 71.4% of S64 trials and 85.7% of S90 trials, but target-versus-neighbour preference changes sign across the tested PSF widths and registration shifts; template correlations are 0.934-0.986 because the pair is separated by only 0.184 TESS pixel. A calibrated TESS PRF or higher-resolution observation is required.
- Aperture-loss artifact: applies to E2 only (rejected); E1 carries no POS_CORR excursion and 237/237 usable cadences.
- Sibling-TOI contamination (TOI-3500.01's P 7.34-d ephemeris): excluded by the sibling-ephemerides check — no catalogued sibling transit at E1's epoch.

#### 6. Reproduction

- **2026-09-30:** python reports/lead-resolution-2026-09-30/resolve_leads.py --help; config.json; see REPORT.md for ordered modes and validation
- **code:** cygnus (src/cygnus/); historical baseline gate at commit 6a3aa66: 639 passed, 37 deselected; current workspace gate 2026-09-27: 644 passed, 37 deselected
- **figures:** vetting/figures/ and vetting/*.png in the campaign directory
- **follow_up_2026_09_27:** reports/lead-followup-2026-09-27/independent_tpf_check.py and toi3500_two_source_test.py; results in independent_tpf_results.json, toi3500_two_source_results.json and REPORT.md
- **package_versions:** python 3.13; astropy/lightkurve/numpy per requirements.txt; candidates rendered by cygnus.reporting.dossier
- **run:** python -m cygnus.multi run campaigns/toi-3500-02.yaml ; python -m cygnus.campaign vet campaigns/toi-3500-02.yaml

#### 7. Follow-up

Use validated empirical sector PRFs or resolved time-series photometry for A/B; seek another clean event or component RV series. Retain all16 aliases, exclude S101 from period evidence, and do not treat catalog RV range as an orbital semiamplitude. Improve and validate line-mask/continuum spectral RV extraction; test the50.0446-day hypothesis against activity and blended components using additional accessible spectra.

---
*Generated from ledger/candidate records only; any field the evidence does not support renders '(none recorded)' rather than a fabricated value.*
