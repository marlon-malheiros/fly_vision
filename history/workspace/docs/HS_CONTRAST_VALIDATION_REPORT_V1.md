# Frozen-circuit HS contrast-response physiological benchmark V1, source correction R2

2026-11-02. **The completed comparison is in disagreement with the descriptive simultaneous band. Full biological validation is not established.** The successful small-turn simulation detector, connectivity, functional frontend and neural parameters are preserved unchanged. This study evaluates neurons against published recordings, independently of the artificial turn classifier.

## Main result

Under the source-supported order correction, current LPi-intact HS has **4/8** prespecified lower-contrast endpoints outside the descriptive joint recording-row band; normalized RMSE **0.39100**. The maximum standardized discrepancy is 21.7451, versus the source-bootstrap joint critical value 2.7491. This comparison tests normalized response shape, not calibrated membrane voltage or an animal's 2-degree/s threshold.

| Contrast | Recorded PD | Model PD | Recorded ND | Model ND |
|---|---:|---:|---:|---:|
| 10% | 0.24956 | 0.00448 | 0.04825 | -0.00034 |
| 25% | 0.72515 | 0.04016 | -0.05160 | -0.00315 |
| 50% | 0.91377 | 0.21846 | -0.05095 | -0.01733 |
| 75% | 0.97534 | 0.53895 | -0.16144 | -0.04288 |
| 100% | 1.00000 | 1.00000 | -0.33010 | -0.07968 |

All values are divided by that system's full-contrast PD mean. The positive scale is anchored once; no gain, offset, sign, timing, adaptation, connectivity or physiological parameter was fitted to the lower contrasts. All 120 source values, all twelve rows per direction, every phase/subtype, alternative display and observation are retained. No quiet or unusual recording was excluded.

![Corrected recording/model contrast curves](../results/hs_contrast_validation_v1/corrected_hs_contrast_comparison.png)

## A material source correction, not a silent rewrite

The earlier [HS full-contrast comparison](HS_VOLTAGE_BENCHMARK_REPORT_V1.md) used worksheet 5l's column labeled 100%. This study discovered that the worksheet headers ascend while the pinned author export/plot axes run high-to-low. The published Fig. 5l agrees with reverse-order source means, not the literal label order: the fixed raster check has RMSE 0.220 versus 2.419 mV under a common source-only scale of 100. Pixel error bars and coarse sampling limit that digitization; it is an order check, not exact voltage reconstruction.

Source-supported interpretation: worksheet columns B:F correspond to 100,75,50,25,10%. Raw recording stimulus logs and the exact five-level projector LUT remain unavailable, so this is explicitly conditional rather than an author-confirmed relabeling. The source numbers and sealed earlier reports are untouched. The old +0.19333 ND/PD result is reproducible for the **100%-labeled** column, but no longer supports a true full-contrast biological comparison. The corrected full-contrast ratio is -0.33010. See the [correction protocol](HS_CONTRAST_SOURCE_CORRECTION_PROTOCOL_R2.md) and [source audit](../results/hs_contrast_validation_v1/source_correction_r2/source_order_figure_check.json).

The original V1 literal-header analysis also remains: 4/8 violations, RMSE 2.51649. It is source-confounded, not an additional valid biological failure. R2 was frozen after seeing the biological source discrepancy and before scoring any new model response; all source values were then inspected. Neither R2 nor the repeatedly used paper is described as a blind biological discovery or new animals. Commits `3a167f9` and `67d69a0` preserve these two decision stages.

As a secondary full-contrast control, corrected ND/PD is -0.33010, with descriptive independent-row interval [-0.46434,-0.22405]. The old broad interval therefore should not be reused for this corrected full-contrast target. This control was not added to the eight-coordinate primary decision after seeing model results.

## Complete fixed comparisons

| Circuit | Display assumption | Endpoints outside band | Normalized RMSE | Conditional compatibility |
|---|---|---:|---:|---|
| original_frozen | methods85_4bit | 5/8 | 0.39994 | False |
| original_frozen | figure90_4bit | 5/8 | 0.40004 | False |
| original_frozen | methods85_continuous | 5/8 | 0.38490 | False |
| expanded_pre_LPi | methods85_4bit | 5/8 | 0.39997 | False |
| expanded_pre_LPi | figure90_4bit | 5/8 | 0.40007 | False |
| expanded_pre_LPi | methods85_continuous | 5/8 | 0.38493 | False |
| LPi_intact | methods85_4bit | 4/8 | 0.39100 | False |
| LPi_intact | figure90_4bit | 4/8 | 0.39094 | False |
| LPi_intact | methods85_continuous | 4/8 | 0.37489 | False |

The separately frozen descriptive contrast diagnostic compares the continuous-display curve with the inherited frontend's analytic squared-contrast prediction. Rectified contrast and its linear delayed signal each scale with contrast around neutral grey; their product scales with contrast squared before clipping/routing. Current LPi PD/ND curves differ from that squared-contrast shape by at most 0.00117479 after each direction's own full-contrast normalization. This diagnostic fits no coefficient. The largest saved wide-cell rate is 0.0333869, consistent with weak nonlinear saturation in these equations. These facts motivate examining contrast processing and the measurement mapping, rather than another classifier threshold change. They do not uniquely locate biological contrast gain control or determine a justified repair. [All diagnostics](../results/hs_contrast_validation_v1/interpretation_diagnostics.json).

Primary: LPi-intact, methods85_4bit, right HSN/HSE/HSS equal mean, x=atanh(rate), full two-second response, independent PD/ND row resampling. Other graphs are fixed controls, not a post-score model search. First-half-second, rate, individual subtype and unverified row-paired summaries are available in the [complete comparisons](../results/hs_contrast_validation_v1/source_correction_r2/curve_comparisons.json). Display and subtype uncertainty cannot be removed by choosing the best curve afterward.

