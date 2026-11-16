# H2 reference resolution addendum V3

25 October 2026. V2 retained the corrected raw-clock treatment, but was
interrupted after a bounded performance probe found repeated HDF5 object-name
searches costly: one local table took 9.55 s, while each repeat clock took
0.005–0.015 s and each raw-repeat name lookup took 1.33–1.39 s. Source objects
are reached through MATLAB references; discovering their string names is not
needed to decode them. Preserve the interrupted V2 log/code and profiling log.

V3 stores HDF5 object addresses instead of asking for reference object names.
Each address is paired with the exact raw-file hash and an explicit route:
cell/protocol/newIndex, then repeat number for raw data/position arrays.
The independent reviewer follows those routes and compares object addresses.
All rows, repeats, clock checks and exact metadata criteria are unchanged.
This changes provenance addressing and runtime, not numerical extraction.

The source-curve procedure is updated before any spike-rate extraction to
follow these explicit routes. Preserve its original frozen version in the
study's source snapshots. Freeze the new route implementation again before
execution. No response values or model outcomes select this change.
