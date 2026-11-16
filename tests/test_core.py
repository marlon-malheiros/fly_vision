import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

from alignment_assessment.core import (
    led_weights, sample_led_images, rectangle_response, assess_known_noise)


def test_led_integral_and_boundary_convention():
    p = np.array([0., .5, 2.2, -1.])
    exact = led_weights(p, 4, 0)
    np.testing.assert_array_equal(exact[1], [.5, .5, 0, 0])
    for sigma in (.5, 1.):
        actual = led_weights(p, 4, sigma)
        for i, center in enumerate(p):
            for j in range(4):
                expected = quad(lambda x: norm.pdf((x-center)/sigma)/sigma, j-.5, j+.5)[0]
                assert abs(actual[i,j]-expected) < 1e-13


def test_separable_sampling_matches_literal_pixel_sum():
    images = np.arange(24).reshape(2,3,4) / 24
    points = np.array([[1.2, 1.1], [-.6, 0.], [2.5, 2.]])
    for sigma in (0, .5, 1.):
        actual = sample_led_images(images, points, sigma)
        wx, wy = led_weights(points[:,0],4,sigma), led_weights(points[:,1],3,sigma)
        expected = np.array([[sum(images[k,y,x]*wx[j,x]*wy[j,y]
                              for x in range(4) for y in range(3))
                              for k in range(2)] for j in range(3)])
        np.testing.assert_allclose(actual, expected, atol=1e-15)


def test_bar_has_no_transverse_information_when_infinite():
    centers = [[0, -2], [0, 2]]
    rect = [[-.5, .5, -100, 100]]
    for kind in ('isotropic','elongated','double_lobe'):
        a = rectangle_response(rect, centers, kind)
        assert abs(a[0,0]-a[1,0]) < 1e-14
    assert abs(rectangle_response([[-100,100,-100,100]], [[0,0]], 'double_lobe')[0,0]-1)<1e-14


def test_correct_alternative_retained_and_unresolved_is_not_support():
    cp = np.zeros((2, 3)); tp = np.array([[0.,0.],[1.,1.]])
    result = assess_known_noise(np.zeros((1,3)), np.zeros((1,2)),cp,tp,.01)
    assert result['set_unresolved'][0] and not result['set_reject'][0]
    assert not result['set_support'][0]
    assert result['compatible'].all()


def test_empty_calibration_set_rejects():
    result = assess_known_noise(np.ones((1,3)), np.zeros((1,2)),np.zeros((2,3)),np.zeros((2,2)),.01)
    assert result['set_reject'][0] and not result['set_support'][0]


def test_independent_test_and_truth_index_are_not_fit():
    cp = np.array([[0.,0.],[1.,1.]])
    tp = np.array([[1.,1.],[0.,0.]])
    a = assess_known_noise([[0.,0.]], [[0.,0.]], cp, tp,.01)
    assert a['selected_index'][0] == 0
    assert not a['single_pass'][0] and a['set_reject'][0]
