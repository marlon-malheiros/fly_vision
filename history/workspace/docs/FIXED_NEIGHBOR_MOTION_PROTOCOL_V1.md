# Fixed-neighbor functional motion frontend — protocol V1

Client date 13 October 2026, America/Belem; execution timestamps use UTC.
The user authorized implementation and testing of the proposed simpler frontend.
This is a new algorithmic surrogate, not a repair of the published membrane
equations or proof of biological T4/T5 accuracy. All older positive/negative
studies and sealed sources remain intact. Defer degeneracy.

**Architecture.** Reuse physical pixel rendering and the label-free bilinear
luminance sampler. Both modeled eyes use the previously declared ±80° reference
centers and opposite world-horizontal signs. Introduce a regular eye-coordinate
grid, -86° to +86° at 1° spacing in both axes. These are computational conventions,
not measured optics. All 13,579 target positions must have complete support.

At every grid site construct ON=max(2L-1,0), OFF=max(1-2L,0). Each has a 30-ms
first-order low-pass state initialized to the first image's stationary equilibrium.
Propagate exactly over each previous-sample luminance hold. For each family and
axis, use the two neighbors ±1 grid step around each site:

```text
signed_motion = delayed(lower_neighbor)*current(upper_neighbor)
              - delayed(upper_neighbor)*current(lower_neighbor)
```

Average this signed output over a fixed 7×7-site neighborhood, then rectify its
positive and negative parts into separate channels. All eight ON/OFF × four-axis
channels exist everywhere, regardless of target types. Keep unrectified information
through the signed difference of opponent channels. No clipping/gain fitting.
The nearest-neighbor and pooling support exclude four border steps; all mapped
target readout vertices must lie within the valid region.

This is an explicit fixed-connectivity computation. Image sampling never chooses
a neighbor using a target's preferred direction or subtype. After all channels
are computed, a separately declared output routing maps ON channels to T4-like
and OFF channels to T5-like a/b/c/d slots, respectively +H/-H/+V/-V. The names are
surrogate channel assignments; their anatomical agreement is not independent
validation or a discovery of biological subtype preferences. Runtime removal of
preferred-direction metadata must leave the entire calculation operational.
The old per-target preferred-angle correlator is not on this path.

