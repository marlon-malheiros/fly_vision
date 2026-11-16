# T4 eye mapping and held-input controls V1

Frozen plan for a bounded technical stage, 13 November 2026. This is not a
physiological acceptance test or walking experiment. The prior smoke and its
failed historical-solver numerical check remain unchanged. The new circuit
integrator holds the previous source sample on each half-open interval; its
rules are separately versioned and do not replace the historical solver.

## Metadata-only population mapping

Check that all saved population inventory IDs and types match the LPi graph's
13,579 source IDs, each position is finite, and each axis is finite and unit
length. Report all T4/T5 type counts and observed versus donor-imputed axes.
The inventory's spatial axes and T5 mapping are inherited assumptions, not
new anatomical validation. Existing RF samples use eleven positions 2.25°
apart and nine transverse offsets. That is distinct from the per-recording
alias ensemble and delay used in the reserved T4 assay; no such calibration is
invented for individual MaleCNS neurons.

Choose four cells before simulated responses: one T4a and T4b per eye, with
non-imputed axis closest in degree-coordinate Euclidean distance to (-80,0)
for left or (80,0) for right; numeric body ID breaks ties. Compare selected
metadata to graph exactly. Other cells are zero, including T5. This sparse
control does not implement an eye-wide voltage population and cannot test
walking or qualify a biological downstream response.

## Five local-image controls

At each chosen cell, generate a local 0.5° raster centered on its inventory
position with a 2.25°-wide bright or dark bar moving in either direction
along the axis at 40°/s, and a uniform grey condition. The per-cell patches
are not one shared global scene. Produce images at 5 ms intervals on demand,
sample via existing bilinear sampling and nine-point transverse averaging,
apply the existing grey-centered ON contrast, and retain sampled inputs and
hashes rather than movies. Frames are grey before 300 ms and after 800 ms;
simulations stop at 1300 ms. Dark-on-grey necessarily supplies zero under the
existing ON-only contrast convention; this is a property to expose, not a T5
or biological OFF validation. A shared grey baseline is an explicit image
normalization, not the recording-calibrated mapping in the prior study.

Run the original full cable with pinned NEURON 8.2.7/NumPy 1.26.4 for four
cells and five conditions, plus 0.05 ms refinements of the eight bright
motions. Compare 0.1 and 0.05 ms traces on common 1 ms samples against the
unchanged 0.005 mV max error guard before interpreting graph outcomes. Uniform
grey and dark ON inputs must remain zero; bright signals must contain positive
input; voltages must be finite. Do not require a particular direction or
biological response amplitude. Convert voltage with the explicitly assumed
`max(V+65,0)/65` bridge, reject out-of-range values, and sample on the 10 ms
network clock. Compare 1 ms and 0.5 ms held-input network solvers with the
previous `1e-8` maximum absolute wide-output guard. Model responses and
directional differences are exploratory, not physiological qualification.

One worker; maximum 300 scientific child CPU seconds; estimated permanent
output less than 64 MiB and 20 GiB free-space reserve. Do not store generated
movies or download raw datasets. The worker records actual resource counters;
the graph review is additional work outside those counters. If the environment
cannot be restored, document the failure and complete metadata and numerical
checks that need no new cable. If any numerical gate fails, preserve the result
and stop this stage without selecting cases or relaxing thresholds.
