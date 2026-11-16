# Neural population release — 1 November 2026

The scientific protocols/results are dated 31 October. Release verification
continues on 1 November, following the current project date in America/Belem.
The date-aware release wrapper changes packaging/progress dates only; all
frozen scientific code, criteria, models, readouts and numerical results remain
unchanged. It preserves the existing sealed V1 index and creates a correctly
dated progress snapshot in R2 before sealing.

After ordinary V1 sealing, the actual final release commands are:

```text
python scripts/release_neural_population_v1.py post-v1 --date 2026-11-01
python scripts/release_neural_population_v1.py seal-r2 --date 2026-11-01
python scripts/release_neural_population_v1.py post-r2 --date 2026-11-01
```

Run each in a separate process, stopping on any error. No original sealed file
is overwritten; post-exit verification receipts and the live progress report
remain outside the respective immutable indexes. This wrapper supplements the
earlier reproduction guide's hardcoded October packaging dates.

The primary 2°/s target remains failed. A predefined secondary neural-only
reader passes the finite 5°/s behavioral criteria and all 135 declared numerical
comparisons. This is an external supervised observer of a frozen functional
surrogate/MaleCNS circuit; physiological validation and an identified biological
readout remain unestablished. See the [brief](NEURAL_POPULATION_MILESTONE_BRIEF_V1.md).
