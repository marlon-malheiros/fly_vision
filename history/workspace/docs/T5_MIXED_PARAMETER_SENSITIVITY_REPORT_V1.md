# Native T5 mixed-benchmark parameter sensitivity — technical report V1

Client date: 2026-10-12 (America/Belem). UTC audit timestamps are saved in evidence.

**Decision: `LIMITED_FEATURE_EQUIVALENCE_FOUND`.** One materially changed parameter set preserves all 26 features and 13 pair gates. This completes the authorized finite
pilot. Numerical reproducibility and biological validation are distinct.

## What was tested

The fixed published cell-7/iteration-52 model was replayed on 18 moving bars and
8 gratings. One baseline, 80 predeclared active-parameter candidates, and four
excluded controls give **2,210 trajectories**. No observations were fitted and
no candidates or thresholds were changed after scoring. [Frozen protocol](T5_MIXED_PARAMETER_SENSITIVITY_PROTOCOL_V1.md),
[bank](../results/t5_mixed_parameter_sensitivity_v1/candidate_bank.json),
[prospective hashes](../results/t5_mixed_parameter_sensitivity_v1/prospective_manifest.json).

All 26 baseline traces reproduce the previous sealed predictions bitwise.
The primary features are the 18 bars' 0.995-quantile stimulus-window peaks and
8 gratings' robust oscillation amplitudes in retained cycles 2–3. Every feature
must be within 5%, every paired DSI within 0.02, and all 13 direction classes must
remain unchanged. These are engineering margins, not physiological uncertainty.
Secondary means, voltage waveforms and E/I conductances are retained.

Material change means ≥1.25 multiplicative distance in at least two canonical
positive parameters, or ≥0.5 native-column change in a center. Sorting E/I time
poles excludes filter-label symmetry; the unused first parameter is excluded.
Of 80 candidates, **19** satisfy this distance definition.

## Results, including failed candidates

**53/80** retain every direction class;
**6/80** meet all feature/DSI gates;
**1/19** materially changed candidates meet them.
Direction preservation alone is robustness, not quantitative equivalence.

| Candidate family | Count | Material | Direction preserved | Feature equivalent | Material and equivalent |
|---|---:|---:|---:|---:|---:|
| one_at_a_time | 40 | 4 | 26 | 4 | 0 |
| coordinated | 8 | 7 | 6 | 2 | 1 |
| random | 32 | 8 | 21 | 0 | 0 |

| Candidate | Worst feature error | Worst DSI change | Max waveform difference | Conductance change | Full waveform gate |
|---|---:|---:|---:|---:|---|
| i_poles_spread | 3.5664% | 0.011852 | 0.304069 mV | 2.174% | True |

| Single parameter | Direction preserved (of 4) | Feature equivalent (of 4) | Worst-feature error range |
|---|---:|---:|---:|
| decay_e | 2 | 0 | 5.955–18.825% |
| decay_i | 2 | 0 | 7.348–21.125% |
| rise_e | 4 | 4 | 0.138–0.388% |
| rise_i | 2 | 0 | 7.674–22.463% |
| gain_e | 4 | 0 | 17.974–47.840% |
| gain_i | 4 | 0 | 15.463–48.957% |
| center_e | 2 | 0 | 13.380–27.416% |
| center_i | 2 | 0 | 13.870–30.570% |
| sigma_e | 2 | 0 | 11.527–31.949% |
| sigma_i | 2 | 0 | 13.334–44.326% |

All scores and parameters, including failures, appear in the
[full machine-readable scores](../results/t5_mixed_parameter_sensitivity_v1/scores.json)
and [compact CSV](../results/t5_mixed_parameter_sensitivity_v1/candidate_summary.csv).
The four trivial controls preserve voltage within
**6.39e-14 mV**, and count as zero candidate wins.
Sorting labels removes their apparent parameter distance; differing hidden first
filter states under a label swap do not establish a different output mechanism.

For diagnosis only, the closest material candidate minimizes the maximum of
worst-feature-error/0.05 and worst-DSI-error/0.02. This post-analysis ranking
does not change the frozen criteria: **`i_poles_spread`**, worst feature error
**3.5664%**, worst DSI change
**0.011852**, max voltage difference
**0.304069 mV**, pooled RMS difference
**0.097553 mV**, maximum normalized E/I
conductance difference **2.174%**.
Feature equivalence and full-waveform equivalence are separate:
**6/80** pass the latter.

## Interpretation of the material candidate

