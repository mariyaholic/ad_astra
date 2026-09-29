# Search log — independent cached-TPF follow-up, 2026-09-27

The canonical TOI-7610 retirement is applied idempotently with `python reports/lead-followup-2026-09-27/retire_toi7610.py`. It removes only the active candidate row, preserves measurements and prior-art history, and records `campaigns/toi-7610-01/REJECTION.md` as the durable reference.

This is a finite re-reduction of 12 already retrieved SPOC TPFs for four named leads. It is not an independent epoch, an all-archive search, or a new MAST discovery. No source FITS file was modified or moved.

## Input products

| Lead | TPF filename | Sector | Bytes | SHA-256 |
|---|---|---:|---:|---|
| TOI-224.01 | `tess2018234235059-s0002-0000000070797900-0121-s_tp.fits` | 2 | 48,355,200 | `A216CE5334B9548BEB6137D7D1F97BBD5AD7CDF1BCFBEFD7CB5D1820B47BED1E` |
| TOI-224.01 | `tess2020238165205-s0029-0000000070797900-0193-s_tp.fits` | 29 | 46,218,240 | `C53F5BFC72EE2FA974D717BED8528FF4DA206ED171626BEE3322F9A6174B3D4A` |
| TOI-224.01 | `tess2023237165326-s0069-0000000070797900-0264-s_tp.fits` | 69 | 45,495,360 | `E6D1B5738B43DE6FA95BFC86FA6D22EF84D7CF2E26A00E11A9E3252096CD8052` |
| TOI-224.01 | `tess2025232030459-s0096-0000000070797900-0293-s_tp.fits` | 96 | 45,293,760 | `00FFB20B5287A817B6FA05ECDAA29FC36E5971DB113C1EE31E9414956D9E1A39` |
| TOI-224.01 | `tess2026192185000-s0106-0000000070797900-0308-s_tp.fits` | 106 | 50,184,000 | `3DF0FFA33FCE53A78FBD44FC495AD63834ADA8F17DED240C0C1C89F3F573BD0F` |
| TOI-2666.01 | `tess2021039152502-s0035-0000000170889511-0205-s_tp.fits` | 35 | 52,012,800 | `7BF671F85BF7D8EBEF001C30B6A1AAA8FD0355A86D51FB746AB9C65E7A8580B9` |
| TOI-2666.01 | `tess2026005125623-s0099-0000000170889511-0300-s_tp.fits` | 99 | 57,574,080 | `77CBE1764AD84D32D653200972CE0725C1E984E5E35A542EE3537A7413A3F059` |
| TOI-3500.02 | `tess2023096110322-s0064-0000000443666343-0257-s_tp.fits` | 64 | 47,494,080 | `DAB6E7568827AD9A34D72001D1BF3E8200EFA852474FEA937D03B071FF32F52E` |
| TOI-3500.02 | `tess2025071122000-s0090-0000000443666343-0287-s_tp.fits` | 90 | 49,256,640 | `772E4D5E4D75DF82D563F3238AD978FA81FD1AFCF9B0AE2B1F46D834973C5027` |
| TOI-3500.02 | `tess2026060005000-s0101-0000000443666343-0303-s_tp.fits` | 101 | 46,094,400 | `3C607E6CD7A7DA0371AA562A06B089AD3A910129CDAF069DEC375316E3A0D38C` |
| TOI-7610.01 | `tess2025014115807-s0088-0000000121341000-0285-s_tp.fits` | 88 | 48,997,440 | `4BAF947215854D36E2CC2D46C2FE43C1D3D68E454328E4874794585122A3CF65` |
| TOI-7610.01 | `tess2026005125623-s0099-0000000121341000-0300-s_tp.fits` | 99 | 48,807,360 | `1C5357DC2B6C61AC867ACAA7C23406C255A996996C116ED74B91CCC00AA4AA7C` |

