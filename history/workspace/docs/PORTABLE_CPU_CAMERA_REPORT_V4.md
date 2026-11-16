# Equivalent camera projection and scheduled CPU delivery — V4

Completed 2026-10-22, America/Belem. Numerical/engineering component; broad hardware/biological goal remains active.

**Outcome:** compiled camera projection preserves every tested retinal value and matched-kernel neural output. The optional four-thread implementation reduces median processing from 9.075 to 5.802 ms per neural update in the frozen comparison. Actual scheduled delivery still misses deadlines, including delays larger than a processing-only benchmark reveals. The strict-default portable CPU archive is reproducible; no physical camera, physiological validity or hard-real-time controller has been established.

## What changed and what was preserved

A separately versioned C++17 kernel replaces temporary NumPy projection arrays with one loop per eye. It applies the same photometric lookup before the same four-corner FP64 interpolation and FP32 conversion, without fast math, contraction or native architecture flags. The adapter inherits V1 calibration/coverage/digest checks and reset/commit semantics, preserves integer timestamps and acquisition-mode checks, and returns independent read-only retinal arrays. Noncontiguous images are explicitly copied into a contiguous buffer; their pixel meaning does not change.

The original frontend, MaleCNS graph, parameters, 1-ms solver and 70-sample historical decoder remain unchanged. No missing connection, conductance or physiological parameter was added. Seven tests cover uint8/uint16, arbitrary fractional maps, image edges, Fortran/negative-stride layouts, large integer clocks and error/reset behavior. All **72,009,174** retinal pixels in three complete camera episodes match V1 bit for bit. This verifies software arithmetic on declared inputs; the included calibration remains SYNTHETIC_TEST_ONLY. [Prospective protocol](COMPILED_CAMERA_PROJECTION_PROTOCOL_V4.md), [preflight](../results/validation_hardware_v1/cpu_camera_projection_v4/preflight/preflight.json), [adapter](../src/male_optic_frontend/sensor_adapter_v2.py).

## Frozen comparison and numerical review

The 2×2 comparison crosses NumPy/compiled projection with strict single-thread/explicit bounded-activation four-thread neural kernels. Three interleaved repeats each contain the same three two-second cases: 16.5-mm/s forward walking with yaw 0,+20,−20°/s in historical training room s01. Each configuration has nine full episodes and 1,800 noninitial neural updates. These are repeated software fixtures, not independent biological trials or a fresh held-out environment study. The random order, acceptance criteria and method digests were frozen before new timing outputs. [Configuration](../configs/compiled_projection_v4.json), [manifest](../results/validation_hardware_v1/cpu_camera_projection_v4/prospective_manifest.json).

| Projection / neural kernel | Median (ms) | p95 (ms) | p99 (ms) | Processing above 10 ms |
|---|---:|---:|---:|---:|
| NumPy / strict one-thread | 16.532 | 17.455 | 19.101 | 1,800/1,800 |
| Compiled / strict one-thread | 13.740 | 14.594 | 15.735 | 1,800/1,800 |
| NumPy / four threads | 9.075 | 10.546 | 13.013 | 167/1,800 |
| Compiled / four threads | 5.802 | 7.189 | 9.250 | 6/1,800 |

Compiled projection reduces frontend-only median frame time from 3.009 to 1.425 ms in the four-thread comparison; neural-frame median falls from 6.049 to 4.357 ms. Nevertheless, 200/3,600 frames exceed 5 ms, and six paired updates exceed the 10-ms processing budget. The strict default still exceeds every paired-update budget. No failed deadline is excluded or acceptance threshold relaxed.

Independent review reconstructed every timing summary, population-rate/final-state discrepancy and original episode score/decision, checked archive contents and reverified the 7,230-entry scientific seal and 183-entry CPU V3 seal. Matched-kernel outputs are bit identical across projector versions and repeats. Maximum discrepancy from the independent Python neural reference is 1.74×10⁻¹⁸ in rates and 8.14×10⁻²⁰ in full final states; maximum episode arithmetic difference is 1.78×10⁻¹⁴. This is not an independent new solver or biological validation. [Review](../results/validation_hardware_v1/cpu_camera_projection_v4/independent_review_v1/review.json).

![Projection timing](../results/validation_hardware_v1/cpu_camera_projection_v4/report_v1/projection_timing.png)

## Scheduled delivery, interruption and full repeat

The scheduled protocol preloads the same raw cameras, assigns availability every 5 ms on a single monotonic clock, and preserves every input even when processing falls behind. It cycles 300 reset episodes, totaling 600 simulated seconds, 120,300 frame pairs and 60,000 noninitial neural updates. The nominal availability span is 601.495 s because every episode includes its initial frame. There is no hidden warmup, clock retiming, dropped frame or pause for logging. Full FP64 final states, all population trajectories and frame timing are saved in ten-episode chunks through a bounded background writer. This is simulated software availability, not actual exposure capture or transport. [Protocol](SCHEDULED_CPU_CAMERA_PROTOCOL_V1.md).

