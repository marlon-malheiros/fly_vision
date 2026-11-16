# Frozen raw-local control qualification V1 — 2026-11-02

## Why this is a separate study

The [local-subunit pilot](LOCAL_SUBUNIT_PILOT_REPORT_V1.md) is sealed as a negative
primary result. Its raw control unexpectedly passes the fast necessary gate:
30/32 small turns, 16/16 and 14/16 per direction, 1/16 straight alarms. This
study nominates that control **retrospectively**; it does not convert the pilot
into a primary success or call the inspected fast rooms independent validation.
New evidence justifies reassessing the plan to abandon this entire readout
family after normalization failure. No original criterion or result changes.

Freeze this document, implementation, candidate coefficients, original feature
implementation/map/floor, all additional calibration/numerical plans and their
old receipts before extracting any additional features. Exactly one candidate:
the pilot's `raw_local` model. No fit, hyperparameter comparison, sign flip,
feature change, normalization adjustment or relaxed gate is allowed. Old fast
features are referenced, not copied or overwritten. Existing source/graph,
functional routing and parameters remain frozen; no biological connection is
inserted and no physiological validity is inferred from decoding.

## Sequential qualification

1. Reuse the pilot's 80 fast w episodes and extract the remaining 176 w episodes
   with exactly the frozen observer/feature code. Full calibration comprises
   256 episodes across 16 previously inspected development rooms. Set one common
   cutoff from zero-yaw/static controls only: the maximum per-group order
   statistic allowing <=1/16 strict-threshold episode alarms. Turns use callback
   119, 190 ms after onset; negatives use callbacks 100..299 continuously.
   At every speed and both +/-2 and +/-5 require >=26/32 joint signed detections,
   >=13/16 per direction, <=1/16 straight alarms, and <=1/16 static alarms.
   If any condition fails, stop; no numerical run or new-room evaluation.
2. If calibration passes, evaluate the original 27 numerical conditions
   (three scenes, three speeds, zero/+/-2) with primary and spatial profiles.
   Compare all 27 spatial refinements first, then all 27 temporal refinements,
   then all 27 solver refinements. At each completed profile require max absolute
   score difference <=0.2 on the declared endpoint/negative callbacks, identical
   signed endpoint decisions, and identical negative-episode alarm status.
   Record callback decision flips descriptively. Stop after any failed profile.
   Qualification requires all **81 comparisons**, never a subset. A partial
   failing run may establish failure, never success. Use the existing 0.5-degree
   spatial, doubled input/image sampling, and half-step solver definitions;
   retain the one-ms forcing ramp. No tuning from numerical outcomes.
3. Only if all calibration and 81 numerical gates pass may a further explicit
   test freeze admit the still-unused 24 st environments. Their seeds/outcomes
   are not accessed by this protocol's execution stages. Fresh testing must
   retain the original per-direction/joint/false-alarm rules and both yaw
   magnitudes at all speeds, with the same fixed model and common cutoff. A
   separate total-runtime/storage estimate must precede rendering. Test data
   cannot select another candidate or threshold.

## Integrity, resources and limitations

Require source-drive/image hash agreement and bitwise re-pooled population,
checkpoint and final-state agreement with the archived circuit outputs for each
new known/numerical solve. This reproduces original numerical profiles; it does
not guarantee score convergence. No movies or full neural traces are saved.
Copy only small maps/floor/manifests; streamed neural rates are temporary. Save
compact features/scores, exact model, comparison rows, receipts and failures.
Verify pre-onset feature/score equality and independently recompute all scores
and gates from the saved features without a model refit.

At most four one-thread CPU workers, no GPU, <=3,600 aggregate new observation
CPU seconds, <=1 GiB peak worker RSS, <=512 MiB persistent output and >=20 GiB
free space. Based on measured pilot cases, plan <=1,200 CPU seconds for the
remaining calibration and <=2,000 for all numerical profiles; actual costs are
recorded. Estimated persistent output <=100 MiB calibration, <=60 MiB numerics,
and <=40 MiB overhead. Completed in-flight jobs may exceed a newly detected
limit; preserve/report the overrun and stop rather than weakening rules.

No novel physiological measurement is available from this computation. The
candidate directly reads T4/T5 and downstream cells, so passing would establish
an artificial neural decoder under specified simulations, not proof of the
HS/H2/bIPS/DNp15 mechanism or biological causality. Electrical/upstream gaps and
measurement-model limitations remain. Preserve the original negative pilot,
all old studies, progress snapshots, and failed qualification outcomes.
