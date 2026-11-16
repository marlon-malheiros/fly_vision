# Pre-score loader correction for the mixed T5 pilot

Client date: 2026-10-12 (America/Belem).

The frozen runner stopped at `ROOT[x['path']]` in its input loader with
`TypeError: 'PosixPath' object is not subscriptable`. The error preceded baseline
replay and all candidate calculations. Its source and frozen manifest remain
unchanged; no scientific scores existed at correction time.

The separately hashed recovery wrapper changes only path access to
`ROOT/x['path']` in an otherwise identical loader. All original candidate,
measurement, comparison, integration and review functions run unchanged.
The new integration check loads all 26 real native inputs and confirms recorded
clocks, sample counts and baseline/observation array alignment. No candidate
selection, threshold, stimulus, parameter or outcome definition changes.

The original run's [failure](../results/t5_mixed_parameter_sensitivity_v1/loader_failure_v1.txt)
and [amendment hashes](../results/t5_mixed_parameter_sensitivity_v1/loader_amendment_manifest.json)
are retained. Subsequent execution/review use
`scripts/recover_t5_mixed_parameter_sensitivity_v1.py`, whose CLI verifies both
the amendment hashes and the original manifests.
