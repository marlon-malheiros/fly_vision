# Active T5 sensitivity and E/I compensation — technical report V1

Client date: 2026-10-12 (America/Belem); saved timestamps use UTC.

**Decision: `NO_MATERIAL_OUTPUT_EQUIVALENCE_IN_LOCAL_BANK`.** Sensitivity interpretation provisional:
**False**. None of the generated material alternatives preserves all declared outputs. This finite, local algorithm does not prove that broader compensation is impossible.

## What changed and what the analysis can establish

The preceding [challenge](T5_COMPENSATION_CHALLENGE_REPORT_V1.md) validated a
two-inhibitory-pole timing alternative. Here we ask whether response preservation
also permits substantial changes in final excitation/inhibition. All **78** old
and challenge bar/grating inputs are retained, with their previous windows and
clocks. Stack 78 primary scores and 78 signed means into **156** features.
Baseline responses replay bitwise in all 78 conditions.

The ten coordinates exclude the unused parameter and sort poles within each
cascade to quotient exact label swaps. Eight positive coordinates use log ratios;
two centers use native-column differences. Scale feature rows by
max(abs(baseline),0.065 mV). Singular values depend on this normalization and units;
they are not experimental confidence intervals or global identifiability tests.
[Frozen protocol](T5_ACTIVE_SENSITIVITY_PROTOCOL_V1.md),
[methods hashes](../results/t5_active_sensitivity_v1/prospective_manifest.json),
[benchmark](../results/t5_active_sensitivity_v1/benchmark.json).

No physiological observations were refitted. Candidate generation is an explicit
**model-guided local search**: linear compensation is computed against the
baseline model's outputs, on the same stimuli subsequently used for screening.
The algorithm was frozen before derivatives; the derived parameter bank was
hashed before candidate scores. This is not held-out biological validation.
Repeated stream interruptions occurred during development and later execution.
Saved files and on-disk logs allowed work to resume; completed simulations were
retained. No scientific rule or previously completed evidence changed.

## Local sensitivities

Central differences at h=0.005 and 0.0025 yield relative Frobenius discrepancy
**1.1015%**; maximum column discrepancy
**4.6008%**. Declared step-stability gate:
**True**. The smaller-step matrix generates candidates regardless;
an unstable derivative estimate makes its interpretation provisional, not a
retroactive change in the candidate output gates.

Full matrix numerical rank: **10/10**, singular values
**[29.248703828614573, 7.5768754197061545, 5.790516524780349, 4.4936722117782395, 2.112445885781235, 1.2143766542589949, 0.9507696201392551, 0.44836431789398173, 0.10249852139148924, 0.04775711428773556]**. Gain/width/center-only rank:
**6/6**, singular values **[29.223855930207954, 5.779002432041419, 3.8129111740605595, 3.282278857001922, 1.0615837967619839, 0.45790331901925196]**.
Numerical rank uses a machine-epsilon cutoff; even a full-rank matrix can contain
weak directions. A small singular value is a local sensitivity result, not proof
of an exact output null space. Clock-free analysis prevents timing flexibility
alone from answering the E/I question.

| Coordinate | Column sensitivity norm | Relative step change |
|---|---:|---:|
| e_fast_pole | 0.177288 | 4.6008% |
| e_slow_pole | 4.316 | 0.9828% |
| i_fast_pole | 4.42238 | 2.2129% |
| i_slow_pole | 4.62364 | 2.2477% |
| gain_e | 17.5205 | 0.1322% |
| gain_i | 13.7566 | 0.2626% |
| sigma_e | 15.6331 | 1.7715% |
| sigma_i | 12.4712 | 0.4965% |
| center_e | 2.56147 | 2.5979% |
| center_i | 3.3739 | 2.8262% |

![Singular values](../results/t5_active_sensitivity_v1/figures/singular_values.png)

![Weak coordinate directions](../results/t5_active_sensitivity_v1/figures/weak_directions.png)

## Fixed derived bank and actual nonlinear responses

40 prescribed alternatives: 12 full-SVD, 12 gain/spatial-SVD, eight gain-constrained
spatial least-squares and eight gain-constrained full ridge-compensation sets.
Gain patterns are common scaling or opposite changes, at ±log(1.1)/±log(1.25).
The three references are not new candidate wins. **40**
candidates satisfy bounds; **0** are rejected without
clipping/replacement. Rejected IDs: **[]**.
[Derived bank](../results/t5_active_sensitivity_v1/derived_candidate_bank.json),
[post-derivative, pre-score hashes](../results/t5_active_sensitivity_v1/derived_manifest.json).

Each primary/mean score must remain within 5%, every paired DSI within 0.02 and
all 39 pair classes preserved per readout. Each full trace must differ by ≤5% of
its baseline maximum magnitude. Material distance retains the earlier ≥1.25
change in two canonical positive coordinates or ≥0.5-column center shift.
Both-channel mechanism change requires E and I each to differ ≥10% in final
conductance somewhere in the benchmark; intermediate states and labels do not
qualify. Maxima can occur in different trials and are not measured synaptic data.

