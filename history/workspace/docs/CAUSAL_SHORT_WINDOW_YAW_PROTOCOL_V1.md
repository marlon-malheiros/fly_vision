# Causal and shorter-window yaw detection, V1

Prospective engineering follow-up, 2026-10-27, to the sealed
[reliability-weighting study](RELIABILITY_WEIGHTED_YAW_REPORT_V1.md). Preserve
all earlier code, parameters, graph and evidence. No closed-loop controller.

## Fixed candidates and question

Can the successful engineering readout detect small turns promptly, using
only images available by its decision time? Keep the velocity encoding,
source interpolation, confidence/geometric weighting and 1-degree/s cutoff
fixed. Compare two finite-difference implementations, not a tuned filter:

* `delayed_centered`: the exact previous five-image centered derivative,
  returned only when its last required image arrives. Its velocity refers to
  10 ms earlier at the primary 5-ms image cadence. This obtains causality by
  acknowledging a delay, not by claiming that the old calculation no longer
  needs those images.
* `backward_current`: three-image second-order backward temporal derivative
  `(3 I(t)-4 I(t-dt)+I(t-2dt))/(2dt)`, with image gradients at t. No future image
  or imposed derivative lookahead; truncation error may be larger.

Both use the previous tensor conditioning and registered source readout.
The streaming interface receives time and binocular images only. It stores a
bounded past-frame buffer and emits at 10-ms cadence. Each emits source values,
local yaw/confidence evidence and a scalar yaw estimate. Five predeclared
trailing means use 100/200/300/500/700 ms (10/20/30/50/70 estimates). No new
threshold, image blur, regularization, neural parameter or training on test
labels. This is an engineered image/source-coordinate readout, not a repaired
MaleCNS circuit or physiological validation.

## Timing and outcome definitions

Preserve the exact previous SE(2) motion conditions: translation and prescribed
yaw both begin at 0.5 s. This study does not yet test a yaw perturbation during
already established walking. Keep that limitation explicit. Render images
0.48--1.40 s at 5 ms, sufficient for estimates at signal times 0.50--1.39 s.
Camera geometry, 1-degree pitch, source locations and textures stay unchanged.

For each method/window, evaluate two endpoints with the same historical
accuracy targets:

1. **Early:** the first N motion-signal estimates in `[0.5, 0.5+W)`.
2. **Late:** the N estimates in `[1.4-W, 1.4)`; W=0.7 matches the previous
   long-window reference exactly for delayed_centered at its signal times.

The early result is physically available at onset+W-10 ms+method_delay for
the primary cadence; explicitly retain actual image-arrival times. Report
nominal W+method_delay as a conservative bin-boundary latency as well. Never
backdate an estimate to imply that it was available at its signal time.
Event labels locate evaluation windows only; they do not enter inference.

At each speed and +/-2 and +/-5 deg/s require >=80% detection, >=80% correct
raw sign (including undetected turns), <=10% observed straight false alarms.
Undefined values are failures. With 24 test rooms the limits remain >=39/48
turns, >=39/48 signs, <=2/24 straight alarms. Primary success requires both
early and late endpoints at every speed/magnitude, plus the predeclared
numerical checks. Report joint correct-sign detections as a diagnostic.

Additionally retain every rolling decision over the common signal interval
0.5--1.39 s, each room's any-alarm indicator and first correct turn crossing.
The any-alarm rate is a distinct, more demanding continuous-monitoring metric
over repeated decisions; do not substitute it for the historical endpoint
criterion or claim reliable continuous control merely from endpoint success.

## Development and prospective selection

Use the same 112 archived episodes (four known training rooms, 16 known
straight-calibration rooms). No fit of neural/velocity/decision parameters.
Select the candidate with smallest nominal W+delay that passes both endpoints
at all speeds/magnitudes on development and passes its numerical controls.
Break an exact latency tie in favor of backward_current. With only four
development turn rooms, report the small-sample limitation and fresh-test
result, not an optimized population threshold. If no candidate qualifies,
retain delayed_centered/700 ms as an explicitly nonqualifying fallback and
complete the same fresh comparison; do not invent another candidate.

Freeze both implementations, all window choices, this selection rule and the
analysis code before development. Freeze the selected primary and its known
development results before generating fresh-room images. Test 24 independent
room seeds 202610274000--202610274023 (r00--r23), collision-checked against all
existing scene inventories; 384 fresh episodes in the same scene family.
Retain all candidate outcomes as predefined diagnostic curves, but do not
replace a failed primary with a post-test-selected winner. No test tuning.

## Numerical, causal and timing checks

* Prove prefix invariance of the streaming outputs under changed future input,
  enforce chronological input and check expected signal/arrival timestamps.
  Compare delayed_centered with all archived primary reliability-weighted
  source drives and long-window frame estimates exactly.
* Check the derivative formulas on independent polynomial image sequences,
  and recompute moments/confidence using independent spatial convolution.
* Use the three predeclared f00 fast cases (0,-2,+2) on archived 0.5-degree and
  2.5-ms images. Compare every method/window/endpoint against primary at
  <=0.2 deg/s. Store failures; only selected method/window checks gate its
  claim. Finer time steps change the derivative's truncation and intrinsic
  delay; compare matched signal times and report actual delay separately.
* Independently reconstruct rolling means, endpoint counts, source-readout
  weighted medians and selected candidate. Verify representative fresh
  renderer outputs against NumPy and four fixed full-episode replays.
* After worker processes exit, benchmark the selected single-method streaming
  pipeline plus rolling mean serially on the four fixed config cases, five
  repeats after one whole-episode warm-up. Time each push with a monotonic
  high-resolution clock; include past-buffer copying, image processing,
  source sampling, weighted median and rolling averaging. Exclude setup,
  rendering, camera transfer and disk reads; record setup separately. Report
  output-call p50/p95/p99/max and sustained throughput. A soft CPU-feasibility
  check requires output-call p95 and mean <=10 ms on this host. This is not
  a hard real-time or physical-hardware guarantee.

## Deliverables and preservation

Preserve complete raw fresh movies, timestamped per-method source/readout
evidence, decisions for all windows, frozen selection, numerical controls,
runtime samples, failures, figures and a concise report with an undergraduate
explanation. Add dated project progress, snapshot it before sealing and verify
the artifact index after writers exit. Keep live AGENTS.md and progress outside
the immutable index. The original circuit's biological validity remains open.
