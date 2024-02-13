# Stacks:
# Stacks are a type of container that stores elements in a Last-In/First-Out (LIFO) order.
# It is a linear data structure.
# It is used to represent different data types:
# 1. Function Calls: Stacks are used to store the return addresses of function calls.
# 2. Undo Mechanism: Stacks are used to implement undo mechanisms in text editors.
# 3. Expression Evaluation: Stacks are used to convert infix expressions to postfix expressions.
# 4. Backtracking: Stacks are used to implement backtracking in algorithms.

# Stack Operations:
###################
# 1. Push: It adds an element to the stack.
# 2. Pop: It removes an element from the stack.
# 3. Peek or Top: It returns the top element of the stack.
# 4. isEmpty: It checks if the stack is empty.

# Stack Implementation:
######################
# 1. Using List:
stack = []
stack.append(1) # Push
stack.append(2) # Push
stack.append(3) # Push
peek = stack[-1] # Peek
is_empty = not bool(stack) # isEmpty
print(stack.pop()) # 3, Pop
print(stack.pop()) # 2, Pop
print(stack.pop()) # 1, Pop

# 2. Using collections.deque: deque is preferred over list in the cases where we need quicker append and pop operations 
# from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations 
# as compared to list which provides O(n) time complexity.
from collections import deque
stack = deque()
stack.append(1) # Push
stack.append(2) # Push
stack.append(3) # Push
print(stack.pop()) # 3, Pop
print(stack.pop()) # 2, Pop
print(stack.pop()) # 1, Pop

# 3. Using User-Defined Class:
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is Empty"
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is Empty"
    def isEmpty(self):
        return not bool(self.stack)
stack = Stack()
stack.push(1) # Push
stack.push(2) # Push
stack.push(3) # Push
print(stack.pop()) # 3, Pop
print(stack.pop()) # 2, Pop
print(stack.pop()) # 1, Pop
print(stack.isEmpty()) # True
print(stack.peek()) # Stack is Empty
