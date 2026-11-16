# One calibrated HS gain-control revision and frequency transfer V1 (missingness recovery R2)

2026-11-02. **This candidate does not pass the complete physiological advancement rule.** The original frontend, MaleCNS graphs, time constants, successful small-turn detector and all previous results remain unchanged. This separately versioned candidate calibrates one upstream functional gain parameter from known physiology, with no walking-label fit or classifier optimization.

## Findings

At 50% contrast the recorded preferred response is **91.4%** of full contrast, baseline **21.8%**, candidate **94.8%**. The candidate's two unfit PD50/75 coordinates both inside the declared seven-coordinate joint band: **True**. This is a response-shape improvement on known measurements excluded from fitting, not new animal-level validation. The full seven-coordinate gate includes all opposite-direction contrasts, so a preferred-direction improvement cannot hide a directional failure.

| Assay | Frontend | Coordinates outside joint band | Normalized RMSE | Conditional compatibility |
|---|---|---:|---:|---|
| contrast | baseline | 3/7 | 0.32874 | False |
| contrast | gain_control | 1/7 | 0.10389 | False |
| frequency | baseline | 15/15 | 0.79786 | False |
| frequency | gain_control | 15/15 | 0.80264 | False |

The independently scored frequency dataset has a peak at **0.5 Hz** on its sampled grid. Baseline peak: **5 Hz**; gain-candidate peak: **5 Hz**. These are grid maxima, not fitted preferred frequencies. No temporal parameter, lag, sign, gain or source order was changed to match those outcomes. Full-contrast opposite/preferred ratios are recorded **-0.33010**, candidate **-0.08009**. Contrast compression and direction opponency are distinct response properties.

![Calibration and independent-condition transfer](../results/hs_gain_transfer_v1_r2/gain_and_frequency_transfer.png)

## Biological motivation and exactly what was fitted

