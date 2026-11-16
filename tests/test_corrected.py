import numpy as np
from alignment_assessment.corrected import corrected


def test_numerical_tie_uses_first_alignment_even_if_second_predicts_test_better():
    cal = np.array([[0., 0.], [1e-15, 1e-15]])
    test = np.array([[1., 1.], [0., 0.]])
    result = corrected([[1., 1.]], [[0., 0.]], cal, test, .1)
    assert result['selected_index'][0] == 0
    assert not result['single_pass'][0]


def test_real_calibration_difference_is_not_treated_as_roundoff():
    cal = np.array([[0., 0.], [1., 1.]])
    test = np.zeros((2, 2))
    result = corrected([[1., 1.]], [[0., 0.]], cal, test, .1)
    assert result['selected_index'][0] == 1