The files are cached at `D:\AO_Artifacts\cygnus_scratch\` and are not repository inputs. The campaign sky records retain the corresponding light-curve product provenance. The input paths are intentionally recorded here so a later agent can verify the cache before reusing it.

## Selection and calculation

- Source: MAST TESS SPOC target-pixel files listed above; the exact archive product IDs are the filenames.
- Time: FITS `TIME` plus `BJDREFI/BJDREFF`, treated as BJD_TDB as declared by the SPOC campaign records.
- Quality: `QUALITY == 0`; all TPF pixels in a cadence must be finite.
- Event: `abs(time - mid_bjd) <= 0.4 * duration_days`.
- Flank: `duration/2 + 1/48 d < abs(time - mid_bjd) <= duration/2 + max(duration, 0.25 d)`.
- Baseline: per-pixel linear fit to flank cadences, evaluated across event cadences.
- Apertures: `APERTURE & 2`, `APERTURE & 8`, all low four aperture bits, and a 2-pixel circle around the WCS target pixel.
- Localization: positive event-minus-baseline local-peak centroid compared with the local-peak control centroid; 300 bootstrap resamples of event and flank cadence indices, seed `20260927`; TESS pixel scale 21 arcsec.
- Output: `independent_tpf_results.json` records every aperture, event/flank cadence count, descriptive depth, centroid, bootstrap scatter, and caveat.

The local-peak metric is deliberately compared with the stored vetting metric. A significant displacement is evidence that the target localization failed; it does not identify a specific contaminating object without a PRF/WCS registration model. The broad all-designated mask is retained for sensitivity context but is not used as a decision mask.

## Scope and nulls

Screened: 4 targets, 12 target TPFs, 12 listed event/control windows, 48 aperture/event combinations and 300 bootstraps per combination. No event is promoted by this reduction.

## Exact catalog follow-up

`catalog_followup.py` queried the official Gaia Archive TAP service and SIMBAD
TAP service on 2026-09-27. `catalog_followup.json` records the UTC retrieval
time, endpoint, exact ADQL, response metadata and rows. The Gaia query refreshed
DR3 astrometry for source IDs 3471495415361216512, 3471495419656596352 and
3071787586789910144. Four exact-source NSS tables were tested for TOI-7610:
`nss_two_body_orbit` returned one SB1 row; `nss_non_linear_spectro`,
`nss_acceleration_astro` and `nss_vim_fl` returned zero rows. SIMBAD identity
and bibliography queries returned the matching UCAC4/2MASS/WISE identifiers and
the Gaia DR3 stellar-multiplicity paper (`2023A&A...674A..34G`).

The SB1 row contains 23 accepted of 23 considered RVs, P = 90.422418 ±
0.380457 d, e = 0.309317 ± 0.095243 and K1 = 12.140633 ± 1.314917 km/s.
`toi7610_sb1_check.py` used those fields and the campaign mass prior in 200,000
Monte Carlo draws with seed 20260927. It records the direct mass function and
conditional sin(i)=1 companion mass in `toi7610_sb1_results.json`.

## TOI-3500 two-source sensitivity grid

`toi3500_two_source_test.py` reused only the listed S64 and S90 TPFs and the
refreshed Gaia DR3 positions. It compared target-only, neighbour-only and joint
pixel-integrated circular-Gaussian templates over FWHM 0.8–2.0 pixels and common
registration shifts {-0.1, 0, +0.1} pixel in x/y, fitting a planar background
and flank-derived per-pixel noise. The two sources are separated by only
0.183–0.185 pixel. Target-vs-neighbour preference changes sign across the grid
and residualized template correlations span 0.934–0.986, so the source split is
inconclusive. The target is favored in 71% of S64 trials and 86% of S90 trials;
those fractions are descriptive sensitivity counts, not probabilities.

Still untested by this work: new MAST sectors, FFI/HLSP products, ground
photometry, a calibrated sector/camera/CCD TESS PRF, registration covariance,
high-resolution time-series imaging, new RVs, search-wide false-alarm
calibration and injection–recovery for later predicted epochs.