## Measurement and numerical limits

Pokusaeva et al. (2024) [published methods and source data](https://www.nature.com/articles/s41467-024-53173-w) define a square-wave grating, nominal 0.04 cycles/degree, 1 Hz, two seconds static/two moving/one static. The source caption supplies the temporal frequency. The projector refresh is 60 Hz with four-bit luminance; retinal/source/solver steps are 5/10/1 ms. The two fields bracket missing exact registration; unquantized luminance brackets the unresolved LUT. Ten-percent nominal contrast becomes approximately 6.67% under our declared four-bit rounding. Real luminance calibration is unknown. The nominal grating speed is 25 degrees/s image motion, not body yaw or a walking trial.

Bootstrap rows as whole five-column vectors, independently within PD and ND, with a separately reported unverified paired sensitivity. No animal IDs establish independent animals or true PD/ND pairing. Simultaneous bands are descriptive row-resampling uncertainty, not verified animal-level confidence, equivalence margins, or individual response prediction intervals. A mismatch can involve frontend/circuit, subtype mixture, display, or observation assumptions; a compatible curve alone would not validate the full system.

Completed 144 input slots: 120 main, six stationary, eighteen refinements; 16 full-contrast slots reuse prior observations. There are 384 new main/control/refinement graph solves plus six graph solves for two exact replay cases. Numerical checks pass **27/27** under the frozen response/normalization tolerances:

| Refinement | Checks passed | Largest normalized change |
|---|---:|---:|
| spatial | 9/9 | 0.000384569 |
| temporal | 9/9 | 0.00094548 |
| solver | 9/9 | 3.17303e-10 |

The half-degree check also changes the discretization of a fixed physical pooling-center radius; it is not an exact same-quadrature solver test. Preserve every numerical failure and avoid an unrestricted convergence claim. All six stationary controls and all pre-motion baselines are zero within 1e-12.

Independent implementations check 120 raw XLSX cells, 5184 response values via log1p (maximum error 2.08e-17), 288 literal and 288 corrected curve comparisons, and both 10,000-draw bootstrap schemes. Weighted-sum bootstrap disagreement is at most 1.07e-14. Two prespecified legacy replays reproduce images, inputs, neural rates, final states and checkpoints bitwise; the frozen detector files and graph arrays remain identical. Numerical review success does not imply physiological success.

Observation plus replay CPU 3685.36 s, below 7,200. Outputs before completion copies 37.46 MB, below 256 MiB. No movie or full T4/T5 state archive, no duplicate source ZIP, no parameter optimization. Initial restricted-network failures are retained; public-source retrieval succeeded. See [execution and checks](../results/hs_contrast_validation_v1/independent_review.json), [corrected checks](../results/hs_contrast_validation_v1/source_correction_r2/independent_review.json), [all numerical results](../results/hs_contrast_validation_v1/numerical_sensitivity.json).

## What this means for the full circuit

| Component | Evidence already available | Remaining limit |
|---|---|---|
| HS | This executed multi-contrast test; older scalar benchmark now explicitly corrected | Response shape, observation scale, subtype and display constraints; no complete validation |
| H2 | [Earlier direction-tuning benchmark](H2_FROZEN_MODEL_BENCHMARK_REPORT_V2.md): original model mean PD error 16.72 degrees vs 13.76-degree body-horizontal reference, median shape correlation 0.69 | Approximate moving-edge replay; original graph, known source animals; not validation of current LPi graph or walking thresholds |
| bIPS | [Known Erginkaya comparison](HORIZONTAL_OPPONENCY_REPORT_V1.md): LPi magnitude index +0.15382 vs recorded +0.15599 | Mean waveform skill worsens from +0.45738 to +0.32544; inspected recordings, missing exact G3 stimulus arrays |
| DNp15 | Same known study: LPi median skill +0.37853; negative null-yaw mean restored | Pooled skill worsens to +0.27114; index -0.64982 vs measured -0.26170; no independent matched small-turn recordings |

Do not rerun these known downstream assays and call them fresh validation. Electrical conductances, unresolved homolog identities and physiological parameters are not invented. No biological bIPS causal mechanism is proved, and the readout's direct T4/T5 access remains an artificial analysis choice.

## Undergraduate explanation and next decision

We want the simulated neurons to respond like real fly neurons, while preserving their ability to signal small turns. We tested a different property from turn classification: how the neurons change their response when the moving stripes become faint. We also caught a source-label inconsistency that made the earlier comparison unreliable at its claimed contrast. Correcting that interpretation is necessary before deciding whether the circuit matches the measurements. A successful turn classifier cannot repair a disagreement in the neurons that feed it.

This milestone completes the fixed physiological **test**, not physiological validation of the whole model. Keep the detector frozen and use the demonstrated response discrepancies to specify a separately versioned, biologically constrained frontend/observation revision or seek a better calibrated independent dataset. Do not launch another classifier sweep or invent synapses to make this benchmark pass. Any fitted biological revision needs separate calibration and independent validation, followed by the unchanged walking tests.

Use the [isolated reproduction commands](HS_CONTRAST_REPRODUCTION_V1.md), [frozen protocol](HS_CONTRAST_VALIDATION_PROTOCOL_V1.md) and [R2 correction](HS_CONTRAST_SOURCE_CORRECTION_PROTOCOL_R2.md). Existing sealed destinations intentionally reject writes. Use the read-only audit command documented in the completion receipt for retained-file integrity.
