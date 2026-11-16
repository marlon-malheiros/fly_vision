# Original-clock CUDA deployment preflight — V1

Specified 2026-10-21 before numerical outputs from the new GPU implementation.
This implementation is separate from the frozen running scientific methods.
No study input, graph, neural gain, response window, decoder or outcome criterion
is changed. Existing CPU implementations and unsuccessful timing results remain
preserved. No drivers or software frameworks are installed.

Use the installed CUDA Driver API with generated PTX, FP64 states and weights,
explicit rounded multiply/add/divide instructions, sequential CSR row sums and
the original 1-ms RK4 clock, including its input-boundary convention and actual
floating-point step differences. Nonzero electrical coupling must be rejected
rather than silently omitted. The CUDA cache must use an explicitly supplied
writable path. This GPU is a candidate development target, not a robot-board test.

Activation uses the previously checked degree-13 polynomial on |x| ≤ 0.125.
Outside this interval use the Lambert continued fraction with 16 terms for
|x| ≤ 2 and 64 terms for |x| ≤ 20, and signed saturation beyond 20. This is an
explicit numerical approximation to validate, not a fitted physiological change.
Compare at least 100,000 dense and boundary probes with NumPy tanh; require
maximum absolute difference ≤ 1e-12 on this declared test set. A grid check alone
is not a rigorous global error proof.

Compare four historical two-second original-intact walking inputs (straight,
±2 and +20 degrees/s at 16.5 mm/s), expanded intact/new-family-silenced copies,
and original bIPS-silenced/outgoing-removed copies using exactly the same source
drives. Compare all full cell states at each 10-ms sample with strict CPU RK4 and
the appropriate sealed trajectories when available. Include strong all-ones
inputs and nonphysiological large signed initial states to exercise activation
fallbacks; these are software stress tests, not biological input predictions.
Also compare a short independently implemented Python/SciPy trajectory.
Require maximum absolute full-state/rate difference ≤ 1e-10 on every declared
case. Preserve every failure, code snapshot, generated PTX, source hashes and log.
Do not relax a failed gate based on classification agreement.

Check reset determinism, multiple contexts, identity coverage, read-only graph
buffers, invalid-input state preservation, closed-backend rejection and explicit
rejection of unsupported electrical coupling. A successful preflight permits
timing measurements; it does not establish full-case deployment equivalence.

After numerical preflight, benchmark the existing calibrated-retina fixture
through the unchanged compiled frontend and GPU circuit at the original 5-ms
retinal/10-ms neural clocks. Save per-frame and paired-update timings, errors,
device/driver/source provenance and concurrent-load conditions. The existing
10-ms paired-update budget stays fixed. Report percentile latencies and every
deadline miss. Acquisition/rendering are excluded unless explicitly added in a
separate measurement. No physical-camera validity, hard-real-time guarantee or
motor-control readiness follows from replay speed alone.

Primary implementation references: [NVIDIA Driver API execution control](https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__EXEC.html),
[driver programming guide](https://docs.nvidia.com/cuda/cuda-programming-guide/03-advanced/driver-api.html),
[PTX instruction specification](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html).
