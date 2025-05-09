class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []
    
    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        self.queue.append(value)
    
    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)  # Remove and return the front element
    
    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]
    
    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


if __name__ == '__main__':
    # Create a queue instance
    queue = Queue()

    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Check the front element
    print("Front element:", queue.front())  # Output: 10

    # Dequeue elements
    print("Dequeued element:", queue.dequeue())  # Output: 10
    print("Dequeued element:", queue.dequeue())  # Output: 20

    # Check the size
    print("Queue size:", queue.size())  # Output: 1

    # Check if the queue is empty
    print("Is queue empty?:", queue.is_empty())  # Output: False

    # Dequeue the last element
    print("Dequeued element:", queue.dequeue())  # Output: 30

    # Try dequeuing from an empty queue
    try:
        queue.dequeue()
    except IndexError as e:
        print("Error:", e)  # Output: Error: Dequeue from an empty queue
