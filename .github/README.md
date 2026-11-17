# Fly Vision: optomotor circuitry and embodied testing

Model fly optomotor processing with connectome constraints, test neural and perturbation predictions, and develop an embodied implementation for realistic evaluation.

**Student: [start here](../STUDENT_START_HERE.md).**

The new **[closed-loop optomotor prototype](../optomotor_closed_loop/README.md)** uses real MaleCNS v1.0 chemical connectivity, functional ON/OFF visual inputs and DNp15-driven steering in a virtual robot. Its primary stimulus is a random-square cylindrical display.

- [Exact setup, replay commands and AI prompts](../optomotor_closed_loop/STUDENT_HANDOFF.md)
- [First student task: gain, delay and the disturbance/drift tradeoff](../optomotor_closed_loop/FIRST_STUDENT_TASK.md)
- [Results and scientific limitations](../optomotor_closed_loop/docs/RESULTS_APPRAISAL_R2.md)
- [Reference result figure](../optomotor_closed_loop/results/r2/overview.png)

The completed synthetic benchmark passes its declared engineering checks: 66.4% median yaw-RMS reduction, 0.20 degrees/s median straight-travel yaw RMS, fourteen implementation checks and a separate arithmetic/integrity review. The conventional visual controller achieves 67.2%. Neural-recording validation, a biological architectural advantage and physical field testing remain unestablished. Read the appraisal before interpreting the small bIPS-associated lesion effect.

The next student experiment characterizes gain and added delay with fixed neural weights and fair conventional-control comparisons. The gain of 2 used in R2 gives an idealized steady-state reduction of 66.7%, so the existing compensation figure should not be treated as the circuit's limit. Anatomical boundary completion and matched physiological validation follow that bounded study.

The original **[alignment-assessment pilot and manuscript](../README.md)**, [history guide](../HISTORY.md), release inventory and archived results remain unchanged. They document a separate supporting investigation. This new GitHub landing page preserves the original pilot README's frozen checksum.
