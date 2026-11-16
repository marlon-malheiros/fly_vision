# Causal solver-work distribution and matched scheduled CPU comparison — V5

Completed 2026-10-22, America/Belem. This is a numerical and software engineering component. The broad biological/hardware goal remains active.

**Outcome:** distributing already known solver work between camera arrivals preserves the original source-time states and outputs, while reducing the size of individual processing bursts in the unpaced four-thread comparison. That comparison also shows added overhead and more paired processing misses. The matched scheduled run retains every input and deadline failure; its results below determine timing success independently of the unpaced improvement. No physiological validity, physical camera calibration or hard-real-time certification is established.

## What changed, and why it is causal

The original model has camera/frontend frames every 5 ms, neural inputs and published rates every 10 ms, and ten 1-ms RK4 steps per input interval. Its first nine steps use the previous input; only the last step uses the historical old/midpoint/new boundary convention. V5 executes five already determined steps at the intermediate camera frame, using the previous input for both kernel arguments, and finishes the remaining five steps at the next source frame. The original global step index and floating-point step lengths are preserved. Intermediate images or drives are not used for the prefix, and no future input is predicted.

Separate V5 modules preserve the old implementations. Graphs, gains, time constants, frontend calculations, source/output times, classifiers and cutoffs are unchanged. `circuit.last_time` still denotes the last source-input time; the new `circuit.state_time_s` identifies the time of the internal state, which now advances at 5-ms intervals. Only original 100-Hz rates are published. Reset clears prefix counts and all inherited histories. The portable default remains strict one-thread activation; four-thread bounded activation is explicit. No electrical coupling or missing biological connection is invented. [Prospective protocol](CAUSAL_SOLVER_WORK_SPLIT_PROTOCOL_V5.md), [circuit](../src/male_optic_frontend/held_input_circuit_v1.py), [runtime](../src/male_optic_frontend/hardware_runtime_split_v1.py).

## Numerical evidence and remaining precision differences

Three unit tests compare small recurrent graphs with independent original Python derivatives, unknown-future forks, strong states, reset and invalid-clock handling. The full preflight preserves all 401 × 13,593 FP64 states in each of three original camera fixtures for strict and four-thread kernels. It also retains every 5-ms state for four original/expanded intact/lesioned stress copies with initial states uniformly drawn from −3 to 3. The unchanged numerical tolerance is 1e-10. Camera-reference discrepancies reach 2.564e-12; strong-state discrepancies reach 6.67e-16. Every matched-kernel source-time output and state is bit identical to the original batched computation. Published rates and full final states agree with original goldens within 1.73e-18 and 8.13e-20; original episode arithmetic agrees within 1.78e-14. [Full preflight](../results/validation_hardware_v1/cpu_work_split_v5/preflight.json), [independent saved-array review](../results/validation_hardware_v1/cpu_work_split_v5/independent_review_v1/review.json).

A separately labeled post-score precision diagnostic examines the largest minus-yaw discrepancy. Python and compiled frontend source drives differ by at most 2.91e-11, over 206,453 entries. Reintegrating the original Python equations using the captured compiled drives yields a maximum full-state difference of 6.94e-18. The matched original batched source-time states remain bit identical to splitting. This isolates input precision from scheduling without relaxing the original criterion or altering saved references. It does not validate biological optics. [Diagnostic and retained numerical evidence](../results/validation_hardware_v1/cpu_work_split_v5/precision_diagnostic_v1/diagnostic.json).

## Frozen unpaced comparison

The 2×2 comparison crosses batched/split scheduling with strict/four-thread kernels using the identical V4 libraries. Three randomized repeats contain the same three full two-second raw binocular fixtures, giving 36 episodes and nine episodes per configuration. All are historical room s01 at 16.5 mm/s, yaw 0,+20,−20°/s; there is no fresh scene-generalization claim. Four-thread activation and OpenMP settings were declared in advance. The independent review reconstructs all raw processing durations, paired sums, numerical discrepancies, original episode arithmetic, package/archive contents and prior seal hashes. [Frozen configuration](../configs/causal_work_split_v5.json), [manifest](../results/validation_hardware_v1/cpu_work_split_v5/prospective_manifest.json).

