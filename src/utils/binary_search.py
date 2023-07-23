"""Module with binary search algorithm implementation."""
from typing import Optional

import numpy as np


def binary_search(
    array: np.ndarray,
    value: float,
    left: Optional[int] = None,
    right: Optional[int] = None,
) -> int:
    """Find index of the element in the sorted array.

    Args:
        array: sorted array.
        value: value to search.
        left: left bound of the search.
        right: right bound of the search.

    Returns:
        index of the element in the array.

    Raises:
        ValueError: if the value is not in the array.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if right < left:
        raise ValueError(f"Value {value} is not in the array.")

    middle = (left + right) // 2
    if array[middle] == value:
        return middle
    elif array[middle] > value:
        return binary_search(array, value, left, middle - 1)
    else:
        return binary_search(array, value, middle + 1, right)


def binary_search_iterative(
    array: np.ndarray,
    value: float,
    left: Optional[int] = None,
    right: Optional[int] = None,
) -> int:
    """Find index of the element in the sorted array.

    Args:
        array: sorted array.
        value: value to search.
        left: left bound of the search.
        right: right bound of the search.

    Returns:
        index of the element in the array.

    Raises:
        ValueError: if the value is not in the array.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1

    raise ValueError(f"Value {value} is not in the array.")