The passing `i_poles_spread` set changes inhibitory decay from
**156.287 to 117.216 ms**
and inhibitory rise from **165.922 to
207.403 ms**. All other active parameters stay fixed.
This is not an exact rise/decay label swap: its sorted pole values also differ.
Its worst full-waveform relative difference is
**3.8662%**, within the predeclared 5% gate.

The elementary cascade equations give
`H_i(s)=1/((1+s*tau_r_i)*(1+s*tau_d_i))`. The pole sum changes by only
**0.7476%**, and the product by
**-6.25%**. This supplies a concrete
mathematical explanation for near compensation, especially at low frequencies;
it is a **post-analysis interpretation**, not an additional search or a changed gate.
[Saved interpretation](../results/t5_mixed_parameter_sensitivity_v1/compensation_interpretation.json).

The intermediate inhibitory filter changes by up to
**14.847%**, but
the filtered E/I conductance supplied to the voltage equation changes by only
**2.174%**.
The candidate therefore **does not reach the prospectively declared 10%
conductance-change diagnostic**. The result is parameter compensation in one
cascade, not evidence of substantially reorganized excitation/inhibition.
The secondary mean-direction diagnostic remains 9/9 bar pairs and 0/4 grating
pairs for both baseline and candidate: this finding does not fix weak grating means.

![Every candidate and feature](../results/t5_mixed_parameter_sensitivity_v1/figures/feature_errors.png)

![Equivalence gates](../results/t5_mixed_parameter_sensitivity_v1/figures/equivalence_gates.png)

![Closest material candidate diagnostic](../results/t5_mixed_parameter_sensitivity_v1/figures/closest_material_candidate.png)

The closest-candidate plot shows its worst primary-feature trial, rather than a
selected favorable condition. Relative feature errors use the declared 0.065-mV
denominator floor; all baseline primary features exceed it. Conductance errors
are normalized per trial and E/I channel using their baseline peak, with a
1e-12 floor. This is a model mechanism diagnostic, not measured synaptic activity.

## Validation and preservation

Eight focused tests passed (seven rule tests and one loader integration check).
The first execution stopped before any responses because its loader used
`ROOT[path]` instead of `ROOT/path`. The frozen runner and failure remain;
a separately hashed wrapper corrects only that join. No scientific rules or
candidates changed. [Pre-score amendment](T5_MIXED_PARAMETER_SENSITIVITY_LOADER_AMENDMENT_V1.md).
All **2,210** waveforms
match an independent matrix-exponential solution of the model, maximum
**1.48e-11 mV**. Independent sorted-sample
quantiles and summation reproduce primary features/means within
**3.55e-15 mV**. All pair classes, final
equivalence decisions, waveform metrics and conductance comparisons were
recomputed. [Numerical review](../results/t5_mixed_parameter_sensitivity_v1/independent_review.json).
A supplemental event-split DOP853 audit checks all four internal states in the
52 baseline/passing-candidate trajectories within the declared 1e-8 tolerance.
The initial uncapped dense-output attempt exceeded that tolerance on one state
(1.80e-8); a 1-ms maximum integration step passes the unchanged tolerance.
The original audit source, method and failure are preserved.
[Internal-state review](../results/t5_mixed_parameter_sensitivity_v1/internal_state_review.json),
[failed attempt](../results/t5_mixed_parameter_sensitivity_v1/internal_state_failure_v1.txt),
[refined method](../results/t5_mixed_parameter_sensitivity_v1/internal_state_audit_refinement_v2.json).
Seven predecessor seals and all 12,086 entries passed before execution; final
preservation checks, local Git source checkpoint and immutable sealing complete
the provenance record. [Completion](../results/t5_mixed_parameter_sensitivity_v1/completion.json),
[artifact index](../results/t5_mixed_parameter_sensitivity_v1/artifact_index.json),
[Git checkpoint](../results/t5_mixed_parameter_sensitivity_v1/git_snapshots.json).
The live [progress report](PROJECT_PROGRESS_REPORT.md) remains appendable.

## Scientific meaning and practical next step

The pilot tests a finite set of mathematical model alternatives against a single
fixed model reference. It does not establish exact non-identifiability or rule
out compensation outside this bank. The 5%/0.02 gates do not prove physiological
equivalence. Earlier bar stimulus-window model/recording RMSE remains 2.629398 mV;
grating retained-window RMSE remains 4.020545 mV. These discrepancies were not
optimized away. Weak grating means, random-texture failures, T4, HS/H2 and full-eye
population validity remain unresolved. No independent neurons were added.

Freeze a separate challenge set before evaluating these candidates: new native bar speeds/widths and grating frequencies/phases, with full-waveform/mean readouts. This would test whether the limited equivalence generalizes; existing physiological validation remains confined to one cell.
