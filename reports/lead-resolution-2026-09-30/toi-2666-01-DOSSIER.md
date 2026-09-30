### CYGNUS CANDIDATE DOSSIER

**Working identifier:** CYG-2026-09-TOI2666.01 (local working ID — not an official designation)
**Evidence level:** unverified_lead
**Bottom line:** S35/S99 V-shaped dips persist under independent baseline choices. Zhang2024 primary Keck/HIRES evidence identifies HIP45621/TOI2666 as a spectroscopic binary with35-km/s component separation, corroborating the close-companion alternative. The later eclipse is not linked to a solved stellar orbit. Earlier S8 FFI tests robustly exclude0 of52 historical aliases across exposure integration and timing slack; noisy reductions cannot supply a clean nondetection. Unverified event interpretation; binarity independently established. Two public FEROS spectra from2006/2009 were retrieved; their relative-shift blocks disagree by53km/s, so no usable component velocities or orbit are claimed. A bounded public Keck HIRES coordinate query returns three raw observations from1998/2021; exact-name selection returns zero. Documented public access recovered all three primary header prefixes: each TARGNAME is80133, consistent with intended HD80133 targeting. Iodine is out for1998/February2021 and in forMay2021. KOA lists18/59/58 associated calibrations; suitability, acquired component identity and component velocities remain untested. No full science or calibration FITS was downloaded; no extra velocities or orbit are claimed.

#### 1. Provenance

- **2026-09-30 follow-up:** reports/lead-resolution-2026-09-30/REPORT.md; exact queries/checksums in companion JSON outputs
- **archive:** MAST (TESS SPOC 120-s light curves, TPF difference images; NASA Exoplanet Archive TOI table for target metadata)
- **campaign:** campaigns/toi-2666-01.yaml and campaigns/toi-2666-01; vetting artifacts campaigns/toi-2666-01/../vetting/ (vetting.json, VETTING.md, figures)
- **position:** RA 139.480865 deg, Dec -3.387525 deg (ICRS; TOI-table position at Gaia DR2 epoch J2015.5 — reports/position-epoch-audit-01)
- **products:** `tess2021039152502-s0035-...s_lc.fits`, `tess2023018032328-s0061-...s_lc.fits`, `tess2026005125623-s0099-...s_lc.fits` (SHA-256 in the sky record)
- **sectors:** S35 (reference), S61, S99
- **target:** TOI-2666.01 (TIC 170889511), Tmag 6.99
- **time_standard:** BJD_TDB (SPOC light-curve timestamps)
- **vetting:** python -m cygnus.campaign vet, 2026-09-26; per-lead reading in campaigns/tess-{mono-01,periodic-01}/LEAD_VETTING_LOG.md
- **worktree_commit:** 6a3aa66

Prior-art gate results (ledger-pinned):

- catalog/NASA_Exoplanet_Archive: no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T08:15:12Z (as of 2026-09-26T08:15:12Z)
- catalog/SIMBAD: 2 match(es) in SIMBAD within 30" as of 2026-09-26T08:15:20Z: TOI-2666.01 (Pl?); HD  80133 (PM*) (as of 2026-09-26T08:15:20Z)
- catalog/TESS_TOI: 1 match(es) in TESS_TOI within 30" as of 2026-09-26T08:15:14Z: TOI-2666.01 (TIC 170889511, disposition APC) (as of 2026-09-26T08:15:14Z)
- catalog/VSX: no match in VSX within 30" as of 2026-09-26T08:15:17Z (as of 2026-09-26T08:15:17Z)

#### 2. Measured signal

- **E1_S99:** value=BJD 2461049.1644, depth 15464 +/- 181 ppm, 1.16 h
- **alias_family:** value=52 data-allowed aliases of dT/n, all P >= 12.79 d by the Gaia density limit
- **delta_T_reference_to_E1:** value=1790.006; unit=d
- **depth_ratio_E1_reference:** value=1.02; uncertainty=+/-0.02
- **positional_verification:** value=difference-image centroid 0.4 arcsec from the out-of-transit centroid (0.7 sigma); 97 percent of the deficit inside the optimal aperture
- **red_noise_significance:** value=local robust statistic 158.1 relative to 300 random epochs; zero exceedances, search-wide false-alarm rate not estimated
- **reference_V_shape_index:** value=1.47; method=profile comparison (grazing geometry)
- **reference_depth:** value=15215; unit=ppm; uncertainty=+/-176; method=PDCSAP median residual
- **reference_duration:** value=1.16; unit=h; method=box fit
- **reference_transit_S35_bjd:** value=2459259.1579; unit=BJD_TDB; method=box fit
- **stellar_priors:** value=1.11 Rsun, 0.90 Msun host (Mamajek dwarfs from Gaia colour); method=Gaia DR3 colour+parallax; host spot variability 1-3.4 ppt dips, 2-61 h, every sector
- **superseded_bottom_line_2026-09-27:** value=Two deep, coincidentally-equal V-shaped dips on HD 80133 measured in S35 and S99, 1790.006 d apart, survive several artifact tests, with quality/box-fit checks inconclusive (on-target difference image 0.4 arcsec/0.7 sigma, shape ratio 1.02 +/- 0.02, strong local box statistic against 300 random epochs; search-wide false-alarm rate uncalibrated, no capable neighbour). All short SPOC-DV periods (13.93/34.37/7.50 d) and the P 36.53 d alias are refuted as two-event artifacts and parity-inconsistent rows; 52 data-allowed aliases (P >= 12.79 d) remain. A grazing planet (Rp ~ 1.1-1.4 Rjup) or an equal-depth grazing EB is unresolved — RV is decisive — Unverified lead.; method=historical narrative; superseded by2026-09-30 follow-up; original measurements retained

