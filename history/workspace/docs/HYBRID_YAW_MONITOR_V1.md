# Using the hybrid yaw monitor, V1

This external engineering readout combines the frozen MaleCNS DNp15 change
estimate with the frozen image-derived geometric estimate. It leaves the
neural model unchanged. See the [study report](AGREEMENT_YAW_REPORT_V1.md) for
measured performance and limitations; this interface alone is not validation.

Use the existing project Python environment with NumPy. Replay recorded inputs:

```bash
PYTHONPATH=src python scripts/monitor_hybrid_yaw_v1.py \
  --network results/agreement_yaw_v1/held_out/c01_v16.5_y-2_primary/network.npz \
  --reference results/agreement_yaw_v1/held_out/c01_v16.5_y-2_primary/reference.npz \
  --speed 16.5 \
  --output <TEMP>/hybrid_yaw_example_v1.npz
```

The output path must not exist. This command reads only the neural/reference
arrays and the versioned model. It does not read scene identity, imposed yaw,
onset labels, trial summaries or future input values for a current decision.
The constant walking-speed condition is supplied explicitly, as in training.

For an online application:

```python
import json
from male_optic_frontend.hybrid_yaw_monitor_v1 import HybridYawMonitor

with open("configs/agreement_yaw_model_v1.json") as f:
    model = json.load(f)
fit = next(row["fitted"] for row in model["readouts"] if row["speed"] == 11.0)
monitor = HybridYawMonitor(fit, model["confirmation"])

# Call in chronological order at 100 Hz, using current observations only.
result = monitor.push(time_s, left_dnp15_rate, right_dnp15_rate, image_yaw_deg_s)
if result["ready"]:
    decision = result["decision"]
```

Supply the current individual left/right DNp15 model rates and the **unaveraged**
`yaw_deg_s` estimate emitted by the existing `CausalYawDetector` with
`backward_current`. The monitor performs its own 100-ms image averaging and
neural own-history subtraction. Supplying a pre-averaged estimate would change
the tested algorithm. Use `None` while the image estimate is unavailable.

`ready` is false until 30 valid neural samples and the required image history
are available (about 0.3 s). Read it before using `decision`. Ready decisions
are -1 for negative yaw, +1 for positive yaw and 0 for no accepted turn.
`support` is a dimensionless agreement margin, not a yaw velocity. The two
component estimates are retained in `neural_deg_s` and `image_deg_s`.
Callback counts printed by the replay CLI are not counts of independent turns.

The tested conditions use constant 5.5, 11 or 16.5 mm/s walking, calibrated
synthetic binocular inputs and prescribed yaw onset. Variable walking speed,
missing/irregular frames, biological measurements and physical deployment are
not validated here. The class rejects nonuniform timestamps. It contains no
motor controller or closed-loop policy.
