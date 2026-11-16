# Independent review correction, V1

The initial frozen review stopped before waveform review on 12 October 2026 UTC:
`OverflowError: Python integer -40 out of bounds for uint8`. Some published
`PosD_mg` arrays contain only nonnegative values and load as unsigned integers.
The independent full-field stripe reconstruction adds negative tile offsets,
which NumPy 2.4 rejects for those arrays. This is an audit implementation error,
not a failed numerical tolerance or a simulation result.

Retain the original frozen analysis/review script and all 280 outputs unchanged.
The new review wrapper converts only `PosD_mg` metadata to signed 64-bit integers
and explicitly verifies that every integer value is unchanged, then reruns the
original independent review. The production renderer already casts positions to
signed integers and does not require a correction. No fitting, raster, sampling,
timing, numerical dynamics, scoring rule, threshold or scientific decision is
changed. This correction was introduced after the transfer scores and must not
be described as part of the original prospective freeze. Hash this amendment
and the wrapper before the corrected review runs; preserve the failed attempt.
