# Input mapping and research-direction audit V1

24 October 2026. Authorized after the continuous-yaw study. This is a bounded
retrospective implementation/accountability audit with new, fixed decomposition
checks. Existing outputs are known; no test room becomes fresh again. Preserve
all prior sealed evidence, parameters and scientific acceptance criteria.

## Questions and stopping rules

1. Which proposed checks have already been completed? Assemble a linked
   question/evidence/decision ledger before launching another neural sweep.
2. Do the active target IDs, subtype channels, sides, coordinates and source
   column order match their actual curated inputs and graph?
3. Can the difference in delivered source drives under equal retinal fields
   be reconstructed from the unequal spatial sampling measures, without a
   routing, interpolation or indexing discrepancy?

If a production mismatch is found, retain the failure, identify its first stage
and implement a separate correction with identity/analytic regression controls.
Only a confirmed, justified correction can trigger new neural/generalization
experiments. No neural sweep, threshold search, count balancing, ad hoc coordinate
shift or circuit tuning is authorized by an algebraic input difference alone.
If no mismatch is found, close the implementation-error hypothesis within the
tested scope and explicitly state the next distinct evidence requirement.
Do not describe a limitation of the specified model as a confirmed coding bug.

## Fixed evidence and checks

Reconcile all 13,579 active T4/T5 targets against curated `cells.csv`,
`eyemap.csv`, graph arrays and the active source identities. Verify unique IDs,
type/hemisphere/coordinate/routing equality, exact graph-source coverage, target
order and held-input assembly. Check deterministic joint permutations of source
IDs and columns without changing network equations. Use the source-defined
coordinate formula independently of `EyeTransform`. Tolerances: coordinates
1e-10 degrees; array IDs, routes and assembly exact. Validate the checker with
five deliberately corrupted metadata copies; these are fixtures, not lesions.

Use the eight existing S/straight cases: rooms s07/s12, speeds 0/5.5/11/16.5,
yaw zero. Replay retained retinal movies through the unchanged frontend and
independently sample its fields using SciPy's `RegularGridInterpolator`, rather
than the production vertex/weight sampler. Check all 401 frames' image/field
equality, all 201 saved source samples and their body-ID ordering. Saved drive
error tolerance is 1e-7, matching the original independent-source contract;
field/checkpoint tolerance is 1e-12. No new anatomical homology is assumed.

Construct independent per-side/per-channel normalized sampling measures on the
retinal grid. Their dot product with the time-mean common field must reproduce
each side/channel's primary-window mean source drive within 1e-7. Retain all
eight channels and both sides, including zeros. The primary window is the
unchanged [0.70,1.40), source indices 70:140 / image indices 140:280 at stride 2.

Separate the all-source population difference into the exact symmetric identity

`mean_L - mean_R = sum_k pbar_k*(mu_Lk-mu_Rk)
                  + sum_k (p_Lk-p_Rk)*mubar_k`.

Here p is each channel's fraction of target cells and mu its mean drive. The
first term summarizes within-channel spatial sampling; the second summarizes
channel-mixture counts. This is an accounting identity about delivered drives,
not a causal decomposition of recurrent neural output or classifier errors.
Means within one channel are not made equal merely by equal population counts.

Keep all sampling measures, per-case mean fields, full independently rebuilt
source arrays, cell/channel tables and errors. Check the time-window/identity
arithmetic with a separately coded reviewer. Do not reuse new outcome-dependent
normalizations or redefine success after seeing the result.

## Deliverables and decision discipline

Produce a versioned script, evidence/duplication ledger, complete numerical
audit, concise report, one diagnostic figure and an undergraduate explanation
of what was done, what remains wanted, and why. Append progress and save a
dated progress snapshot before sealing. Separate numerical implementation
consistency, declared modeling assumptions and biological validation.

Any subsequent experiment must state a new falsifiable question, its prior
evidence, one justified change, unused test data and a fixed stop decision.
Repeated sampling sweeps, readout complexity, anatomical additions, saturation
claims and exact-file searches cannot be presented as new fixes without new
evidence addressing their already documented limitations. The original ±2°/s
aim remains unfulfilled; no new threshold is established by this audit.
