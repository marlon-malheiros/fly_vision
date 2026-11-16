# T4/T5 stage result and numerical sampling repair R3

2026-11-05. **A bar-sampling defect was corrected in a separate renderer. None of
the current T4/T5 source representations passed the frozen physiological
compatibility screen.** Four reserved control flies remain unscored. No original
frontend, MaleCNS graph or neural parameter was modified.

The [primary report](T4T5_STAGE_BENCHMARK_REPORT_V1.md) and its quantitative
[decision](../results/t4t5_stage_benchmark_v1/decision.json) remain the original
scientific result. The primary freeze is `230bca2`; the pre-outcome label-loader
correction is `902b4a7`; the explicitly post-outcome sampling diagnostic was
frozen at `71294ff`. This report distinguishes the new numerical repair from
that earlier decision. It does not convert a failed development screen into
successful biological validation.

## What we learned about motion selectivity

All seven named development animals were retained, including those outside the
paper's seven-of-eleven selected subset. The analysis includes154 T4A/B ROIs and
115 T5A/B ROIs, with no undefined selectivity denominators. Empty subtype layers
are preserved as missing, not fabricated cells. Animal means receive equal
weight; abundant cells do not count as extra independent flies.

For each ROI, PD is the maximum native response peak across eight directions;
ND is the response four circular indexes away, following the source analysis.
The model uses its two opposite horizontal directions. Define
`D = (PD − ND) / (|PD| + |ND|)`. D=1 means complete null-direction suppression.
This relative calculation cannot verify absolute subtype direction. It also
cannot validate vertical tuning or the eight-direction tuning width of this
horizontal-only adapter.

| Quantity | Recorded development mean | 95% simultaneous mean band | Primary model result |
|---|---:|---:|---:|
| T4 relative direction selectivity | 0.639310 | [0.504489, 0.774132] | 1.000000 for all three copies |
| T5 relative direction selectivity | 0.759269 | [0.657520, 0.861018] | 1.000000 |

Primary means bright-on-dark / dark-on-bright bars and the squared positive-drive
observer. All primary fixed-template direction contrasts are also positive1;
own-peak alignment did not conceal a sign reversal in this particular assay.
The measured-Mi1, adaptive-Mi1 and HP-removed copies disagree in response
amplitude but all suppress the opposite-motion source peak to zero here.
**The low-selectivity fast-grating result does not generalize to these slow
bars.** This is stimulus dependence, not an identified unique circuit mechanism.

Both observation assumptions and backgrounds were predeclared. On grey, measured
T4 D is0.788296 squared versus0.488019 linear; HP-removed D is0.826978 versus
0.529356. Adaptive T4 and the T5 surrogate stay approximately1. A secondary
value entering a band does not authorize selecting that observer/background
after looking at outcomes or qualifying the primary candidate. The choice of
measurement representation materially affects the conclusion.

These are **conditional compatibility checks**, not physiological equivalence
tests. The deterministic source output has no trial variability or calibrated
calcium noise. Taking a maximum of noisy recorded samples can produce a positive
ND peak even for weak underlying neural responses; this is a possible observation
bias, not a measured explanation of these data. Native timing, trial sequences,
RF coordinates and indicator transfer parameters are missing. Consequently this
result cannot distinguish a too-sharp neural computation from an incomplete
stimulus/measurement comparison. Do not add arbitrary null responses or noise
merely to hit the recorded band.

## What was numerically wrong and what was fixed

The original renderer included both endpoints when a bar edge landed exactly on
a raster sample. At0.5deg spacing this sometimes represented a5deg bar as5.5deg;
at0.25deg, as5.25deg. The original1deg display samples represented5deg exactly.
Both neural responses and stimulus geometry must converge before claiming that
a finer simulation is an independent numerical confirmation.

The separate R3 renderer assigns half occupancy at an exact discontinuity,
preserving a symmetric quadrature rule. This is a mathematically motivated
sampling correction. It is not evidence about the original projector pixels,
optics or biological receptive fields. All existing neural routines, filters,
conductances, contrast normalization and dynamics are imported unchanged.

| Numerical check | Original raster | Corrected endpoint quadrature |
|---|---:|---:|
| Largest represented bar-width error | 0.5deg | 0deg |
| Largest adjacent-grid squared-peak change | 12.8253% | 2.8454% |
| Adjacent-grid checks across three models/two observers/two refinements | 6/12 pass | 12/12 pass |
| Change in direction selectivity | 0 | 0 |
| Original1deg model traces | retained | all6 bitwise identical |

