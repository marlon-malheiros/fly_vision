# Neural/image agreement for small-turn onset, V1

2026-10-27. User authorizes another implementation toward a working solution.
This is a hybrid engineering readout, not a repaired biological circuit.
Preserve all prior sealed evidence, original HRC frontend, MaleCNS graph,
parameters and the two branch algorithms. Do not fit circuit physiology.

## Frozen development recipe

Reuse the frozen DNp15 change readouts from neural_change_readout_v1 and the
unchanged backward_current/100-ms registered confidence-weighted image estimate.
Both use identical images. They are correlated computations, not independent
biological sensors. No neural coefficients, thresholds or image parameters change.

At each callback, if both continuous estimates have the same nonzero sign,
support is that sign times min(abs(neural)/its frozen cutoff, abs(image)/1).
Otherwise support is zero. A turn requires abs(support)>1. For confirmation
counts 1,2,3,5 require all successive supports to have the same sign and take
their minimum absolute support. No future samples or event labels enter the
rule. The largest candidate adds 40 ms; the original 200-ms deadline remains.
Raw support is dimensionless and is not a calibrated yaw velocity.

The previously examined p and w rooms are now explicitly known development
sets. Evaluate every candidate separately on each set, every speed and +/-2
and +/-5. Preserve >=39/48 detections, >=39/48 raw-sign accuracy including
undetected turns and <=2/24 endpoint straight alarms. Additionally require
<=2/24 rooms with any rolling alarm at callbacks 1.0--1.79 s. Undefined outputs
fail. Select the smallest confirmation count passing every development gate;
if none passes, do not promote a failing rule as working. No threshold search.
Retain all candidates and failures. All four candidates precede new development
scoring; no best post-test policy is allowed.

Check the selected rule on existing f00 fast 0,-2,+2 spatial/temporal controls:
margin changes <=0.2 in normalized support units, with decisions unchanged.
Also retain component errors against the preceding 0.2-degree/s checks.
This is a finite-case numerical check, not a uniform bound or physiology.

## Fresh test, if a candidate passes development

Freeze code, selected count, both branch identities and criteria before any
c-room images. Generate 24 new seed-disjoint rooms, seeds
202610278000--202610278023, same balanced empty/three-sphere scene family.
Cross all three speeds with 0,+/-2,+/-5 and stationary: 384 episodes.
Walk starts at 0.5 s and yaw at 1.0 s, with continuously running frontend/neural
state, unchanged rendering, retina and time/solver parameters.

Turn episodes stop at 1.25 s; stationary/straight controls stop at 1.8 s.
Thus all inputs through the primary 1.2-s deadline are unchanged in definition,
and straight monitoring retains the exact earlier 80-callback interval. This
study tests onset detection, not maintained turning beyond 250 ms. The shorter
turn tail is defined before new outcomes and is not a change in latency or
accuracy criteria. Compare the hybrid, neural-only and image-only branches on
identical inputs and report all speed/magnitude gates regardless of outcome.

Disk has 17 GiB free, insufficient for another original-format 23-GB archive.
Retain full movies with a lossless float32 XOR/byte-shuffle/deflate codec;
retain every source/neural/reference array, timestamp, final state and receipt.
Synthetic arbitrary-bit tests and archived-case parity must verify exact codec
reversal. Shorter turn tails plus lossless encoding preserve all new inputs
within available space without deleting or rewriting old evidence.

Independently reconstruct component scores, normalized support, confirmation,
endpoint/rolling counts, selected-candidate rules and sample windows. Verify
pre-yaw image/source/neural/reference prefixes and full state. Check sampled
retinal images with independent NumPy rendering; reproduce four fixed fresh
episodes exactly (c00 fast straight, c01 fast -2, c02 slow +2, c03 medium +5).
Preserve failures and provide figures, a technical report and undergraduate
explanation. Snapshot live progress before sealing; verify hashes after all
writers exit. Keep live AGENTS.md/progress outside immutable indexes.

Endpoint and rolling success on these rooms establishes only a tested
engineering capability. It does not establish population reliability, reliable
arbitrary-duration monitoring, neural noise tolerance, physiological validity,
movement intention, variable-speed robustness or autonomous control.
