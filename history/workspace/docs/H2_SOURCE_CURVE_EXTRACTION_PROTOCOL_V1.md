# H2 source-only spike-curve extraction V1

25 October 2026. Freeze before reading spike-rate endpoints. Execute only after
the all-row metadata join and independent review pass. This is a reproduction
of the supplied author's analysis, not a neural prediction or fresh validation.

For every condition and repeat retain the frame event immediately after the
last `fullFN`; decode its MATLAB 1-based raw-data row into that repeat's own
clock. Reproduce the author exactly: protocol response end is the mean stop
time from the **first repeat of each condition**, response starts at 1 ms;
baseline is −750 to −50 ms. In aligned time select the first sample strictly
greater than each boundary and include both indexed endpoints. Raster count
is divided by specified window duration, reproducing the author's inclusive
sample convention rather than silently correcting it. Protocol baseline pools
all condition/repeat columns, weighted by their trial counts. Retain negative
baseline-subtracted rates and all repeats, indices, frame events and counts.

Retain all 16 directions, both polarities and all positions, including source
curves absent from the published summary sheet. Key the sheet by cell,
**original** protocol number, polarity and both display coordinates; require
unique complete matches for all summary rows. Absence is an explicit flag,
not an extraction exclusion. Inventory any speed differences and do not
silently replace recorded speeds with the paper's typical value.

Compute source-only vector DSI from the author's direction-wise minimum shift
and theta=−2*pi*relOrt/8. Retain the unshifted signed curve. Use atan2 for the
vector phase (author plot uses atan(imag/real), which is quadrant ambiguous);
label this as an explicit derived descriptive statistic, not an exact replica
of the author's phase marker or independently validated body direction.
No agreement tolerance with the older summary is invented after inspection.
Any differences must be reported, not fitted away.

Independent review checks every spike count with sparse nonzero event indices,
all baseline/response sample boundaries, all stop events and derived curves.
Do not fit a model, infer side conventions from responses, estimate walking
thresholds, or claim biological validation from this source extraction.
