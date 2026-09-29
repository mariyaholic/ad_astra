# Independent cached-TPF follow-up — 2026-09-27

## Bottom line

The four leads surviving the first errata pass were remeasured from cached target-pixel files with a separate aperture and pixel-difference implementation. Follow-up then queried the exact Gaia/SIMBAD rows for TOI-7610 and ran a bounded two-source separability test for TOI-3500. Three active Unverified leads now remain:

- **TOI-224.01 remains an Unverified lead.** S29, S69 and S96 remain near the out-of-transit source centroid under the optimal aperture; S106 E4 independently reproduces the displaced difference source at **8.70 arcsec and 8.60 bootstrap sigma**. E4 is rejected as target localization evidence, while the other three events do not by themselves establish a planet or a unique period.
- **TOI-2666.01 remains an Unverified lead, but localization survives this reduction.** S35 and S99 have optimal-aperture local-peak offsets of 0.50 arcsec/0.16 sigma and 0.37 arcsec/0.74 sigma. The planet-versus-grazing-binary question remains unresolved; multi-epoch RV is still the decisive test.
- **TOI-3500.02 remains an Unverified lead.** S90 E1 is on-source in the optimal aperture at 0.35 arcsec/0.65 sigma. S101 E2 independently reproduces the rejected off-source event at 6.74 arcsec/7.60 sigma, so it supplies no preference for the 350.31 d alias. A two-source Gaussian-PRF sensitivity grid favors the target in 71% of S64 trials and 86% of S90 trials, but the target/neighbour templates are strongly correlated (0.934–0.986) and the preferred source flips under allowed registration/width changes. This is suggestive for the target and remains inconclusive without a calibrated PRF or higher-resolution data.
- **TOI-7610.01 is retired as an exoplanet lead.** S99 E1 independently reproduces the 2.92 arcsec/5.71 sigma displaced localization. The former SIMBAD `SB*` flag is now traced to an exact Gaia DR3 `SB1` orbit: P = 90.4224 ± 0.3805 d, K1 = 12.14 ± 1.31 km/s, 23 accepted RVs. The measured mass function is 0.0144 solar masses and the conditional minimum companion mass is about 0.238 solar masses. The photometric anomaly is preserved, but the original target-planet reading fails both the host and localization gates.

No lead is promoted. TOI-7610 is retired from the candidate queue using the independent pixel failure plus the external Gaia RV orbit. The resulting route is: TOI-224 remains first for new coverage/host resolution; TOI-2666 moves to RV/independent-epoch work; TOI-3500 needs calibrated source separation or higher-resolution imaging.

## Method and limits

The script `reports/lead-followup-2026-09-27/independent_tpf_check.py` reads the cached SPOC TPFs without modifying them. For every listed event it applies `QUALITY == 0`, rejects cadences with non-finite pixels, selects an event window of 0.8 transit durations and a flank window matching the earlier vetting bounds, fits a linear per-pixel flank baseline, and forms an event-minus-flank difference image. Four fixed pixel selections are compared: TPF optimal-aperture bit 2, target-aperture bit 8, all designated aperture bits, and a 2-pixel target-centered circle. The reported localization uses the optimal-aperture local-peak centroid, with 300 event/flank bootstrap resamples and seed `20260927`; whole-aperture centroid results remain in `independent_tpf_results.json`.

The output is descriptive. It does not include a calibrated PRF fit, WCS registration uncertainty, a search-wide false-alarm probability, new pixels, a new sector, RV, or an independent sky epoch. The alternative masks are sensitivity checks; the broad `all_designated` mask includes non-target pixels and is not used as a source-localization decision. Depths from this extraction are not substituted for the campaign's calibrated light-curve measurements.

`catalog_followup.py` queried the official Gaia and SIMBAD TAP services on 2026-09-27. It records the exact ADQL, endpoint, retrieval time and returned rows in `catalog_followup.json`. `toi7610_sb1_check.py` computes the binary mass function and a 200,000-draw conditional minimum-mass distribution with seed 20260927. `toi3500_two_source_test.py` compares pixel-integrated circular-Gaussian templates at the refreshed Gaia DR3 target and neighbour positions over FWHM 0.8–2.0 pixels and common registration shifts of -0.1, 0 and +0.1 pixels, with a fitted planar background. That grid is an identifiability test, not a calibrated TESS PRF.

## Localization results