#### 3. Artifact audit

| test | state |
| --- | --- |
| 2026-09-30 SAP/PDCSAP baseline persistence | passed |
| 2026-09-30 fixed-epoch injection sensitivity | passed |
| 2026-09-30 search-wide false-alarm calibration | not_tested |
| Gaia RVS RV | not_tested |
| Gaia neighbours able to mimic the depth (E1) | passed |
| KOA calibrated component velocities | not_tested |
| KOA three raw-prefix access | passed |
| Kepler/K2 independent epoch | not_tested |
| S8 alias exclusions across reduction variations | inconclusive |
| SPOC DV periods (13.92639 / 34.36669 / 7.50451 d) | failed |
| Two-epoch FEROS component-RV extraction | failed |
| ZTF independent epoch | not_tested |
| alternative detrending (E1) | passed |
| archival/new RV | not_tested |
| background/centroid/pointing shifts (E1) | passed |
| box fit with pipeline errors (E1) | inconclusive |
| difference-image centroid (E1) | passed |
| future-sector alias test | not_tested |
| independent cached TPF localization (2026-09-27) | passed |
| parity test on P 36.53 d alias secondary | failed |
| quality flags and coverage (E1) | inconclusive |
| red-noise significance (E1) | inconclusive |
| same-CCD common mode (E1) | passed |
| shape vs reference (E1) | passed |
| single-star host interpretation | failed |
| stellar-density duration limit on aliases | passed |

(States: passed | failed | inconclusive | not_tested — 'not_tested' never supports an evidence upgrade.)

#### 4. Catalog and literature audit

- **2026-09-30 primary literature and exact-source refresh:** reports/lead-resolution-2026-09-30/PRIOR_ART_AUDIT.md; archive_refresh.json. Companion/binary evidence is not an event-time matched orbit.
- **Gaia DR3 NSS:** no two-body solution for the host (campaigns/toi-2666-01-nss/); RUWE 1.464 weakly consistent with an unseen companion, not diagnostic
- **NASA Exoplanet Archive (pscomppars, 30 arcsec):** no match (as of 2026-09-26T08:15:12Z)
- **SIMBAD (30 arcsec):** TOI-2666.01 (Pl?) and HD 80133 (PM*) — no EB class; no literature entry found by web search 2026-09-24
- **TESS_TOI (30 arcsec):** TOI-2666.01 (TIC 170889511, APC); the TOI table row carries no period (row updated 2022-04-19)
- **VSX (30 arcsec):** no match (as of 2026-09-26T08:15:17Z)

#### 5. Competing explanations

- Spectroscopic stellar binary independently identified by Zhang2024 Keck/HIRES; unresolved component orbit remains the leading alternative to a planet interpretation.
- Grazing transiting planet/brown dwarf: Rp ~ 1.1-1.4 Rjup at b near 1 — allowed by all data.
- Equal-depth grazing eclipsing binary: a stellar companion gives K ~ km/s under every surviving alias; secondary eclipses could hide in the seasonal gaps of the long aliases. Distinguishing prediction: RV K; grazing EBs also often show b-dependent depth variation across sectors, and none is seen.
- Host-spot artifact: the host varies with 1-3.4 ppt dips (2-61 h) in every sector and explains the chi2_nu 21.8 and the 316 +/- 62 ppm phase-0.5 rows; the two measured events are 15.2–15.5 ppt (1.52–1.55%); a joint spot/eclipsing model has not yet excluded activity or detrending coupling.
- Contamination: rejected — no Gaia source bright enough within 52 arcsec; on-target difference image; empty common mode.

#### 6. Reproduction

- **2026-09-30:** python reports/lead-resolution-2026-09-30/resolve_leads.py --help; config.json; see REPORT.md for ordered modes and validation
- **code:** cygnus (src/cygnus/); historical baseline gate at commit 6a3aa66: 639 passed, 37 deselected; current workspace gate 2026-09-27: 644 passed, 37 deselected
- **figures:** vetting/figures/ and vetting/*.png in the campaign directory
- **follow_up_2026_09_27:** reports/lead-followup-2026-09-27/independent_tpf_check.py; results in independent_tpf_results.json and REPORT.md
- **package_versions:** python 3.13; astropy/lightkurve/numpy per requirements.txt; candidates rendered by cygnus.reporting.dossier
- **run:** python -m cygnus.multi run campaigns/toi-2666-01.yaml ; python -m cygnus.campaign vet campaigns/toi-2666-01.yaml

#### 7. Follow-up

Recover multi-epoch component spectra/RVs of HD80133/HIP45621 and fit an SB2 orbit against the observed eclipse times. No S8 alias exclusion is robust; do not restore a single-star radius or infer a planet from the light curve alone. Screen the three public KOA raw observations for exact-source identity and science-grade calibration before extracting component velocities.

---
*Generated from ledger/candidate records only; any field the evidence does not support renders '(none recorded)' rather than a fabricated value.*