| Scheduling / kernel | Frame median (ms) | Frame p95 (ms) | Frames above 5 ms | Pair median (ms) | Pairs above 10 ms |
|---|---:|---:|---:|---:|---:|
| Batched / strict | 5.886 | 12.326 | 1,800/3,600 | 13.327 | 1,800/1,800 |
| Split / strict | 6.714 | 7.162 | 3,600/3,600 | 13.555 | 1,800/1,800 |
| Batched / four threads | 3.661 | 5.066 | 195/3,600 | 5.640 | 3/1,800 |
| Split / four threads | 2.892 | 3.818 | 39/3,600 | 5.816 | 16/1,800 |

Splitting reduces four-thread frame-processing misses from 195 to 39/3,600, but paired median rises from 5.640 to 5.816 ms and paired misses rise from 3 to 16/1,800. Strict defaults still fail timing. Both favorable and unfavorable outcomes are retained, without tuning the neural model or the acceptance gates.

![Unpaced processing](../results/validation_hardware_v1/cpu_work_split_v5/report_v1/unpaced_work_split.png)

## Matched scheduled delivery

Before these scheduled outcomes, freeze fifty randomized six-episode blocks, each containing both modes and all three fixtures exactly once (seed 10211000). Each mode therefore receives 150 reset episodes and each identical fixture 50 times. One uninterrupted monotonic 5-ms availability clock covers all 300 episodes, 120,300 binocular pairs, 60,000 noninitial updates and a nominal 601.495-s span. There is no clock retiming, dropped input, hidden warm-up, changed priority/affinity or concurrent heavy analysis. Initializations and image loading occur before timing; all resets, background logging effects, startup frames and late responses remain included. Two bounded recording buffers feed one uncompressed background writer. Full final FP64 states and all published wide-cell rates are retained in 30 chunks. [Scheduled protocol](SCHEDULED_CAUSAL_WORK_SPLIT_PROTOCOL_V5.md), [order and source hashes](../results/validation_hardware_v1/scheduled_causal_work_split_v5_r2/before_execution.json).

Frame response is completion minus scheduled frame availability, with a 5-ms budget. Paired response is the even-frame neural result's completion minus the preceding odd-frame availability, with a 10-ms budget. Paired processing is only the sum of the two frame processing durations and excludes waiting/backlog. Scheduled frame counts include initial frames; pairs exclude them. These differ from the unpaced frame denominator, which excludes each initial frame.

| Scheduling | Frame response median/p95/p99 (ms) | Frame responses above 5 ms | Pair responses above 10 ms | Pair processing above 10 ms | Maximum frame response (ms) |
|---|---:|---:|---:|---:|---:|
| Batched | 4.140/6.502/21.435 | 8,552/60,150 | 7,630/30,000 | 507/30,000 | 121.608 |
| Split | 3.095/4.801/14.876 | 2,402/60,150 | 1,306/30,000 | 513/30,000 | 118.835 |

The split mode changes frame-response misses by 71.9% relative to the contemporaneous batched count (positive means fewer misses). The original zero-miss gate is reported directly and not replaced by an improved mean or median. The complete run's frame-response gate passes: **False**. Independently reconstructed per-mode timing and all fifty block comparisons remain available. Randomization reduces simple mode-order confounding; repeated fixtures are still repeated engineering trials, not independent visual environments or animals. Cross-episode backlog can affect either mode, so the comparison measures performance under this mixed schedule, not isolated hard-real-time guarantees. [Complete execution](../results/validation_hardware_v1/scheduled_causal_work_split_v5_r2/execution_complete.json), [independent review](../results/validation_hardware_v1/scheduled_causal_work_split_v5_r2/independent_review_v1/review.json), [all raw chunks](../results/validation_hardware_v1/scheduled_causal_work_split_v5_r2/chunks).

