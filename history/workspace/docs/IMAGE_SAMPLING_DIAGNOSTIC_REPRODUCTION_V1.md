# Reproduce the image-sampling diagnostic V1

The authoritative experiment is `results/image_sampling_diagnostic_v1`, with
conditions in `configs/image_sampling_diagnostic_v1.json`. Use the recorded
Python/NumPy/SciPy environment and unchanged selected predecessor artifacts.
The binary `results/validation_hardware_v1/methods/streaming_core_v1_r2.so`, original
graph, frontend configuration, targets and Study A decoders are required. Their
identities are recorded before execution. This is a numerical research replay,
not a camera deployment or physiological validation procedure.

The original phase commands, executed from the repository root, are:

```bash
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/run_image_sampling_diagnostic_v1.py prepare
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/run_image_sampling_diagnostic_v1.py preflight
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/run_image_sampling_diagnostic_v1.py freeze
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/run_image_sampling_diagnostic_v1.py run
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/analyze_image_sampling_diagnostic_v1.py
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/review_image_sampling_diagnostic_v1.py
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/plot_image_sampling_diagnostic_v1.py
```

These commands refuse already existing output paths. Preserve the completed
authoritative experiment. To reproduce it, choose a **new** namespace and use
the wrapper for each phase, in the same order:

```bash
env PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/reproduce_image_sampling_diagnostic_v1.py prepare --destination results/image_sampling_reproduction_YYYYMMDD_R1
```

Then replace `prepare` with `preflight`, `freeze`, `run`, `analyze`, `review` and
`plot`, retaining exactly the same destination. The wrapper redirects output
paths; it preserves the methods, inputs, selected scenes, parameters, stopping
rule and tolerances. It requires its namespace marker for later phases and
rejects the authoritative destination. No second full sweep is implied by
providing this reproduction entry point.

The run retains approximately 21 GB of uncompressed binocular retinal movies
plus source/motion/network evidence. It checks a 10-GB free-space reserve before
each profile and uses three independent input workers with single-thread BLAS.
Failures leave their existing artifacts and logs. Do not delete or overwrite a
failed attempt to obtain a successful run; diagnose it and declare any changed
method as a separate version.

Interpret `analysis_v1/complete.json` carefully: analysis can complete with
`stability_gate_met: false`. The independent review checks calculations and
declared gate classification; it does not require a scientifically favorable
result. `diagnostic_counts.csv` concerns two previously inspected rooms and
omits ±40°/s, so it does not supply a new generalization threshold. Direct rays
are a reference for the same synthetic point-sampling model.
