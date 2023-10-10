"""Utils for min-max normalization."""
import numpy as np


def min_max_normalize(array):
    """Min-max normalize array."""
    return (array - np.min(array)) / (np.max(array) - np.min(array))


def min_max_denormalize(array, min_value, max_value):
    """Min-max denormalize array."""
    return array * (max_value - min_value) + min_value


def min_max_normalize_2d(array):
    """Min-max normalize 2d array."""
    return np.array([min_max_normalize(array[:, i]) for i in range(array.shape[1])]).T


def min_max_denormalize_2d(array, min_values, max_values):
    """Min-max denormalize 2d array."""
    return np.array([min_max_denormalize(array[:, i], min_values[i], max_values[i]) for i in range(array.shape[1])]).T
