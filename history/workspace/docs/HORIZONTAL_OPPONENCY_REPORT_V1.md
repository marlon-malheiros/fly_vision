# Horizontal LPi reconstruction and functional opponency diagnostic, V1

2026-10-27. **Both requested approaches were implemented and executed. Recorded
LPi circuitry corrects the sign of DNp15's mean null-yaw response in this assay,
but neither candidate passes the full frozen advancement rule.** This is a
supported improvement in a model mechanism, with mixed recording agreement.
It does not establish reliable small-turn detection or biological validation.

## Design and provenance

[Frozen protocol](HORIZONTAL_OPPONENCY_PROTOCOL_V1.md),
[configuration](../configs/horizontal_opponency_v1.json),
[pre-response manifest](../results/horizontal_opponency_v1/before_opponency.json),
[Git freeze](../results/horizontal_opponency_v1/git_freeze.json).
Methods were committed at `76e525a` before new candidate responses.

Replayed eight identical sealed image-derived inputs: two dot realizations and
four protocols (yaw, opposed-hemifield translation cue, left-only, right-only).
These are inherited **45 degree/s** dot stimuli, with motion at 2–4 and 9–11 s,
not new 3D walking environments or small-yaw threshold trials. The exact original
modified G3 image arrays remain unavailable. All recordings have previously
been inspected and remain development data, including those named `test` in
the inherited split. No independent physiological dataset was scored here.

Kept the original frontend, all prior graphs/results and baseline parameters
unchanged. Used the inherited 20 ms node pole, chemical gain 0.873579331825114,
drive gain 0.21936608020509474, 10 ms source clock and RK4 1 ms step, with the
original last-1-ms forcing ramp. No neural or observation parameter was fitted.
All eight original reporter/compartment mappings were transferred unchanged.

| Model copy | Definition |
|---|---|
| Expanded control | Sealed 13,618-cell chemical graph and responses |
| Recorded LPi | Append six MaleCNS LPi12/LPi21 cells; 13,624 cells total |
| LPi silent | Same enlarged weights/normalization, all six added cells clamped |
| Functional diagnostic | Original expanded graph with a fixed balanced opponent T4/T5-to-HS/H2 input block |

The LPi bodies are 10066, 10308, 10436, 11041, 11709 and 13310. The previously
audited raw export supplies **22,338 included connection pairs / 276,577
synapses** involving these cells, including selected feedback and recurrent
partners. Retained every old-to-old integer count. **137,516 incident pairs /
322,776 synapses** lead outside this selection and remain omitted, with a full
ledger. These figures describe six selected cells, not the complete LPi system.

The six cells have GABA consensus predictions, with confidence 0.895–0.906;
negative outgoing signs follow that annotation under the inherited sign rule.
The common pole, count-to-weight normalization, receptor action and effective
strength remain modeling assumptions. No electrical connection or conductance
was invented. MaleCNS LPi12/LPi21 labels are not interchangeable with similarly
numbered FlyWire types or the vertical LPi3–4/4–3 pathway.

The functional diagnostic replaces each direct HS/H2 input pool by its original
total weight times a preferred-minus-null activity difference, separately for
source eye and T4 versus T5. HS uses a minus b; H2 uses b minus a. Preferred
weights retain relative recorded weighting; the opposite pool is uniformly
averaged. This creates **artificial effective signed weights**, removes that
block's off-axis excitation and changes null spatial pooling. Its balanced
unit coefficient was frozen without response fitting. It tests computational
sufficiency, not a biological reconstruction or LPi conductance.

[Graph build](../results/horizontal_opponency_v1/graph_build.json),
[included connections](../results/horizontal_opponency_v1/included_lpi_edges.csv),
[omissions](../results/horizontal_opponency_v1/omitted_lpi_edges.csv),
[functional definitions](../results/horizontal_opponency_v1/functional_pool_definitions.json).

## Response changes and mechanism

