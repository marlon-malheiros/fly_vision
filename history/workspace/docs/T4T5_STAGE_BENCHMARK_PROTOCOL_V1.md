# T4/T5 intermediate direction-selectivity benchmark V1

2026-11-05. Freeze before reading control response amplitudes. Existing qualitative
paper findings, dataset metadata, Mi1 results and the failed HS integration are
known. This is a **conditional source-stage comparison**, not a full neural
circuit, small-yaw, or exact calcium-waveform validation.

Question: does the currently injected horizontal T4 representation retain the
preferred/null separation observed in control T4 recordings? Compare unchanged
measured-Mi1, adaptive-Mi1, and high-pass-removed source adapters. T5 uses the
existing slowing-only functional surrogate; no T5 biological reconstruction.
Import existing functions and fixed parameters; never refit them here. No
connectome, solver, neural state, classifier or old artifact is modified.

Sources: [Henning et al.](https://doi.org/10.7554/eLife.108529.3), pinned repository
`silieslab/C2C3_feedback_Henning` at
`745c6114b72a61dabc9389a1f024dbe22f679edf`, already audited in
[the suitability report](C2C3_DATA_SUITABILITY_REPORT_V1.md). Use only the control
ON file's T4A/B and OFF file's T5A/B. Keep all 11 inventoried controls, including
animals outside the source's seven-animal subset. Retain the existing 7 development /
4 holdout naming-group split; match by names, never array position. Empty layers
are missing, not zero observations. No response-based fly/ROI exclusions.

## Stimulus and observation assumptions

Article specifications: 5-degree bars, 20 degrees/s, 100-Hz display, approximately
80 by 55-degree field. The original processed files have no native clock,
stimulus generator, trial sequence or ROI receptive-field coordinates. Therefore
reconstruct one central horizontal transect, not a purported original movie.
The template was implemented only horizontally; do not invent its transverse RF.
No claim about vertical tuning, absolute anatomical PD, trial variability or
repetition reliability. Female recordings to MaleCNS is cross-sex transfer.

Use fixed 360-degree computational padding and an 80-degree visible aperture;
central readout, constant initial-image prehistory. Bar center moves -45 to +45
degrees from 1 to 5.5s; opposite motion is its exact spatial reflection.
Render full-contrast bright-on-dark / dark-on-bright as primary; grey-background
bright/dark bars are a separately reported ambiguity bracket, never selected to
rescue a result. Hard raster centers and 100-Hz sample-and-hold, not continuous
motion pretending to be the original display. Config specifies clocks/refinements.
The T4 adapter retains its existing contrast-energy normalization, 5.7-degree
Gaussian, 5-degree branch spacing, measured 250-ms-deconvolved filters, source
conductances and bounded positive fractional-voltage output. The adaptive bridge
retains LP54ms/HP318ms and its fixed source norm. T5 retains OFF44ms, delay30ms,
1-degree neighbor spacing and 7-position signed pooling before rectification.
This central-row reduction must be checked independently against the existing
2D T5 operations on synthetic vertically constant fields.

Primary observer is the published parallel-T4 port's positive voltage squared,
with stationary baseline subtraction; the scale cancels in selectivity. Linear
drive is a mandatory sensitivity analysis. Applying either proxy to T5 is an
assumption, not a measured GCaMP transfer. No extra calcium kernel or fitted gain.
For each direction, peak means maximum above pre-motion baseline over the full
reconstructed trajectory, floored at zero. Retain raw peaks and baselines too.

## Frozen analysis and decision

For every ROI, independently extract eight native trial-averaged direction peaks
(maximum over native time). As in source `Plot_allresp_relative.m`, choose the
maximum as PD and index+4 modulo8 as ND; circular ordering is inherited explicitly
from that code. Source arrays alone do not establish absolute screen angles.
Compute D=(PD-ND)/(|PD|+|ND|), with undefined denominators retained and counted.
No per-ROI min subtraction, which could manufacture perfect selectivity. Source
own-PD selection across eight directions differs from model selection across two;
this bias limits quantitative interpretation. Model PD is the larger of its two
horizontal peaks. Also report signed fixed-template contrast so own-peak alignment
cannot conceal wrong direction preference. A normalized PD/ND shape check cannot
validate absolute subtype direction or membrane hyperpolarization.

Average valid ROIs within animal and cell family, then animals equally. Retain
subtype, animal and ROI tables. Seven development animals define a simultaneous
95% bootstrap mean band for T4 and T5 (10,000 equal-animal resamples, seed in
config, max standardized deviation across the two families). At least three
animals per family and finite nonzero bootstrap dispersion required. This is a
predeclared compatibility screen, not a physiological equivalence margin.

Freeze all simulated predictions and development bands before any test scoring.
A T4 candidate advances only if primary squared/opposite-background D lies in
the T4 development band and all numerical checks pass. T5 can advance separately
under its own band; it cannot rescue T4. Only advancing candidates are scored
once on reserved animals, with the same independently computed simultaneous
bands. If none advances, stop and preserve all four holdout response sets.
Report all background/observer sensitivities, not the best one as the primary.

## Independent checks and resources

Test reflection, display timestamps, physical bar displacement/width, causal
prehistory, analytic selectivity, equal-animal weighting and constant-input T5.
Recompute all development native peaks/PD/ND/D in an independent Octave loop,
with explicit empty-layer handling; do not invoke source plotting code with its
known stale-variable hazard. Compare T5 reduction against existing 2D operations.
Refine time and space separately: peak error <=5% of each model's PD peak and
D change <=0.02. Verify source and prior-study retained-file indexes before/after.
Record exceptions, CPU/storage and failures. No interpretation of numerical
reproducibility as biological validation. No large movies or whole-graph solve.
Budget 1,200 CPU seconds, estimated8MiB, cap32MiB, one worker and20GiB free reserve.
No parameter search or physiological adjustment after inspecting these outcomes;
any later adjustment requires a separately versioned protocol and fresh evidence.
