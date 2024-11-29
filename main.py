import numpy as np

def generate_normal_array(mean, std_dev, shape):
    """
    Generates a numpy array of normally distributed numbers.
    :param mean: Mean of the distribution
    :param std_dev: Standard deviation of the distribution
    :param shape: Shape of the array (tuple)
    :return: Numpy array of normally distributed numbers
    """ 
    return np.random.normal(mean, std_dev, shape)





















def test_generate_normal_array():
    mean = 0
    std_dev = 1
    shape = (3, 3)
    result = generate_normal_array(mean, std_dev, shape)
    assert result.shape == shape, "Array shape mismatch"
    assert np.abs(result.mean() - mean) < 1, "Mean is not within expected range"
    assert np.abs(result.std() - std_dev) < 1, "Standard deviation is not within expected range"

def test_solve_linear_system():
    A = np.array([[2, -1], [1, 1]])
    b = np.array([1, 5])
    expected_solution = [3, 2]  # Known solution for this system
    result = solve_linear_system(A, b)
    assert np.allclose(result, expected_solution), "Solutions do not match expected values"

    A_singular = np.array([[1, 2], [2, 4]])
    b_singular = np.array([3, 6])
    with pytest.raises(ValueError):
        solve_linear_system(A_singular, b_singular)
