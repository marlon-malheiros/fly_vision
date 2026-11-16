# Camera-to-retina implementation contract — V1

Implemented 2026-10-21. This is a portable software adapter with synthetic tests.
No physical camera, lens calibration, board or robot has been validated.

The frozen circuit requires two registered 173×173 retinal luminance grids,
with local axes −86…+86 degrees at 1-degree spacing, sampled every 5 ms. A raw
camera image has different geometry and photometry. The adapter therefore
requires supplied ray-to-pixel maps and photometric response tables, rather
than treating raw pixels as the model's eyes.

## Calibration directory

`calibration.json` identifies schema `stereo_retinal_calibration_v1`, a declared
status (`MEASURED_CALIBRATION` or `SYNTHETIC_TEST_ONLY`), provenance, the SHA-256
of `arrays.npz`, `retinal_axis_deg`, 5,000,000-ns frame period, and explicit
maximum stereo skew and clock jitter in integer nanoseconds. Timing limits must
be below half the period to identify one sample unambiguously. The software
checks the declaration; it cannot certify that measurements were performed.

Each camera (L/R) declares camera ID, monochrome image shape, uint8/uint16 dtype,
fixed exposure in microseconds, analog gain, and the same eye reference/basis as
the model. Record the physical calibration method, sensor/lens identity, mode
and synchronization measurements in provenance. Do not substitute synthetic
coordinates for a measured physical calibration.

`arrays.npz` contains, for each side:

- `L_x_px`, `L_y_px` (or R): the sensor pixel coordinates corresponding to every
  frozen retinal sample, each shape (173,173).
- `L_covered` (or R): a boolean coverage map; every required sample must be covered.
- `L_photometric_lut` (or R): a finite monotone lookup of all 256 or 65,536 raw
  levels into the model's declared linear [0,1] luminance normalization.

Insufficient field of view, out-of-image coordinates or unknown coverage cause
rejection. No guessed field filling, chart mirroring, automatic contrast scaling
or exposure compensation occurs. LUT linearization precedes bilinear spatial
interpolation, because gamma correction and interpolation do not commute.

## Streaming and timing

`StereoRetinalAdapter.prepare` accepts one raw binocular pair, two common-clock
integer exposure-midpoint timestamps, and actual camera acquisition modes.
Exposure/gain/identity must match calibration. The adapter checks stereo skew,
frame order, missing samples, drift and the declared clock-jitter bound before
advancing any state. It maps accepted samples onto the nominal 5-ms model clock
and reports the actual timestamp error separately. That explicit time quantization
is a deployment assumption requiring measured temporal-sensitivity checks; it
does not imply that camera jitter has been validated biologically.

`CameraPerceptionPipeline` projects the pair, advances `HardwareRuntimeV2`, then
commits the sensor clock. Rejected sensor inputs leave the pipeline unadvanced.
A neural runtime failure requires a full reset. State is bounded by one pair,
fixed calibration maps, motion-filter state and the selected graph.

Neural rates are emitted every 10 ms. The optional yaw readout still requires
known model-scale walking speed and the complete original episode window; it is
not an instantaneous steering controller. Real-world metric scale, baseline,
camera mounting and odometry require their own calibration before interpreting
that speed as robot motion. No motor commands or camera drivers are included.

## Verification boundary

Tests check nonlinear photometry/interpolation order, integer timestamp handling,
missing/out-of-order/skewed frames, changed exposure, coverage failure, reset and
an end-to-end comparison with the actual frozen neural runtime. Synthetic tests
do not validate physical optics or the accuracy of a claimed measured ray map.
Hardware readiness requires a target camera/board, measured calibration and a
new timing/visual-input benchmark using its captured frames.
