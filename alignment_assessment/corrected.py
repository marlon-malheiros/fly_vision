"""Post-outcome R2 amendment; see docs/ALIGNMENT_ASSESSMENT_NUMERICAL_TIES_R2.md."""
import numpy as np

from .core import assess_known_noise


def corrected(*args, **kwargs):
    """Select the first lexicographic alignment within 1e-9 chi-square of best."""
    result = assess_known_noise(*args, **kwargs)
    scores = result["calibration_statistic"]
    eligible = scores <= scores.min(axis=1)[:, None] + 1e-9
    result["selected_index"] = np.argmax(eligible, axis=1)
    result["single_pass"] = result["test_passes"][
        np.arange(len(scores)), result["selected_index"]]
    return result
