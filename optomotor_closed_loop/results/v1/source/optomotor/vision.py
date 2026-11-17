"""Equatorial camera and a functional ON/OFF correlation motion frontend.

This is a planar virtual-robot sensor, not an anatomically calibrated fly eye.
Positive azimuth is left of the robot's forward x axis. Features depend only
on the image history; there is no true-motion input to the detector.
"""
from __future__ import annotations

import numpy as np


CHANNELS = tuple((kind, side) for kind in ("T4a", "T4b", "T5a", "T5b") for side in ("L", "R"))


class Arena:
    def __init__(self, seed: int, pixels: int = 256):
        rng = np.random.default_rng(seed)
        self.half_size = rng.uniform([0.9, 0.9], [1.4, 1.4])
        self.frequencies = rng.uniform(3.0, 16.0, (4, 6))
        self.phases = rng.uniform(-np.pi, np.pi, (4, 6))
        self.azimuth = np.linspace(-np.pi, np.pi, pixels, endpoint=False)

    def render(self, position, heading):
        position = np.asarray(position, float)
        if position.shape != (2,) or np.any(np.abs(position) >= self.half_size):
            raise ValueError("Camera is outside the arena")
        angle = self.azimuth + float(heading)
        direction = np.stack((np.cos(angle), np.sin(angle)), axis=1)
        safe_direction = np.where(np.abs(direction) < 1e-12, 1e-12, direction)
        distances = (np.sign(safe_direction) * self.half_size - position) / safe_direction
        distance = distances.min(axis=1)
        point = position + distance[:, None] * direction
        vertical = distances[:, 0] <= distances[:, 1]
        wall = np.where(vertical, np.where(direction[:, 0] > 0, 0, 1), np.where(direction[:, 1] > 0, 2, 3))
        coordinate = np.where(vertical, point[:, 1], point[:, 0])
        texture = np.sin(2 * np.pi * coordinate[:, None] * self.frequencies[wall] + self.phases[wall]).mean(axis=1)
        image = 0.5 + 0.45 * texture
        # Declared angular optical smoothing: [1, 2, 1] / 4, periodic panorama.
        return (np.roll(image, 1) + 2 * image + np.roll(image, -1)) / 4


class MotionFrontend:
    def __init__(self, pixels: int = 256, delay_s: float = 0.03):
        if pixels < 16 or delay_s <= 0:
            raise ValueError("Invalid detector geometry or delay")
        self.azimuth = np.linspace(-np.pi, np.pi, pixels, endpoint=False)
        self.delay_s = delay_s
        self.delayed_on = None
        self.delayed_off = None
        self.left = (self.azimuth > np.deg2rad(15)) & (self.azimuth < np.deg2rad(165))
        self.right = (self.azimuth < -np.deg2rad(15)) & (self.azimuth > -np.deg2rad(165))

    def update(self, image, dt):
        image = np.asarray(image, float)
        if image.shape != self.azimuth.shape or not np.isfinite(image).all() or dt <= 0:
            raise ValueError("Invalid camera observation or time step")
        on = np.maximum(image - 0.5, 0)
        off = np.maximum(0.5 - image, 0)
        if self.delayed_on is None:
            self.delayed_on, self.delayed_off = on.copy(), off.copy()
        on_motion = np.roll(self.delayed_on, 1) * on - self.delayed_on * np.roll(on, 1)
        off_motion = np.roll(self.delayed_off, 1) * off - self.delayed_off * np.roll(off, 1)
        feature = []
        for kind, side in CHANNELS:
            motion = on_motion if kind.startswith("T4") else off_motion
            # T4a/T5a: front-to-back on each side; T4b/T5b: opposite.
            sign = (1 if side == "L" else -1) * (1 if kind.endswith("a") else -1)
            mask = self.left if side == "L" else self.right
            feature.append(float(np.maximum(sign * motion[mask], 0).mean()))
        alpha = -np.expm1(-dt / self.delay_s)
        self.delayed_on += alpha * (on - self.delayed_on)
        self.delayed_off += alpha * (off - self.delayed_off)
        # Conventional visual controller uses the signed camera-motion signal.
        conventional = float((on_motion[self.left | self.right] + off_motion[self.left | self.right]).mean())
        return np.array(feature), conventional

