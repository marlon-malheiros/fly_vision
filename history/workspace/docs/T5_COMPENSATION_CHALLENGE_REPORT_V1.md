# Prospective T5 compensation challenge — technical report V1

Client date: 2026-10-12 (America/Belem). Saved audit timestamps use UTC.

**Decision: `CHALLENGE_EQUIVALENCE_COMPLETE`.** Sampling-provisional: **False**.
The fixed alternative meets all primary-feature, mean and waveform gates on this challenge. This strengthens limited parameter compensation over the predeclared native stimuli; it does not establish equivalence for arbitrary inputs or biologically distinct circuits.

## Fixed question and prospective scope

The preceding [parameter pilot](T5_MIXED_PARAMETER_SENSITIVITY_REPORT_V1.md)
found one material alternative changing inhibitory decay 156.287→117.216 ms
and rise 165.922→207.403 ms. We copied that exact alternative and the published
baseline. The candidate was selected from previous scores; the new challenge
was frozen before its responses. No fitting or candidate search occurred.

52 synthetic conditions: 32 bars at widths 1/2/3/4 and new steps
20/60/120/240 ms; 20 gratings at dwell 10/20/60/120/240 ms (period = 8×dwell),
new starting phases 2/6, and paired directions. Native source occupancy and its
25-ms effective input offset remain. There are **no recorded observations for
these new conditions**, no new neurons, and no new image/frontend validation.
[Protocol](T5_COMPENSATION_CHALLENGE_PROTOCOL_V1.md),
[prospective hashes](../results/t5_compensation_challenge_v1/prospective_manifest.json),
[plans](../results/t5_compensation_challenge_v1/plans.json).

Four sets at 1 ms (baseline, alternative, pole-swap and E-gain mismatch controls)
plus baseline/alternative at 0.5 ms give **312 trajectories**. The exact pole-swap
control is excluded from scientific candidates. All inputs/outputs are retained.

## Results with all gates and failures

Primary scores use bar q0.995 peaks in [0,duration) and grating half(q95−q05)
amplitudes in retained cycles 2–3. Every response must be within 5%, every DSI
within 0.02, and all resolved/sign/pass classes preserved. Means use the same
5%/0.02/class gates; full voltage uses 5% of baseline trace maximum magnitude.
Denominator floor is 0.065 mV. These are engineering margins, not physiological
uncertainty estimates. No weak/reversed condition is omitted.

| Family | Conditions | Peaks/amplitudes within 5% | Means within 5% | Waveforms within 5% |
|---|---:|---:|---:|---:|
| bar | 32 | 32 | 32 | 32 |
| grating | 20 | 20 | 20 | 20 |

- Primary-feature equivalence: **True**, worst response error
  **3.5141%**, worst DSI change
  **0.011701**; changed pair classes
  **[]**.
- Mean equivalence: **True**, worst response error
  **2.0603%**, worst DSI change
  **0.007816**; changed pair classes
  **[]**.
- Full-waveform equivalence: **True**; worst normalized
  difference **3.4797%**, max absolute voltage
  difference **0.377068 mV**, pooled RMS difference
  **0.097185 mV**.
- Maximum normalized E/I conductance difference:
  **2.5959%**. This is simulated conductance,
  not a synaptic recording. The prior compensation occurs within one cascade.

| Largest error conditions (post-analysis ranking) | Peak/amplitude | Mean | Waveform |
|---|---:|---:|---:|
| grating_s60_p2_d-1 | 3.5141% | 1.0814% | 3.2519% |
| bar_w4_s60_d0 | 2.4467% | 0.4915% | 3.4797% |
| bar_w3_s60_d0 | 1.8500% | 0.4508% | 3.3524% |
| bar_w2_s60_d0 | 2.4754% | 0.3652% | 3.1178% |
| grating_s20_p6_d-1 | 3.1041% | 0.9636% | 1.5770% |
| grating_s120_p2_d-1 | 1.9070% | 0.2619% | 2.9035% |
| grating_s20_p2_d-1 | 2.8589% | 0.5828% | 1.9114% |
| bar_w1_s120_d0 | 2.3165% | 1.2952% | 2.6876% |