The table averages four seed/side cases. Responses are signed tanh deviations
in arbitrary model units, after local baseline subtraction and averaging each
full two-second motion epoch. Positive unwanted/desired ratios are clipped at
zero only in the numerator; signed amplitudes are retained in the evidence.
Ratios measure unwanted response size, not detection accuracy or false positives.

| Copy | Desired yaw | Null yaw | Positive null/desired | Regressive/forward translation ratio |
|---|---:|---:|---:|---:|
| Expanded control | 0.012653 | +0.002516 | 0.19882 | 0.74223 |
| Recorded LPi | 0.008489 | -0.000616 | 0.00000 | 0.62360 |
| LPi silent | 0.008701 | +0.001130 | 0.12982 | 0.73473 |
| Functional diagnostic | 0.010810 | -0.006448 | 0.00000 | 0.21265 |

Both active approaches reduce both unwanted/desired ratios in **all four
seed/side cases**, while keeping desired yaw and forward-translation means
positive. Recorded LPi changes mean null yaw from excitation to suppression in
all four cases. Desired yaw becomes about 33% smaller, and forward translation
about 44% smaller, versus expanded control. The regressive translation response
remains positive: the improvement is partial, not elimination of that mismatch.
The functional diagnostic suppresses null yaw much more strongly and reduces
regressive contamination further, but also changes response amplitude and bIPS.

**The LPi activity effect is distinguishable from normalization.** In the same
enlarged graph, silencing LPi leaves null-yaw means positive in all four cases
(+0.00103 to +0.00126); activating them makes those means negative (-0.00054 to
-0.00069). Thus the sign change requires the added cells' activity within these
equations. Normalization alone already reduces amplitudes and null/desired
ratios, so attributing the entire improvement to transmitted inhibition would
be incorrect. This six-cell intervention does not isolate a single edge route
or prove biological causality.

HS/H2 null responses also become near zero or slightly negative with LPi;
the functional control produces stronger negative responses. The raw arrays
retain both sides, all four recorded groups, full time courses and source-role
currents. These are model deviations; neither negative calcium fluorescence
nor signed tanh values constitute a calibrated voltage measurement.

[All raw epochs](../results/horizontal_opponency_v1/neural_epochs.csv),
[per-case ratios](../results/horizontal_opponency_v1/unwanted_response_ratios.csv),
[bilateral asymmetry](../results/horizontal_opponency_v1/bilateral_asymmetry.csv),
[neural time courses](../results/horizontal_opponency_v1/figures/neural_timecourses.png),
[ratio figure](../results/horizontal_opponency_v1/figures/unwanted_response_ratios.png).

## Recording agreement: improvement and regressions both retained

Skill is `1 - model_MSE / zero_response_MSE`. Positive means better than a
zero-response predictor under that measurement mapping, not physiological
validation. Mean and median aggregate individual-fly skills. Pooled skill is
the ratio of equal-fly mean errors and gives larger-response flies more influence
on the resulting ratio. These estimands answer different questions.

Primary DNp15/GC6f/WT: **all five flies and four motion protocols retained**.

| Copy | Mean fly skill | Median fly skill | Pooled-error skill |
|---|---:|---:|---:|
| Expanded control | -0.25730 | +0.34686 | +0.33117 |
| Recorded LPi | +0.09978 | +0.37853 | +0.27114 |
| LPi silent | +0.05253 | +0.36367 | +0.27251 |
| Functional diagnostic | +0.09060 | +0.45583 | +0.31604 |

The mean becomes positive with both approaches, but the pooled result worsens.
The low-response fly 240221/1 improves from -2.84770 to -0.91798 with recorded
LPi, while the large-response fly 240212/2 worsens from +0.34441 to +0.22804.
No fly was removed. Even the silent normalization control improves the mean,
so the mean sign change is not sufficient evidence of a specific LPi rescue.
Per-fly errors, leave-one-out summaries and bilateral/unilateral results are
retained, rather than selecting the most favorable statistic.

