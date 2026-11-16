# Biological selectivity benchmark — V1

Completed 27 October 2026. Decision: **CONDITIONAL_PROPERTY_NOT_SUPPORTED**.
The benchmark is executed and independently checked. This status concerns one
prospectively defined response property under approximate reconstructed stimuli;
it does not establish physiological validation of the complete circuit.

A [separately frozen supplement](BIOLOGICAL_WALKING_TRANSFER_REPORT_V1.md) tests
four additional, independently held-out bIPS animals identified from walking
preparation metadata. That supplement does not alter this main reused-animal
comparison or supply matched small-turn behavior.

## Main response-property comparison

The primary magnitude index compares the absolute second-minus-first epoch
contrast for horizontal translation cues with that for yaw. Positive means
stronger translation contrast; negative means stronger yaw contrast. This is
not the publication's signed discrimination index and does not validate motion
direction. Each recorded fly has equal weight. Zero denominators are undefined.

| Cohort | Paired test flies | Recorded mean [95% fly bootstrap CI] | Primary model mean | Frozen decision |
|---|---:|---:|---:|---|
| bIPS / sytGC7f / native | 4 | 0.1560 [0.0014, 0.3438] | -0.1644 | NOT SUPPORTED |
| DNp15 / GC6f / WT | 5 | -0.2617 [-0.7041, 0.2814] | -0.9062 | NOT SUPPORTED |

The criterion requires at least three paired flies, a measured interval wholly
on the expected side of zero, primary model mean inside that interval and the
expected model sign for all three display hypotheses. Both primary cohorts must
pass for overall support. All secondary cohorts, undefined counts, signed epoch
contrasts and alternative profile predictions are retained in the evidence.
Single-animal secondary cohorts do not establish population agreement.

The bIPS prediction has the opposite index sign from the recorded mean under
all three display hypotheses. DNp15 retains a rotational model preference, but
its predicted index is more negative than the measured interval. That recorded
DNp15 interval crosses zero: this small cohort and magnitude-based assay do not
establish the expected preference, and do not refute the paper's signed-index
result. The bIPS measured interval's lower bound is close to zero; four flies
give limited population evidence. Neither primary gate passes.

Some conditional waveform fits are useful: primary-display bilateral skill is
0.5106 for bIPS/sytGC7f and 0.6069 for HS/GC7f, with positive fly-bootstrap lower
bounds. Nevertheless, none of the eight primary-display unilateral cohort
comparisons passes the transfer rule. Thus a favorable aggregate waveform error
does not establish the required selectivity or generalization.

![Selectivity and held-out condition comparison](../results/biological_selectivity_benchmark_v1/figures/comparison.png)

## What was actually calibrated and tested

Metadata selected 79 sessions from 63 previously
studied flies. Preserved the original 35 calibration/28 test assignments; exact
eligible counts vary by condition. Extracted 96 bilateral calibration
trace summaries and 124 test summaries across eight separate reporter,
compartment and genetic-background cohorts. No test animal or unilateral
condition contributed to any observation fit. All animals' earlier outcomes and
the paper were already inspected: this is not fresh animal validation or a
discovery of the published preference. Unilateral scoring tests generalization
beyond this study's calibration stimuli on the inherited animal partition.

For each cohort, all 56 existing observation candidates were compared only on
calibration bilateral data. They use signed or rectified rate, zero/one/two causal
filter stages and nonnegative gain without offset. The minimum equal-fly MSE
fit was hashed before test extraction/scoring. These phenomenological filters
are not measured calcium constants, membrane voltages or neural parameter fits.
All candidates and all eight selected fits remain available. Transfer the same
fit to every alternative display hypothesis, without selecting the best one.

## Held-out unilateral condition prediction

Skill is calculated per fly as `1 - model_MSE/zero_response_MSE`, then averaged
across flies. Positive means better than a measured zero-response comparator;
it does not mean an exact waveform prediction. Full-clock scores can be
influenced by long stationary intervals; motion-only errors are also saved.
Support requires at least three flies and a lower 95% bootstrap bound above zero.

- bIPS / sytGC7f / native, aligned_100: n=4, mean fly skill -0.5381, 95% CI [-2.6478286391087975, 0.6337369598884257]; support=False.
- bIPS / sytGC7f / native, aligned_50: n=4, mean fly skill -0.4131, 95% CI [-2.3207026297609916, 0.6242105155787012]; support=False.
- bIPS / sytGC7f / native, pitched_100: n=4, mean fly skill 0.2241, 95% CI [-0.1920907115930511, 0.5115674276252773]; support=False.
- DNp15 / GC6f / WT, aligned_100: n=5, mean fly skill -0.5295, 95% CI [-1.6854395146958037, 0.3326103893559173]; support=False.
- DNp15 / GC6f / WT, aligned_50: n=5, mean fly skill -0.4795, 95% CI [-1.5777689960206909, 0.34105838344106765]; support=False.
- DNp15 / GC6f / WT, pitched_100: n=5, mean fly skill 0.0312, 95% CI [-0.2935952232138236, 0.28056009729882714]; support=False.

![All primary-cohort test time courses](../results/biological_selectivity_benchmark_v1/figures/primary_timecourses.png)

## Stimulus fidelity and biological interpretation

