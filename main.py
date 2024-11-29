import numpy as np
import pytest

def generate_normal_array(mean, std_dev, shape):
    """
    Generates a numpy array of normally distributed numbers.
    :param mean: Mean of the distribution
    :param std_dev: Standard deviation of the distribution
    :param shape: Shape of the array (tuple)
    :return: Numpy array of normally distributed numbers
    """ 
    return np.random.normal(mean, std_dev, shape)

def solve_linear_system(A, b):
    """
    Solves a system of equations using Cramer's rule.
    :param A: Coefficient matrix (square matrix).
    :param b: Constant terms vector
    :return: List of solutions for the variables
    """
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("The coefficient matrix is singular; system has no unique solution.")
    
    num_vars = A.shape[0]
    solutions = []
    for i in range(num_vars):
        A_i = A.copy()
        A_i[:, i] = b
        solutions.append(np.linalg.det(A_i) / det_A)
    
    return solutions

def test_generate_integers_and_index():
    shape = (4, 4)
    array, even_indexes, odd_indexes = generate_integers_and_index(shape)
    assert array.shape == shape, "Generated array shape mismatch"
    for idx in even_indexes:
        assert array[idx] % 2 == 0, f"Even index {idx} has an odd value"
    for idx in odd_indexes:
        assert array[idx] % 2 != 0, f"Odd index {idx} has an even value"

















def test_should_generate_normal_array():
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
    expected_solution = [2, 3]  # Correct expected solution
    result = solve_linear_system(A, b)
    assert np.allclose(result, expected_solution), f"Expected {expected_solution}, but got {result}"

    # Test for singular matrix
    A_singular = np.array([[1, 2], [2, 4]])
    b_singular = np.array([3, 6])
    with pytest.raises(ValueError):  
        solve_linear_system(A_singular, b_singular)

