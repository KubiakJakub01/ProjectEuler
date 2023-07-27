"""Module with heap utils"""
import numpy as np


def heapify(array: np.ndarray, n: int, i: int) -> None:
    """Heapify
    
    Args:
        array: array to heapify
        n: size of heap
        i: index of root"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array: np.ndarray) -> np.ndarray:
    """Heap sort

    Args:
        array: array to sort"""
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def heap_push(array: np.ndarray, value: int) -> None:
    """Push value to heap

    Args:
        array: heap
        value: value to push"""
    array.append(value)
    i = len(array) - 1
    while i > 0 and array[i] > array[(i - 1) // 2]:
        array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
        i = (i - 1) // 2


def heap_pop(array: np.ndarray) -> int:
    """Pop value from heap

    Args:
        array: heap"""
    array[0], array[-1] = array[-1], array[0]
    value = array.pop()
    heapify(array, len(array), 0)
    return value
