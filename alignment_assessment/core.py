"""Finite stimulus-alignment sensitivity and known-noise assessment helpers."""
from __future__ import annotations

import numpy as np
from scipy.special import ndtr
from scipy.stats import chi2


def led_weights(coordinates, count, sigma):
    """Integrate square LEDs against a normalized Gaussian, or sample at sigma=0."""
    coordinates = np.asarray(coordinates, float).reshape(-1)
    if sigma < 0 or count < 1 or not np.isfinite(coordinates).all():
        raise ValueError('Invalid sampling specification')
    pixels = np.arange(count)[None, :]
    delta = pixels - coordinates[:, None]
    if sigma:
        return ndtr((delta + .5) / sigma) - ndtr((delta - .5) / sigma)
    return np.where(np.abs(delta) < .5 - 1e-10, 1.,
                    np.where(np.abs(np.abs(delta) - .5) <= 1e-10, .5, 0.))


def sample_led_images(images, points, sigma):
    """Images are contrasts above a zero-contrast background; result [point,image]."""
    images = np.asarray(images, float)
    points = np.asarray(points, float)
    if images.ndim != 3 or points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('Expected images [condition,y,x] and points [point,xy]')
    wx = led_weights(points[:, 0], images.shape[2], sigma)
    wy = led_weights(points[:, 1], images.shape[1], sigma)
    intermediate = np.einsum('cyx,px->cpy', images, wx, optimize=True)
    return np.einsum('cpy,py->pc', intermediate, wy, optimize=True)


def rectangle_response(rectangles, centers, kind, optical_sigma=.5):
    """Integral of a frozen toy RF over each rectangle; [center,condition]."""
    rectangles = np.asarray(rectangles, float)
    centers = np.asarray(centers, float)
    if kind not in ('isotropic', 'elongated', 'double_lobe'):
        raise ValueError(kind)
    sx = np.sqrt(1. + optical_sigma**2)
    sy = np.sqrt((1.6 if kind == 'elongated' else 1.)**2 + optical_sigma**2)
    x = (ndtr((rectangles[None, :, 1] - centers[:, None, 0]) / sx)
         - ndtr((rectangles[None, :, 0] - centers[:, None, 0]) / sx))
    yy = np.zeros_like(x)
    offsets = (-1.5, 1.5) if kind == 'double_lobe' else (0.,)
    for offset in offsets:
        yy += (ndtr((rectangles[None, :, 3] - centers[:, None, 1] - offset) / sy)
               - ndtr((rectangles[None, :, 2] - centers[:, None, 1] - offset) / sy)) / len(offsets)
    return x * yy


def assess_known_noise(calibration, test, cal_predictions, test_predictions,
                       noise_sd, repeats=3, alpha=.025):
    """Return per-trial statistics and single/set decisions without fitting outcomes."""
    calibration, test = np.asarray(calibration), np.asarray(test)
    cp, tp = np.asarray(cal_predictions), np.asarray(test_predictions)
    variance = noise_sd**2 / repeats
    cal_stat = np.sum((calibration[:, None, :] - cp[None, :, :])**2, axis=-1) / variance
    test_stat = np.sum((test[:, None, :] - tp[None, :, :])**2, axis=-1) / variance
    kept = cal_stat <= chi2.ppf(1 - alpha, cp.shape[1])
    passes = test_stat <= chi2.ppf(1 - alpha, tp.shape[1])
    choice = np.argmin(cal_stat, axis=1)
    single_pass = passes[np.arange(len(choice)), choice]
    any_pass = np.any(kept & passes, axis=1)
    any_fail = np.any(kept & ~passes, axis=1)
    return dict(calibration_statistic=cal_stat, test_statistic=test_stat,
                selected_index=choice, compatible=kept, test_passes=passes,
                single_pass=single_pass, set_reject=~any_pass,
                set_support=any_pass & ~any_fail, set_unresolved=any_pass & any_fail)
