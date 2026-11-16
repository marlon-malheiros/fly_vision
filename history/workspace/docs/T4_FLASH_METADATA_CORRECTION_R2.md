# Stationary-flash metadata serialization correction R2

2026-11-06. The first metadata audit verifies the cell3 image/time rows but fails
while writing `inputParams.intFrames=NaN` into strict JSON. That missing value is
legitimate source metadata, not a voltage defect. No response amplitude was
processed. The original acquisition/metadata helper remains unchanged and its
incomplete JSON stream is moved to `failed_metadata/cell03_partial_v1.json`.

The separate `t4_flash_metadata_r2.py` wrapper converts nonfinite metadata to
JSON null, retaining every image/time/schema check. Acquisition provenance,
source bytes, cell selection, voltage conventions and later scientific rules
are unchanged. Preserve the initial exception description alongside the stream.
Successful metadata outputs are never overwritten. The scientific calibration
protocol will freeze after all metadata admissions, before any voltage scoring.
