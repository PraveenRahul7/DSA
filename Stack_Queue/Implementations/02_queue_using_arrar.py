import threading
from collections import deque
from typing import TypeVar, Generic, Deque

T = TypeVar('T')

""" 
Features:
- Thread-safe implementation using a lock to ensure that multiple threads can safely enqueue and dequeue items.
- O(1) time complexity for min() operation by maintaining a separate queue to track minimum elements.
- Capacity limit to prevent overflow.
- Custom exception for queue underflow.
- Clear method to empty the queue.
- String representation for easy debugging and visualization of the queue contents.
- Generic type support to allow any data type to be used in the queue.

"""

import threading
from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')


class QueueEmptyError(Exception):
    """Raised when queue operations are performed on an empty queue."""
    pass


class ThreadSafeMinQueue(Generic[T]):
    """Thread-safe array-based circular queue with O(1) min() support."""

    def __init__(self, capacity: int = 1000):
        # Explain use of each attribute:
        # _array: List to store the queue elements.
        # _min_list: List to maintain the minimum elements in ascending order.
        # _capacity: Maximum number of elements the queue can hold.
        # _front: Index of the front element in the queue.
        # _rear: Index of the rear element in the queue.
        # _size: Current number of elements in the queue.
        # _lock: Lock to ensure thread safety during enqueue and dequeue operations.
        self._array: List[Optional[T]] = [None] * capacity
        self._min_list: List[T] = []
        self._capacity = capacity
        self._front = 0
        self._rear = -1
        self._size = 0
        self._lock = threading.Lock()

    def enqueue(self, item: T) -> None:
        """ 
        Enqueue operation adds an item to the rear of the queue.
        It checks if the queue is full, raises an OverflowError if it is,
        and then adds the item to the rear, updates the rear index, size, and min_list accordingly.
        
        """
        with self._lock:
            if self._size == self._capacity:
                raise OverflowError("Queue capacity exceeded")

            self._rear = (self._rear + 1) % self._capacity # Circular increment to wrap around 
            self._array[self._rear] = item
            self._size += 1

            # Maintain min_list in ascending order
            while self._min_list and self._min_list[-1] > item:
                self._min_list.pop()
            self._min_list.append(item)

    def dequeue(self) -> T:
        """ 
        Dequeue operation removes an item from the front of the queue.
        It checks if the queue is empty, raises a QueueEmptyError if it is,
        and then retrieves the item from the front, updates the front index, size, and min_list accordingly.

        """
        with self._lock:
            if self.is_empty():
                raise QueueEmptyError("Cannot dequeue from an empty queue")

            item = self._array[self._front]
            self._array[self._front] = None  # Optional: free slot
            self._front = (self._front + 1) % self._capacity
            self._size -= 1

            if item == self._min_list[0]:
                self._min_list.pop(0)

            return item

    def peek(self) -> T:
        with self._lock:
            if self.is_empty():
                raise QueueEmptyError("Cannot peek into an empty queue")
            return self._array[self._front]

    def min(self) -> T:
        with self._lock:
            if self.is_empty():
                raise QueueEmptyError("Queue is empty, no minimum available")
            return self._min_list[0]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def clear(self) -> None:
        with self._lock:
            self._array = [None] * self._capacity
            self._min_list.clear()
            self._front = 0
            self._rear = -1
            self._size = 0

    def __str__(self) -> str:
        with self._lock:
            result = []
            idx = self._front
            for _ in range(self._size):
                result.append(self._array[idx])
                idx = (idx + 1) % self._capacity
            return f"Queue(front -> rear): {result}"


if __name__ == "__main__":
    queue = ThreadSafeMinQueue[int](capacity=5)

    queue.enqueue(4)
    queue.enqueue(2)
    queue.enqueue(5)

    print(queue)         # Queue(front -> rear): [4, 2, 5]
    print(queue.min())   # 2

    queue.dequeue()
    print(queue.min())   # 2

    queue.dequeue()
    print(queue.min())   # 5

    queue.clear()
    print(queue.is_empty())  # True
