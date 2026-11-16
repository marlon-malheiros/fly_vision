# H2 stimulus/trial metadata and benchmark specification V1

25 October 2026, America/Belem. The user authorized the distinct unfinished
task identified by the mapping/research audit. Preserve the raw H2 deposit,
previous studies and all frozen model parameters. This work decodes source
metadata and specifies a benchmark; no neural score is allowed before its
input, observation and independent-testing gates are satisfied.

The source is the already verified Zhao H2 deposit v2, containing seven cells,
two protocols per cell, indexed stimulus responses, the MATLAB `edgeTable`
and author scripts. Existing processed tuning summaries were inspected before
this work. These animals cannot be relabeled wholly fresh validation data.

## Bounded execution

1. Inspect only serialization/schema first. Preserve exploratory tools,
   interruptions and failed decoder versions. Build a decoder for the actual
   MATLAB table representation; never guess a row mapping from model responses.
2. Freeze the extraction implementation before full metadata extraction and
   any source-response analysis. Decode cell/protocol/index, direction,
   position, polarity, duration and original protocol fields, retaining all
   columns and provenance. Expected counts from the earlier source admission
   are checks, not reasons to discard inconsistent rows.
3. Check every table row against its `edgeStruct(cell).aligned(protocol)`
   indexed response metadata. Require unique joins, integer/in-range indices,
   complete declared coverage, and exact agreement for shared numeric/text
   metadata. Preserve exceptions and stop scoring if correspondence is ambiguous.
4. Independently verify column names, row order and response indexing, including
   first/last and every joined condition. Exercise a small synthetic malformed
   metadata fixture to ensure that duplicate/out-of-range/mismatched joins fail.
5. Inventory trial repeats, time axes and available observation types without
   fitting the neural model. If the source index is verified, reproduce the
   author's baseline and stimulus-window definition as a source-only check,
   preserving signed responses and coverage/missingness. Any physiological
   endpoint extraction receives a separate pre-outcome freeze; do not silently
   turn metadata exploration into a tuned benchmark.
6. Define one directional-tuning benchmark: stimulus reconstruction, display/eye
   mapping, observable and statistic, prior-inspection status, calibration/test
   separation, uncertainty and stop gates. Run model scoring only if those
   definitions have enough independent evidence. Otherwise complete the metadata
   work and report precisely which gate remains unresolved.

## Limits and deliverables

Keep metadata admission, source analysis, observation calibration and model
validation separate. Do not compare uncalibrated model activity directly with
voltage/spike frequency, invent trial stimulus frames, choose favorable side
conventions or use PD summaries as complete 16-direction trial curves. Missing
biological constraints are not repaired by optimizing yaw classification.

Produce versioned decoding/review code, all decoded tables and join checks,
source provenance, a machine-readable benchmark specification, appropriate
figures and a concise report ending with an undergraduate what/we-want/why
explanation. Append progress throughout, preserve failures, save a dated
progress copy and seal completed evidence separately. Stop repeating old
mapping or yaw sweeps: this is an external-data task with a distinct endpoint.
