"""Module with sort utils"""
import time

import numpy as np

from ..heap import Heap, PriorityHeap


def quick_sort(array):
    """Quick sort"""
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(array):
    """Merge sort"""
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def insertion_sort(array):
    """Insertion sort"""
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def selection_sort(array):
    """Selection sort"""
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


def bubble_sort(array):
    """Bubble sort"""
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


def counting_sort(array):
    """Counting sort"""
    max_value = max(array)
    min_value = min(array)
    counting_array = [0] * (max_value - min_value + 1)
    for i in array:
        counting_array[i - min_value] += 1
    array = []
    for i in range(len(counting_array)):
        array += [i + min_value] * counting_array[i]
    return array


def radix_sort(array):
    """Radix sort"""
    max_value = max(array)
    exp = 1
    while max_value / exp > 0:
        counting_sort(array, exp)
        exp *= 10
    return array


def head_sort(array):
    """Heap sort"""
    heap = Heap()
    for i in array:
        heap.insert(i)
    array = []
    while not heap.is_empty():
        array.append(heap.remove())
    return array


def run_sort(array, sort):
    """Run sort"""
    start_time = time.time()
    sort(array)
    return f"{time.time() - start_time:.4f} [s]"


def run_all_sorts(array):
    """Run all sorts"""
    print(f"Quick sort: {run_sort(array, quick_sort)}")
    print(f"Merge sort: {run_sort(array, merge_sort)}")
    print(f"Insertion sort: {run_sort(array, insertion_sort)}")
    print(f"Selection sort: {run_sort(array, selection_sort)}")
    print(f"Bubble sort: {run_sort(array, bubble_sort)}")
    print(f"Counting sort: {run_sort(array, counting_sort)}")
    print(f"Radix sort: {run_sort(array, radix_sort)}")


if __name__ == "__main__":
    array = np.random.randint(0, 10 ** 6, 10 ** 4)
    run_all_sorts(array)