The original study's global numerical gate failed on4/32 checks. Its all-false
gate column does **not** mean every model individually failed numerical tests:
adaptive T4 and T5 each passed their individual checks. All four representations
separately missed their primary physiological band anyway. The R3 follow-up
does not retrospectively replace the frozen result.

The original independent Octave loop reproduces all269 ROI scores exactly and
all14 animal-family means within2.23e-16. The central-row T5 reduction agrees with
the existing2D functions within5.56e-17. R3 additionally reopens compact traces,
recalculates every score independently and verifies represented widths using
exact rational endpoint counting. These checks establish numerical consistency,
not a validated biological neuron or circuit.

## Evidence, reproduction and cost

- [Primary protocol](T4T5_STAGE_BENCHMARK_PROTOCOL_V1.md),
  [loader correction](T4T5_STAGE_BENCHMARK_LOADER_CORRECTION_R2.md),
  [post-outcome numerical protocol](T4T5_SAMPLING_DIAGNOSTIC_PROTOCOL_R3.md).
- [Primary model metrics](../results/t4t5_stage_benchmark_v1/model_metrics.csv),
  [animal metrics](../results/t4t5_stage_benchmark_v1/development_animal_metrics.csv),
  [independent review](../results/t4t5_stage_benchmark_v1/independent_review.json),
  [figure](../results/t4t5_stage_benchmark_v1/direction_selectivity.png).
- [Corrected sampling decision](../results/t4t5_sampling_diagnostic_r3/decision.json),
  [raw/corrected width evidence](../results/t4t5_sampling_diagnostic_r3/represented_widths.csv),
  [all refinement checks](../results/t4t5_sampling_diagnostic_r3/refinement_checks.csv),
  [independent review](../results/t4t5_sampling_diagnostic_r3/independent_review.json),
  [sampling figure](../results/t4t5_sampling_diagnostic_r3/sampling_convergence.png).

The main successful simulation consumed14.114 CPU seconds; the sampling follow-up
13.592. Main peak RSS~541MiB; follow-up~1017MiB. No permanent input movies or full
MaleCNS solves were produced. These CPU counters exclude Python startup, the
failed initial loader and the Octave subprocess; they are not whole-session
accounting. Both archives, including dated progress copies and method snapshots,
remain below4MiB combined, well below the32MiB caps.
All152 retained files in the source-audit and previous Mi1-HS indexes rehash
unchanged. Sealing receipts are separate from these numerical/biological results.

Original primary commands must use the R2 loader entrypoint after the V1 freeze;
see its correction report. For the numerical follow-up, run
`scripts/t4t5_sampling_diagnostic_r3.py freeze`, then `run`; finally
`scripts/review_t4t5_sampling_r3.py`. Use the scientific Python environment,
`PYTHONPATH=src`, `OPENBLAS_NUM_THREADS=1` and a temporary `MPLCONFIGDIR`. Existing
output files use exclusive creation: a full rerun needs a new version/path.

## What we want, what we did, and why

We want a neural model that notices gentle turns while a fly walks. To trust its
answer, we also want its intermediate motion responses to resemble recordings.
We tested that intermediate stage, found a numerical drawing error and fixed it
without changing neurons. The biological comparison still does not qualify:
this simulated bar produces no opposite-direction response, whereas the measured
calcium peaks usually do. We cannot yet tell how much comes from neural modeling
versus measurement and stimulus differences.

The next useful biological step is to establish a matched T4/T5 observation
benchmark with known stimulus timing and an independently constrained calcium
measurement model. Available processed arrays still support descriptive tuning
checks, but not that exact benchmark. A separate full2D T4 model may address
tuning width, with additional anatomical assumptions explicitly documented;
it must not be introduced simply to optimize this familiar score. Keep the
four reserved flies for a frozen, better-constrained comparison. Another
whole-circuit gain sweep is not justified by the present result.

Sources: [Henning et al.](https://doi.org/10.7554/eLife.108529.3),
[pinned author source and data](https://github.com/silieslab/C2C3_feedback_Henning/tree/745c6114b72a61dabc9389a1f024dbe22f679edf).
