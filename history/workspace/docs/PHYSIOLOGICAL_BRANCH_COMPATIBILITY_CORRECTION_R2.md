# R2: preserve failed literal-Octave oracle; restore real-image arithmetic

2026-11-04. Scientific freeze `dbff5b4` remains unchanged. The V1 Python curves,
all10 passing numerical refinements, seven failed oracle outputs and the explicit
28/28 endpoint disagreement are preserved. All12 kernel comparisons passed before
the endpoint check failed. This correction does not reinterpret that oracle as a
pass and does not change input kernels, model equations, conditions or tolerances.

Isolated runtime probe: Octave10.3 evaluates `[-1+1e-16i,1+1e-16i]>0` as `[1,1]`.
MATLAB's documented `>` compares real parts, yielding `[0,1]:
[MathWorks](https://www.mathworks.com/help/matlab/ref/double.gt.html),
[Octave source](https://docs.octave.org/doxygen/stable/d3/dbc/oct-cmplx_8cc_source.html).
The author's FFT blur is mathematically real, but tiny roundoff imaginary parts
reach the rectifier. Octave consequently admits negative inhibitory/excitatory
values as positive. This is an implementation compatibility failure, not evidence
that real image currents should be complex or that the original MATLAB model is
wrong. The first oracle used no explicit real projection.

Before recomputing any R2 oracle, freeze an Octave `ifft` compatibility shim that
calls its built-in transform, asserts imaginary residual <=1e-12 times the global
real scale (floor1), records the maximum residual, then returns the real part.
No other MATLAB arithmetic is changed. The author functions remain byte-identical.
An R2 wrapper copies the frozen V1 oracle launcher, changes only its output name,
and adds the shim through OCTAVE_PATH. Compare the same seven full-field/four-output
oracles and all12 kernels with the original Python arrays under the original
1e-9 relative/1e-10 absolute tolerances. No parameter fitting or outcome selection.

R2 Python means are not new physiological predictions. Reuse all V1 curves and
ten refinements unchanged. Record the originally failed runtime, R2 correction,
all residual checks, R2 resources and cross-backend discrepancies. V1 aborted
before its terminal resource receipt; its complete CPU accounting is unavailable
and cannot be relabeled as a verified whole-attempt CPU-budget pass. The R2 oracle
gets the same1200s wall limit; report its measured time separately. Retain all
source files, failures, receipts and dated progress in the final artifact index.
This compatibility correction does not create biological validation or make the
published T4-only comparator a replacement MaleCNS frontend.
