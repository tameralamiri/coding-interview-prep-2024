# Linked Lists:
##############
# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# It is a collection of nodes, where each node contains data and a reference to the next node in the sequence.
# It is used to represent different data types:
# 1. Dynamic Memory Allocation: Linked lists are used to allocate memory dynamically.
# 2. Implementation of Stacks and Queues: Linked lists are used to implement stacks and queues.
# 3. Separate Chaining: Linked lists are used to implement separate chaining in hash tables.
# 4. Circular Lists: Linked lists are used to implement circular lists.

# Linked List Operations:
#################
# 1. Insertion: O(n)
# 2. Deletion: O(n)
# 3. Traversal: O(n)
# 4. Search: O(n)
# 5. Update: O(n)

# Types of Linked Lists:
########################
# 1. Singly Linked List: each node contains a data and a reference to the next node in the sequence.
# 2. Doubly Linked List: each node contains a data and a reference to the next node and the previous node in the sequence.


# Singly Linked List Implementation:
# #################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion, O(n)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Traversal, O(n)
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # Search, O(n)
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node
        return False
    
    # Deletion, O(n)
    def remove(self, key):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == key:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

    # Update, O(n)
    def update(self, key, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                current_node.data = new_data
                return
            current_node = current_node.next

# Singly Linked List Usage:
###########################
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.display() # 1 2 3
print(sll.search(2)) # True
sll.remove(2)
sll.display() # 1 3
sll.update(3, 4)
sll.display() # 1 4

# Doubly Linked List Implementation:
# #################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion, O(n)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    # Traversal, O(n)
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # Search, O(n)
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node
        return False
    
    # Deletion, O(n)
    def remove(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                return
            current_node = current_node.next

    # Update, O(n)
    def update(self, key, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                current_node.data = new_data
                return
            current_node = current_node.next

# Doubly Linked List Usage:
###########################
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display() # 1 2 3
print(dll.search(2)) # True
dll.remove(2)
dll.display() # 1 3
dll.update(3, 4)
dll.display() # 1 4
