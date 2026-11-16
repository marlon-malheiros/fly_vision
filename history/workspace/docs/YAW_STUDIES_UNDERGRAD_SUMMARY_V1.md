# What we did, what we want to learn, and why

Completed 2026-10-19. Undergraduate explanation of the two open-loop studies.

A fly moving forward sees objects slide across its eyes. If its body also turns left or right, that turn adds another pattern of image motion. We want to understand whether its visual circuit can separate a small unwanted turn from the much larger motion caused by walking forward. This matters because a useful steering signal must detect a turn without repeatedly reporting turns during straight walking.

HS, H2, bIPS and DNp15 name identified neuron classes or families. HS is a family of horizontal-system visual neurons; H2 is another motion-sensitive type. bIPS is an inhibitory interneuron class, and DNp15 is a descending neuron type that can carry signals toward motor circuits. Our original model represents eight HS cells and two cells in each other class, with cells on both anatomical sides. These names are not four entire brain regions.

## What we did

In Study A, we preserved the existing image-processing frontend, connectome and numerical parameters. We rendered separate images for the two eyes as a virtual observer moved through twelve independently generated 3D rooms. It moved forward at three speeds, with small leftward or rightward yaw rotations added. Yaw means turning around the vertical axis. We also included straight-walking and stationary controls.

We passed each image sequence through the same frozen model and compared left/right neural responses. Copies of the model had bIPS silenced, selected bIPS outputs removed, or HS/H2 silenced. Every copy received the same input. These comparisons isolate consequences of changes inside the computer model.

A small statistical readout learned response patterns from three rooms. Three different rooms set its false-alarm cutoff. Six unseen rooms tested performance. The readout was told which walking speed applied; it did not receive the answer about yaw. We kept every error and checked whether smaller numerical timesteps changed the conclusions.

In Study B, we used recorded anatomical evidence to add 25 candidate homologs from two missing recurrent neuron families, uLPTCrn and H2rn. We repeated the same visual experiments and tested the added families by silencing them. We also compared explicit model summaries with published physiological endpoints, keeping the previous calibration and validation flies separate.

## What the detection numbers mean

The table gives DNp15 thresholds in degrees per second. A threshold had to achieve at least 80% detection and 80% correct yaw signs, with no more than 10% straight-walking false alarms, at that magnitude and every larger tested magnitude. “Unresolved” means false alarms prevented a threshold claim. “≤2” only means the smallest tested turn passed. These are results across six virtual test rooms, not sensory thresholds measured in real flies.

| Walking speed (mm/s) | Original model | Expanded model, original readout | Expanded model, recalibrated readout |
|---:|---|---|---|
| 5.5 | unresolved (FPR 17%) | unresolved (FPR 33%) | unresolved (FPR 17%) |
| 11 | unresolved (FPR 33%) | unresolved (FPR 33%) | unresolved (FPR 17%) |
| 16.5 | 20 (FPR 0%) | 20 (FPR 0%) | unresolved (FPR 17%) |

A larger response after adding a neuron does not automatically mean better detection. Straight-walking responses can also shift and cause false alarms. Likewise, a readout can fail after a lesion even though another readout, trained only on that lesion’s training rooms, can recover information. The detailed reports show both comparisons.

In Study A, DNp15 reached a 20°/s threshold at the fastest walking speed. Slower-speed thresholds were unresolved because of false alarms, and reliable 2–5°/s detection across speeds was not established. Silencing bIPS disrupted the original readout, but recalibrating that readout recovered the fast threshold. This supports a role in balancing the existing signal, rather than proving that yaw information disappears without bIPS.

Adding anatomical detail also did not improve the frozen physiological diagnostic overall. That comparison has unresolved readout alignment: it pools both model sides while recorded neurites are hemisphere-aligned. The yaw detector still uses separate left/right features. The published-calcium comparison remains a diagnostic with known limitations, not physiological validation.

## What we want next, and why

The long-term objective is a physiologically grounded fly sensorimotor model that produces experimentally testable predictions and eventually controls an autonomous agent. These studies supply response curves and specific perturbation predictions to test first. The model has no motor-intention signal, so it cannot tell whether a turn was intended. It does not yet supply a walking controller.

The main gap is biological grounding. Chemical synapse counts do not specify electrical coupling, every cell’s dynamics, or how modeled activity becomes a recorded calcium signal. Earlier T4/T5 software-transfer successes coexist with physiological discrepancies. We therefore retained the functional frontend and documented where a physiological reconstruction could not be justified, instead of filling the gaps with parameters chosen to improve detection.

The purpose is to learn which computations are supported, which depend on modeling assumptions, and which experiments would distinguish the possibilities. Numerical reproducibility means the calculations can be checked. Physiological validation requires agreement with appropriate independent measurements. Effects of silencing a model neuron are hypotheses about biological circuitry until experiments test them.

[Study A technical report](YAW_SENSITIVITY_ABLATION_REPORT_V1.md) · [Study B technical report](ANATOMICAL_STRENGTHENING_REPORT_V1.md) · [Development progress](PROJECT_PROGRESS_REPORT.md)

## Main finding from the reconstruction

Adding the two candidate neuron families did not establish better reliable detection of small turns. It also changed the model’s numerical input scaling, which explains much of the smaller left–right response difference. The purpose of these studies is to expose such distinctions and produce testable predictions, while identifying the biological measurements needed before building a steering controller.
