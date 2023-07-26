"""Module with heap utils"""
import numpy as np


def heapify(array, n, i):
    """Heapify"""
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
