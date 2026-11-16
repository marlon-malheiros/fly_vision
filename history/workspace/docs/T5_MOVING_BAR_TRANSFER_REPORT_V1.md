# Moving-bar transfer and observation report, V1

Decision: **`MOVING_BAR_TRANSFER_COMPLETE`**, after separate technical review.
Completed 12 October 2026 UTC (11 October local time).

## TLDR

The second stimulus family passes. All **144 primary image responses** preserve
the native robust peak and all **72 direction pairs** agree. Maximum peak error
is **0.1865%** at existing production
1°/5-ms resolution; 0.5° pixels reproduce the native waveforms within ~1.7e-12 mV.
Recorded and fixed-model peaks have expected direction in **9/9** width/speed
pairs. Moving-bar mean responses also pass 9/9 in both modalities; weak mean
results depend on the stimulus/window and are not a universal model property.
Full waveform accuracy is still imperfect: stimulus-window RMSE is
**2.629398 mV**. No fitting or new neurons were added.

## What was tested and frozen

All 18 published cell-7 bar conditions are retained: widths 1/2/4 columns,
40/80/160-ms steps, both directions. There are nine width/step pairs and 5,932
observed samples, from one physiological example. The author plotting script
explicitly labels flag 1 PD and flag 0 ND for this example; response values are
not used to choose direction. Eight existing geometry templates share the same
fixed cell-7/iteration-52 parameters, not eight independent recorded neurons.

All 612 trajectories comprise 144 primary, three 144-case refinements, 18 native
references and 18 delayed controls. No T4, HS/H2 or parameter optimization runs.
Code/configuration/tests, mapping, windows and thresholds were frozen before new
bar scores in [the manifest](../results/t5_moving_bar_transfer_v1/prospective_manifest.json).
Historical native waveform/error analyses already existed; this new scoring
freeze does not claim complete historical blinding.

