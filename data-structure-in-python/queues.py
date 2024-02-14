# Queues:
# Queues are a type of data structure that operates on a first-in, first-out (FIFO) basis.
# It is a linear data structure.
# It is used to represent different data types:
# 1. Print Queue: Queues are used to manage print jobs in operating systems.
# 2. Task Scheduling: Queues are used to manage tasks in operating systems.
# 3. Message Queues: Queues are used to manage messages in networking.
# 4. Breadth-First Search: Queues are used to implement BFS in graph algorithms.


# # Queue Operations:
# ###################
# # 1. Enqueue: It adds an element to the queue.
# # 2. Dequeue: It removes an element from the queue.
# # 3. Front: It returns the front element of the queue.
# # 4. isEmpty: It checks if the queue is empty.

# # Queue Implementation:
# ######################
# # 1. Using List:
queue = []
queue.append(1) # Enqueue
queue.append(2) # Enqueue
queue.append(3) # Enqueue
front = queue[0] # Front
is_empty = not bool(queue) # isEmpty
print(queue.pop(0)) # 1, Dequeue
print(queue.pop(0)) # 2, Dequeue
print(queue.pop(0)) # 3, Dequeue

# # 2. Using collections.deque: deque is preferred over list in the cases where we need quicker append and pop operations
from collections import deque
queue = deque()
queue.append(1) # Enqueue
queue.append(2) # Enqueue
queue.append(3) # Enqueue
front = queue[0] # Front
is_empty = not bool(queue) # isEmpty
print(queue.popleft()) # 1, Dequeue
print(queue.popleft()) # 2, Dequeue
print(queue.popleft()) # 3, Dequeue

# # 3. Using User-Defined Class:
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is Empty"
    def front(self):
        if self.queue:
            return self.queue[0]
        return "Queue is Empty"
    def isEmpty(self):
        return not bool(self.queue)
queue = Queue()
queue.enqueue(1) # Enqueue
queue.enqueue(2) # Enqueue
queue.enqueue(3) # Enqueue
queue.front() # 1
is_empty = queue.isEmpty() # False
print(queue.dequeue()) # 1, Dequeue
print(queue.dequeue()) # 2, Dequeue
print(queue.dequeue()) # 3, Dequeue

# 4. Using Linked List:
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None # Both front and rear are None initially

    def enqueue(self, data: int):
        new_node = Node(data)
        if not self.rear: # If the queue is empty, the new node is both front and rear
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = self.rear.next

    def dequeue(self):
        if not self.front:
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        if not self.front:
            self.rear = None
        return temp.data
    def peek(self):
        if not self.front:
            return "Queue is Empty"
        return self.front.data
    def isEmpty(self):
        return not bool(self.front)

queue = Queue()
queue.enqueue(1) # Enqueue
queue.enqueue(2) # Enqueue
queue.enqueue(3) # Enqueue
queue.peek() # 1
is_empty = queue.isEmpty() # False
print(queue.dequeue()) # 1, Dequeue
print(queue.dequeue()) # 2, Dequeue
print(queue.dequeue()) # 3, Dequeue