| Lead/event | TPF sector | Optimal-aperture depth (descriptive ppm) | Local-peak offset from control | Bootstrap significance | Disposition |
|---|---:|---:|---:|---:|---|
| TOI-224.01 S2 reference | 2 | 87,313 | 0.45 arcsec | 1.24 sigma | control; not a new event |
| TOI-224.01 E1 | 29 | 86,867 | 0.27 arcsec | 1.29 sigma | localized on source in this reduction |
| TOI-224.01 E2 | 69 | 86,944 | 0.52 arcsec | 3.84 sigma | sub-pixel offset; not failed by the angular rule |
| TOI-224.01 E3 | 96 | 83,368 | 0.35 arcsec | 2.66 sigma | localized on source in this reduction |
| TOI-224.01 E4 | 106 | 81,316 | 8.70 arcsec | 8.60 sigma | **failed localization; reject event for period evidence** |
| TOI-2666.01 S35 reference | 35 | 16,720 | 0.50 arcsec | 0.16 sigma | control; not a new event |
| TOI-2666.01 E1 | 99 | 16,871 | 0.37 arcsec | 0.74 sigma | localized on source in this reduction |
| TOI-3500.02 S64 reference | 64 | 6,890 | 7.43 arcsec | 2.13 sigma | control; source registration requires two-source fit |
| TOI-3500.02 E1 | 90 | 7,248 | 0.35 arcsec | 0.65 sigma | localized on source in this reduction |
| TOI-3500.02 E2 | 101 | 7,338 | 6.74 arcsec | 7.60 sigma | **failed localization; reject event for alias preference** |
| TOI-7610.01 S88 reference | 88 | 18,975 | 1.11 arcsec | 2.88 sigma | inconclusive localization |
| TOI-7610.01 E1 | 99 | 17,148 | 2.92 arcsec | 5.71 sigma | **failed localization; target origin not established** |

The descriptive depths differ from the PDCSAP/box-fit values because this check uses raw TPF flux and a simple flank baseline. They are included to make the computation auditable, not as revised astrophysical measurements.

## Lead dispositions and next discriminating tests

### TOI-224.01 — retain, but do not promote

The independent reduction confirms that the S106 event is displaced while S29/S69/S96 remain close to the control centroid. Keep the S106 event out of period fitting. Refit the 31.5798-day family using only the source-vetted events, then test later target-specific MAST products with injection recovery at the measured depth and duration. Resolve the host's Gaia RUWE 9.18 and obtain phase-spread RV before assigning a precise companion radius or planet interpretation.

### TOI-2666.01 — retain for RV/independent epoch

The S35/S99 source localization is stable under the new reduction. This does not distinguish a grazing planet from a stellar eclipse. Keep all 52 aliases, revisit the 316 ± 62 ppm phase-0.5 feature only where coverage exists, and search or obtain multiple RV epochs on HD 80133 with instrument offsets and stellar jitter. One RV visit remains insufficient.

### TOI-3500.02 — retain, source assignment still unresolved

The accepted S90 event remains on-source, while the S101 event is again displaced and cannot select P = 350.312 d. Gaia places the target and 3.74-arcsec neighbour only 0.183–0.185 TESS pixel apart. The Gaussian-PRF grid's best single-source fits favor the target, but source preference changes sign across the declared grid and residualized template correlations reach 0.986. The current TPFs therefore suggest, but do not establish, a target-sourced deficit. Use a calibrated sector/camera/CCD PRF or higher-resolution time-series imaging next; all 16 `700.6242/n` aliases remain open.

### TOI-7610.01 — reject target-planet interpretation

The S99 event's displaced localization is reproducible, while the S88 reference does not provide a clean on-source control. SIMBAD's `SB*` class traces to Gaia DR3 source 3071787586789910144 and a published SB1 solution with 23 accepted RVs, P = 90.4224 d, e = 0.309 and K1 = 12.14 km/s. The binary mass function is 0.0144 solar masses; under the campaign primary-mass prior, the sin(i)=1 companion minimum is 0.238 solar masses (16th–84th percentile 0.204–0.274). The TESS event interval is 4.0408 Gaia periods and does not securely identify the dips with that orbit. The former exoplanet dossier is nevertheless retired because the host is a stellar binary and the extra S99 deficit repeatedly fails localization. A future circumbinary/tertiary claim requires a fresh, on-source independent epoch.

## Reproduction and validation

Run from the repository root:

```text
python reports/lead-followup-2026-09-27/independent_tpf_check.py
```

The script expects the 12 cached TPFs under `D:\AO_Artifacts\cygnus_scratch\campaign_toi-{224-01,2666-01,3500-02,7610-01}\tpf\` and writes `independent_tpf_results.json`. Input filenames, byte sizes and SHA-256 hashes are listed in the search log. The calculation used Python 3.13.3, astropy 8.0.1 and numpy 2.3.4. The script completed successfully on 2026-09-27 and `python -m py_compile reports/lead-followup-2026-09-27/independent_tpf_check.py` passed. This report's sky record lists all tested and untested checks.
