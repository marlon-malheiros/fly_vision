# Full published T4 cable versus matched electrical recordings V1

2026-11-06. Methods/protocol freeze: `1642677`.

**The full published cable is a substantial improvement, but does not meet the
frozen advancement criterion.** Its signed physical-voltage prediction reduces
MSE51.89% relative to the preceding best source adapter on the same three
comparison cells. It beats the early direction-blind reference in cells3 and4;
cell5 remains worse, making pooled reference skill negative. No additional
recordings were opened. This is useful retrospective component evidence, not
complete biological validation or new small-turn qualification.

## Audit: what changed and what was already done

The project already reproduced the full Gruntman2018 T4 cable in October:
344 sections,235 relevant dendritic sections,99 excitatory and55 inhibitory
sites, seed300 and all12 source parameters. That implementation success was
documented in the [earlier execution report](PHYSIOLOGICAL_PROTOTYPE_EXECUTION_REPORT_V1.md).
The recent [direct-voltage round](T4_DIRECT_VOLTAGE_REPORT_V1.md) evaluated a
different, simplified five-input source adapter. Repeating native author-code
reproduction alone would not have addressed its negative result.

This round therefore uses the complete cable on the actual experimental
movies/events. All source physiology, original frontend/MaleCNS parameters,
graph, old implementations and results remain unchanged. No new connections,
neural parameter fits, closed loop or full downstream solve were introduced.

The [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/) fits conductance
dynamics to stationary flashes and then predicts moving stimulation. Its source
code treats unit pulses at eleven positions as inputs, incorporating upstream
transformations implicitly through that fit. This differs from feeding generic
upstream filters plus a separate contrast-energy normalization into a T4 adapter.
The new comparison changes that entire source/input package; it does not isolate
a causal effect of cable morphology versus input preprocessing.

## Frozen assay and exposure limits

The [protocol](T4_CABLE_MATCHED_PROTOCOL_V1.md) specifies cells1–2 for diagnostic
gain calibration and cells3–5 for comparison. All five cells' moving responses
were previously inspected. They are not a fresh held-out validation cohort.
The author also fitted stationary-flash responses from this experiment, so this
is stimulus generalization/retrospective reproduction, not proof of generalizing
to independent animals absent from all parameter estimation.

All96 trials per cell are available. Previously fixed first repetitions provide
the PD-axis localizer and direction-blind reference; only the later PD/ND
repetitions enter scored means. Four dwell times20/40/80/160ms×two directions
give eight conditions per cell,80 scored repetitions and40 condition means.
Native voltage uses exact microsecond bin boundaries,2ms bins and baseline
[-250,−50)ms. Windows and condition/cell weights match the preceding R2 assay.

Eleven author bins sample the recorded LED movie along the existing canonical
PD axis,2.25deg apart through the source-defined center. Grey3 maps to0 and
bright7 to a native unit pulse using `(pixel−3)/4`. Piecewise-constant pixels
receive symmetric halfweights at exact boundaries. The model receives actual
event times,300ms grey prehistory, frame0 resets and a grey terminal hold.
Its fixed exact cascades and1ms resistance replay use the unchanged wrapper;
NEURON integrates at0.1ms and records signed soma voltage at1ms.

Canonical-axis transport and centerline RF sampling remain assumptions. No
absolute T4 subtype direction, individual MaleCNS dendrite or independently
measured voltage-to-release relation is established by this mapping.

Three readouts were fixed before predictions:

* **Primary physical voltage:** soma Vm minus its baseline, gain1, no fit.
* **Calibrated diagnostic:** one nonnegative zero-intercept gain from cells1–2,
  equal condition/cell weighting; locked value0.2912807424.
* **Rectified diagnostic:** the former `max(Vm+65,0)/65` release surrogate,
  baseline subtraction, then the same type of development-only gain18.99030444.

The two scalar fits are observation calibration, not conductance estimation.
No RF shift, latency, filter, source parameter or condition-specific amplitude
was optimized. Additional cells6–8 were selected in advance by dates and earliest
protocol, but acquisition required a raw/calibrated waveform pass; that gate failed.

## Quantitative comparison

