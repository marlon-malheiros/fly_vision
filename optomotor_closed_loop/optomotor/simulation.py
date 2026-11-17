"""Causal virtual-robot loop; controller interface exposes images only."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .circuit import Circuit
from .vision import Arena, MotionFrontend, RandomSquareDisplay


@dataclass(frozen=True)
class MotorCalibration:
    neural_gain: float
    visual_gain: float
    neural_baseline: float = 0.0
    visual_baseline: float = 0.0


class VisualController:
    def __init__(self, data_dir, calibration, mode="intact", pixels=256, circuit_dt=0.001, max_command=np.pi / 2):
        if mode not in ("intact", "bips_silent", "h2_silent", "open_loop", "visual_reference"):
            raise ValueError("Unknown controller mode")
        self.mode = mode
        self.frontend = MotionFrontend(pixels)
        silenced = {"bips_silent": "bips", "h2_silent": "h2"}.get(mode)
        self.circuit = Circuit(data_dir, silenced=silenced)
        self.calibration = calibration
        self.circuit_dt = circuit_dt
        self.max_command = max_command

    def update(self, image, dt):
        features, visual = self.frontend.update(image, dt)
        neural = self.circuit.update(features, dt, self.circuit_dt)
        if self.mode == "open_loop":
            command = 0.0
        elif self.mode == "visual_reference":
            command = -self.calibration.visual_gain * (visual - self.calibration.visual_baseline)
        else:
            command = -self.calibration.neural_gain * (neural - self.calibration.neural_baseline)
        return float(np.clip(command, -self.max_command, self.max_command)), neural, visual


def run_episode(data_dir, config, calibration, seed, speed, disturbance_deg_s, mode, camera_dt=None, circuit_dt=None, calibration_replay=False):
    dt = config["camera_dt_s"] if camera_dt is None else camera_dt
    circuit_dt = config["circuit_dt_s"] if circuit_dt is None else circuit_dt
    n = int(round(config["duration_s"] / dt))
    if not np.isclose(n * dt, config["duration_s"]):
        raise ValueError("Duration must be divisible by camera period")
    stimulus = config.get("stimulus", {})
    arena = RandomSquareDisplay(seed, square_width_deg=stimulus.get("square_width_deg", 5.0),
                                 coverage=stimulus.get("coverage", 0.15)) if stimulus.get("kind") == "random_squares" else Arena(seed)
    controller = VisualController(data_dir, calibration, mode, circuit_dt=circuit_dt,
                                  max_command=np.deg2rad(config["max_command_deg_s"]))
    position, heading, motor = np.zeros(2), 0.0, 0.0
    rows = []
    for step in range(n):
        t = step * dt
        image = arena.render(position, heading)
        command, neural, visual = controller.update(image, dt)
        disturbance = np.deg2rad(disturbance_deg_s) if config["disturbance_on_s"] <= t < config["disturbance_off_s"] else 0.0
        # Exact zero-order-hold motor response and integrated angle over this frame.
        decay = np.exp(-dt / config["motor_tau_s"])
        integrated_motor = command * dt + (motor - command) * config["motor_tau_s"] * (1 - decay)
        motor_end = command + (motor - command) * decay
        yaw_increment = integrated_motor + disturbance * dt
        omega = yaw_increment / dt
        # Midpoint kinematics; renderer sees the resulting pose on the next update.
        position += speed * dt * np.array([np.cos(heading + yaw_increment / 2), np.sin(heading + yaw_increment / 2)])
        heading += yaw_increment
        motor = motor_end
        rows.append((t, omega, heading, command, neural, visual, position[0], position[1], disturbance))
    trace = np.array(rows)
    if not np.isfinite(trace).all():
        raise FloatingPointError("Nonfinite closed-loop trajectory")
    return trace


TRACE_COLUMNS = ("time_s", "yaw_rad_s", "heading_rad", "command_rad_s", "descending_signal", "visual_signal", "x_m", "y_m", "disturbance_rad_s")


def metrics(trace, config):
    t = trace[:, 0]
    active = (t >= config["disturbance_on_s"]) & (t < config["disturbance_off_s"])
    steady = active & (t >= config["disturbance_on_s"] + 0.5)
    pre = t < config["disturbance_on_s"]
    return {
        "rms_yaw_deg_s": float(np.rad2deg(np.sqrt(np.mean(trace[active, 1] ** 2)))),
        "steady_rms_yaw_deg_s": float(np.rad2deg(np.sqrt(np.mean(trace[steady, 1] ** 2)))),
        "pre_disturbance_rms_deg_s": float(np.rad2deg(np.sqrt(np.mean(trace[pre, 1] ** 2)))),
        "final_heading_deg": float(np.rad2deg(trace[-1, 2])),
        "peak_command_deg_s": float(np.rad2deg(np.max(np.abs(trace[:, 3])))),
        "finite": True,
    }
