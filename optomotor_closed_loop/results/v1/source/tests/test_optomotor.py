from __future__ import annotations

import csv
import inspect
import json
from pathlib import Path
import unittest

import numpy as np

from optomotor.circuit import Circuit, side_of, transmitter_sign
from optomotor.simulation import MotorCalibration, VisualController, run_episode
from optomotor.vision import Arena, CHANNELS, MotionFrontend

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/derived"


class SensorTests(unittest.TestCase):
    def test_uniform_and_constant_images_have_no_motion(self):
        for image in (np.full(256, 0.7), Arena(17).render([0, 0], 0)):
            detector = MotionFrontend()
            for _ in range(50):
                features, visual = detector.update(image, 0.01)
                np.testing.assert_array_equal(features, np.zeros(8))
                self.assertEqual(visual, 0)

    def test_motion_direction_and_mirrored_eye_channels(self):
        detector = MotionFrontend()
        phase = detector.azimuth
        for i in range(150):
            image = 0.5 + 0.3 * np.sin(8 * (phase - 0.3 * i * 0.01))
            features, visual = detector.update(image, 0.01)
        self.assertGreater(visual, 0)
        for prefix in ("T4", "T5"):
            self.assertGreater(features[CHANNELS.index((prefix + "a", "L"))], features[CHANNELS.index((prefix + "b", "L"))])
            self.assertGreater(features[CHANNELS.index((prefix + "b", "R"))], features[CHANNELS.index((prefix + "a", "R"))])

    def test_camera_is_world_anchored_and_periodic(self):
        arena = Arena(13)
        base = arena.render([0.1, -0.2], 0.4)
        np.testing.assert_allclose(base, arena.render([0.1, -0.2], 0.4 + 2 * np.pi), atol=2e-14)
        self.assertGreater(np.max(np.abs(base - arena.render([0.2, -0.2], 0.4))), 0.01)

    def test_invalid_observation_stops(self):
        for frame in (np.zeros(2), np.full(256, np.nan)):
            with self.assertRaises(ValueError):
                MotionFrontend().update(frame, 0.01)


@unittest.skipUnless((DATA / "connectome_provenance.json").exists(), "Official circuit extraction is required")
class CircuitTests(unittest.TestCase):
    def test_direct_edge_sum_matches_one_dynamical_step(self):
        circuit = Circuit(DATA)
        metadata = json.loads((DATA / "selected_neurons.json").read_text())
        all_nodes = {n["bodyId"]: n for group in metadata.values() for n in group}
        boundary = json.loads((DATA / "connectome_provenance.json").read_text())["central_boundary"]
        denominators = {r["bodyId"]: r["total_incoming_synapses"] for r in boundary}
        rate_by_id = {bid: 0.01 * np.sin(i) for i, bid in enumerate(circuit.body_ids)}
        features = np.linspace(0.001, 0.008, 8)
        incoming = dict.fromkeys(circuit.body_ids, 0.0)
        with (DATA / "chemical_edges.csv").open(newline="") as stream:
            for row in csv.DictReader(stream):
                pre, post, n = [int(row[k]) for k in ("body_pre", "body_post", "synapse_count")]
                self.assertGreater(n, 0)
                neuron = all_nodes[pre]
                value = rate_by_id[pre] if pre in rate_by_id else features[CHANNELS.index((neuron["type"], side_of(neuron)))]
                incoming[post] += 0.9 * transmitter_sign(neuron) * n * value / denominators[post]
        initial = np.array([rate_by_id[b] for b in circuit.body_ids])
        expected = initial + 0.05 * (-initial + np.tanh([incoming[b] for b in circuit.body_ids]))
        circuit.rates[:] = initial
        circuit.update(features, 0.001)
        np.testing.assert_allclose(circuit.rates, expected, atol=1e-15, rtol=1e-13)

    def test_silencing_preserves_normalization_and_clamps_rates(self):
        intact, silent = Circuit(DATA), Circuit(DATA, silenced="bips")
        np.testing.assert_array_equal(intact.w, silent.w)
        np.testing.assert_array_equal(intact.b, silent.b)
        for _ in range(20):
            silent.update(np.full(8, 0.1), 0.01)
        self.assertEqual(silent.silence_mask.sum(), 2)
        np.testing.assert_array_equal(silent.rates[silent.silence_mask], np.zeros(2))

    def test_circuit_step_refinement(self):
        coarse, fine = Circuit(DATA), Circuit(DATA)
        feature = np.linspace(0.001, 0.02, 8)
        coarse.update(feature, 0.2, 0.001)
        fine.update(feature, 0.2, 0.0005)
        relative = np.linalg.norm(coarse.rates - fine.rates) / max(np.linalg.norm(fine.rates), 1e-12)
        self.assertLess(relative, 0.005)

    def test_controller_receives_only_images_and_time(self):
        parameters = list(inspect.signature(VisualController.update).parameters)
        self.assertEqual(parameters, ["self", "image", "dt"])
        a = VisualController(DATA, MotorCalibration(100.0, 100.0))
        b = VisualController(DATA, MotorCalibration(100.0, 100.0))
        arena = Arena(9)
        for i in range(30):
            frame = arena.render([i * 0.0001, 0], i * 0.001)
            self.assertEqual(a.update(frame, 0.01), b.update(frame, 0.01))
        # The prior outputs are already fixed before any later frame is supplied.
        a.update(arena.render([0.2, 0.1], 1.0), 0.01)
        b.update(arena.render([-0.2, -0.1], -1.0), 0.01)

    def test_uniform_camera_cannot_trigger_motor(self):
        for mode in ("intact", "bips_silent", "h2_silent", "visual_reference"):
            controller = VisualController(DATA, MotorCalibration(1e8, 1e8), mode)
            for _ in range(25):
                self.assertEqual(controller.update(np.full(256, 0.5), 0.01)[0], 0)

    def test_open_loop_recovers_imposed_motion(self):
        config = json.loads((ROOT / "configs/experiment_v1.json").read_text())
        trace = run_episode(DATA, config, MotorCalibration(0, 0), 99, 0.04, 20, "open_loop")
        on = (trace[:, 0] >= 1) & (trace[:, 0] < 4)
        np.testing.assert_allclose(trace[on, 1], np.deg2rad(20), atol=1e-14)
        np.testing.assert_array_equal(trace[:, 3], np.zeros(len(trace)))
        self.assertAlmostEqual(np.rad2deg(trace[-1, 2]), 60, places=10)


if __name__ == "__main__":
    unittest.main()