Skill is `1−model_MSE/reference_MSE`. The direction-blind reference uses each
cell's early PD/ND average at each dwell, predicting later repetitions. It has
cell-specific physiological information, rather than being an image-driven
neural model. It is a demanding empirical comparator, not the definition of a
biologically correct circuit.

The unchanged waveform rule requires positive pooled skills against zero and
direction-blind references, positive zero skill in every comparison cell, and
positive5th percentile of the joint minimum skill across all27 cell-bootstrap
resamples. No claim of physiological equivalence follows from passing this rule.

| Representation | RMSE, mV | Skill vs zero | Skill vs direction-blind | Joint bootstrap lower bound |
| --- | ---: | ---: | ---: | ---: |
| Previous delivered output, exact-clock R2 | 8.013764 | +0.097106 | −1.693822 | −1.945156 |
| Previous signed adapter, exact-clock R2 | 7.272243 | +0.256467 | −1.218363 | −1.504489 |
| **Full cable, physical mV** | **5.044183** | **+0.642278** | **−0.067278** | **−0.285436** |
| Full cable, calibrated | 6.850591 | +0.340189 | −0.968575 | −1.141447 |
| Full cable, rectified/calibrated | 6.856087 | +0.339130 | −0.971735 | −1.149794 |

The primary cable reduces MSE60.38% versus the previous delivered output and
51.89% versus the previous signed adapter. Its MSE is still6.73% above the
direction-blind reference. All three new readouts fail the waveform criterion.
The calibrated fit transfers poorly from the two calibration cells; scaling
down responses is not a successful repair for comparison cells3–5.

| Comparison cell | Physical-cable zero skill | Physical-cable direction-blind skill |
| --- | ---: | ---: |
| 3 | +0.686079 | +0.073112 |
| 4 | +0.760629 | +0.172545 |
| 5 | +0.418384 | −0.459093 |

The inhibition mask rule is unchanged: a sustained negative160ms-ND localizer
epoch, confirmed in later repetitions, in at least two cells. None qualifies,
so inhibitory validation remains unqualified by the sample. Although some
predictions and traces show negative voltage, that does not replace this check.

Evidence: [decision and per-cell scores](../results/t4_cable_matched_v1/decision.json),
[120 condition-output rows](../results/t4_cable_matched_v1/condition_metrics.csv),
[waveforms](../results/t4_cable_matched_v1/figures/comparison_waveforms.png),
[skill comparison](../results/t4_cable_matched_v1/figures/comparison_skills.png).
Both figures also have PDF copies. All input sequences, individual soma traces,
observations, means and81 three-cell bootstrap pairs are retained.

## Post-outcome diagnostic: amplitude alone does not resolve cell5

An explicitly exploratory calculation fits an ideal nonnegative scalar to each
cell's own scored responses. These are optimistic explanatory lower bounds,
not deployable predictions or new validation candidates. No frozen gain or
decision is changed, and no recording is excluded.

| Cell | Oracle gain | Best possible direction-blind skill under one scalar |
| --- | ---: | ---: |
| 1 | 0.334900 | +0.309685 |
| 2 | 0.233393 | +0.301248 |
| 3 | 0.938264 | +0.081921 |
| 4 | 1.126431 | +0.206091 |
| 5 | 0.734360 | **−0.301079** |

Cell5's optimally rescaled MSE30.655989mV² still exceeds reference23.561972mV².
Thus even a scalar chosen using its own scored data cannot repair that
comparison: waveform/timing/relative-condition structure matters. This does not
identify whether RF alignment, upstream temporal integration, cell variability
or another assumption is responsible. The gain differences also show why a
single amplitude fitted on cells1–2 transfers poorly in this sample; they do
not prove those cells are biologically defective or justify dropping them.

[Exploratory diagnostic](../results/t4_cable_matched_v1/exploratory_amplitude_diagnostic.json).
It cannot qualify the model or open the conditional additional files.

## Numerical reproduction and independent checks

The restored pinned NEURON8.2.7 environment reproduces four saved author
PD/ND20/160ms native simulations within5.019e-5mV, under the0.001mV limit.
All344 sections,235 dendritic sections,99/55 sites,12 parameters and seed300
are retained. This reconfirms implementation; it is not new physiological evidence.

