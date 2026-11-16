# Simple summary: looking beyond timing compensation

We asked whether different excitation/inhibition strengths could give nearly the
same responses. We measured ten active parameters across **78 inputs**, then
tested **40 valid alternatives** from a fixed local algorithm.

**NO_MATERIAL_OUTPUT_EQUIVALENCE_IN_LOCAL_BANK**. None of the generated material alternatives preserves all declared outputs. This finite, local algorithm does not prove that broader compensation is impossible.

The easiest changes are still mostly filter timing. Twelve alternatives meet our
substantial-change definition, and none passes all response checks. Eleven alter
both E/I conductances by at least 10%, and all fail the response criteria. The
earlier timing-compensation example still passes all 78 inputs.

The full sensitivity matrix has numerical rank 10/10;
the gain/spatial-only matrix 6/6. Small sensitivity
does not mean an exact alternative circuit exists. Sensitivity interpretation
provisional: **False**.
All 6,552 calculations passed separate numerical verification.
No new recordings were used or fitted.

Close this bounded E/I search and keep the validated timing-compensation result with its narrow scope. The present bank does not support a stronger both-channel claim. A concrete next step is a short evidence package for the supervisor, stating the numerical successes and the remaining biological/mean-response limits; further expansion should require a new scientific hypothesis or independent data, rather than additional unstructured searching.

[Technical report](T5_ACTIVE_SENSITIVITY_REPORT_V1.md).
