# Mi1 benchmark R3 — verifier-only dtype correction

2026-11-05. R2 independent review failed on raw uint8 `istim`: NumPy unsigned
differences wrap downward transitions instead of becoming negative, so the
reviewer's raw-input call found no falling edges. Original scientific processing
explicitly converted stimuli to float before prediction and epoch extraction;
its curves and locked zero gains are unchanged. The frozen low-level epoch
helper accepts signed/float input and is not changed in place.

Preserve the failed R2 traceback, oracle files and source. R3 first casts only
reviewer inputs to float, documents the unsigned-input regression, compares
already-generated original-author development-only Octave output with Python,
and independently checks retained scalar metrics. No rerun of successful model
calculations or Octave job, no new fit and no reserved response processing.
Document the failure in the final report; failed R2 reviewer CPU was not saved,
so successful-stage totals are a lower bound on full-attempt resources. This
changes no biological acceptance criterion. R2 descriptive positive-selection
shape cosines have already been inspected (approximately0.631–0.883 in controls).

Finalize through a separate R3 report writer and subsequent R2 seal/verify stages,
including this correction and exact R3 sources in the immutable archive. The
initial unsealed R2 generated report draft is preserved; the final report
explicitly records the failure rather than claiming an exception-free run.