The first process was interrupted after 200 complete episodes. Its handle was missing, no completion record existed, and termination cause remained unverified. All 20 complete chunks and their ledgers were independently reviewed and preserved. A new full run used the unchanged frozen driver and conditions in a separate directory with a new clock origin. Related outcomes were already known; this engineering replication is not fresh biological confirmation. Its 300 episodes and all 30 chunks completed. No partial and repeated timelines are spliced. [Interruption/repeat amendment](SCHEDULED_CPU_REPLAY_INTERRUPTION_V2.md), [repeat operational manifest](../results/validation_hardware_v1/scheduled_cpu_camera_v1_r2/operational_manifest.json).

Frame-response latency runs from scheduled availability to completed processing, with a 5-ms budget. Paired-response latency runs from the odd frame's availability to the even frame's completed neural result, with a 10-ms budget. The sum of the two processing durations is reported separately; it omits waiting and backlog. These definitions prevent a fast average from hiding late results.

| Run | Episodes | Frame responses above 5 ms | Paired responses above 10 ms | Paired processing above 10 ms | Largest frame response (ms) |
|---|---:|---:|---:|---:|---:|
| Interrupted | 200 | 9,503/80,200 | 7,680/40,000 | 672/40,000 | 1373.791 |
| Full repeat | 300 | 16,510/120,300 | 15,071/60,000 | 743/60,000 | 78.591 |

In the full repeat, median/p95/p99 frame response is 4.096/6.339/12.589 ms. Maximum implied backlog at processing start is 14 later available frames. The longest consecutive frame-response miss streak is 155 frames. All misses, including startup/reset and logging-associated events, remain in the main counts. Association with logging is descriptive and does not establish its cause.

All saved rates and full final states in the repeated run match their original Python references within 1.73e-18 and 8.13e-20, respectively; every original episode decision is reproduced. Process peak RSS changes from 340.68 MiB at startup to 344.68 MiB at the last episode. These process high-water observations do not prove absence of every leak. Reset episodes do not validate continuous walking or novel scenes. [Partial review](../results/validation_hardware_v1/scheduled_cpu_camera_v1/partial_review_v1/review.json), [full repeat review](../results/validation_hardware_v1/scheduled_cpu_camera_v1_r2/independent_review_v1/review.json), [full raw chunks](../results/validation_hardware_v1/scheduled_cpu_camera_v1_r2/chunks).

![Scheduled response timing](../results/validation_hardware_v1/cpu_camera_projection_v4/report_v1/scheduled_delivery.png)

## Portable package and reproduction

The new [32,697,302-byte V4 archive](../results/validation_hardware_v1/deployment/original_runtime_cpu_v4.zip) contains the original model, compiled projection source, both neural build options, calibration, complete fixtures and standalone checks. It has no GPU dependency and defaults to strict one-thread neural computation with the original 1-ms solver. The optional four-thread bounded activation build is explicit. Both were compiled and executed from isolated /tmp directories with project imports cleared. Their 43-entry package checks, three complete episodes, uint16/noncontiguous tests, nine rejected-input checks and reset/fault handling pass. Earlier archives are preserved.

From a fresh extracted package directory with the declared NumPy/SciPy/C++17 dependencies:

```sh
python selfcheck_cpu_camera_v4.py --work selfcheck_strict
OMP_WAIT_POLICY=ACTIVE OMP_DYNAMIC=FALSE python selfcheck_cpu_camera_v4.py --threads 4 --approximate-activation --work selfcheck_parallel
```

Use a fresh work directory for each run. OpenMP is required for optional multiple threads. The exported README supplies build/replay commands, library provenance and the live one-pair API. Physical cameras require measured optical/photometric calibration, complete coverage and justified clock alignment; the supplied synthetic maps do not supply that evidence. [Exported README](../results/validation_hardware_v1/deployment/original_runtime_cpu_v4/README.md), [strict self-check](../results/validation_hardware_v1/cpu_camera_projection_v4/standalone_strict_v1/selfcheck.json), [accelerated self-check](../results/validation_hardware_v1/cpu_camera_projection_v4/standalone_parallel_v1/selfcheck.json).

## Scientific meaning and next work

The optimization preserves the model's errors as well as its outputs. H2 wrong-direction calls at ±20°/s and HS/bIPS straight-case false alarms remain in the regression fixtures. The larger room/resolution study still fails to establish robust small-yaw detection, and missing electrical coupling and image-to-recording constraints still prevent physiological validation. [Scientific findings](VALIDATION_GENERALIZATION_CONVERGENCE_REPORT_V1.md), [physiological limits](CORRECTED_PHYSIOLOGICAL_DIAGNOSTICS_REPORT_V2.md).

The completed work makes CPU implementation faster and more reproducible, but scheduled deadline failures remain. Next engineering changes should distribute already determined held-input solver work between arrivals and explicitly handle stale outputs, with separately frozen tests and unchanged neural clocks. Actual sensor calibration, target-specific timing, biological matching and eventual motor control require further evidence. No closed-loop controller is implemented and the broad goal is not marked complete.

## Undergraduate explanation: what we did, what we want and why

We want a fly-inspired vision model that can notice unwanted turns and eventually run on real hardware. We made its camera-processing calculation faster while checking that every tested image value and neural output stayed the same. The faster version usually finishes its calculation within the intended time, but a regular stream of images can still build up delays when processing or the operating system pauses. The model also retains its incorrect visual predictions. This tells us that matching the calculation, keeping up with a camera and matching a real fly are separate things to test. We now have a reproducible CPU package and precise evidence about the remaining timing and biological problems.
