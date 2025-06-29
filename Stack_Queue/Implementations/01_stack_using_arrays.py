import threading
from typing import Generic, TypeVar, List

T = TypeVar('T')

""" 
Features: 
- Thread-safe implementation using a lock to ensure that multiple threads can safely push and pop items.
- O(1) time complexity for min() operation by maintaining a separate stack to track minimum
elements.
- Capacity limit to prevent overflow.
- Custom exception for stack underflow.
- Clear method to empty the stack.
- String representation for easy debugging and visualization of the stack contents.
- Generic type support to allow any data type to be used in the stack.

"""

class StackEmptyError(Exception):
    """Exception raised when stack is empty."""
    pass


class ThreadSafeMinStack(Generic[T]):
    """Thread-safe stack with O(1) min() support."""

    def __init__(self, capacity: int = 1000) -> None:
        self._items: List[T] = []
        self._min_stack: List[T] = [] # Stack to keep track of minimum elements in O(1) time
        self._capacity = capacity
        self._lock = threading.Lock()

    def push(self, item: T) -> None:
        with self._lock:
            if len(self._items) >= self._capacity:
                raise OverflowError("Stack capacity exceeded")

            self._items.append(item)

            # Maintain min stack
            if not self._min_stack or item <= self._min_stack[-1]:
                self._min_stack.append(item)

    def pop(self) -> T:
        with self._lock:
            if self.is_empty():
                raise StackEmptyError("Cannot pop from empty stack")

            item = self._items.pop()
            if item == self._min_stack[-1]:
                self._min_stack.pop()
            return item

    def peek(self) -> T:
        with self._lock:
            if self.is_empty():
                raise StackEmptyError("Cannot peek from empty stack")
            return self._items[-1]

    def min(self) -> T:
        """Return the current minimum element in O(1) time."""
        with self._lock:
            if not self._min_stack:
                raise StackEmptyError("Cannot get min from empty stack")
            return self._min_stack[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        with self._lock:
            self._items.clear()
            self._min_stack.clear()

    def __str__(self) -> str:
        return f"Stack(top -> bottom): {list(reversed(self._items))}"



if __name__ == "__main__":
    stack = ThreadSafeMinStack[int]()

    stack.push(5)
    stack.push(3)
    stack.push(7)
    print(stack.min())  # 3

    stack.pop()
    print(stack.min())  # 3

    stack.pop()
    print(stack.min())  # 5

