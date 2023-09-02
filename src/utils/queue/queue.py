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


class Deque:
    """Deque class."""

    def __init__(self):
        """Initialize deque."""
        self._deque = deque()

    def add_front(self, item):
        """Add item to the front of the deque."""
        self._deque.appendleft(item)

    def add_rear(self, item):
        """Add item to the rear of the deque."""
        self._deque.append(item)

    def remove_front(self):
        """Remove item from the front of the deque."""
        return self._deque.popleft()

    def remove_rear(self):
        """Remove item from the rear of the deque."""
        return self._deque.pop()

    def is_empty(self):
        """Check if deque is empty."""
        return len(self._deque) == 0

    def size(self):
        """Return deque size."""
        return len(self._deque)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.size())

    print()

    priority_queue = PriorityQueue()
    priority_queue.enqueue(1)
    priority_queue.enqueue(2)
    priority_queue.enqueue(3)
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
    print(priority_queue.is_empty())
    print(priority_queue.size())

    print()

    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.is_empty())
    print(deque.size())