| Candidate family | Planned | Valid | Material | All outputs equivalent | Material equivalent | Both E/I ≥10%, material and equivalent |
|---|---:|---:|---:|---:|---:|---:|
| full_svd | 12 | 12 | 2 | 9 | 0 | 0 |
| strength_svd | 12 | 12 | 2 | 1 | 0 | 0 |
| spatial_only | 8 | 8 | 4 | 0 | 0 | 0 |
| full_ridge | 8 | 8 | 4 | 0 | 0 | 0 |

New material output-equivalent sets:
**[]**. Both-channel candidates:
**[]**; either-channel candidates:
**[]**.

No generated material candidate satisfies every output gate.

The closest generated set by the worst primary/mean/waveform margin ratio is
**`full_svd_v0_a0_+1`**: primary **0.6507%**,
mean **0.4896%**, waveform
**0.6361%**, E conductance
**0.2267%**, I conductance
**0.3731%**. This post-analysis ranking
does not replace any failed pair or material/mechanism criterion. All scores,
failure indices and pair classes are retained in
[full scores](../results/t5_active_sensitivity_v1/candidate_scores.json) and
[compact CSV](../results/t5_active_sensitivity_v1/candidate_summary.csv).

![All valid candidates](../results/t5_active_sensitivity_v1/figures/output_vs_conductance.png)

Known timing reference: primary gate **True**, waveform
gate **True**, newly combined mean gate
**True**. Its 78 trajectories replay prior outputs bitwise.
The swapped-pole control preserves voltages to 1e-8 mV and gain mismatch is detected;
neither is included in the new-candidate decision. Preserved weak/reversed baseline
direction classes remain weaknesses, rather than becoming new physiological passes.

## Interpreting the bounded result

Of 40 generated alternatives, **12** meet the substantial-change definition;
none preserves every output gate. **10** smaller alternatives pass all gates.
**11** alternatives change both final conductances by at least 10%, and none
passes all response gates. No candidate is rejected solely because of pair
classification while passing all scalar 5% margins: the larger alternatives
also exceed the declared response-error margins.

The closest **material** candidate is `full_svd_v0_a2_+1`: peak/amplitude
error **11.4062%**, mean
**8.0922%**, waveform
**11.7490%**. Among alternatives
with both conductances changing by ≥10%, the closest is `spatial_only_g0_a0_+1`
(material: **False**): E **10.1102%**,
I **13.4667%**, primary error
**7.8968%**, mean
**6.7299%**, waveform
**8.7824%**, above the 5% margin.
These rankings are post-analysis description, not new acceptance rules.

Under the declared coordinate normalization, **99.681%**
of the weakest full singular vector's squared norm lies in timing coordinates.
This is a property of the normalized local geometry, not a percentage of neural
causation. The gain/spatial-only weakest singular value is larger. The original
finite timing example still passes all 78 inputs; its success does not imply
that larger straight steps along a local singular vector must also succeed.
A linear tangent estimate cannot by itself guarantee finite nonlinear equivalence.
[Saved descriptive context](../results/t5_active_sensitivity_v1/descriptive_context.json).

## Verification and preservation

Eight focused tests passed before freezing. **6,552** executed
trajectories (84 parameter sets) pass independent
matrix-exponential review of voltage and all four states: max voltage error
**6.18e-12 mV**, state error
**7.05e-13**. Independent features and central differences
agree within **1.1e-10 scaled Jacobian units**.
Independent quantiles/means, pair and mechanism decisions, SVD reconstruction and
orthogonality, bank replay and final normal-equation/step checks validate the
computation, not biological validity.
[Numerical review](../results/t5_active_sensitivity_v1/independent_review.json).

All nine predecessor indexes and 12,306 entries remain intact. Save the source
checkpoint and study progress snapshot, then seal outputs and reports.
[Completion](../results/t5_active_sensitivity_v1/completion.json),
[artifact index](../results/t5_active_sensitivity_v1/artifact_index.json),
[Git checkpoint](../results/t5_active_sensitivity_v1/git_snapshots.json),
[live progress](PROJECT_PROGRESS_REPORT.md).

The model's physiological discrepancies, weak grating mean directionality,
texture, T4, HS/H2 and population questions remain unresolved. Neither numerical
verification, near-insensitive coordinates nor a finite negative search establishes
biological degeneracy or publication acceptance. No cells/repeats were added.

Close this bounded E/I search and keep the validated timing-compensation result with its narrow scope. The present bank does not support a stronger both-channel claim. A concrete next step is a short evidence package for the supervisor, stating the numerical successes and the remaining biological/mean-response limits; further expansion should require a new scientific hypothesis or independent data, rather than additional unstructured searching.
