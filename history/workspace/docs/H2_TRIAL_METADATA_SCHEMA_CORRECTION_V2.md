# H2 raw-repeat clock correction V2

25 October 2026. V1 extraction stopped before saving any joined table or
scoring any response: it required each raw repeat to have the aligned mean's
sample count. The source retains separate raw trial clocks, while its aligned
mean/raster use a common clipped clock. A bounded inspection of the first
condition of each protocol confirmed different lengths (for example, cell 1
protocol 1 mean 47,098 samples; raw repeats 47,114, 47,976 and 47,098).

Preserve V1 code, freeze and failed log. V2 inventories and validates each raw
repeat's own monotonic finite clock; it continues to require exact agreement
between the aligned mean, raster and declared repeats. All original metadata
join, uniqueness, coverage and equality criteria remain unchanged. No samples
are dropped or resampled. No neural or spike-rate outcome was inspected to
select this correction. Freeze V2 before a fresh metadata extraction.
