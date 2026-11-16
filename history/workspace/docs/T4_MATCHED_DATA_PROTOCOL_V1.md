# T4 stimulus/measurement source admission V1

2026-11-05. The user authorized finding a fair T4 biological comparison before
further neural tuning. Existing models, results, response partitions and the four
unscored C2/C3 control flies remain unchanged. This work first tests data
admission, not a model response score. Qualitative paper findings and all earlier
project results are known. A newly downloaded file is not automatically a fresh
biological holdout; past response inspection must be recorded.

Search is bounded to three concrete public sources and the existing local
Henning2022 edge data: (1) Tanaka etal2023, Dryad `10.5061/dryad.bcc2fqzjz`;
(2) Ammer etal2023, GIN `gammer/Ammer_et_al_2023` and publisher source data;
(3) Gruntman etal2018 T4 electrophysiology, Janelia collection3955843. The 2022
parallel-T4 port remains a source-model reference, not new biological data.
Public paper/code metadata may be inspected now. Do not score new amplitudes,
fit observers, alter neural parameters or consume reserved responses during
admission. Preserve HTTP failures; use small metadata/ranged ZIP requests rather
than whole-archive downloads.

Admission requires verifiable neuron/animal/session identity, independently
partitionable animals or repetitions, actual response sampling times and units,
stimulus onset/offset and condition mapping, a reconstructable stimulus
definition/generator with geometry/contrast, and the relevant observation
convention. Distinguish recorded timestamps from inferred nominal frame rates.
Published stimulus parameters alone do not establish projector-frame parity.
Calcium does not have to match voltage1:1; a prospective observer may be
calibrated on development data and evaluated on independent samples. Such
calibration cannot uniquely identify neural and indicator dynamics without
additional constraints. Direct voltage is an explicit alternative.

For each source, produce an evidence/gap table and one of: supported for a
bounded matched comparison, conditional on listed uncertainties, unavailable
within this audit, or previously inspected development evidence. An exact-image
gate and a bounded-stimulus-family gate are distinct. A failed download is an
access limitation, not proof that the biological data do not exist.

If a candidate qualifies, freeze a separate model/observer/analysis/split before
opening its response values. If none qualifies, report the missing constraints
and concrete attainable alternatives rather than launch another parameter
sweep. Do not relabel repeatedly inspected recordings as blind validation.

Resource contract: one worker,20GiB free reserve, at most250MiB acquired payload,
512MiB output cap, individual new data member at most64MiB, metadata request
limit16MiB, request timeout25s, at most two attempts per endpoint. No raw imaging
movies, bulk repositories or whole13.8GB/17.4GB archives. All fetched files and
source receipts are hashed. Append dated project progress, preserve corrections,
copy progress and methods into each completed output, and seal after writer exit.
