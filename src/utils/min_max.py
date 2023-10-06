"""Utils for min-max normalization."""
import numpy as np


def min_max_normalize(array):
    """Min-max normalize array."""
    return (array - np.min(array)) / (np.max(array) - np.min(array))


def min_max_denormalize(array, min_value, max_value):
    """Min-max denormalize array."""
    return array * (max_value - min_value) + min_value
