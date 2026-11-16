# Matched local-motion encoding control

2026-10-26. Addendum to the three sequential repair tests. The original frozen
recipes, predictions and acceptance criteria remain unchanged.

The independent standard check exposed texture-size dependence after scalar
contrast normalization. Also, the original image control samples a denser/larger
support than the source-only spatial readout. To separate local encoding from
integration more fairly, freeze this additional **engineering control** before
computing its development responses or inspecting any new held-out classification.
Some held-out images are already generated; their classification outputs have not
been scored/inspected. This is not a claim that the images are newly generated for
this addendum. No model/interface is selected using held-out results.

Compute the same local Lucas–Kanade velocity field from the identical saved movies.
At existing source-cell locations, map horizontal/vertical velocity to the original
eight nonnegative direction channels. Both ON/OFF populations receive that local
directional estimate; this is a deliberate replacement of the polarity-specific
surrogate, not reconstructed T4/T5 physiology. Scale each axis by the inverse of
the already fixed normalized standard-plaid velocity coefficient. No additional
gain, time constant, yaw decoder penalty or decision cutoff is optimized. Clip
to the original[0,1] source range and retain clipping counts. Supply these local
inputs to a separate copy of the **unchanged original MaleCNS graph and parameters**.
No global yaw estimate is fed into the graph.

Also test geometry-based readouts on these direction channels at exactly the
330original local lattice sites and after exactly the original source-cell
interpolation. Use the same fixed geometry weights and median as the HRC-based
spatial readouts; neither uses texture-confidence weights. This directly controls
readout support and aggregation. The original denser LK image control remains
separate. Keep centered derivative future-data requirements explicit (10ms at
primary5ms image sampling). No depth, speed or yaw truth enters inference.

Reuse all112development and384held-out movies, source identities and room split.
Execute development first, train the same class-mean ridge decoders and use the
same16-room straight calibration cutoff. Freeze all fitted readouts before any
held-out control response is executed. Evaluate original80%/80%/10% criteria at
2and5°/sacross speeds. Geometric readouts retain the1°/s engineering cutoff.
Report every result, even if another method has higher performance.

Execute the same three known fast0/±2controls with0.5°retinal pitch and fully
halved frontend/input/solver clocks. Preserve failed0.2°/s numerical gates; compare
strict graph replay and fixed-physical-input-ramp refinement separately. A positive
result would establish a conditional engineered model capability, not biological
validation or proof that the original T4/T5 circuit computes local velocity.
