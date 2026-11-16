# Neural population readout V1 — frozen protocol

31 October 2026. This is an information/readout experiment, not an anatomical
reconstruction or physiological validation. Earlier published-motif and coupling
reproductions already failed walking transfer; repeating those is excluded.

Question: can a separately trained decoder recover small yaw from the existing
neural population when individual downstream cells or retinotopic T4/T5 activity
are retained? A success would identify recoverable neural information, not prove
that DNp15 or the fly uses this decoder. A failure would close these readouts,
not establish that all neural solutions are impossible.

Preserve the functional HRC frontend, LPi-expanded MaleCNS graph and all numerical
parameters. The new C++ observer changes recorded quantities only. It averages
actual tanh T4/T5 network rates in 6 horizontal × 4 vertical equal bins per eye
and subtype (384 bins), retaining 45 individual downstream cells. Coordinates
come from the existing registration; outlying centers clamp to edge bins.
Empty bins remain zero. No invented synapses or physiological gains are added.
The original surrogate remains unvalidated T4/T5 physiology.

Training uses all 24 previously inspected p rooms, calibration all w00–w15.
These are known development data. Reuse saved positive-trial visual drives,
truncated to 1.30 s; render straight/stationary trials through 3 s to cover
the entire monitoring interval. Preserve provenance of each reused input.
Use the unchanged binocular 1-degree retina, 5-ms images, 10-ms neural inputs,
1-ms RK4, walking onset 0.5 s and yaw onset 1.0 s, without resetting state.

Each input feature is a 100-ms mean and its difference from the mean 200 ms
earlier. Train four separate readouts: DNp15 change (2 features), individual
downstream change (45), spatial T4/T5 level+change (768), and spatial T4/T5
level+change into 32 tanh hidden units then one linear output. The latter is
the fixed primary candidate. Learned output/hidden weights are task-trained
artificial readouts, not measured fly connectivity. The first three minimize
weighted mean squared error plus ridge 0.01 on standardized coefficients;
intercept unpenalized. The MLP uses fixed seed, full-batch Adam, 600 steps,
learning rate 0.003 and weight decay 0.001, with no early stopping/search.
Training-only weighted means/scales use an SD floor of 1e-12. Use all 200
straight/stationary callbacks [1,3), and turn endpoint 1.19 s. Equal total weight
per episode within each negative/zero/positive yaw class; each class gets 1/3.
No true speed, onset, yaw, scene, depth, image gradient or confidence enters
inference. Include the unchanged prior DNp15 readout as a fifth reference.

Freeze every coefficient before scoring calibration or generating test images.
Calibration is diagnostic, not used to tune/select candidates or thresholds.
Evaluate all candidates even if development fails. Generate 24 seed-disjoint
new test rooms (seed 202610319000 onward), balanced A/M material/geometry
reflection and empty/three-sphere clutter, with all 16 conditions per room.
These are new instances of the same environment family, not natural-scene
or out-of-distribution validation. All methods share each exact neural episode.

Decision threshold |score| > 1 remains fixed. Endpoint 1.19 s; straight and
stationary any-alarm monitoring [1,3), 200 correlated callbacks summarized once
per episode. At each speed, both ±2 and ±5 require ≥80% detection, raw-direction
accuracy and joint correct detection, ≥80% each signed direction, ≤10% endpoint
and any-episode straight alarms and stationary alarms, no undefined callbacks,
and stationary raw activity zero. For 24 rooms: ≥39/48 joint, ≥20/24 per sign,
≤2/24 false alarms. Report every method and negative finding, with paired-room
bootstrap intervals. No claim of population false-alarm guarantees.

Numerics use f00/p00/p01, three speeds and yaw 0/±2: 27 primary cases versus
0.5-degree space (same physical HRC offsets/pool), 2.5-ms images/5-ms inputs,
and 0.5-ms RK4. All 81 comparisons per candidate must keep maximum monitored
score difference ≤0.2 and the endpoint/any-alarm decisions unchanged. Retain
failed gates. New observer must match old observer's individual rates/final
states bitwise for one nonzero saved input. Check independent pooling at
saved full-state checkpoints, causal feature/prefix behavior, label-free
inference and independently fitted/predicted linear outputs. Save four fixed
first-test-room full sources for fresh replay (stationary, slow −2, medium +2,
fast straight), plus input hashes and complete neural observations for all.

Writers require fresh paths; incomplete attempts are archived under failures.
Disk budget: store pooled rates rather than all source neurons; do not delete
earlier evidence. Append progress, archive dated progress/source/report copies,
seal artifacts, and verify the index from a separate process. No closed loop.

If all readouts fail, the next alternatives are: a prospectively justified
nonlinear or multiscale visual encoding study, or independent physiological
constraints on HS receptive-field integration. Do not repeat a global gain,
linear electrical-coupling addition or already failed image/neural fusion as a
new biological solution. If spatial decoding succeeds but DNp15 does not,
compare that learned computation with documented anatomy before proposing any
circuit change.
