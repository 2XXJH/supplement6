import numpy as np

def test_generate_normal_array():
    mean = 0
    std_dev = 1
    shape = (3, 3)
    result = generate_normal_array(mean, std_dev, shape)
    assert result.shape == shape
    assert np.abs(result.mean() - mean) < 1
    assert np.abs(result.std() - std_dev) < 1