Primary bIPS/sytGC7f mean full-waveform skill falls from **+0.45738** to
**+0.32544** with LPi, +0.33880 with LPi silent, and +0.36961 with the functional
diagnostic. Its magnitude selectivity index nevertheless moves closer to the
known measured mean: observed +0.15599; control +0.16160; LPi +0.15382;
LPi silent +0.15262; functional +0.14255. Matching one selectivity index can
coexist with worse full-waveform agreement.

DNp15's magnitude index also remains quantitatively mismatched: observed
-0.26170; control -0.63536; LPi -0.64982; LPi silent -0.67051; functional
-0.58398. Opposite-direction suppression therefore does not repair every
rotation-versus-translation measure.

[Primary summaries and every fly](../results/horizontal_opponency_v1/primary_waveform_summary.json),
[936 waveform comparisons](../results/horizontal_opponency_v1/waveform_metrics.csv),
[bilateral/unilateral summaries](../results/horizontal_opponency_v1/transfer_summary.json),
[per-motion shapes](../results/horizontal_opponency_v1/primary_motion_waveforms.csv),
[selectivity results](../results/horizontal_opponency_v1/selectivity_summary.json),
[summary figure](../results/horizontal_opponency_v1/figures/waveform_statistics.png).

## Frozen decision and numerical verification

**No candidate passes the complete advancement rule.** Recorded LPi passes the
unwanted-ratio, desired-sign, DNp15 median and bIPS index checks, but fails the
DNp15 pooled-error nondecrease check. The functional diagnostic also fails the
bIPS index check. The LPi-silent control fails the complete ratio condition
and pooled-error check. These rules were fixed before candidate responses and
were not changed after seeing the positive mean skills.
[Machine-readable decision](../results/horizontal_opponency_v1/decision.json).

Completed **24 new network cases**, **8 reused controls**, a control parity
replay and **6 numerical reference cases** (three new variants at 1 and 0.5 ms).
Every shared control array is bitwise identical to the sealed parent. Independent
raw-count, sign, normalization, artificial-block and clamp audits pass.
Python RK4/checkpoint/current checks pass for all 32 comparison cases, maximum
error 2.78e-17. All three 1-ms reference replays are bitwise identical to
production. With the same 1-ms forcing ramp, half-step maximum rate error is
2.18e-10 and maximum saved-state error 9.22e-10, below frozen tolerance 1e-7.
This refinement check covers one yaw input per candidate, not every stimulus
at every numerical resolution.

Independent measurement checks reproduce 234 recording summaries and 936
waveform comparisons; independent aggregation reproduces 3,300 fly indices
and 714 bootstrap summaries. Separate checks reproduce 512 neural epoch rows,
64 ratios, all primary per-fly summaries/decisions, 288 primary motion-shape
rows and 128 bilateral-asymmetry rows. Three PNG/PDF figure pairs were reviewed.
Numerical reproducibility is established for these checks; biological accuracy
does not follow from it.

One pre-outcome reporting bug is preserved: the first preflight receipt printed
13,618 added pairs because a variable was reused after its count checks. The
actual checks and graph were correct. R2 records 22,338; both receipts and the
original source are retained. Correction preceded the experiment freeze and
changed no scientific criterion or response. The report check also caught a
double-rounded silent-control mean (+0.05254 instead of +0.05253) and bIPS LPi
mean (+0.32543 instead of +0.32544) in the unsealed draft; draft and both failure
receipts are preserved. No neural execution failed.

