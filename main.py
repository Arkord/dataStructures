# main.py

# Import the Stack class from stack.py
from stack import Stack

# Create a new stack instance
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Get the element at the top of the stack
print("Top element:", stack.top())  # Output: Top element: 30

# Pop an element from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 30

# Check if the stack is empty
print("Is the stack empty?", stack.is_empty())  # Output: Is the stack empty? False

# Get the current size of the stack
print("Stack size:", len(stack))  # Output: Stack size: 2

# Pop all elements
stack.pop()
stack.pop()

# Attempt to pop from an empty stack
stack.pop()  # Output: Stack is empty

# Check the top element of an empty stack
stack.top()  # Output: Stack is empty