# Three sequential small-turn repair tests V1

2026-10-26. User authorizes testing all recommended routes, in order, and reporting.
This protocol fixes recipes before new outcomes. Original models and sealed
evidence remain unchanged. A completed experiment does not mean the repair goal
has been achieved. No closed-loop control.

## Shared inputs and criteria

Use the same physical renderer and binocular eye geometry as prior walking studies.
Primary retinal lattice: original ±86° eye coordinates, 1° pitch. Generate actual
stationary pre-motion initialization and 5-ms retinal samples through 1.41s;
observe [0.70,1.40)s. Render directly at receptor rays. The image reference and
both frontend versions consume identical primary frames. Source-to-graph input
clock is 10ms and RK4 is 1ms. Retain full input frames/time maps, both delivered
source arrays, wide-cell traces, final states, local estimates and receipts.

Use four previously inspected V2 training rooms with all yaw/speed conditions,
16 previously inspected calibration rooms with straight walking at each speed,
and stationary development controls. Freeze three candidate recipes now; freeze
all standard-stimulus and physiology calibration results and walking decoders
before generating any of 24 fresh test rooms. All test rooms have stationary
control plus three speeds × yaw0/±2/±5°/s. No use of held-out labels for fitting,
cutoff choice, interface selection or route adaptation. Run route development
1→2→3, then evaluate fixed routes in order on the same fresh images. The same
24 rooms support paired comparisons, not three independent replications.

Maintain ≥80% observed detection, ≥80% raw-direction accuracy and ≤10% observed
false alarms, sustained at ±5°/s, separately at each speed. Raw sign includes all
turns. Classify undefined estimates as failures. With 48 turn/24 straight cases:
at least39 detected,39 correct signs and at most2 false alarms. Neural readouts use
the previous standardized ridge decoder (0.001), trained on training rooms only,
with cutoff maximum absolute straight score across16calibration rooms. Geometric
estimates in degrees/s use the already specified engineering boundary1degree/s;
no post hoc threshold search. Separate numerical gates from detection criteria.

## Route 1: local motion encoding

Keep original output routing, graph and neural parameters. Compare unchanged
functional frontend with one engineering contrast-normalized copy. At each retinal
position, divide each original eight-channel response by the pooled sum of squared
ON/OFF contrast, multiplying by a fixed reference energy measured with independent
standard plaid stimuli. Use the same spatial pooling support as the original
frontend. Exactly zero/roundoff energy produces zero output; clip normalized
source drives to [0,1] and retain clipped counts. This is an algorithmic hypothesis,
not reconstructed T4/T5 physiology. Reference energy is not chosen from walking.

Before walking, simulate horizontal and vertical plaid motion at seven specified
velocities and two contrasts with wavelength24°. Fit scalar positive motion-to-
velocity conversions separately for horizontal/vertical raw and normalized signed
fields, with no offset. Use wavelength32° as a separate standard-stimulus check.
Retain all calibration observations, coefficients and errors. These conversions
permit a geometric readout but do not establish general physiological velocity
encoding. Published electrical or physiological units are not inferred from them.

## Route 2: spatial integration

Keep local channels separate before any eye-wide average. At fixed8°spaced sites
over central±56°horizontal/±40°elevation, estimate signed horizontal/vertical
responses in two ways: directly from the functional channel lattice, and only
from the delivered source-cell responses using precomputed4-neighbor inverse-
distance interpolation within12°. Handle exact coordinate matches without
division by zero; mark sites without all required channels unsupported. Preserve
source IDs, interpolation weights and coverage before walking. ON/OFF groups
are averaged equally, keeping anatomical sampling differences explicit.

Use the frozen eye geometry to remove forward flow locally:
u=t_h*rho−sign*omega, v=t_e*rho, so omega=(t_e*u−t_h*v)/(−sign*t_e).
Combine defined local estimates using weights t_e² and the existing weighted median.
Zero-elevation sites have zero weight. No true speed, depth, pose, yaw or paired
straight test episode enters the readout. The separated-eye lever arm is not
removed with ground truth; quantify its known approximation with analytic controls.
This is an explicit geometric engineering readout of functional channels, not
an anatomically demonstrated bIPS or DNp15 computation. Retain lattice and
source-only results separately; one cannot establish information in the other.

Also execute the existing local Lucas–Kanade median image reference on the same
frames, spatial resolution, central support and observation window. Its centered
derivative uses10msfuture data; functional-channel readouts do not. Independently
check the copied LK implementation against the existing reference calculation.
The image control is not fed to the neural circuit and is not a neural repair.

## Route 3: physiology-constrained inhibition

Use the available [Erginkaya2025](https://www.nature.com/articles/s41593-025-01948-9)
source workbooks already archived locally. Calibrate **one** effective inhibitory
weight, uLPTCrn→bIPS (`B_U_ipsi`), within the author's documented signed magnitude
range[-1,0], holding the other published steady-state motif weights fixed. Minimize
squared error to the median control-bIPS bFtoB–yaw DI in Fig4f. Use idealized
canonical signed input patterns and the published range-based definition; positive
linear calcium-response scaling cancels in DI. These recordings/summaries have
been inspected historically: label the calibration exploratory.

Retain a complete1001-point loss profile and independent bounded optimum check.
Use receptor-disrupted bIPS DI with that inhibitory term set to zero, and DNp15
DI from a separate source sheet, as **not-fitted checks**, not fresh-animal
validation. The effective motif is not a conductance model; the receptor
manipulation disrupts more than the one modeled path. Source workbook ROI columns
do not supply all animal identities; no false claim of independent-ROI animals.

Compare published-fixed versus physiology-calibrated copies on identical original
and normalized walking channels. Pool original subtype means into F/B per eye,
then use the fixed signed-opponent interface from the earlier reproduction.
Do not select another interface after observing outcomes. The test is of a
supported effective-weight calibration; recordings of calcium DI alone cannot
justify inventing nonlinear voltage thresholds or electrical conductances.
If the available constraint does not support those additions, document that limit
and still execute the supported calibration and walking comparison.

## Numerical checks, failures and decisions

Check stationary controls, analytical forward/yaw separation, independent finite-
difference flow geometry, source identity/coverage, baseline replay against known
V2 inputs, RK4 half-step on identical drives, and independent Python solver on
fixed controls. Primary source traces must match their baseline replay within
1e-7; independent/half-step neural rates within1e-10. For straight and ±2 fast
walking on one known control room, compare0.5°receptor sampling with unchanged
1°neighbor displacement and3°pooling-radius center extent, and halve temporal
steps. Preserve field/source sampling assumptions; this differs from the older
panorama interpolation refinement with receptor grid held fixed. Geometric yaw
numerical tolerance0.2°/s. Failed gates remain failed and prevent a general
numerically robust detector claim even if classification passes.

Report all methods, roles, speeds, false alarms, sign accuracy, clipping, missing
coverage, standard-stimulus calibration and not-fitted physiology results. Retain
10,000 paired-room bootstrap draws and intervals. Numerical reproducibility does
not establish physiology. A source-channel geometric success is an engineering
result; a successful original-graph output after frontend revision is a model
repair only under this new encoding assumption. Fresh-room results cannot prove
biological causality. Preserve all failures in new namespaces; no rewriting sealed
evidence. Complete the three tests even if an earlier route fails.

Append decisions and results to the live progress report; save a dated copy before
sealing. Exclude live AGENTS.md/progress and post-exit review from immutable indexes.
