# Soma-matched full-clock physiological diagnostic — V1

Specified 2026-10-21 before new fluorescence-response extraction or model fitting.
This diagnostic addresses identifiable limitations of the earlier comparison;
it does not supply missing frame-exact retinal movies or validate the functional
image frontend. No neural graph, gain or time constant is calibrated here.

## Eligibility and splits

Use cached author MATLAB recordings from [Erginkaya et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12148931/).
Include immobilized HS, H2, bIPS and DNp15 native controls plus explicitly labeled
bIPS/DNp15 RdlFlpStop-WT controls, keeping WT background separate. Exclude mutant
and tetanus manipulations. Require explicit soma L/R, axon/dendrite metadata,
13-s epochs [2,4,9,11,13], and at least one of the three exact standard 20-px/s
protocol labels (yaw, progressive, yaw-right-flipped). Prefer corrected over
uncorrected versions of the same session basename; retain exclusions in a ledger.
Do not use response amplitude/direction to choose recordings.

Keep existing neural-calibration flies in development and existing validation
flies in testing. Cohorts are neuron class × reporter (sytGC7f, GC7f, GC6f) ×
recorded compartment × native/WT background. When a cohort already contains
development flies, assign all additional eligible flies to testing. Otherwise
sort independent fly IDs by SHA-256 and assign the first half to development,
the remainder to testing, always protecting existing validation flies. If a
cohort has protected validation flies and no old development fly, take at least
one additional fly for development when available. A fly never crosses partitions. Small cohorts remain
explicitly weak evidence; no pooling across a reporter/background to create a
favorable result. Record which test flies were already scored in the earlier
diagnostic, and which are previously unused. Source metadata determines splits
before any new response extraction.

## Input and cell readout

Reuse the three saved, signed analytic flow-clamp vectors, at their existing
normalization, for first/second motion epochs. Insert them into full 13-s
still/motion/still/reversed-motion/still protocols, with zero clamp outside
[2,4) and [9,11). This explicitly bypasses retinal images and has signed input
units unlike the nonnegative functional frontend. It is a conditional circuit
diagnostic. Preserve source IDs, graph counts, gains and 1-ms solver/10-ms record
clocks. Test original and expanded chemical circuits with identical inputs.

Read the model cells whose **soma side** matches the recorded soma, averaging
within the stated class only. Do not pool hemispheres, flip observed data to
improve agreement or select an individual modeled HS subtype after scoring.
This is an explicit single-compartment/population readout assumption, not
evidence that a model node reproduces the imaged neurite's local dynamics.

## Recorded fluorescence and observation calibration

Use F_All with author-selected one-based ROIs and PatsOrdered. Use each file's
actual TimeAxis. Baseline indices are the nearest sampled times to 1 and 2 s,
inclusive; standardize each trial/ROI using its measured baseline mean and sample
standard deviation (ddof=1). Reject only nonfinite/zero baseline variance or
traces with less than 95% finite samples over 0–13 s; require two usable trials
per recording/protocol. Preserve every rejected unit and reason. This estimates
measurement variability from recordings; it adds no noise to neural dynamics.
Average trials and selected ROIs, retaining empirical uncertainty and all source
identities. Give each fly equal total calibration weight, then equal recording/
protocol weight within fly. Retain actual clocks rather than compress epochs.

The observation model is a nonnegative scalar gain times one or two causal
first-order filters of either signed rate or its positive part. Fixed candidate
time constants are 0, .05, .1, .2, .4, .8 and 1.6 s (ordered pairs, zero bypasses
a stage). This is a phenomenological measurement model calibrated from data,
not an assertion of measured GCaMP kinetics. Filter using preceding input holds;
interpolate predictions to recorded times. Select candidates and gain using
development-only mean-squared error over 1–13 s; break ties by fixed candidate
order. Do not fit negative gain, per-test-fly scale/offset or neural parameters.
Report all candidate development losses and unidentifiable zero-gain fits.

Primary comparison transfers the original circuit's fitted observation model to
the expanded circuit. Secondary comparison fits each circuit's observation model
on the same development flies. Fit records must be written before test scoring.

## Outcomes and interpretation

Report per-fly full-trace RMSE/MAE and improvement versus a zero-baseline predictor,
motion-window errors, first-versus-second epoch response signs, and normalized
progressive/yaw discrimination wherever both protocols and nonzero denominators
exist. Use the last 0.5 s of each motion epoch for the latter endpoint. Define
each protocol's contrast as first minus second epoch, without class-specific
sign flips. The normalized progressive-versus-yaw contrast index is explicitly
not a reproduction of the published Figure 3e statistic. Report
undefined ratios rather than silently substituting zero. Estimate uncertainty
by resampling flies, retaining repeated recordings together. Preserve all
negative findings, small-cohort uncertainty and prior-test reuse.

This benchmark can test conditional prediction of recorded summaries under
declared input/readout/measurement assumptions. It cannot establish frame-exact
image-to-calcium validation, local neurite physiology, electrical connectivity,
or robustness during active walking (these recordings are immobilized).
Any improvement in this diagnostic must not be called full biological validation.