**Parameter provenance.** Correlation-sensitive computations have physiological
motivation, including fast timing effects in T4/T5. The 30-ms pole, 2° pair span,
7×7 pooling, contrast convention and channel rectification are fixed exploratory
choices, not estimated physiological values. The cited study also finds evidence
inconsistent with one classical model; it does not validate this exact surrogate.
[Salazar-Gatzimas et al. (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5097865/).
Existing chart evidence is in [POSTFIX_COORDINATE_EVIDENCE_V2.md](POSTFIX_COORDINATE_EVIDENCE_V2.md).

**Freeze and bounded benchmark.** Hash code, tests, config, source geometry,
target identity/routing, movie plans and all earlier eleven indexes before new
movie responses. Tests may use analytic/synthetic fixtures, never new benchmark
scores. No parameter search, optimization, threshold changes or best-seed selection.

- Primary: seeds 42, 78201, 78202, 78203; seven original STATIC/global ±60°/s/
  unilateral ±60°/s conditions for each. Seed 42 is historical; the other three
  seeds are prospective new textures. Binary 6° squares, 1° raster, 5-ms samples,
  two seconds, motion [0.5,1.5] s; inactive physical field stays stationary with
  the original 5° midline guard. Four seeds are stimulus replications, not flies.
- Supplemental: new seed 78204, common 600° source world, STATIC and global
  ±30/±90°/s. Different source extent changes texture layout; this set has its
  own matching STATIC and is not paired with the 480° primary world.
- Four cardinal sinusoidal gratings, 24° wavelength, 60°/s. Use the same movie
  clocks/motion interval and neutral contrast convention.
- Sampling comparison: primary seed 78201 STATIC/global ±60°/s and all four
  gratings at 2.5 ms. No parameter/renderer changes otherwise.
- Runtime controls: exact primary movie replay; physical panorama mirror across
  the midline with eye exchange; one fixed-seed frame scramble within the motion
  epoch. Check causality and malformed inputs with analytic tests. Check physical
  unilateral stationarity and reverse translation directly from saved pixels.

This yields 37 main/supplemental movies, seven fine-clock movies and three control
executions: 47 saved source executions. Unlabeled replay and metadata removal are
tested through the complete numeric path; labels exist only in plans/reporting.

**Prospective functional gates.** Retain the old [0.7,1.4]-s response window,
0.001 amplitude/difference floors, absolute DSI ≥0.1 and ≥75% fraction for every
one of eight a/b subtype/eye groups. Require expected physical signs in that
fraction, separately retain all c/d and individual results. Every primary seed
must pass; pooling seeds cannot rescue failure. STATIC maximum activity ≤1e-10.
All four gratings must produce the physically corresponding dominant axis/channel
in both eyes and both contrast families, with opponent DSI ≥0.1.

Require each supplemental speed's eight horizontal groups to pass the same
criterion. Fine-clock comparisons require group preferred/null mean changes ≤10%
(denominator floor 0.001) and group DSI change ≤0.02, with the same group verdicts;
report individual and full-waveform differences separately. The 10% gate is an
engineering sampling tolerance, not biological uncertainty. Require temporal
scrambling to reduce the pooled signed horizontal contrast to ≤50% of the ordered
value in every eye/family. Exact same-input replay and metadata removal must be
bitwise identical; mirrored retinal inputs must be bitwise identical with swapped
eyes, and numeric mirror outputs must agree to 1e-7. Report c/d selectivity and
horizontal/vertical response strength rather than claim complete tuning from
two horizontal movies.

**Independent source verification.** Verify every execution's channels with a
separately coded reference using SciPy lfilter for the delay, direct fixed-pair
products, summed-area spatial averaging, and independently formed bilinear
readouts. Maximum absolute tolerance 1e-7 in normalized output units. Independently
recompute all trial/pair/group decisions; check stored IDs, pixels and clocks.
Do not use the production circuit/scorer to establish its own verdict.

**Downstream gate.** Integrate only after source functional/controls/sampling and
independent review pass. Use all 13,579 body IDs and the existing frozen MaleCNS
graph, gains and 1-ms RK4 solver. The only direct inputs are routed source activity,
with unit scale common to all channels. Use the existing 10-ms drive hold; zero
motion output for stationary prehistory permits common zero network initial state.
Record all downstream T4/T5 and ten HS/H2 responses for the 28 primary trials.
No source type or stimulus sign changes the drive conversion formula. Verify that
non-T4/T5 direct drive is exactly zero. Replay one complete downstream trial with
changed textual labels and removed preferred-direction fields, requiring bitwise
numeric identity. Save actual runtime versions; the previously temporary FlyVis
runtime is absent, so the read-only existing legacy environment executes this new
downstream study. No installation or modification of the legacy workspace.

Use independent RK4 replay from the saved graph/input equations for all 28 trials
(tolerance 1e-7 for float32 all-cell records, 1e-10 for float64 HS/H2 records).
Report all ten targets' direction, static and unilateral contrasts. End-to-end
acceptance additionally requires STATIC stability and measurable expected global
direction in every target for every primary seed. Weak/opposite targets remain
failures and cannot be relabeled or discarded.

**Decisions and completion.** `FUNCTIONAL_FRONTEND_PASS` requires the complete
source gates and independent reference. `FUNCTIONAL_END_TO_END_PASS` additionally
requires the downstream checks and every target gate. Otherwise retain the exact
failed gate and classify incomplete/failed scope. None means biological validation
or degeneracy. On a reproducible implementation bug, preserve the first failure,
issue a versioned correction and hash it before new responses; never repair a
scientific failure by changing parameters. Supervise CPU execution at ≤6 GB RSS,
zero swap and two hours per job; require ≥8 GB free disk. Save each batch promptly
and permit continuation of verified complete batches after stream interruption.

Produce source/target group tables, all individual results, four-direction and
seed figures, architecture/geometry/leakage documents, a report and simple summary,
commands/environment/logs/tests, a live-progress snapshot, Git checkpoint and an
immutable artifact index. No external messages or public deployment.
