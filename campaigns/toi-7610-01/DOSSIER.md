# Retired candidate dossier: TOI-7610.01

> **Retired 2026-09-27.** Gaia DR3 supplies an SB1 orbit for the exact host
> (P = 90.4224 d, K1 = 12.14 km/s, 23 accepted RVs), with a mass function of
> 0.0144 solar masses and a conditional minimum companion mass near 0.238 solar
> masses. The independent cached-TPF reduction also reproduces the failed S99
> localization at 2.92 arcsec/5.71 bootstrap sigma. See
> [REJECTION.md](REJECTION.md). The former dossier below is preserved as the
> historical interpretation; no active candidate dossier remains.

### Historical CYGNUS candidate dossier

**Working identifier:** CYG-2026-09-TOI7610.01 (local working ID — not an official designation)
**Evidence level:** unverified_lead
**Bottom line:** One repeat dip with unresolved localization in S99 (BJD 2461066.3486, depth 15,757 +/- 425 ppm, 3.76 h), 365.379 d from the S88 reference, equal depth and shape; no current TOI linear ephemeris fits (the TOI table's P 22.1441 d is not an integer sub-multiple of dT: 365.379/22.1441 = 16.5); 21 data-allowed aliases of dT = 365.379 d. MOM_CENTR2 shifts by +5.9 local sigma, and the E1 difference-image centroid lies 2.9 arcsec away at 5.9 sigma; on-target origin is not established — Unverified lead.

#### 1. Provenance

- **archive:** MAST (TESS SPOC 120-s light curves, TPF difference images; NASA Exoplanet Archive TOI table for target metadata)
- **campaign:** campaigns/toi-7610-01.yaml and campaigns/toi-7610-01; vetting artifacts campaigns/toi-7610-01/../vetting/ (vetting.json, VETTING.md, figures)
- **position:** RA 129.250045 deg, Dec -3.530909 deg (ICRS; TOI-table position at Gaia DR2 epoch J2015.5 — reports/position-epoch-audit-01)
- **products:** `tess*-s0088-00000000121341000-*-s_lc.fits`, `...s0099-...`
- **sectors:** S88 (reference), S99 (E1)
- **target:** TOI-7610.01 (TIC 121341000), Tmag 11.80
- **time_standard:** BJD_TDB (SPOC light-curve timestamps)
- **vetting:** python -m cygnus.campaign vet, 2026-09-26; per-lead reading in campaigns/tess-{mono-01,periodic-01}/LEAD_VETTING_LOG.md
- **worktree_commit:** 6a3aa66

#### 2. Measured signal

- **E1_S99:** value=BJD 2461066.3486, depth 15757 +/- 425 ppm, 3.76 h, depth ratio 0.95 +/- 0.04, duration ratio 1.00
- **delta_T_reference_to_E1:** value=365.379; unit=d; method=alias family dT/n; 21 data-allowed aliases
- **no_secondary_E1:** value=phase 0.5 covered for 11 of 21 aliases; no >=4-sigma dip; median 1-sigma limit 393 ppm
- **red_noise_significance_E1:** value=local robust statistic 41.6 relative to 300 random epochs; zero exceedances, search-wide false-alarm rate not estimated
- **reference_depth:** value=16594; unit=ppm; uncertainty=+/-529
- **reference_duration:** value=3.76; unit=h; method=box fit
- **reference_transit_S88_bjd:** value=2460700.9701; unit=BJD_TDB; method=box fit
- **residual_caveat:** value=MOM_CENTR2 +5.9 sigma at E1 (pointing/centroid shift vs random epochs); difference-image centroid still 2.9 arcsec from the OOT centroid (5.9 sigma)
- **stellar_priors:** value=0.74 Rsun, 0.74 Msun (density limit), dwarf

#### 3. Artifact audit

| test | state |
| --- | --- |
| Gaia neighbours able to mimic the depth (E1) | passed |
| RV | not_tested |
| ZTF phase coverage | not_tested |
| alternative detrending (E1) | passed |
| background/centroid/pointing (E1) | failed |
| box fit (E1) | passed |
| difference-image centroid (E1) | failed |
| future-sector alias test | not_tested |
| independent cached TPF localization (2026-09-27) | failed |
| quality flags and coverage (E1) | passed |
| red-noise significance (E1) | inconclusive |
| same-CCD common mode (E1) | passed |
| secondary eclipse at phase 0.5 (E1) | inconclusive |
| shape vs reference (E1) | passed |
| stellar-density duration limit on aliases | passed |

(States: passed | failed | inconclusive | not_tested — 'not_tested' never supports an evidence upgrade.)

#### 4. Catalog and literature audit

- **Gaia DR3 cone:** No G<17 neighbour in the queried 52-arcsec cone capable of the 15.8 ppt depth under the adopted blend model.
- **NASA Exoplanet Archive (pscomppars, 30 arcsec):** no match within 30 arcsec (as of 2026-09-26T10:22:38Z)
- **SIMBAD (30 arcsec):** UCAC4 433-048726 (SB*) at 0.3 arcsec — inconclusive SB* class on the host; scrutinize with RV
- **TESS_TOI (30 arcsec):** TOI-7610.01 (TIC 121341000, disposition PC)
- **VSX (30 arcsec):** Gaia DR3 3071787586789910144 (type ROT, no period row) at 0.2 arcsec — a rotationally-variable host, not an eclipsing binary

#### 5. Competing explanations

- Transiting planet (Rp/R* = 0.126 on a 0.74 Rsun host => Rp ~ 0.64 Rjup; P from the 21-alias family).
- Eclipsing binary (secondary grazing star, low-mass): equal depth and duration consistent with a grazing equal-mass pair; RV or a phase-0.5 detection would set M2.
- Contamination, stellar variability or pointing remains unresolved: E1 MOM_CENTR2 moves +5.9 local sigma and its difference-image centroid is displaced 2.9 arcsec at 5.9 sigma. A coarse three-pixel acceptance rule cannot establish source localization; repeat the PRF/registration analysis.
- Sibling-TOI contamination: excluded by the sibling-ephemerides check (the catalogued P 22.1441-d ephemeris predicts no transit at E1's epoch, and 365.379/22.1441 is non-integer — no integer harmonic of the catalogued period fits the train).

#### 6. Reproduction

- **code:** cygnus (src/cygnus/); historical baseline gate at commit 6a3aa66: 639 passed, 37 deselected; current workspace gate 2026-09-27: 644 passed, 37 deselected
- **figures:** vetting/figures/ and vetting/*.png in the campaign directory
- **follow_up_2026_09_27:** reports/lead-followup-2026-09-27/independent_tpf_check.py; results in independent_tpf_results.json and REPORT.md
- **package_versions:** python 3.13; astropy/lightkurve/numpy per requirements.txt; candidates rendered by cygnus.reporting.dossier
- **run:** python -m cygnus.multi run campaigns/toi-7610-01.yaml ; python -m cygnus.campaign vet campaigns/toi-7610-01.yaml

#### 7. Follow-up

Trace the SIMBAD SB* classification to its primary evidence; redo S88/S99 difference imaging and centroid time series with PRF, registration and aperture variations; seek phase-spread RV and a clean independent epoch. Do not promote while localization is unresolved.

---
*Generated from ledger/candidate records only; any field the evidence does not support renders '(none recorded)' rather than a fabricated value.*
