# H2 recorded-response comparison with a detailed T4 population, V1

14 November 2026. This is a retrospective, conditional comparison with real
H2 recordings, not an independent-animal blind validation. It tests a named
combined model against a measured downstream response; it does not claim that
the entire walking model, T5, bIPS or real-fly small-turn detection is valid.

## Recording, input, and exposure

Use Zhao et al. 2025 H2 cell 1, protocol 1, LED position (87,13), bright and
dark edges, relative orientations 0,1,2,3,4,5,6,7 (eight directions spaced
45 degrees). This selection is determined from metadata and the existing
position/geometry audit, not from individual model outcomes. Use all 16
corresponding recorded conditions. Source recordings and aggregate H2 curves
were previously inspected and compared to a functional model; this study is
not a fresh biological holdout. Other animals and directions are not part of
this pilot and cannot be inferred from it.

Use the exact saved image arrays from the prior H2 benchmark: these are
reconstructed stimulus-family images, not verified actual display-frame
recordings. Geometry, background, luminance, temporal windows, head pose,
and fixed opaque-right-eye convention are inherited without tuning. The
recorded fly is female, the connectome model is male; no sex-specific equality
is assumed. Exact LED edge patterns, photometry, timing, initial adaptation,
and voltage-to-spike observation remain approximations.

## Combined model and controls

Baseline: the original saved 13,579 functional T4/T5 source drives for these
16 reconstructed image sequences, remapped by exact ID into the frozen LPi
graph. Candidate: replace every *left-eye T4* source with a full published
T4 cable using its inherited eye-wide inventory center and axis, 11 native
positions at 2.25 degrees and nine transverse offsets. Every left T4 input is
sampled from the same saved left-eye frames; points outside the saved retinal
chart use neutral 0.5 brightness, as in the prior population implementation.
Each cable starts at -65 mV and zero filter states, with original source
parameters/sites, no cell-specific recording calibration, no extra delay,
and the fixed model-unit proxy `max(V_mV+65,0)/65`. Zero-contrast sequences
remain exactly -65 mV. Right-eye sources and all T5 sources remain exactly
the original functional drives. This is a hybrid, not a fully physiological
T4/T5 source population or a transfer of the recording-specific alias ensemble.

Use the same frozen LPi graph and causal held-input solver for baseline and
candidate. Record the anatomically identified left H2 body ID 10019. Both
models start at zero network state, with the same source clock; no model,
observer or gain fitting. Reuse T4 computations only for *identical* complete
sampled contrast arrays and clocks, with array equality verified after hash
matching. This computational caching does not replace a cell with another
cell-specific fitted response: all here are identical published cable clones.

## Comparison specified before predictions

For each condition, use the same source-derived response window as the
previous H2 benchmark and the 1-second stimulus onset. Subtract pre-onset
baseline, then integrate model H2 rate over [0.001 s, response_end] by
trapezoids, yielding one signed dimensionless endpoint. Compare this with the
published baseline-subtracted recorded spikes/s through *directional shape*,
never treating model units as spikes/s. Primary: average bright and dark
endpoint curves, subtract each curve's directional minimum, calculate the
complex preferred direction across the eight fixed angles, and report
absolute circular error relative to the recorded direction. Report the
parameter-free anatomical body-horizontal reference and the paired functional
baseline under the same eight-condition extraction. Also report per-polarity
shape correlations and all signed endpoints; never select a polarity, angle,
cell or readout based on agreement.

A result is a **restricted directional match** only if the candidate direction
is defined, has at most 45 degrees circular error, and beats the fixed
body-horizontal reference error. The 45-degree guard is one sampled direction
spacing, an engineering criterion, not an empirically established clinical or
physiological equivalence limit. The body-horizontal reference is a strong,
nonfitted benchmark. A directionless/flat candidate is uninformative and does
not pass. This rule was chosen after the source and earlier functional outcomes
were known, so even a pass is a retrospective consistency result, not
independent validation. Regardless of pass/fail, report raw values and both
models. No additional parameter search or response-based correction.

## Preflight, numerical checks, storage and stopping

Before new voltage or H2 outcomes, use input-only sampling to count unique
nonzero T4 sequences and estimate full-run CPU, memory and storage from the
November 13 24-solve T4 pilot. Save and hash selected source frames, sequence
definition, graph/model/observer methods, and resource estimate. Zero inputs
may use exact resting voltage without a cable solve. The actual science-run
budget is one worker, maximum 1,200 scientific child-CPU seconds, at most
3,000 distinct nonzero cable solves and 512 MiB new retained output, with
at least 20 GiB free. If estimate or preflight exceeds a limit, record the
resource stop before any new biological outcome; do not silently reduce
directions, cells, histories, or movie fidelity.

Check two preselected unique nonzero cable inputs at 0.1 and 0.05 ms (max
error <=0.005 mV). Compare 1 and 0.5 ms network integration for a
preselected candidate condition (max wide-rate error <=1e-8); independently
recompute actual H2 direction metrics and selected pixel samples. Fixed
numerical thresholds must pass before interpreting score; preserve failures.
Do not open unrelated held-out recordings or regenerate retired movies.
Append progress, report limitations, snapshot methods and dated progress,
then seal and rehash after writers exit.