The [Erginkaya paper](https://www.nature.com/articles/s41593-025-01948-9) describes
the LED geometry, dot family, timings and reporters. The [public analysis](https://github.com/ChiappeLab/Erginkaya_et_al_2025)
identifies YawRightFlipped as binocular horizontal front-to-back/back-to-front
motion. This supplies a translation cue, without the depth/parallax of walking.
The archived recording labels specify nominal 20 pixels/s. Exact trial arrays,
modified G3 generator states and refresh remain unavailable in audited sources.

This reconstruction uses new uniformly distributed spherical dots, subpixel
averaging, grayscale quantization and a source-sized display. Its primary
assumed 100-Hz display is centered in head coordinates; alternatives use 50 Hz
and a 74-degree pitch registration. They are declared hypotheses, not measured
confidence bounds or an exhaustive uncertainty analysis. Dot initialization,
photometry, black exterior, stationary unilaterally masked half and absence of
measured optics remain assumptions. No version was selected for better agreement.
Exact quantitative trial-waveform validation remains open even if an index passes.

Source soma-side metadata selects model populations. It does not establish that
a single model state reproduces a particular axon/dendrite or recording field.
WT/control reporter cohorts remain distinct. Missing electrical coupling and
unresolved recurrent cell identities were not filled with invented parameters.
These immobilized-fly recordings do not validate small-yaw detection in a walking
fly. The external neural/image hybrid agreement rule has no established
biological implementation and was not used in this benchmark.

## Numerical evidence and preservation

All 32 planned image-driven cases completed. Additional numerical cases compare
half solver step, half angular texture raster and doubled LED quadrature on the
fixed first yaw realization. The solver maximum wide-field difference is
1.89757e-10, below the predeclared 1e-7
implementation tolerance. Existing batch/streaming frontend maximum discrepancy
is 0. Raster/quadrature sensitivity is
reported descriptively, without fitting it away or claiming complete sampling
convergence. Numerical correctness is distinct from biological agreement.

The original half-step preflight **failed**: maximum difference 5.03487e-5
exceeded the frozen 1e-7 tolerance. Inspection showed that the inherited kernel
spreads a source change over its final solver step, so halving that step also
changes the input waveform. The [R2 control correction](BIOLOGICAL_SELECTIVITY_NUMERICAL_CONTROL_AMENDMENT_R2.md)
retains the original 1-ms ramp at every numerical resolution. Its 1-ms replay
matches the production arrays exactly; 0.5-ms and 0.25-ms comparisons then pass
the unchanged tolerance. All original failure evidence remains saved. The
production solver and inference are unmodified. This establishes numerical
convergence conditional on the inherited forcing convention, not a physiological
claim about how visual input changes in time. Global stimulus-direction mapping
also remains an assumption for signed waveform comparisons; the primary
magnitude index discards sign rather than resolving that source limitation.

Independent arithmetic checked 220 source trace summaries,
all 448 observation candidates, 372
test trace/profile predictions and 84 paired
fly/profile indices. Maximum discrepancies by quantity are recorded in the
review. The review independently indexes source trial/ROI tensors and uses a
separate filter recurrence. All original stimuli prefixes and fixed-half
unilateral controls pass. Complete failure ledgers are retained if present.

The [source-quality ledger](../results/biological_selectivity_benchmark_v1/quality_unit_review.json)
covers 234 trace summaries across both outputs: 1,696 usable and 282 unusable
trial/ROI/protocol units. Unusable units include padded/empty baselines and
insufficient finite coverage under the unchanged rules. No whole trace summary
was excluded and every saved aggregate recording sample is finite. Initial
baseline warnings reflect those source units. Plot-only warnings concern grid
points outside measured clock support; figures leave those points undefined
and never extrapolate recording data.

## Reproduction and evidence

Use the existing Linux CPU environment with NumPy, SciPy, Matplotlib, pytest and
a C++17 compiler. Set `PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`.
Each producer uses exclusive creation: reproduce in a separate checkout/output
revision with read-only links to the frozen prior circuit and raw recording
sources. Do not rerun fixed-path producers over this sealed study. Run setup,
the targeted pytest test into preflight_tests.log, freeze, numerics (retaining
its expected failed mismatched-waveform check), the isolated R2 numerical
correction, run, fit, score, independent review, reporting and archive checks.
The absolute
raw-data locations and SHA-256 identities are retained in sessions.json; the
raw data are the author archive, not new experiments.

- [Frozen protocol](BIOLOGICAL_SELECTIVITY_BENCHMARK_PROTOCOL_V1.md)
- [Simulation and analysis driver](../scripts/biological_selectivity_benchmark_v1.py)
- [Source and methods freeze](../results/biological_selectivity_benchmark_v1/before_simulation.json)
- [Observation models frozen before testing](../results/biological_selectivity_benchmark_v1/observation_before_test.json)
- [All trace metrics](../results/biological_selectivity_benchmark_v1/trace_metrics.csv)
- [All paired fly indices](../results/biological_selectivity_benchmark_v1/paired_fly_selectivity.csv)
- [All cohort/profile summaries](../results/biological_selectivity_benchmark_v1/selectivity_summary.json)
- [Unilateral and bilateral error summaries](../results/biological_selectivity_benchmark_v1/transfer_summary.json)
- [Numerical checks](../results/biological_selectivity_benchmark_v1/numerical_review.json)
- [Independent review](../results/biological_selectivity_benchmark_v1/independent_review.json)

## Undergraduate explanation: what we want, did and why

We want to know whether our simulated neural circuit responds to visual motion
like a real fly's circuit. We showed it reconstructed moving dots and compared
its responses with published measurements from real neurons. We learned only
the conversion from model activity to the calcium measurement on one set of
flies, then froze that conversion before testing other flies and stimuli. The
table shows whether it reproduces the different rotation/translation preferences
of bIPS and DNp15. This gives us a concrete biological check, while the missing
exact visual movies and recordings matched to small turns during walking limit
what we can conclude. A
successful engineering turn detector and a biologically accurate circuit are
separate results; this experiment tests the latter in a narrow, explicit way.
