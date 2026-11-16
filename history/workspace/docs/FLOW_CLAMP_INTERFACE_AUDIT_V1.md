# Inherited flow-clamp interface audit — V1

Recorded 2026-10-21. Geometry-only audit after inspecting the soma-separated
diagnostic plots; no sign was selected by agreement with recordings.

The inherited signed yaw clamp drives local positive-horizontal T4/T5 channels
positively in both eyes. The frozen frontend's declared eye transform maps a
single world-azimuth velocity to opposite local horizontal signs: negative in
the left eye and positive in the right. A world-grating image check independently
reproduces those opposite local channel responses. The inherited projection
therefore disagrees with the frozen frontend convention for
3367 sensory cells. It also gives negative
input to 3405 cells, whereas the functional
frontend emits only nonnegative channel activity.

This does not change any completed study. The old signed clamp was explicitly a
separate conditional diagnostic; it cannot stand in for the frozen image path.
The new soma-matched benchmark faithfully retained it, so its errors do not by
themselves identify a biological circuit defect. The 3D walking simulations and
hardware image frontend do not use this clamp and are unaffected by this audit.

Any corrected comparison must have a separately frozen version: transform world
flow into each declared eye chart, then distinguish a signed coordinate-corrected
proxy from a rectified proxy compatible with the frontend's nonnegative range.
Neither proxy alone supplies measured T4/T5 amplitudes, retinal movies or reporter
physiology. Keep neural graph/gains unchanged and label reuse of the already
inspected physiological test set. New stimulus conditions or recordings are needed
for an additional independent validation claim.

[Numerical audit](../results/validation_hardware_v1/flow_clamp_interface_audit_v1/audit.json)
· [Every channel](../results/validation_hardware_v1/flow_clamp_interface_audit_v1/channel_comparison.csv)
· [Prior conditional comparison](SOMA_MATCHED_PHYSIOLOGY_REPORT_V1.md)