The previous [provenance audit](../results/t5_matched_grating_observation_v1/provenance.json)
reproduces the archived fitting objective using only 24 width-two single-bar
flash traces. Moving bars are absent from that objective. The author's reasons
for choosing this example and full optimization history remain unreconstructed.
This supports stimulus-held-out relative to the audited objective, not fully
blind example selection or independent-cell validation. No new data were needed
for this bounded comparison. The [original paper](https://elifesciences.org/articles/50706)
describes moving bars and a robust 0.995-quantile voltage response, with
DSI=(PD−ND)/PD; local hashed datasets and released scripts provide exact inputs.

## Mapping, timing and measurement

Retain nine native positions -4..4, partial entry/exit for wide bars and
N+width−1 holds. A separate clipped translating interval validates every author
schedule. Twenty-six distinct neutral/partial/full native bar states are rendered
as real dark/background pixels using the previous grating renderer, unchanged
production sampler, 2.25° pitch, nine transverse points, geometry centers and
structural proxy axes. Assumed isotropic pitch and transverse embedding remain
unvalidated; each template receives its own aligned local movie.

Native -20 ms maps to simulation zero. The author's **25-ms effective input
offset** is retained, giving simulation onset 45 ms. It is not an independently
measured physical LED onset. Earlier grating reports' "native onset 25 ms"
wording refers to this effective-model clock; their numerical records remain
unchanged. The new primary stimulus-aligned scoring window is [0,duration),
with duration=(9+width−1)×step. Actual fractional 5-ms observation clocks remain
unchanged. No extra warmup, time realignment or fitted latency is introduced.

Primary response is q0.995 of the provided author-relative voltage using NumPy
linear sample quantiles, over that window. This is a declared implementation
of the paper's robust-peak measure, not exact reconstruction of unavailable
analysis internals. Grating oscillation amplitude is not reused for transient bars.

The local archive saves only four prestimulus samples in [-20,0). Primary
retains the provided relative voltage rather than estimating a new baseline
from those four points. Baseline-subtracted peak, effective-drive-window peak
[25,25+duration), full-trace maximum (used in the author plotting helper) and
stimulus-window mean are separately declared diagnostics. The largest absolute
measured baseline is 1.564589 mV; uncertainty of that short estimate
cannot be inferred from sample count.

Report the paper DSI=(PD−ND)/PD and the project's signed pair
DSI=(PD−ND)/(abs(PD)+abs(ND)) separately. Project response/difference floors
are 0.065 mV and absolute DSI floor 0.1. They are engineering thresholds, not
physiological significance. Transfer bounds remain 5% peak error and 0.02
project DSI error, with native classification preserved even if weak/wrong.
See [the full protocol](T5_MOVING_BAR_TRANSFER_PROTOCOL_V1.md).

## Complete image-to-native transfer results

| Variant | Peak preserved | Direction preserved | Strict identity | Max peak error | Max project DSI error | Max Vm error mV |
| --- | --- | --- | --- | --- | --- | --- |
| primary | 144/144 | 72/72 | 54/144 | 0.186531% | 0.000823947 | 0.039529 |
| half_frame | 144/144 | 72/72 | 54/144 | 0.186531% | 0.000823947 | 0.039529 |
| half_pixel | 144/144 | 72/72 | 144/144 | 7.07724e-12% | 2.33147e-14 | 1.66267e-12 |
| quarter_pixel | 144/144 | 72/72 | 144/144 | 7.07724e-12% | 2.33147e-14 | 1.66267e-12 |

All primary and refinement cases pass. At 1° resolution 54/144 waveforms
satisfy strict identity; other small raster errors remain visible. Finer pixels
give strict identity in all 144 cases per variant. Maximum half-frame peak and
DSI differences are 4.26898e-14 and
1.62093e-14. Faster sampling adds essentially no
error here because onset and all native steps already lie on the frame grids.
This does not establish convergence for arbitrary continuously moving textures.
All 18 one-frame-late controls exceed the frozen input/waveform mismatch bounds;
direction reversal is not required for detection.

![All refinements and controls](../results/t5_moving_bar_transfer_v1/bar_transfer_refinements.png)

## Recorded versus fixed-model bar responses

All peak values below are mV; all nine pairs are retained:

| Width | Step ms | Observed PD | Observed ND | Model PD | Model ND | Observed paper DSI | Model paper DSI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 40 | 11.670880 | 6.867972 | 12.443419 | 5.182689 | 0.411529 | 0.583500 |
| 2 | 40 | 21.450876 | 10.645910 | 20.098985 | 6.759757 | 0.503707 | 0.663677 |
| 4 | 40 | 29.152908 | 8.585343 | 27.385780 | 7.637122 | 0.705506 | 0.721128 |
| 1 | 80 | 14.474154 | 7.858133 | 14.268065 | 4.347728 | 0.457092 | 0.695283 |
| 2 | 80 | 20.539235 | 5.793119 | 22.274457 | 5.492278 | 0.717949 | 0.753427 |
| 4 | 80 | 23.627079 | 2.651587 | 29.486672 | 5.722702 | 0.887773 | 0.805922 |
| 1 | 160 | 15.292354 | 4.040154 | 15.217900 | 7.001502 | 0.735806 | 0.539917 |
| 2 | 160 | 22.275250 | 8.696999 | 23.349394 | 9.861000 | 0.609567 | 0.577676 |
| 4 | 160 | 26.544596 | 11.473143 | 30.124736 | 11.648133 | 0.567779 | 0.613337 |

The recordings and model agree on expected peak direction in all nine pairs.
They do not agree exactly on response magnitude or direction strength. Across
18 traces, mean absolute peak error is 1.895753 mV and
maximum absolute error is 5.859592 mV. Maximum relative peak
error is 115.82%, in a small ND response; use the absolute
values alongside percentages. Full-recording waveform RMSE is
2.231504 mV and stimulus-window RMSE is
2.629398 mV. No physiological pass/fail cutoff is invented
from those errors, and no parameter is refitted to reduce them.

![All nine bar comparisons](../results/t5_moving_bar_transfer_v1/all_bar_waveforms.png)

![Physiological peak and direction-strength discrepancies](../results/t5_moving_bar_transfer_v1/bar_recording_peak_comparison.png)

## Prespecified baseline/window/mean diagnostics

| Readout | Observed expected direction | Native expected direction |
| --- | --- | --- |
| peak_mv | 9/9 | 9/9 |
| baseline_subtracted_peak_mv | 9/9 | 9/9 |
| effective_window_peak_mv | 9/9 | 9/9 |
| full_trace_max_mv | 9/9 | 9/9 |
| mean_response_mv | 9/9 | 9/9 |

Direction classification survives these baseline/window choices. The magnitudes
remain in complete tables; no favorable diagnostic replaces the primary score.
The mean finding qualifies the earlier [grating observation result](T5_MATCHED_GRATING_OBSERVATION_REPORT_V1.md):
native grating means missed that criterion in 4/4, while moving-bar means pass
9/9. Thus the available data do not support a universal "the model has weak mean
direction selectivity" claim. The grating discrepancy itself is still retained.
Stimuli and finite scoring windows both differ between assays; this comparison
does not isolate their individual causal contributions.

## Technical verification

**14 focused tests passed.** All 24 raster dictionaries match independent
stripe-interval reconstruction; independent SciPy interpolation differs from
the production sampler by at most 0.
Short full movies reproduce cached-state sampling for all eight placements.

Every one of **612 waveforms** passes separate matrix-exponential propagation,
maximum error **1.56319401867e-12 mV**. All
18 native waveforms agree with the previously saved tight author RHS within
1.28522970044e-10 mV. All raw observation extractions
and clocks match bitwise, and parameters are unchanged. Independent sorted
quantiles, sums and peak direction flags agree within
3.5527136788e-15; 306
computational pairs were reviewed. The separate implementation is run by this
agent, not a blinded external scientific reviewer. No numerical correction was
needed in this experiment.

Six predecessor indexes and all 10,758 entries (overlapping) were verified
before scoring. Final preservation and checks are recorded in the completion
metadata. The 5,932 time samples and computational placement repeats are not
independent biological observations; no population p-values or new repeat-level
confidence intervals are claimed.

## Where this leaves the project

We now have passing, fixed-parameter image/native benchmarks for **two distinct
motion families**: grating oscillation amplitude and moving-bar robust peaks.
Measured peak direction is also reproduced for the nine bar conditions in this
one-cell example. These checks can close this bounded frontend-transfer stage.
Further repetition of similar controls is not needed to establish this result.

This does not validate population geometry, T4/HS/H2, arbitrary texture motion,
full physiological waveform accuracy, or neural degeneracy. The grating mean
limitation and texture sign reversals remain unresolved, and publication novelty
or acceptance is not established by a reproducible benchmark.

Next, freeze a mixed-stimulus source benchmark and a small parameter-sensitivity
pilot using active excitation/inhibition parameters. Such a pilot can test
whether materially different configurations preserve defined bar/grating
responses before a larger search. Exclude the unused model parameter and trivial
filter-label symmetries, and distinguish local robustness from nontrivial
degeneracy. It is a proposed next stage, not executed here and not proof of
degeneracy in the connectome circuit.

## Evidence and ongoing tracking

[Complete trace metrics](../results/t5_moving_bar_transfer_v1/trace_metrics.csv),
[all computational pairs](../results/t5_moving_bar_transfer_v1/pair_metrics.csv),
[native/observation readouts](../results/t5_moving_bar_transfer_v1/native_metrics.json),
[observation errors](../results/t5_moving_bar_transfer_v1/observation_errors.csv),
[independent review](../results/t5_moving_bar_transfer_v1/independent_review.json),
and [analysis](../results/t5_moving_bar_transfer_v1/analysis.json) preserve every
case. Raw recordings, native/archive predictions and image outputs are saved.
PNG/PDF figures and [input hashes](../results/t5_moving_bar_transfer_v1/input_manifest.json)
are included in [the artifact index](../results/t5_moving_bar_transfer_v1/artifact_index.json).
See [completion](../results/t5_moving_bar_transfer_v1/completion.json) and
[Git checkpoints](../results/t5_moving_bar_transfer_v1/git_snapshots.json).

Development, limitations and timing clarification are appended to
[the live progress report](PROJECT_PROGRESS_REPORT.md), with a dated
[study snapshot](../results/t5_moving_bar_transfer_v1/project_progress_snapshot.md).
Live files stay outside the immutable seal; all previous evidence is preserved.
Records are local and do not provide an off-device backup. Reproduction stages
are `prepare`, `execute`, `review` in the new run script, then report/check/seal
scripts in a fresh copy/output version. Preparation runs its tests itself;
completed V1 must not be overwritten.