[Drews et al. (2020)](https://doi.org/10.1016/j.cub.2019.10.035) support a fast, spatially pooled contrast-compression mechanism upstream of T4/T5. We test that computational principle rather than adding unmeasured anatomical neurons or electrical conductances. Local rectified ON/OFF image contrasts u are divided by sqrt(sigma^2+E), with E the mean contrast energy over the inherited seven-degree footprint; multiplying by sqrt(1+sigma^2) preserves a homogeneous full-contrast reference. Normalization precedes the unchanged delay and motion correlation. It is causal and receives only images. The shared ON/OFF operation, instantaneous gain and inherited spatial footprint remain phenomenological assumptions; the circuit is not a reconstructed measured upstream neural population.

Exactly one semisaturation **sigma=0.121902688** is fit to the already known corrected PD10/25 ratios, using PD100 as a common positive observation reference and actual quantized contrast. Independent derivative root finding differs by 2.16e-11; no network-response refit follows analytic calibration. The homogeneous-grating objective is 0.00047274574. PD50/75, every ND and all frequency values are excluded from this fit. The measured-curve ratios fit a functional parameter, not a biological conductance. Published [Matulis et al. (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7003801/) physiology also shows heterogeneous temporal adaptation, so this simple shared gain does not establish the full biological computation.

The neural graph and all neural time constants are frozen; the upstream hypothesis changes the new candidate's input and thus its neuronal responses. The original working detector is preserved but its performance does **not** automatically transfer to this different frontend. Final source forcing is clipped to the inherited [0,1] interface; total clipped target-time entries: **0**. No sign swap or truth-label access.

## Calibration versus testing and source limitations

The known 5l contrast dataset uses the documented [source-order correction](HS_VOLTAGE_SOURCE_CORRECTION_R2.md), not a new relabeling. Its validation coordinates are PD50/75 plus ND10/25/50/75/100 (seven total). These data were previously inspected and are explicitly retrospective condition transfer. A new numerical frequency target is extracted from official Source Data 5.xlsx sheet 5m **after the fitted parameter freeze**. All 16 direction/frequency points except normalized PD1Hz enter its 15-coordinate primary vector. The frequency figure's qualitative shape was already viewed; source-family selection and unknown cell overlap mean this is not fully blind discovery or verified independent animals.

Pinned author velocity code groups ascending unique speeds, consistent with 5m headers. The source-only mean peak 0.5 Hz agrees with the published qualitative 0.5–1 Hz peak range; no column reversal or model-dependent source choice. Contrast and frequency curves use their own PD reference means to avoid an unverified absolute voltage scale between assays. Whole source rows are independently resampled within PD/ND, 10,000 draws, seed 2026110204, preserving within-row covariance. Simultaneous bands are descriptive recording-row bands, not individual prediction intervals, equivalence margins or verified animal-level confidence. Every source value and criterion remains fixed.

The model display/stimulus family retains 0.04 cycles/degree square-wave gratings, 60-Hz/four-bit presentation, two static/two moving/one static seconds, original retinal registration and model x=atanh(rate) proxy. All four phases are used for contrast; two phases for frequency, with fixed figure90 sensitivities at 0.5/15 Hz. Unknown projector LUT, exact raw trial histories, subtype mixture, biological observation mapping, animal IDs and missing electrical interactions remain limitations. The membrane proxy is not calibrated mV. Individual subtype/rate/initial-window sensitivities are retained; no favorable one replaces the primary mean.

## Preserved preparation failure and correction

Initial V1 target extraction rejected four blank 5m entries (PD row2 and ND row34 at 0.1/5 Hz), because it assumed complete rows. The subsequent attempted dependent launch rejected its missing target freeze. **No neurons were simulated in the failed attempt.** Both logs, hashes, fitted model and source missingness audit remain in `results/hs_gain_transfer_v1`, with copies in this completion archive. The [R2 missingness amendment](HS_GAIN_TRANSFER_MISSINGNESS_AMENDMENT_R2.md) was frozen before finite frequency summaries or any neural output, retaining the identical sigma and scientific rules. It keeps all twelve recordings and all four explicit blanks, with 11 observed rows at those two frequencies and 12 elsewhere. No imputation, quiet-cell exclusion or favorable source substitution. Available-case means and whole-row bootstrap preserve the missingness pattern; nonrandom missingness remains an uncertainty. Independent XML/mask arithmetic checks all 312 entries: 308 finite values and 4 blanks.

## Numerical checks, reproducibility and storage

Completed 98 shared image slots: 40 contrast, 32 main frequency, eight display sensitivities, sixteen numerical refinements, two stationary controls. New network solves: 98 candidate and 50 baseline; 48 baseline rate cases reused bitwise from the preceding assay. Two independent full source-to-neuron baseline replays additionally verify images, input hashes, rates, final states and checkpoints. Four focused tests cover literal local normalization, causal prefix/reset/stationary behavior, one-parameter fitting, disjoint scoring and missing-value bootstrap parity. Numerical endpoint checks pass **22/26** with unchanged tolerances. All stationary/baseline rates remain zero within 1e-12. New gain-footprint spatial convergence is not established; inherited baseline spatial checks do not prove it.

| Failed time-refinement case | Frontend | Error / primary PD reference |
|---|---|---:|
| frequency_x2.5_d0_p0_methods85_temporal | baseline | 0.09083 |
| frequency_x2.5_d0_p0_methods85_temporal | gain_control | 0.09052 |
| frequency_x15_d0_p0_methods85_temporal | baseline | 0.06132 |
| frequency_x15_d0_p0_methods85_temporal | gain_control | 0.06273 |

The 2.5/15-Hz preferred-direction endpoints are sensitive to halving the image/input step in both frontends. These failures prevent claiming convergence across the full frequency bank or treating its exact peak/error counts as numerically certified physiological results. The contrast and other frozen numerical checks remain reported individually; no failed tolerance is relaxed, and no additional smoothing/time-constant adjustment is selected after the test. The primary 15-coordinate disagreement is a conditional output comparison, with these numerical limitations alongside stimulus/observation uncertainty. Calibration success does not override either biological or numerical advancement gates.

Independent XML, weighted available-case bootstrap, derivative-based calibration, log1p observations and every decision pass arithmetic review. It verifies 2352 response entries (maximum error 6.94e-18), all 64 curve comparisons and all numerical checks. Bootstrap maximum discrepancy 8.88e-16. Observation plus replay CPU **2743.63s**, below 3,600. Output before completion copies **22.89 MB**, below 128 MiB. No movies, duplicate source ZIP, full-state archive or previous artifact overwrite. [Independent review](../results/hs_gain_transfer_v1_r2/independent_review.json), [all response curves](../results/hs_gain_transfer_v1_r2/comparisons.json), [numerics](../results/hs_gain_transfer_v1_r2/numerical_checks.json), [fixed display sensitivity](../results/hs_gain_transfer_v1_r2/display_sensitivity.json).

Source checkpoints `76a7b63` (original pre-calibration design) and `19da6ed` (missingness recovery) preserve the decision stages. Reproduce original recovery CLI stages `prepare`, `calibrate`, `targets`, `run`, `analyze` only in an isolated project copy/new result namespace with retained dependencies. Existing destinations intentionally reject writes. Review with `scripts/review_hs_gain_transfer_v2.py review`; final completion uses this report's companion finish script. A second full experiment is not claimed: the independent exact replays and source/target arithmetic are the executed reproduction checks. Read-only post-exit audit: `scripts/finish_hs_gain_transfer_v1.py audit` using the scientific interpreter and `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`.

## Decision and undergraduate explanation

Walking advancement flag: **False**. The complete physiological gate must pass before testing unused walking rooms or changing readout training. No full biological validity, real-fly small-turn threshold, biological bIPS causality or closed-loop control is established.

We want a model that both notices small turns and responds like real fly neurons. We added one biologically motivated sensitivity adjustment so faint motion does not become unrealistically weak. Only two known preferred-direction measurements set its strength; different contrast/direction conditions and frequency responses test what it predicts afterward. A successful calibration addresses one problem but cannot guarantee the model's direction or timing is correct. This experiment measures those properties separately and keeps every failure visible.

The next decision must follow the reported discrepancies. A further revision would need justified constraints on remaining direction opponency and/or temporal filtering, with separate calibration and another independent test; raising decoder gains or quietly fitting the just-tested frequency data cannot supply independent validation. The baseline small-turn result and all unused rooms remain preserved.
