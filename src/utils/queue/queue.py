"""Module with queue class."""

from collections import deque


class Queue:
    """Queue class."""

    def __init__(self):
        """Initialize queue."""
        self._queue = deque()

    def enqueue(self, item):
        """Add item to the queue."""
        self._queue.append(item)

    def dequeue(self):
        """Remove item from the queue."""
        return self._queue.popleft()

    def is_empty(self):
        """Check if queue is empty."""
        return len(self._queue) == 0

    def size(self):
        """Return queue size."""
        return len(self._queue)


class PriorityQueue:
    """Priority queue class."""

    def __init__(self):
        """Initialize priority queue."""
        self._queue = []

    def enqueue(self, item):
        """Add item to the priority queue."""
        self._queue.append(item)

    def dequeue(self):
        """Remove item from the priority queue."""
        max_priority = 0
        for i in range(1, len(self._queue)):
            if self._queue[i] > self._queue[max_priority]:
                max_priority = i
        return self._queue.pop(max_priority)

    def is_empty(self):
        """Check if priority queue is empty."""
        return len(self._queue) == 0

    def size(self):
        """Return priority queue size."""
        return len(self._queue)
