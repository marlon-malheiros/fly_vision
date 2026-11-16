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


class RandomSquareDisplay:
    """World-fixed random squares on a virtual cylindrical display.

    The robot is inside the cylinder. Rotation and translation change its
    camera projection; squares remain attached to the display surface. The
    selected sizes/contrast are documented engineering settings, not an exact
    reproduction of a particular fly experiment.
    """
    def __init__(self, seed, pixels=256, elevation_pixels=48, square_width_deg=5.0, coverage=0.15):
        from scipy.ndimage import gaussian_filter

        if not 0 < coverage < 0.5 or not 1 <= square_width_deg <= 30:
            raise ValueError("Invalid square display specification")
        rng = np.random.default_rng(seed)
        self.radius = float(rng.uniform(0.9, 1.4))
        self.azimuth = np.linspace(-np.pi, np.pi, pixels, endpoint=False)
        self.elevation = np.linspace(-np.pi / 6, np.pi / 6, elevation_pixels)
        texture_pitch = np.deg2rad(0.5)
        width = 720
        height = int(np.ceil(3.0 / texture_pitch))
        square_side = max(1, int(round(np.deg2rad(square_width_deg) / texture_pitch)))
        count = int(round(coverage * width * height / square_side ** 2))
        texture = np.full((height, width), 0.5)
        for i in range(count):
            x, y = int(rng.integers(width)), int(rng.integers(height - square_side))
            columns = (x + np.arange(square_side)) % width
            texture[y:y + square_side, columns] = 1.0 if i % 2 else 0.0
        self.raw_texture = texture.copy()
        self.texture = gaussian_filter(texture, sigma=1.5, mode=("nearest", "wrap"))
        self.height, self.width = texture.shape
        self.texture_pitch = texture_pitch
        self.specification = {
            "kind": "random_squares_on_cylindrical_display", "azimuth_pixels": pixels,
            "elevation_pixels": elevation_pixels, "elevation_fov_deg": 60.0,
            "square_width_deg_at_display_center": square_width_deg,
            "nominal_area_coverage": coverage, "square_count": count,
            "luminance_levels": [0.0, 0.5, 1.0], "texture_pitch_deg": 0.5,
            "prefilter_sigma_deg": 0.75, "radius_m": self.radius,
            "coherence": 1.0, "lifetime": "World-fixed pattern throughout each episode",
        }

    def render(self, position, heading):
        position = np.asarray(position, float)
        if position.shape != (2,) or np.linalg.norm(position) >= self.radius:
            raise ValueError("Camera is outside the cylindrical display")
        angle = self.azimuth + float(heading)
        direction = np.stack((np.cos(angle), np.sin(angle)), axis=1)
        projection = direction @ position
        distance = -projection + np.sqrt(projection ** 2 + self.radius ** 2 - position @ position)
        point = position + distance[:, None] * direction
        phi = np.arctan2(point[:, 1], point[:, 0])
        x = (phi + np.pi) / (2 * np.pi) * self.width
        z_over_radius = np.tan(self.elevation[:, None]) * distance[None, :] / self.radius
        y = (z_over_radius + 1.5) / self.texture_pitch
        y = np.clip(y, 0, self.height - 1.000001)
        ix = np.floor(x).astype(int) % self.width
        iy = np.floor(y).astype(int)
        fx, fy = x - np.floor(x), y - iy
        ix2, iy2 = (ix + 1) % self.width, iy + 1
        image = ((1 - fy) * ((1 - fx) * self.texture[iy, ix] + fx * self.texture[iy, ix2])
                 + fy * ((1 - fx) * self.texture[iy2, ix] + fx * self.texture[iy2, ix2]))
        # Camera aperture averages neighboring horizontal samples.
        return (np.roll(image, 1, axis=-1) + 2 * image + np.roll(image, -1, axis=-1)) / 4


class MotionFrontend:
    def __init__(self, pixels: int = 256, delay_s: float = 0.03):
        if pixels < 16 or delay_s <= 0:
            raise ValueError("Invalid detector geometry or delay")
        self.azimuth = np.linspace(-np.pi, np.pi, pixels, endpoint=False)
        self.delay_s = delay_s
        self.delayed_on = None
        self.delayed_off = None
        self.previous_on = None
        self.previous_off = None
        self.left = (self.azimuth > np.deg2rad(15)) & (self.azimuth < np.deg2rad(165))
        self.right = (self.azimuth < -np.deg2rad(15)) & (self.azimuth > -np.deg2rad(165))

    def update(self, image, dt):
        image = np.asarray(image, float)
        if image.ndim not in (1, 2) or image.shape[-1] != len(self.azimuth) or not np.isfinite(image).all() or dt <= 0:
            raise ValueError("Invalid camera observation or time step")
        on = np.maximum(image - 0.5, 0)
        off = np.maximum(0.5 - image, 0)
        if self.delayed_on is None:
            self.delayed_on, self.delayed_off = on.copy(), off.copy()
            self.previous_on, self.previous_off = on.copy(), off.copy()
        # R2: integrate the continuous delay filter up to the current frame.
        # Exact solution for linearly interpolated past/current observations;
        # this uses no future frame and avoids V1's extra frame of delay.
        q = dt / self.delay_s
        total = -np.expm1(-q)
        current_weight = 1 - total / q if q > 1e-6 else q / 2 - q * q / 6 + q ** 3 / 24
        previous_weight = total - current_weight
        self.delayed_on += previous_weight * (self.previous_on - self.delayed_on) + current_weight * (on - self.delayed_on)
        self.delayed_off += previous_weight * (self.previous_off - self.delayed_off) + current_weight * (off - self.delayed_off)
        on_motion = np.roll(self.delayed_on, 1, axis=-1) * on - self.delayed_on * np.roll(on, 1, axis=-1)
        off_motion = np.roll(self.delayed_off, 1, axis=-1) * off - self.delayed_off * np.roll(off, 1, axis=-1)
        feature = []
        for kind, side in CHANNELS:
            motion = on_motion if kind.startswith("T4") else off_motion
            # T4a/T5a: front-to-back on each side; T4b/T5b: opposite.
            sign = (1 if side == "L" else -1) * (1 if kind.endswith("a") else -1)
            mask = self.left if side == "L" else self.right
            feature.append(float(np.maximum(sign * motion[..., mask], 0).mean()))
        self.previous_on, self.previous_off = on.copy(), off.copy()
        # Conventional visual controller uses the signed camera-motion signal.
        conventional = float((on_motion[..., self.left | self.right] + off_motion[..., self.left | self.right]).mean())
        return np.array(feature), conventional
