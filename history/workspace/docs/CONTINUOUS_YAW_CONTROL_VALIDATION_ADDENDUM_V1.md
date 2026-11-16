# Preserved-weight control: supplementary solver check

24 October 2026. Added before any new probe/normalization outcomes were inspected.
This supplements numerical validation; it changes no original primary input,
metric, frozen gate, neural parameter, source drive or classification criterion.

Preparation established that the restored-weight graph's largest incoming
absolute weight sum is 1.46875. Therefore the previous simple contraction bound
for normalized graphs cannot be assumed to qualify this counterfactual. The
main protocol's original-graph temporal checks do not themselves test that new
matrix. An independent Python replay at the same timestep checks implementation
agreement, but alone does not establish timestep insensitivity.

For the already fixed probes c=0.05, dc=0, d=±0.001, replay all six circuit
copies at 0.5-ms RK4 using exactly their existing 10-ms source inputs. This adds
12 numerical-control trajectories and no new input condition or resolution.
Retain arrays/final states and compare the primary-window left/right class
means with their original 1-ms results using the same 5% tolerance and 1e-5
floor. Compare differential-input gains using the same 5% tolerance and 1e-6
floor, with actual float32 input denominators. Include added families where
present; inactive/zero outputs retain their raw errors.

Report this separate supplementary gate whether it passes or fails. It does
not replace the original fixed three-case temporal gate or qualify all possible
counterfactual inputs. Stop at the two stated solver resolutions. The signed
tanh system remains a computational counterfactual rather than a physiological
reconstruction. This test is motivated by the changed weight bound, not by
selecting outcomes favorable to yaw detection.