Primary feature failures: condition indices **[]**;
DSI-pair failures **[]**. Mean failures:
conditions **[]**, DSI pairs **[]**.
Full-waveform failures: **[]**. Indices refer to the
fixed [plans](../results/t5_compensation_challenge_v1/plans.json), not a reordered set.
[Full scores](../results/t5_compensation_challenge_v1/analysis.json),
[per-case CSV](../results/t5_compensation_challenge_v1/case_summary.csv).

![All new conditions](../results/t5_compensation_challenge_v1/figures/challenge_errors.png)

![All direction pairs](../results/t5_compensation_challenge_v1/figures/pair_dsi.png)

![Worst primary case](../results/t5_compensation_challenge_v1/figures/worst_primary_case.png)

The diagnostic voltage plot uses the worst primary-response condition, not a
favorable trace. The largest-error table is a post-analysis diagnostic ranking
and changes no criterion. Every condition remains in the score.

## Direction-performance context

Preserving direction classification compares the alternative to the baseline;
it does not imply every baseline condition has strong expected-direction tuning.
At both sampling resolutions and in both models, primary bar peaks pass expected
direction in **16/16** pairs. Grating amplitudes pass in **8/10**, with **2/10
unresolved**: dwell 10 ms/phase 6 and dwell 20 ms/phase 6. The latter has a weak
raw ND-greater-than-PD amplitude (DSI −0.0444 at 1 ms), below the declared absolute
DSI resolution threshold; it is retained. Mean direction passes in **16/16** bar
pairs and **0/10** grating pairs, all grating mean pairs unresolved. Mean voltage
can be substantial while providing little directional discrimination.
These are preserved model limitations, not new physiological validation or fixes.
[Descriptive pair context](../results/t5_compensation_challenge_v1/direction_context.json).

## Sampling check and controls

0.5-ms results are a predeclared sensitivity check, not substituted for 1-ms scores.
Sensitivity gates are 1% feature/mean, DSI 0.005, same classes, and common-clock
voltage identity to 1e-8 mV. Fine-resolution primary equivalence:
**True**; mean equivalence:
**True**; waveform equivalence:
**True**.

| Model | Largest primary sampling error | Largest mean sampling error | Largest DSI error | Stable |
|---|---:|---:|---:|---|
| baseline | 0.76649% | 0.27279% | 0.004018 | True |
| candidate | 0.75935% | 0.27149% | 0.003962 | True |

Swap-control maximum voltage error **8.53e-14 mV**.
E-gain mismatch control fails primary equivalence, max voltage difference
**4.681407 mV**. Neither counts as a new candidate.

## Validation, preservation and scientific limit

Nine focused tests pass, including real source loading and width-3 native
schedule agreement. Before freezing, one test caught list-order differences
between identical PD bar occupancy sets; the reference ordering was corrected.
No challenge responses existed then. The initial test result is preserved in
[test history](../results/t5_compensation_challenge_v1/prefreeze_test_history.txt).

All **312** voltage and four-state trajectories pass independent augmented
matrix-exponential review: max voltage error **2.13e-12 mV**,
max state error **4.53e-13**, primary/mean arithmetic
error **3.55e-15 mV**. Independent geometry and phase
reconstruction agrees for all 52 conditions; quantiles, means, pair classes,
gate decisions and sampling checks were recomputed.
[Numerical review](../results/t5_compensation_challenge_v1/independent_review.json).
Eight predecessor seals and 12,257 entries are preserved before/after execution;
live progress remains appendable and its study snapshot is sealed.
[Completion](../results/t5_compensation_challenge_v1/completion.json),
[artifact index](../results/t5_compensation_challenge_v1/artifact_index.json),
[source checkpoint](../results/t5_compensation_challenge_v1/git_snapshots.json),
[progress](PROJECT_PROGRESS_REPORT.md).

This is a finite native-input test of one selected mathematical model pair.
Synthetic means that preserve the baseline do not fix its physiological mean
errors. Earlier texture, T4, HS/H2 and population concerns remain unresolved.
It establishes neither exact equivalence for every possible input nor biological
degeneracy, publication novelty, acceptance, or new-cell predictive validity.

Keep this candidate as a bounded example of temporal-parameter compensation. Before pursuing a stronger degeneracy claim, use a separately frozen local sensitivity/Jacobian analysis to ask whether compensation also permits changes in final excitation/inhibition contributions. A biological claim would need independent physiological cells/repeats; this study supplies none.
