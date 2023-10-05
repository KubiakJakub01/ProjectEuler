"""Utils for min-max normalization."""
import numpy as np


def min_max_normalize(array):
    """Min-max normalize array."""
    return (array - np.min(array)) / (np.max(array) - np.min(array))
