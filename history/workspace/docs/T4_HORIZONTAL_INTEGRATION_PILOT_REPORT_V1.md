# Horizontal T4 integration pilot V1

2026-11-04. **Decision: STOP this candidate without retuning. Biological validation: incomplete.**

## Question and frozen scope

Does one fixed integration of the published2022 T4 mechanism improve known HS
frequency responses and opposite-direction suppression without losing the prior
contrast result? The [protocol](T4_HORIZONTAL_INTEGRATION_PILOT_PROTOCOL_V1.md)
and code were frozen at `c92b600` before new candidate outcomes. The recording
targets and earlier standalone source results were already inspected. This is
development evidence, not fresh held-out physiological validation.

Fifteen input cases and18 neural solves completed: eight preferred/null frequency
conditions, two half-contrast conditions, one stationary pattern and four finer
clock cases; additional half-solver, horizontal-sampling and exact baseline
replay solves. There was one candidate, no parameter search or revised threshold.
The original graph, numerical neural parameters, decoder and earlier results
remain unchanged. Complete [decision](../results/t4_horizontal_integration_pilot_v1/decision.json)
and [comparison](../results/t4_horizontal_integration_pilot_v1/comparison.json).

## Integration feasibility and assumptions

The independently reproduced [Gonzalez-Suarez et al.2022 source](https://doi.org/10.1016/j.cub.2022.06.075)
was connected to **3374 horizontal T4a/b sources** across both eyes. All
other source columns retain the frozen slowing-only functional frontend.
Measured input filters and author relative conductances/reversals remain fixed.
No calcium trace is injected: the bridge is max(model voltage,0)/60, where60mV
is the author model's positive driving force. Nonnegative conductances bound
this quantity in[0,1]. No condition-specific scale or fitted gain is added.

This is a **computationally feasible but biologically uncalibrated bridge**.
The reversal bound does not measure synaptic release or establish the correct
relative T4/T5 gain in MaleCNS. An unsuccessful result cannot distinguish a wrong
mechanism from incorrect coupling, normalization, routing or spatial embedding.
The older published-frontend experiment also used driving-force normalization;
that principle is not a new biological discovery. The new element here is a
narrow integration of the2022 measured, input-specific parallel-inhibition model.

The source's1D horizontal template is applied only to the vertical gratings used
here. All in-field elevation rows share one temporal profile, and all out-of-field
rows share grey; original bilinear row weights handle the boundary. No vertical
receptive-field width, vertical T4 model or T5 physiology is invented. The
Gaussian needs support wider than the old173deg raster near edge cells, so a
full360deg horizontal profile is sampled from the same known analytic display,
with the inherited eye chart. The display is identical; receptive-field support
differs. Anatomical eye coverage and these subtype-direction mappings remain
assumptions rather than newly verified connectivity.

FIR prehistory equals the actual initial static image. Static T4 activity is
allowed; no source-baseline subtraction is introduced to force a desired output.
The network retains2s static initialization and its old zero state. Source
fraction range is[0,0.397903], initial static maximum
0.220797, with no clipping. T5 gain and dynamics are unchanged. This is
a partial hybrid frontend, not a full physiologically reconstructed circuit.

## Frequency responses

Ratios use each model's own right-HS preferred1Hz response. The HS observation
is mean HSN/HSE/HSS atanh(rate), motion[2,4)s minus static[1,2)s.
This remains an arbitrary-unit graded-state proxy, not calibrated HS membrane
voltage. Reference normalization removes an overall scale, not uncertainty about
the measurement model or recorded/model cell-population correspondence.

| Variant | Frequency normalized RMSE | Coordinates outside retained band |
|---|---:|---:|
| none | 0.661121 | 7/7 |
| slowing_only | 0.313121 | 6/7 |
| adaptation_only | 0.700675 | 6/7 |
| both | 0.398686 | 4/7 |
| Horizontal T4 patch | 0.297220 | 4/7 |

The continuation rule requires both error and count to be no worse than the
best prior values, even when different prior models set the two bounds. It was
not chosen after seeing these outcomes. The source bands remain conditional
descriptive comparisons with previously documented recording/label limitations;
they are not new animal-level equivalence or confidence claims.

| Hz | Recorded PD | Candidate PD | Recorded ND | Candidate ND |
|---|---:|---:|---:|---:|
| 0.5 | 1.068203 | 0.609996 | -0.355941 | -0.105899 |
| 1 | 1.000000 | 1.000000 | -0.299986 | -0.144403 |
| 2.5 | 0.676028 | 1.221711 | -0.045738 | -0.039126 |
| 15 | 0.076436 | -0.069478 | -0.070846 | -0.121747 |

A further adverse result is a negative preferred-direction motion-minus-static response at [15.0]Hz, while the recorded preferred means are positive. This qualitative sign mismatch must remain visible even if aggregate error improves. It is reported descriptively, not added retrospectively to the frozen guards. The pilot cannot establish whether source dynamics, tonic static activity, inherited wiring or the uncalibrated coupling causes it.

![Matched frequency comparison](../results/t4_horizontal_integration_pilot_v1/integration_comparison.png)

## Opposite-direction, contrast and stationary controls

Full-contrast ND1Hz/PD1Hz=-0.144403, recorded contrast
ratio-0.330100. Its absolute error is
0.185697; the best prior error is
0.248387. This quantity is separately judged
from aggregate frequency RMSE, so one improvement cannot hide the other failure.

At half contrast, preferred/full=0.739503 and
null/full=-0.097801; retained-band membership is
PD=False, ND=True.
Stationary HS endpoint=2.76745e-08 arbitrary model
units, PD1Hz reference=0.0103502. Baseline drift and
stationary endpoints use their frozen5%-reference limits. This is a stability
control, not a turn-decoder false-positive rate. No walking stimulus or2deg/s
turn detection was tested in this pilot.

| Frozen continuation guard | Result |
|---|---|
| numerical | Pass |
| images and baseline sources match | Pass |
| one bitwise neural replay | Pass |
| other source columns bitwise | Pass |
| source range and zero clipping | Pass |
| positive PD1 | Pass |
| stationary endpoint | Pass |
| baseline drift | Pass |
| frequency rmse | Pass |
| frequency violation count | Pass |
| null suppression error | Pass |
| half contrast both inside | **Fail** |

Both favorable and unfavorable values are retained. Bilateral HS/H2/bIPS/DNp15
group responses are provided in [CSV](../results/t4_horizontal_integration_pilot_v1/group_responses.csv),
but they are exploratory summaries without new physiological acceptance tests.
The HS role-wide CSV pools all same-side HS cells; the scored endpoint uses the
three named subtypes above. No circuit lesion or biological causal attribution
is inferred from changing source dynamics.

## Numerical verification and resources

| Case | Refinement | Difference / primary PD1 reference | Result |
|---|---|---:|---|
| frequency_x0.5_d0_fine | temporal | 0.027348% | Pass |
| frequency_x1_d0_fine | temporal | 0.039631% | Pass |
| frequency_x15_d0_fine | temporal | 0.044309% | Pass |
| contrast_x0.5_d180_fine | temporal | 0.007874% | Pass |
| PD1 | solver | 0.000000% | Pass |
| PD1 | horizontal_sampling | 0.894271% | Pass |

All14 corresponding image and full baseline-source hashes reproduce exactly;
the stationary functional source is zero. Every non-T4a/b input column remains
bitwise identical. One complete baseline replay matches retained neural rates,
final states and checkpoints bitwise. Six comparisons preserve the old5%
tolerance: four joint image/source clocks, one horizontal sampling check and
one solver check. These are limited convergence tests, not proof for every image,
spatial wavelength or environment. The inherited absolute1ms network forcing
ramp remains unchanged; no closed-loop causality certification is implied.

Three focused tests passed before freezing: constant-history causal FIR versus
independent direct filtering, voltage/calcium algebra and reversal bounds with
mirror symmetry, and coordinate interpolation. Independent scalar log1p/fsum
arithmetic rechecks all15 HS endpoints (maximum difference1.73e-18),
frequency RMSE/count, null error and continuation guards. All per-case CPU
receipts reconcile; their failure fields are empty.

Case CPU before receipt writes1232.349s and including those
writes1232.358s, both below1800s; peak RSS
1,254,825,984bytes below3GiB. The run contains compact wide-neuron
arrays and hashes, no movies or permanent full-source arrays. Exact final package
bytes appear in the post-exit integrity receipt. Previous59-file source study,
230-file temporal study and frozen graph/decoder dependencies are rehashed;
this does not include intentionally retired historical movies.

## Decision and next alternatives

**STOP this candidate without retuning.** Failed guards: half_contrast_both_inside.
The fixed criteria remain in force; no gain search, extra condition, coupling
adjustment or decoder refit follows this result inside the pilot.

If this candidate stops, preserve the original functional small-turn model and
this negative integration result. The next alternatives are: resolve the
unmeasured coupling/contrast normalization using matched physiological evidence,
or retain the functional detector with clearly limited biological claims. A new
calibration must have separate unused validation conditions. Do not repeat a
wide yaw sweep or consume uninspected recordings while this integration fails
its development guards. Previous full published T4/T5 population attempts and
their heterogeneous failures remain relevant controls, not untried suggestions.

If it qualifies, only a separately frozen development extension is authorized;
qualification does not validate the complete model. Missing electrical synapses,
upstream anatomy/CT1 localization, T5 physiology and coupling calibration remain.
No new release, anatomical connection, conductance or cellular identity was
invented to obtain the expected response.

## Reproduction and undergraduate explanation

Use the scientific interpreter in environment.json, PYTHONDONTWRITEBYTECODE=1,
OPENBLAS_NUM_THREADS=1 and the indexed local dependencies. In an isolated fresh
result revision, run the three focused tests and
`scripts/t4_horizontal_integration_pilot_v1.py prepare`, `run`, `analyze`.
Run this reporting script once, then the pilot's `seal` and `audit` stages.
Exclusive writes prevent overwriting the sealed evidence. The presentation
script is captured before indexing; no network access is needed for these runs.

We want a small-turn detector whose neurons also behave like real fly neurons.
Here we connected one published mechanism to our actual network, using one fixed
conversion and keeping the rest unchanged. We checked whether it fixes several
response properties together. The result tells us whether this particular
connection deserves further work; it does not prove or disprove the real fly's
mechanism or establish a biologically validated walking model.

## Presentation completion correction R2

The initial presentation script completed the report and independent scalar review, then failed while formatting the live progress entry because a file-handle variable shadowed the frequency-score dictionary. The failed source and error are preserved. A corrected presentation source and this separate completion script finish reporting without rerunning any model, overwriting numerical evidence or changing criteria. Model execution has zero failures; this one postprocessing failure is recorded separately.
