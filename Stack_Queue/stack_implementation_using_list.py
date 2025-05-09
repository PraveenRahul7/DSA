

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []
    
    def push(self, value: int):
        """ Add an element to the top of the stack"""
        self.stack.append(value)
    
    def pop(self):
        """Remove and return the top element of the stack"""
        if self.is_empty():
            raise IndexError("Top from an empty Stack")
        return self.stack.pop()
    
    def top(self):
        """Returns the top element of the stack"""
        if self.is_empty():
            raise IndexError("Top from an empty Stack")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        """ Check if the stack is empty."""
        return len(self.stack) == 0
    
    def display(self):
        print("Display Stack: ", end = " >")
        for element in self.stack:
            print(element, end=" ")
        print()


if __name__=='__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print(f"Top element: {stack.top()}")
    stack.display()
    print(f"Pop element: {stack.pop()}")
    stack.display()
    print(f"Top element: {stack.top()}")
    stack.display()
    