All four development-cell0.1→0.05ms solver checks pass the0.005mV bound;
maximum0.00286622mV. Three focused pixel/boundary/native-bin/baseline tests pass.
All three worker runs have identical source parameters and sampled synapse sites.

Independent review reconstructs integer-clock means via bincount aggregation,
231,616 scalar pixel evaluations,5,264 frame-event samples, readouts, diagnostic
gains and all81 bootstrap pairs. Maximum native voltage-bin error5.68e-14mV,
readout error7.79e-14mV, metric/bootstrap error7.11e-15. A separate final check
verifies identical response/reference arrays and trial IDs against the preceding
exact-clock archive, pooled scores, inhibition and the conditional stop.
[Independent review](../results/t4_cable_matched_v1/independent_review.json),
[final bookkeeping](../results/t4_cable_matched_v1/final_bookkeeping_review.json).

All368 indexed prior direct-voltage artifacts rehash unchanged. The old movie
retirement remains intentional; this study neither regenerates those movies
nor claims that every historical project index is completely available.

## Failures, resources and reproduction

The previous temporary NEURON environment had disappeared. The first attempt
to restore packages failed sandbox DNS resolution; a network-authorized retry
installed NEURON8.2.7 and NumPy1.26.4 in a separate temporary environment, without
modifying existing environments. This setup failure is recorded in
`environment_setup.json`. No new scientific execution or audit failed in this
round. The waveform failure and lack of inhibition evidence remain explicit.

There were88 scientific solves:4 native replays,32 calibration-trial solves,
4 refinement solves and48 comparison-trial solves. Total scientific worker
CPU25.713852s, peak worker RSS376,717,312bytes. These exclude installation,
MAT loading/input preparation, reviews and plotting. Results before snapshots
occupy5,878,859bytes; no new raw data were downloaded, and existing176MB raw
recordings are referenced once. This is well inside the frozen resource limits.

Reproduction uses the repository scientific Python environment with
`PYTHONPATH=src`, `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`.
The worker uses the separate Python3.11/NEURON8.2.7/NumPy1.26.4 environment in
the configuration; its exact installed dependencies are recorded at completion.
In a fresh output location/check-out, run stages `freeze`, `native`,
`calibration`, `comparison` of `scripts/t4_cable_matched_v1.py`, followed by
`review_t4_cable_matched_v1.py`, `plot_t4_cable_matched_v1.py`,
`diagnose_t4_cable_matched_v1.py` and `complete_t4_cable_matched_v1.py finish`.
Successful stages refuse to overwrite outputs. Copy methods/progress and seal
only after all writers exit, then verify with the separate `check` process.

## Decision and useful alternatives

The full published neural mechanism is a more promising component under these
assumptions than the previous adapter. It is not a biologically validated
image-to-walking circuit. Additional project-unscored moving files dated
20160504/20160505/20160510 remain unopened; the four C2/C3 holdout animals remain
unscored. No new small-yaw detection claim or downstream validation follows.

The most directly supported next investigation is **individual stationary-flash
calibration**, using the public single-position flash trials to measure RF shape
and temporal response before predicting motion. This follows the paper's
strategy, addresses a waveform mismatch rather than another output-volume
adjustment, and would need a separately frozen model/data split. Published
population parameters need not predict every individual cell without such
calibration. A pretrained FlyVis benchmark remains a broader alternative if
that constrained route fails; it also needs stimulus/interface checks and is
not automatically valid for MaleCNS or slow walking yaw. Neither alternative
was executed in this stopped experiment.

## Undergraduate explanation

We want a neural model that explains how a fly notices a small turn. This round
used a more complete published model of T4, an early motion-detecting neuron,
and compared it with real electrical recordings. Its error fell by about half,
and it beat our simple reference in two of three comparison cells. The third
cell still disagreed even when we gave the model its best possible volume
adjustment, so the remaining problem includes the response shape. We now have
a stronger candidate and a specific next test: measure each cell's response
to stationary flashes, then ask whether those measurements predict motion.
Biological validation of the full walking circuit remains unfinished.