All 300 episode rate trajectories and full final states pass the unchanged numerical criteria and preserve original decisions. Recorded process peak RSS changes from 359.12 to 363.53 MiB. This high-water observation does not prove absence of leaks. Scheduled availability is generated in software; exposure capture, transport, actual camera clocks, power limits and physical deployment remain untested.

![Scheduled delivery](../results/validation_hardware_v1/cpu_work_split_v5/report_v1/scheduled_work_split.png)

## Portable archive, reproduction and retained failures

The [V5 archive](../results/validation_hardware_v1/deployment/original_runtime_cpu_v5.zip) contains 50 indexed files and is 32,809,218 bytes; SHA-256 `a7c22dfcbfde6243970893da2cc40935771e94ce763d698c0354d966b2d3c8ac`. All previous archives remain unchanged. It requires Python, NumPy, SciPy and a C++17 compiler; optional parallel builds need OpenMP. No GPU or precompiled native binary is required. Both builds were compiled and run in an isolated extracted folder with project PYTHONPATH cleared, reproducing three complete cases, intermediate wide-cell rates, exact batched source states, reset during a prefix and six rejected-input cases per build. The 5-ms full-population evidence remains in the project rather than inflating the package. [README](../results/validation_hardware_v1/deployment/original_runtime_cpu_v5/README.md), [strict check](../results/validation_hardware_v1/cpu_work_split_v5/standalone_strict_v1/selfcheck.json), [accelerated check](../results/validation_hardware_v1/cpu_work_split_v5/standalone_parallel4_v1/selfcheck.json).

In a freshly extracted package directory with its declared dependencies:

```sh
python selfcheck_cpu_camera_v5.py --work check_strict
OMP_WAIT_POLICY=ACTIVE OMP_DYNAMIC=FALSE python selfcheck_cpu_camera_v5.py --threads 4 --approximate-activation --work check_parallel
```

Always choose fresh output directories. The preserved study scripts use exclusive creation to prevent overwrites; their frozen paths cannot be rerun in place. The exported CLI supports new output paths and either scheduling mode with identical sources. Raw results and figure CSVs preserve all failures.

The first isolated launch used the archive parent folder and exited with code 2 before tests; corrected R2 checks pass. The first scheduled freeze referenced a parallel folder named differently from the copied parallel4 folder. It failed before any manifest or timed outcome existed. Its failed source and JSON are preserved; corrected preparation uses a fresh R2 study path. Neither failure represents discarded numerical/timing outcomes. [Failed launch](../results/validation_hardware_v1/causal_work_split_standalone_strict_execution_v5.log), [failed freeze](../results/validation_hardware_v1/scheduled_causal_work_split_v5).

## Scientific interpretation and next work

The change preserves model errors: H2 wrong-direction decisions for both turning fixtures and HS/bIPS straight-walking false alarms remain. It does not improve the frozen circuit's small-yaw sensitivity or resolve room/resolution failures. Those require separate biological and scientific evidence, including missing electrical interactions and matched image-to-recording data. [Scientific report](VALIDATION_GENERALIZATION_CONVERGENCE_REPORT_V1.md), [physiological limitations](CORRECTED_PHYSIOLOGICAL_DIAGNOSTICS_REPORT_V2.md).

The useful engineering result is a causal portable implementation with smaller per-frame compute bursts and explicit evidence about its overhead and scheduled delays. Next, add an explicit clock-alignment and stale-output handling contract under separate versioning, without hiding late frames in these benchmarks. Physical camera calibration and target-specific execution remain necessary. No closed-loop locomotion or motor output is implemented; numerical reproduction alone cannot establish physiological validity or hardware safety.

## Undergraduate explanation: what we did, what we want and why

We want a fly-inspired visual system that notices unwanted turns and can eventually run on real hardware. We divided each neural calculation across two camera arrivals, using only information the model already had. The tested outputs stayed the same. This makes individual processing bursts smaller, but adds some overhead; the scheduled experiment checks whether complete results arrive on time. The model still makes its earlier visual mistakes, and the cameras are simulated. We are separating three questions: does the code reproduce the intended calculation, can it keep up with incoming images, and does it behave like a real fly? Each needs its own evidence before the system can control a robot.
