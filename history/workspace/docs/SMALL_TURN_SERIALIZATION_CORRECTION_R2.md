# Small-turn JSON export correction R2

1 November 2026. Preserve the original executable freeze and all produced values.
The existing-reader calibration finished neural predictions and saved its full NPZ
and score JSON, then failed while exporting the summary: Python sum over NumPy
boolean comparisons produced numpy.int64, which the default JSON encoder rejects.
The exact traceback and partial summary remain archived. This is an export failure,
not a failed neuronal simulation or a reason to relax an acceptance rule.

The separate R2 runner converts NumPy scalar values to their exact native Python
equivalents when encoding JSON. It leaves all model, fit, feature, prediction,
cutoff and counting code unchanged. Recover the existing summary from saved scores
using the original frozen counting function; no neural inference or fit is rerun.
Use the same serializer for later stages. Archive/hash this runner before the
recovered export. Existing sources, outputs and pre-calibration cutoff amendment
remain unchanged.
