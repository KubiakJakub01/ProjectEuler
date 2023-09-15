"""Utils for priority heap"""
import numpy as np

from src.utils.heap.heap import Heap


class PriorityHeap(Heap):

    def __init__(self, array: np.ndarray) -> None:
        """Initialize heap

        Args:
            array: array to heapify"""
        super().__init__(array)

    def heapify(self, array: np.ndarray, n: int, i: int) -> None:
        """Heapify
        
        Args:
            array: array to heapify
            n: size of heap
            i: index of root"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[i][0] < array[left][0]:
            largest = left
        if right < n and array[largest][0] < array[right][0]:
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
        while i > 0 and self.array[i][0] > self.array[(i - 1) // 2][0]:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2

    def heap_pop(self) -> int:
        """Pop value from heap

        Args:
            array: heap"""
        if len(self.array) == 0:
            return None
        if len(self.array) == 1:
            return self.array.pop()
        root = self.array[0]
        self.array[0] = self.array.pop()
        self.heapify(self.array, len(self.array), 0)
        return root
