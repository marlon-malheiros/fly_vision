# Original-clock GPU deployment progress — V1

Checkpoint dated 2026-10-21. Numerical preflights and short replay comparisons are complete. Sustained replay, complete camera processing and physical robot testing remain separate gates. This is a development report; the main frozen validation/convergence study remains running and its scientific outcomes have not been scored.

## Result

The original frozen MaleCNS rate model now runs on the available NVIDIA GeForce RTX 2050 through its installed driver. No CUDA toolkit/framework installation, driver change, GPU clock adjustment or neural parameter tuning was performed. Original CPU paths, model files, scientific methods and unsuccessful timing results remain preserved.

The latest short calibrated-retina replay reaches median paired-update latencies of 8.65–8.99 ms with the portable optimized frontend, compared with 17.52–18.30 ms for strict CPU replay in that same interleaved test. It still misses 3 of 120 measured 10-ms deadlines. Native compilation misses 4 of 120. These are improved throughput measurements on one laptop, not real-time certification or a demonstrated camera/robot system.

## Preserved computation and implementation versions

All GPU versions keep FP64 weights/states, the original 1-ms RK4 clock, actual floating step differences, input-boundary convention and the same order of chemical additions. Nonzero electrical coupling is explicitly rejected because this backend does not implement it. Neither anatomical graph gains connections, and no cell or edge is pruned.

V1 assigns one thread to each ordered CSR row. V2 computes connection products in parallel, then sums each row in the original order; an optional CUDA graph schedules those operations. V3 copies the ten longest rows' products into shared memory and has one thread sum them in the same order. The 64-term split and 2,048-term shared-storage limit are computational decomposition choices. Both supplied graphs fit this limit; a larger incompatible row is rejected.

The activation is an explicitly tested approximation: the existing degree-13 polynomial on |x|≤0.125, a fixed continued fraction outside that interval up to |x|=20, and signed saturation beyond 20. Dense/boundary numerical testing is not a global analytical error proof. The functional frontend's V3 pooling traverses independent columns contiguously while retaining every column's original arithmetic sequence; it does not reconstruct physiological upstream visual circuitry.

[V1 protocol](CUDA_DEPLOYMENT_PREFLIGHT_PROTOCOL_V1.md), [V2 protocol](CUDA_DEPLOYMENT_PRODUCTS_PROTOCOL_V2.md), [V3 protocol](CUDA_DEPLOYMENT_SHARED_PROTOCOL_V3.md), [frontend memory protocol](DEPLOYMENT_FRONTEND_MEMORY_PROTOCOL_V3.md).

## Numerical evidence

Each GPU version passed the same 11 predeclared cases: four historical full two-second walking inputs; original bIPS silencing and outgoing-removal copies; expanded intact and new-family-silenced copies; strong-input and large-initial-state software stress cases; and a short independent Python/SciPy RK4 comparison. Full cell states were compared at each recorded update in the preflight runner. Reset, multiple contexts, invalid input, identity coverage, immutable graph buffers, closed-backend handling and unsupported electrical coupling were also checked.

Across the 33 neural cases, maximum cumulative full-state difference was 3.55e-15 and maximum population-rate difference was 1.11e-16, below the unchanged 1e-10 gate. Each version's 160,016 activation probes differed from NumPy tanh by at most 4.45e-16, below its 1e-12 test-set gate. The portable/native frontend builds both gave bit-identical drives and filter states to the preceding compiled frontend across 119 frames each (81 walking, 32 random, six boundary/pattern controls) and all 13,579 source targets; maximum difference from the independent Python frontend was 8.89e-16, below the existing 1e-7 drive tolerance.

A separate saved-array review verified all 33 neural cases, source/factory/PTX provenance, all 33 timing records and all 1,320 paired-update measurements. It recalculated summary errors, deadlines and scalar-interpolated quantiles without importing production solver/timing helpers. It verifies saved-array and summary arithmetic; the full-state comparisons during integration remain those recorded by the preflight runner. It does not independently reimplement the GPU driver, validate untested inputs or establish physiological validity.

[Independent review](../results/validation_hardware_v1/cuda_deployment_review_v1/independent_review.json), [all numerical comparisons](../results/validation_hardware_v1/cuda_deployment_review_v1/numerical_comparisons.json), [all timing records](../results/validation_hardware_v1/cuda_deployment_review_v1/timing_comparisons.json).

## Timing outcomes, including failures

Each table is one separate interleaved three-repeat experiment on logical CPU 0 with the four scientific workers still running. Each configuration has 40 paired updates per repeat. Ranges show variation across repeats; the miss count totals all 120 updates. Full first-update, setup, maximum and percentile measurements remain in the linked JSON/NPZ files. Camera acquisition, raw-camera projection and virtual rendering are excluded. The later 0.4-s benchmark clip contains actual simulated forward walking with a small yaw; it is not a stationary-frame control.

### Driver / product factorization

