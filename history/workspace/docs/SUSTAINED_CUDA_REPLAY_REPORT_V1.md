# Sustained original-clock CUDA replay — V1

Completed 2026-10-21. **Numerical gate: PASS. Every-update 10-ms timing target: FAIL.** The broader validation/hardware goal remains active; this result does not establish physical-camera or robot readiness.

## What was tested

The original frozen circuit ran on the RTX 2050 with the checked shared-memory FP64 GPU backend and portable, arithmetically equivalent compiled frontend. The neural solver remains 1 ms, retinal samples 5 ms and neural updates 10 ms. All parameters, anatomy, image filtering and source routing remain unchanged. No motor commands, new neural fits or hardware-driver/clock/scheduler changes were introduced.

The prospectively specified test repeats the existing 0.4-s binocular walking clip 1,500 times. The model state and clocks reset between clips, while device allocations and the prepared kernel graph persist. This is 600 simulated seconds as repeated episodes, not a continuous 600-s walk, 1,500 independent environments or actual camera acquisition. The previously defined episode yaw decoder is outside this short-clip test.

Startup initialized the runtime in 449.97 ms and explicitly prepared it in 13.84 ms using three neutral synthetic frames, followed by a complete reset before replay. The startup test confirmed that preparing an active stream is rejected without changing its state. All cold-start/earlier timing failures remain in the [preceding checkpoint](CUDA_DEPLOYMENT_PROGRESS_REPORT_V1.md).

[Prospective protocol](SUSTAINED_CUDA_REPLAY_PROTOCOL_V1.md), [frozen methods/input manifest](../results/validation_hardware_v1/hardware_sustained_cuda_v1/before_execution.json), [startup evidence](../results/validation_hardware_v1/hardware_sustained_cuda_v1/startup.json).

## Quantitative result

| Measure | Result |
|---|---:|
| Completed reset episodes | 1,500 |
| Measured paired updates | 60,000 |
| Simulated time | 600 s |
| Entire wall duration, including setup/reset/bookkeeping | 538.83 s |
| Median paired processing | 8.851 ms |
| p95 / p99 | 9.560 / 10.326 ms |
| Worst paired processing | 20.856 ms |
| Updates exceeding 10 ms | 1,096 (1.827%) |
| Maximum observed population-rate discrepancy | 8.67e-19 |
| Maximum full final-state discrepancy reported by runner | 3.47e-18 |
| Recorded process peak RSS, first → last episode | 308.55 → 308.80 MiB |
| Explicit model device buffers at completion | 5,015,261 bytes |
| Cached kernel-graph update shapes | 1 |

The measured unpaced replay throughput was 111.35 paired updates/s when total wall time is included. This exceeds 100 updates/s on average for this repeated clip, while 1,096 individual updates still exceed the fixed budget. Mean throughput and deadline reliability are different results. The run was not paced by real camera arrivals and does not establish their queueing or latency behavior.

The following split was added after scoring as a descriptive timing diagnostic. It leaves the original every-update gate unchanged.

| Update position | Count | Median (ms) | p95 (ms) | Misses |
|---|---:|---:|---:|---:|
| First update of each reset episode | 1,500 | 8.982 | 9.666 | 41 |
| Other updates | 58,500 | 8.848 | 9.555 | 1,055 |

Deadline failures also occur after the first update, so graph preparation alone does not remove them. This experiment does not uniquely localize their causes. The timing measurements include sequential frontend processing, GPU transfers/dispatch/computation and host scheduling on a shared laptop. The four scientific workers remained active. Camera acquisition, raw-camera projection and virtual rendering are excluded.

The process high-water mark rose by 0.25 MiB during the recorded episodes. This is an observed peak-RSS trace, not current live memory or a proof of absence of every possible leak. The explicit model-buffer count excludes GPU driver/context allocations. The one cached update shape and fixed graph buffers support bounded allocation for this tested runtime configuration.

## Numerical review and preservation

The frozen runner compared every population-rate sample and every episode's full final state with the preserved strict CPU replay, under the unchanged 1e-10 tolerance. A separate implementation loaded all 30 raw chunks, independently reconstructed all 60,000 paired times from their two frame durations, recomputed every recorded population-rate discrepancy, and rechecked all episode errors, quantiles, deadline counts, first-update timings and wall-time accounting. All 121,500 raw frame timings remain saved.

Full final states were compared online by the runner; the compact chunks store their error ledger rather than all 1,500 full state arrays. The independent review therefore verifies the stored state-error ledger and its summary, and independently rechecks saved population rates. It does not claim to reconstruct unsaved full states or independently implement the GPU solver. These distinctions limit the verification claim without changing the numerical gate's recorded outcome.

The review reverified all 2,950 original indexed artifacts and every entry in the sustained-run manifest. No old sealed report/result was rewritten. Source hashes, generated PTX, initial import failures, unsuccessful timing variants and all new chunked evidence remain preserved.

[Independent review](../results/validation_hardware_v1/hardware_sustained_cuda_v1/review_v1/independent_review.json), [complete run summary](../results/validation_hardware_v1/hardware_sustained_cuda_v1/sustained.json), [raw chunks](../results/validation_hardware_v1/hardware_sustained_cuda_v1/chunks), [timing/memory figure](../results/validation_hardware_v1/hardware_sustained_cuda_v1/review_v1/sustained_timing_and_memory.png), [PDF](../results/validation_hardware_v1/hardware_sustained_cuda_v1/review_v1/sustained_timing_and_memory.pdf).

## Interpretation and next work

This is evidence of sustained numerical reproducibility and improved computational throughput on actual GPU hardware. The repeated clip and one device cannot establish biological generalization, reliable small-yaw detection, continuous camera operation or hard real-time response. No statistical independence or biological confidence interval is assigned to these repeated updates. All physiological limitations and the running convergence/new-environment study remain separate.

Next steps are a versioned standalone package and full calibrated raw-camera replay, followed by numerical cutoff-margin diagnostics and timing validation on a specified physical camera/platform. Current synthetic camera-adapter tests do not supply measured physical calibration. The fixed episode decoder still needs its original full response window and known model-scale speed; faster neural throughput does not eliminate that decision delay. Closed-loop motor control remains deferred.

Reproduction uses `env PYTHONPATH=src python scripts/run_sustained_cuda_replay_v1.py --cycles 1500 --output FRESH_WORKSPACE_PATH` with the preserved baseline/model and checked frontend library. Existing result directories are refused. The script sets a run-local CUDA cache and saves bounded chunks throughout execution.

## Undergraduate explanation

We ran the same visual-neural calculation repeatedly on the laptop GPU to check whether it stays accurate and fast over time. Its answers stayed extremely close to the original CPU calculation, and average processing was fast enough for 100 updates per second in this replay. Some updates were still late, so average speed does not yet guarantee reliable real-world timing. This moves us toward a hardware implementation while showing exactly what still needs work before using camera input or controlling a robot.
