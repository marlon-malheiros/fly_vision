# T5 moving-bar transfer and observation protocol, V1

## Scope

Second stimulus family after the passing matched grating transfer. Keep fixed
published cell-7/iteration-52 parameters, all 18 bar conditions and all eight
previously selected T5 geometry templates. Widths are 1/2/4 columns, steps
40/80/160 ms, flags 0/1. The author plotting script explicitly labels flag 1 PD
and flag 0 ND for this example; do not select preference from response values.
Use nine width/step pairs. The eight placements share one physiological model,
not independent recorded cells. No fitting, T4, downstream run or degeneracy
search. Native waveform/error analyses were previously performed; only these
new bar response comparisons are prospectively frozen, not all project history.

## Stimulus, pixel mapping and timing

Use the author's `stimulus_schedule` protocol 3 unchanged. Independently verify
every schedule by translating a width-W interval across positions -4..4 and
clipping it to that aperture. Wide bars enter and exit partially: N+W−1 holds,
not N full-width flashes. The published effective-model onset offset is 25 ms.
Render occupied columns using the previous matched dark/background pixel
renderer, inherited 2.25° pitch, fixed proxy axes, nine transverse samples,
finite longitudinal aperture and unchanged production sampler. Cache distinct
frames and verify actual short movies give identical sampled contrast.

Primary resolution: existing production 1° pixels, global half-degree anchor,
5-ms frames. Separately repeat 2.5-ms frames, 0.5° pixels and 0.25° pixels; none
replaces a failed primary result. Native -20 ms maps to simulator 0, so effective
drive onset is simulator 45 ms. All holds align with both frame grids. Preserve
each recorded trace's fractional 5-ms clock. Save all pixels, input sequences,
observations, exact native predictions, archived predictions and image outputs.
Only numeric sampled contrasts enter unchanged `t5_voltage` dynamics.

Execute 144 image traces per variant (18 × eight placements), 576 total; add 18
native references and 18 one-frame-late controls for T5a_R: **612 trajectories**.
All 18 observations (5,932 samples) are used once in the biological comparison;
image repeats do not increase the biological sample size.

## Measurement rules

Primary response is the linear 0.995 sample quantile of author-relative voltage
over [0,(N+W−1)×step) ms. The paper describes stimulus-aligned voltage and a
0.995 quantile within stimulus presentation; this is a declared implementation
of that measure, not a claim to reconstruct the unavailable full analysis code.
Keep the model's 25-ms offset. Treat it as effective-drive timing; do not shift
observations or assert independently measured physical LED latency. Earlier
grating transfer also compared effective model drives rather than establishing
physical display timing.

The saved prestimulus interval [-20,0) contains four 5-ms samples. Primary uses
the provided relative voltages without estimating a new baseline from those
four samples. Save baseline level/range and separately report (a) the same peak
after own-baseline subtraction, (b) q0.995 over the effective-drive interval
[25,25+duration), (c) full-trace maximum as used by the local author plotting
helper, and (d) signed mean over the primary window. Do not select a favorable
window or baseline after seeing scores. Peak is the appropriate transient-bar
measure; do not reuse the grating half-quantile oscillation estimator.

Report signed project pair DSI=(PD−ND)/(abs(PD)+abs(ND)) and, separately, the
paper DSI=(PD−ND)/PD when PD>epsilon. Never interchange those denominators.
Project classification uses the inherited 0.065-mV response/difference floors
and |DSI|>=0.1; resolved negative direction is retained. These are engineering
criteria, not biological confidence bounds. Record model/observation peak
errors, all nine paired discrepancies and full/stimulus-window waveform RMSE.
No global physiological pass cutoff, p-values or repeat-level uncertainty is
invented from condition-mean vectors.

## Transfer decision and technical prerequisites

Transfer passes only if every primary peak agrees with native within 5%
(denominator floor 0.065 mV), every primary paired DSI agrees within 0.02 and
all 72 primary pairs preserve the native resolved/unresolved and preference
classification. Require the same in each refinement and primary-to-half-frame
agreement by those bounds. A native weak/wrong-sign condition must not be
silently dropped or converted to successful expected direction. Report native
expected-direction pass counts separately; preservation and correctness differ.

Strict identity is separate: contrast maximum discrepancy <=1e-7 and waveform
maximum difference <=1e-8 mV. Late controls must have input difference >0.1 and
waveform difference >1e-4 mV; they need not reverse preference. Decision is
`MOVING_BAR_TRANSFER_COMPLETE` or `MOVING_BAR_TRANSFER_INCOMPLETE`, conditional
on independent alignment/numerical validation; failed technical validation is
`TECHNICAL_COMPARISON_INVALID`. Model-to-recording results are descriptive and
cannot be turned into population validation by a transfer pass.

## Evidence and tracking

Freeze code/configuration/protocol/tests and dependencies before new scores.
Validate every bar schedule with separate clipped-interval logic, all raster
pixels and spatial samples with independent interval/SciPy interpolation, all
612 waveforms with the existing independent matrix-exponential solver, and all
18 native traces with saved tight author-RHS results. Review sorted-quantile
arithmetic and direction flags independently. Audit raw recording bounds,
unchanged parameters and the prior bar-only training provenance; these motion
stimuli are outside that objective, but author example selection and new-cell
validation remain unestablished. Verify six predecessor indexes and all 10,758
entries before/after work (overlapping counts). Save complete tables, plots,
tests, report/TLDR, Git checkpoint and sealed evidence. Append dated progress
and a completion snapshot; exclude the live report and AGENTS.md from seals.