[Corrected preflight](../results/horizontal_opponency_v1/preflight_review_r2.json),
[original count-label receipt](../results/horizontal_opponency_v1/preflight_review.json),
[checkpoint/current review](../results/horizontal_opponency_v1/neural_review.json),
[solver refinement](../results/horizontal_opponency_v1/numerical_review.json),
[measurement review](../results/horizontal_opponency_v1/measurement_review.json),
[aggregation review](../results/horizontal_opponency_v1/aggregation_review.json),
[new-analysis review](../results/horizontal_opponency_v1/analysis_review.json),
[supplementary arithmetic](../results/horizontal_opponency_v1/supplementary_review.json).

## Experimental interpretation and next alternatives

The reduced unwanted response is qualitatively consistent with the motivation
for motion-opponent inhibition. Published LPi experiments support opponent
computations, but vertical-circuit physiology does not supply the missing
horizontal MaleCNS receptor strengths or time constants. [Ammer et al. (2023)](https://www.nature.com/articles/s41593-023-01443-z).
Connectomic motion integration provides anatomical context, not an automatic
conversion from synapse counts to functional strength. [Shinomiya et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/35839763/).
The downstream combination of excitation and disinhibition is motivated by
the Erginkaya recordings, but our mixed waveform/index results are insufficient
for quantitative agreement with that study. [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9).

Recommended next: preserve LPi V1 as a mechanistic candidate and resolve the
amplitude/measurement question with a separately frozen, calibration-only
observation-scale comparison plus independent voltage-response constraints.
Use independent quantitative targets for confirmation, record any prior
qualitative source inspection, and keep the unchanged controls in the comparison.
Do not call a gain fitted to these known flies a new physiological validation.

Alternative: acquire independently measured horizontal LPi/HS/H2 dynamics or
receptor constraints, then revise the physiological mapping in a new version.
Raw data may be unavailable; predeclared digitization with uncertainty is an
external evidence option. Another alternative is new small-yaw walking trials
with LPi V1 as an explicitly unvalidated candidate; those would test functional
generalization, not remove the physiological limitations. A neural gain sweep
chosen to maximize yaw scores is not justified by this result.

Experimentally testable hypotheses include reduced HS/H2 and DNp15 null-motion
suppression after selective horizontal LPi perturbation, with preferred and
regressive responses measured together. The computational six-cell clamp is
not proof that a matching biological intervention would produce its effect.
Missing electrical synapses, incomplete surrounding circuitry, qualified
uLPTCrn/H2rn identities, compartment/indicator mappings and behavioral-state
variation remain unresolved. No autonomous agent or closed-loop controller was
implemented, and no new false-positive rate, small-yaw threshold or directional
accuracy is claimed.

## Reproduction and plain-language explanation

Code: [driver](../scripts/horizontal_opponency_v1.py),
[independent reviewer](../scripts/review_horizontal_opponency_v1.py),
[analysis](../scripts/analyze_horizontal_opponency_v1.py),
[archive/review utility](../scripts/finish_horizontal_opponency_v1.py),
[functional operator](../src/male_optic_frontend/horizontal_opponency_v1.py).
Use the sibling project's Python environment with `PYTHONPATH=src:scripts`,
`OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. The execution sequence in a fresh
versioned destination is setup, unit test/preflight, freeze/Git checkpoint,
parity, run, transfer-only fit initialization, score, analyze/figures and all
review actions, then report/archive/seal and postseal in a separate process.
The committed destination intentionally refuses overwriting existing evidence.
Parent inputs, exact sources, compiled solvers and environment versions are
hashed in the archive. See the completion index for all numerical arrays.

**What we wanted:** a fly visual circuit that detects small accidental turns
while the animal walks forward, for reasons consistent with real neurons.
**What we did here:** added real candidate inhibitory wiring, and separately
tested a simple direction-subtraction rule. Both improved the response to the
opposite turn direction. **Why it matters:** we now have evidence for a specific
missing computation rather than another unexplained score change. The model
also weakened useful responses and matched some recordings less well, so this
is a partial mechanism improvement, not a finished small-turn detector. The
next useful evidence should constrain response size and physiology, rather
than repeatedly adjusting the model until its score looks good.
