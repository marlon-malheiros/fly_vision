# Direct-voltage V1 audit correction and integer-clock sensitivity R2

2026-11-05, after V1 held-out outcomes. Preserve every V1 result, gain, frozen
method, failed reviewer and discrepancy diagnostic. The initial independent
review converted microseconds by division; the producer used multiplication by
1e-6. At exactly aligned bin edges, floating-point differences move one native
sample between adjacent bins. Three of80 scored repetitions differ by more than
roundoff; maximum discrepancy0.02495421246mV. This is a preprocessing boundary
issue, not cumulative-sum cancellation or a biological/model-parameter repair.

Before further response calculations, freeze this finite audit:

1. Re-run the unchanged independent raw-data reviewer with a separate direct-sum
   extraction using the producer's literal time conversion. Retain its1e-8mV
   tolerance. Save the successful continuation under a new R2 name, preserving
   the first failure. This checks V1 reproducibility under its implemented clock.
2. Independently bin in **integer microseconds**, with left-inclusive,
   right-exclusive2000us bins and baseline[-250000,-50000)us. Require native
   timestamps and onset to be exact integers. Recompute every early localizer,
   the two later response repetitions, direction-blind references and inhibitory
   masks. Require the early selected PD to stay identical; otherwise stop because
   the already simulated canonical inputs would differ.
3. Reuse the identical saved model forecasts. Bin centers agree within1e-14s;
   no neural re-solve, parameter/axis/latency/gain search, new stimulus or new
   recordings. Recompute the same two development-only scalar gains, held-out
   MSEs, all27 bootstrap resamples per output and all unchanged success rules.
   Archive corrected mean responses and summary outcomes separately under
   `results/t4_direct_voltage_v1/clock_sensitivity_r2/`.
4. Report both V1 and exact-tick sensitivity. R2 uses already inspected test
   recordings and is a numerical correction/sensitivity, not a new biological
   validation experiment. It must not replace a failed scientific criterion.

The separate scalar pixel/event/gate audit has already passed; that does not
resolve the bin issue. Original primary waveform failures and zero qualifying
inhibition masks are known before R2. No criterion, model or selected cell may
change. Freeze script/protocol/V1-result hashes before executing R2. The four
C2/C3 animals remain unscored. No additional movie/source download.
