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