| Implementation | Median range (ms) | p95 range (ms) | Misses / 120 |
|---|---:|---:|---:|
| cpu_strict | 17.98–28.09 | 24.53–29.20 | 120 |
| sequential | 16.33–16.93 | 17.36–18.40 | 120 |
| products_launches | 12.88–13.07 | 13.64–15.06 | 120 |
| products_graph | 12.72–13.06 | 13.18–13.85 | 120 |

[Full measurements](../results/validation_hardware_v1/hardware_cuda_benchmark_v1/benchmark.json).

### Ordered shared-memory sums

| Implementation | Median range (ms) | p95 range (ms) | Misses / 120 |
|---|---:|---:|---:|
| cpu_strict | 17.34–18.27 | 18.34–26.67 | 120 |
| products_graph | 12.77–13.10 | 13.62–13.95 | 120 |
| products_shared_graph | 9.15–9.23 | 9.54–11.30 | 7 |

[Full measurements](../results/validation_hardware_v1/hardware_cuda_benchmark_v2/benchmark.json).

### Equivalent frontend memory access

| Implementation | Median range (ms) | p95 range (ms) | Misses / 120 |
|---|---:|---:|---:|
| cpu_strict_frontend_v2 | 17.52–18.30 | 18.38–21.51 | 120 |
| gpu_frontend_v2 | 9.19–9.48 | 10.29–11.34 | 12 |
| gpu_frontend_v3_portable | 8.65–8.99 | 9.10–9.92 | 3 |
| gpu_frontend_v3_native | 8.61–8.65 | 9.13–9.52 | 4 |

[Full measurements](../results/validation_hardware_v1/hardware_frontend_benchmark_v3/benchmark.json).

The unoptimized GPU and the product-only optimization missed every deadline in their initial complete replay test. Shared memory removes most of that cost, and the frontend memory change yields a smaller additional improvement. Every new configuration preserves numerical agreement. The differing CPU timing ranges across tables also show why results from separate load/thermal conditions should not be treated as one controlled speed ratio.

[Timing figure (PNG)](../results/validation_hardware_v1/cuda_deployment_review_v1/timing_progress.png), [PDF](../results/validation_hardware_v1/cuda_deployment_review_v1/timing_progress.pdf). All three panels were visually inspected for labels, separate experiments, the fixed budget and visible failures.

## Failures and reproducibility boundary

Initial GPU and frontend-preflight launches failed before numerical execution because the project source path was absent. The original logs and code snapshots are retained in the import-failure directories; adding explicit `PYTHONPATH=src` fixed the environment without changing implementation or gates. The numerical comparisons then completed. All timing failures remain part of this report. The previously failed 2-ms solver equivalence gate remains failed and is not used by these original-clock implementations.

Commands use a normal GPU-enabled host environment, the existing Python/NumPy/SciPy stack, g++ for the frontend, and the installed NVIDIA driver. For example: `env PYTHONPATH=src python scripts/preflight_cuda_shared_v3.py --output results/validation_hardware_v1/cuda_driver_v3/FRESH_RUN`. Preflight scripts require a new output path; existing evidence is never overwritten. Benchmark scripts likewise refuse to overwrite their fixed versioned result directories. GPU cache paths are explicitly set inside each run.

Primary implementation references: [NVIDIA driver execution API](https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__EXEC.html), [CUDA graphs](https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__GRAPH.html), [PTX instructions](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html).

## Work still required

The separately specified [sustained replay](SUSTAINED_CUDA_REPLAY_PROTOCOL_V1.md) is running; its complete numerical/timing result is not yet available at this checkpoint. It preloads the graph using neutral synthetic frames, resets all state before data, and repeats a 0.4-s clip 1,500 times. It must be reported as a repeated-episode stress test rather than continuous walking or real camera acquisition.

Next, package the checked source/model with reproducible standalone camera replay fixtures; measure the complete calibrated raw-camera-to-neuron path; inspect numerical readout margins near fixed cutoffs; and test an actual specified camera/platform when available. Existing short standalone V1/V2 packages remain unchanged and do not yet include the new GPU backend. The camera adapter currently has synthetic software tests, not measured physical calibration. The episode decoder still requires known model-scale speed and the complete original response window, with output around 1.4 s; neural throughput is not instantaneous turn-decision latency. No motor-control loop is implemented.

Physiological stimulus/measurement limitations and unresolved electrical/anatomical constraints remain those documented in the scientific reports. Running the same equations faster improves computational implementability; it supplies no new evidence that those equations fully reproduce a fly's physiology. The frozen new-environment/convergence study must also finish and receive its prospectively specified analysis before the broader validation goal is complete.

## Undergraduate explanation

We want the model to recognize visual motion reliably and eventually run as part of a real sensing system. We translated the same neural equations to the laptop's GPU and changed how memory is accessed, then checked that the answers stayed the same. Typical processing became roughly twice as fast in the latest controlled comparison, but some updates still take too long. This is useful engineering progress: it brings hardware implementation closer while keeping biological accuracy, camera calibration and robot control as separate questions that still need evidence.
