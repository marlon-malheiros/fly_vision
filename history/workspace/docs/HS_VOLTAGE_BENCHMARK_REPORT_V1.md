# Limited independent HS voltage comparison V1

2026-10-30. **The source-data comparison is executed; this single constraint is inconclusive for model selection. Complete physiological validation is not established.** The prior download blocker is resolved. No new physiological parameter was fitted.

## What was actually compared

We acquired the official 156,151,246-byte source archive, 19,854,029-byte supplement and pinned author analysis code for [Pokusaeva et al. 2024](https://www.nature.com/articles/s41467-024-53173-w). Its published methods and qualitative findings were previously inspected; the numeric source responses used here were newly extracted after the [V2 protocol](HS_VOLTAGE_BENCHMARK_PROTOCOL_V2.md) froze. This is not a fully blind paper discovery or a new experiment on flies.

Source Data 5.xlsx, sheet 5l, 100% contrast: all twelve HS_FlpND_PD and all twelve HS_FlpND_ND recording rows. The stimulus family is a square-wave grating, nominal 0.04 cycles/degree and 1 Hz, with two static seconds, two moving seconds and one static second. The target is opposite-direction (ND) mean divided by preferred-direction (PD) mean. A common positive observation scale cancels; baseline-subtracted source values receive no fitted offset. Unknown row pairing/animal IDs prevent an animal-level confidence claim.

The initial unexecuted V1 target draft used the eight-direction panel, but the acquired generic plotting script has mismatched example parameters/window. Before reading any response values we selected the contrast panel whose caption specifies the frequency and duration. Both drafts and that decision are preserved. The paper's normalization description and current generic script also differ; the ratio avoids a common positive scale ambiguity without pretending that all preprocessing is recovered.

## Results and strength of evidence

The recorded ratio of means is **0.193333**, with independent-within-group recording-row bootstrap interval **[-0.170174, 0.901604]** (10,000 draws). The unverified row-order-paired sensitivity gives [-0.173332, 0.730542]. These are descriptive row-resampling intervals, not verified independent-fly uncertainty. All rows remain included, including the large positive ND response in spreadsheet row 36. The sheet alone does not establish that it is an artifact or justify removing it.

Three frozen circuits receive the same 16 primary image episodes (two display approximations, two directions, four phases). Eight fixed numerical-control episodes bring the total to 24 shared inputs and 72 graph solves. The model observation is baseline-subtracted x=atanh(signed rate), a graded membrane proxy with unknown positive scale. It is not a calibrated voltage measurement. The population comprises the three right HSN/HSE/HSS cells, equally weighted; HST is excluded. Phase/population means form the predicted ratio. No decoder or physiological gain is trained.

| Circuit | Display approximation | Predicted ND/PD | Recorded mean | Within recording-row interval |
|---|---|---|---|---|
| original_frozen | methods85 | +0.175178 | +0.193333 | True |
| original_frozen | figure90 | +0.177459 | +0.193333 | True |
| expanded_pre_LPi | methods85 | +0.175767 | +0.193333 | True |
| expanded_pre_LPi | figure90 | +0.178051 | +0.193333 | True |
| LPi_intact | methods85 | -0.079677 | +0.193333 | True |
| LPi_intact | figure90 | -0.082143 | +0.193333 | True |


![All source rows and circuit comparisons](../results/hs_voltage_benchmark_v1/figures/hs_recording_comparison.png)

All three predictions lie inside both row-resampling intervals. Thus this scalar constraint cannot select a circuit. The original model is closer to the observed mean point than the LPi model; the data do not establish a physiological improvement from adding LPi. LPi predicts a negative null response in this assay, whereas the measured group mean is positive with substantial uncertainty. Neither a preselected expected sign nor a favorable point estimate replaces the complete observed distribution. A compatibility interval this broad is weak evidence, not a demonstration that all circuit physiology is correct.

## What is matched, and what remains assumed

Nominal contrast, grating waveform/frequency, motion duration, display refresh (60 Hz), 4-bit luminance and baseline subtraction are specified. The two-second response is primary; the first half-second and rate-based observation are fixed sensitivities. Both display approximations are retained. The primary field spans 140 by 85 degrees, approximately centered at elevation 20 degrees; the second uses the plotted 90-degree elevation envelope. Exact projector LUT/pixel warp, angular registration and cell/animal identities were not recovered. Experimental subtype mixture is not known per source row. These limitations prevent a claim of exact experimental reproduction.

The functional T4/T5 surrogate, missing electrical coupling, and arbitrary model state-to-voltage mapping remain substantive biological limitations. The source archive supplies figure-level responses, not independently audited raw trial voltage and stimulus histories. This one HS response ratio does not validate DNp15, bIPS, yaw thresholds or walking behavior.

## Numerical and source audit

All 24 input cases retain zero static-baseline neural activity within tolerance. Halving image/input steps changes the phase-zero ratios by at most 0.000958992; halving the solver step, while retaining the one-millisecond forcing ramp, changes them by at most 5.16067e-11. These differences are small relative to the recording-row interval. Retinal pitch is the inherited one-degree grid; this assay does not establish convergence to arbitrarily fine retinal sampling.

An independent XLSX XML parser verifies all 24 used source values and both bootstrap intervals. Independent log1p-based observation arithmetic verifies all 864 saved cell/phase/window/observation response rows, maximum difference 2.09e-17. [Source rows](../results/hs_voltage_benchmark_v1/recording_rows.csv), [target](../results/hs_voltage_benchmark_v1/target.json), [all model responses](../results/hs_voltage_benchmark_v1/model_responses.csv), [all ratios](../results/hs_voltage_benchmark_v1/model_ratios.csv), [numerical sensitivity](../results/hs_voltage_benchmark_v1/numerical_sensitivity.csv), [independent review](../results/hs_voltage_benchmark_v1/independent_review.json).

Initial restricted-network and obsolete-host DNS failures remain archived. Reading the current publisher article exposed working media.springernature.com URLs; this solved access without contacting authors. An auxiliary article parser initially lacked BeautifulSoup and used standard-library parsing instead; no response or model result changed. There were no neural simulation failures, exclusions or data-dependent fitting.

## Undergraduate explanation and next decision

We finally compared a fixed model response with newly extracted published neuron measurements. The question was deliberately small: how strong is the response to opposite motion compared with preferred motion? The recordings vary enough that several different models fit this one broad constraint. That is a completed comparison with limited information, not complete biological validation or proof that the models are equivalent.

The next biological step should use stronger prespecified observations from the acquired archive, with verified display registration and recording identities where available. The alternative is an explicitly conditional multi-stimulus benchmark that retains those uncertainties; it must not select the best-looking stimulus after inspecting results. No additional physiological fitting or literature search is performed here. [False-alarm diagnosis](YAW_FALSE_ALARM_LOCALIZATION_REPORT_V1.md); [reproduction](YAW_HS_FOLLOWUP_REPRODUCIBILITY_V1.md).
