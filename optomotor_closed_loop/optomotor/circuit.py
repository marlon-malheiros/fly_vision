"""A neuron-resolved central rate circuit with measured chemical topology.

Only the visual source populations are lumped. Presynaptic signs are explicit
model assumptions based on the release's transmitter predictions. Model
activity represents signed deviations, not measured firing rates.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from .vision import CHANNELS


SIGN = {"acetylcholine": 1.0, "ach": 1.0, "gaba": -1.0, "glutamate": -1.0}


def side_of(neuron):
    instance = neuron.get("instance") or ""
    if instance.endswith("_L"):
        return "L"
    if instance.endswith("_R"):
        return "R"
    side = neuron.get("rootSide") or neuron.get("somaSide")
    if side not in ("L", "R"):
        raise ValueError(f"Unresolved side for body {neuron['bodyId']}")
    return side


def transmitter_sign(neuron):
    prediction = neuron["transmitter_prediction"]
    name = prediction.get("consensus_nt") or prediction.get("celltype_predicted_nt") or prediction.get("predicted_nt")
    name = str(name).lower()
    if name not in SIGN:
        raise ValueError(f"Unmodeled transmitter {name!r}, body {neuron['bodyId']}")
    return SIGN[name]


class Circuit:
    def __init__(self, data_dir, silenced=None, gain=0.9, tau_s=0.02):
        data_dir = Path(data_dir)
        nodes = json.loads((data_dir / "selected_neurons.json").read_text(encoding="utf-8"))
        provenance = json.loads((data_dir / "connectome_provenance.json").read_text(encoding="utf-8"))
        self.neurons = nodes["central"]
        core_index = {n["bodyId"]: i for i, n in enumerate(self.neurons)}
        inputs = {n["bodyId"]: n for n in nodes["inputs"]}
        denominator = {r["bodyId"]: r["total_incoming_synapses"] for r in provenance["central_boundary"]}
        self.w = np.zeros((len(core_index), len(core_index)))
        self.b = np.zeros((len(core_index), len(CHANNELS)))
        with (data_dir / "chemical_edges.csv").open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                pre, post, count = (int(row[k]) for k in ("body_pre", "body_post", "synapse_count"))
                j = core_index[post]
                if count <= 0 or denominator[post] <= 0:
                    raise ValueError("Invalid synaptic count or normalization")
                if pre in core_index:
                    self.w[j, core_index[pre]] += count * transmitter_sign(self.neurons[core_index[pre]]) / denominator[post]
                else:
                    n = inputs[pre]
                    channel = CHANNELS.index((n["type"], side_of(n)))
                    self.b[j, channel] += count * transmitter_sign(n) / denominator[post]
        if not 0 <= gain < 1 or tau_s <= 0:
            raise ValueError("Invalid dynamics")
        self.w *= gain
        self.b *= gain
        if np.max(np.sum(np.abs(self.w), axis=1)) > gain + 1e-12:
            raise ValueError("Recurrent contraction bound failed")
        self.tau_s = tau_s
        self.rates = np.zeros(len(core_index))
        kind = {"bips": "PS321", "h2": "H2"}.get(silenced)
        if silenced is not None and kind is None:
            raise ValueError("Unknown silencing intervention")
        self.silence_mask = np.array([n["type"] == kind for n in self.neurons])
        self.readout_vector = np.array([(1.0 if side_of(n) == "L" else -1.0) if n["type"] == "DNp15" else 0.0 for n in self.neurons])
        if np.sum(np.abs(self.readout_vector)) != 2:
            raise ValueError("Expected exactly two descending output neurons")
        self.body_ids = [n["bodyId"] for n in self.neurons]

    def update(self, features, dt, max_step=0.001):
        features = np.asarray(features, float)
        if features.shape != (len(CHANNELS),) or not np.isfinite(features).all() or dt <= 0 or max_step <= 0:
            raise ValueError("Invalid circuit input or time step")
        steps = max(1, int(np.ceil(dt / min(max_step, self.tau_s))))
        alpha = dt / steps / self.tau_s
        drive = self.b @ features
        for _ in range(steps):
            self.rates += alpha * (-self.rates + np.tanh(self.w @ self.rates + drive))
            self.rates[self.silence_mask] = 0
        return float(self.readout_vector @ self.rates)

    def structural_summary(self):
        return {
            "central_neurons": len(self.neurons), "central_body_ids": self.body_ids,
            "nonzero_recurrent_pairs": int(np.count_nonzero(self.w)),
            "max_absolute_recurrent_row_sum": float(np.abs(self.w).sum(axis=1).max()),
            "readout": "DNp15_L - DNp15_R only", "source_channels": [list(c) for c in CHANNELS],
            "source_drive_mapping": "Equal pooled motion drive within each type/side; no fitted per-neuron retinal map",
            "sign_assumptions": SIGN,
        }
