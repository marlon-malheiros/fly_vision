# Summary for discussion: yaw detection and bIPS

24 October 2026. Synthesis of completed open-loop studies; no new model fitting.

We asked whether a MaleCNS-based visual model can distinguish a small body turn
from straight forward walking, and whether bIPS helps. We simulated binocular
views of 3D environments at three walking speeds, compared intact and perturbed
circuits using identical inputs, and tested separate rooms that were excluded
from decoder training and calibration.

**The model contains yaw-dependent signals, but reliable small-turn detection
across the tested speeds and environments remains unestablished.** In the larger
40-room test, the original DNp15 readout detected ±2°/s turns in 46/80, 26/80 and
14/80 cases at 5.5, 11 and 16.5 mm/s. It also falsely reported turns during
straight walking in 6/40, 8/40 and 6/40 rooms, exceeding the frozen 10% allowance
at every speed. The earlier 20°/s fast-walking threshold in six rooms did not
survive finer image sampling. It should be described as a preliminary result
at the original resolution.

**bIPS changes DNp15 response strength and balance within the model.** At fast
walking, silencing bIPS increased false alarms from 6/40 to 14/40 with the same
readout. Its effect was not uniformly beneficial at other speeds. Substantial
yaw-dependent response remained after silencing, and earlier lesion-specific
recalibration recovered the fast threshold. These results support a role in
shaping the signal, without establishing that bIPS is indispensable for yaw
information or proving biological causality. Adding 25 anatomically supported
candidate recurrent neurons did not establish a consistent improvement.

The next priorities are to resolve image-sampling sensitivity, establish a
matched image-to-recording comparison using verified cell identities and an
explicit calcium/voltage measurement model, and test how bIPS perturbation
changes bilateral DNp15 responses during both straight walking and turns.
Electrical coupling and walking-related nonvisual inputs remain unresolved
biological constraints. The current visual-only model tests rotation; it has no
signal specifying whether a turn was intended.

The contribution is a reproducible set of response and perturbation predictions,
with identified failures that guide the next experiments. Physiological validity
and reliable robot steering remain future objectives.

[Evidence report, figure and numerical checks](YAW_BIPS_EVIDENCE_SYNTHESIS_V1.md)

**In simple terms:** we built and checked a model that responds to turning, found
that it still confuses some straight movement with turns, and identified how
bIPS changes that response. We now know which claims need stronger numerical
and biological tests before using the model to guide a robot.
