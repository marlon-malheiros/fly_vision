# Sustained original-clock replay — V1

Specified 2026-10-21 before sustained-test outputs. Earlier short replay results
remain preserved: numerical gates pass, typical GPU latencies improve, and some
10-ms deadlines are still missed. This test cannot erase those misses or certify
hard real-time operation.

Use the same original graph, 1-ms neural solver, 5-ms retinal frames and 10-ms
neural updates with the checked portable V3 CPU frontend and shared-memory GPU
backend. No neural/decoder parameters or scientific conditions change. Startup
preparation explicitly processes three synthetic uniform-0.5 frames to load the
kernel graph, then fully resets frontend, neural state, readout and sample clocks
before any replay input. Record its duration separately. Reject preparation
after real input begins unless the caller first explicitly resets. Original
cold-start measurements remain unchanged.

Replay the existing 0.4-s walking retinal clip 1,500 times, with a full model
state/clock reset between clips while retaining allocated buffers and the GPU
graph cache. This gives 600 simulated seconds and 60,000 paired updates. It is an
unpaced repeated-episode software stress test, not a continuous 600-s walking
simulation, scheduled camera acquisition, new environment test or yaw-decoder
validation. The clip begins from the original runtime's zero initial state.

Check every returned population rate and each episode's full final state against
the independently preserved strict CPU replay, with unchanged 1e-10 tolerance.
Record all raw frame/update timings, rates, per-episode errors, initialization,
reset/first-frame costs, wall duration, device/source hashes and host memory.
Write bounded chunks throughout the run so interruption/failure evidence is
retained. Verify startup/reset determinism and rejection of preparation on an
active stream before the stress test.

Keep the 10-ms paired-update budget, report every miss including maxima and
percentiles, and distinguish numerical passage from timing outcomes. Setup,
reset and each clip's initial frame are reported separately from the paired
updates, and included in total wall time. Keep the four scientific workers
running; record this concurrent-load condition. No scheduler, GPU clock, power
mode or system driver is modified. Input capture, camera projection and virtual
rendering are excluded from the timing path and require separate tests.

The goals are sustained numerical reproducibility, stable resource use and an
honest account of throughput/deadline limitations on the available laptop GPU.
No physical-camera calibration, biological validation, deterministic controller
latency or robot motor-control readiness is established by this test.
