"""Module with heap utils"""
import numpy as np


class Heap:
    """Heap class"""

    def __init__(self, array: np.ndarray) -> None:
        """Initialize heap

        Args:
            array: array to heapify"""
        self.array = array
        self.heapify()

    def heapify(self, array: np.ndarray, n: int, i: int) -> None:
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
            self.heapify(array, n, largest)

    def heap_sort(self) -> np.ndarray:
        """Heap sort

        Args:
            array: array to sort"""
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.array, n, i)
        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(self.array, i, 0)
        return self.array

    def heap_push(self, value: int) -> None:
        """Push value to heap

        Args:
            array: heap
            value: value to push"""
        self.array.append(value)
        i = len(self.array) - 1
        while i > 0 and self.array[i] > self.array[(i - 1) // 2]:
            self.array[i], self.array[(i - 1) // 2] = (
                self.array[(i - 1) // 2],
                self.array[i],
            )
            i = (i - 1) // 2

    def heap_pop(self) -> int:
        """Pop value from heap

        Args:
            array: heap"""
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        value = self.array.pop()
        self.heapify(self.array, len(self.array), 0)
        return value

    def heap_replace(self, value: int) -> int:
        """Replace value in heap

        Args:
            array: heap
            value: value to replace"""
        self.array[0], value = value, self.array[0]
        self.heapify(self.array, len(self.array), 0)
        return value

    def heap_pushpop(self, value: int) -> int:
        """Push and pop value in heap

        Args:
            array: heap
            value: value to push and pop"""
        if self.array[0] < value:
            self.array[0], value = value, self.array[0]
            self.heapify(self.array, len(self.array), 0)
        return value

    def heap_merge(self, heap: np.ndarray) -> None:
        """Merge heaps

        Args:
            array: heap
            heap: heap to merge"""
        self.array = np.concatenate((self.array, heap))
        self.heapify(self.array, len(self.array), 0)

    def heap_nlargest(self, n: int) -> np.ndarray:
        """Get n largest values from heap

        Args:
            array: heap
            n: number of values"""
        return self.heap_sort()[-n:]

    def heap_nsmallest(self, n: int) -> np.ndarray:
        """Get n smallest values from heap

        Args:
            array: heap
            n: number of values"""
        return self.heap_sort()[:n]

    def heap_max(self) -> int:
        """Get max value from heap

        Args:
            array: heap"""
        return self.array[0]

    def heap_min(self) -> int:
        """Get min value from heap

        Args:
            array: heap"""
        return self.array[-1]
