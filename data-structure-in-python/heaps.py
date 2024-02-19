# Heaps:
# a binary tree with the following properties:
# 1. It is a complete binary tree.
# 2. The key at the root must be the minimum or maximum key in the tree.

# Min Heap:
# 1. The minimum key is at the root.
# 2. The key of each node is greater than or equal to the key of its parent.
# 3. The left and right subtrees of the root are also min heaps.

# Max Heap:
# 1. The maximum key is at the root.
# 2. The key of each node is less than or equal to the key of its parent.
# 3. The left and right subtrees of the root are also max heaps.

# Heaps are used to implement priority queues, which are used in algorithms such as Dijkstra's algorithm and the heap sort algorithm.

# Python provides the heapq module which implements a min heap.

# Heap Operations:
# 1. Insertion: Insert a new element into the heap.
# 2. Deletion: Remove the minimum or maximum element from the heap.
# 3. Heapify: Convert an array into a heap.
# 4. Extract: Remove the minimum or maximum element from the heap and return it.
# 5. Replace: Remove the minimum or maximum element from the heap and insert a new element.

import heapq

# Creating a min heap:
heap = [1, 4, 2, 7, 9, 3]
heapq.heapify(heap) # Convert a list into a heap
print(heap) # Output: [1, 4, 2, 7, 9, 3]
heapq.heappush(heap, 5)
print(heap) # Output: [1, 4, 2, 5, 9, 3, 7]
smallest = heapq.heappop(heap)
print(smallest) # Output: 1
print(heap) # Output: [2, 4, 3, 5, 9, 7]
largest_number = heapq.nlargest(1, heap)
print(largest_number) # Output: [9]
smallest_number = heapq.nsmallest(1, heap)
print(smallest_number) # Output: [2]
smallest_two_numbers = heapq.nsmallest(2, heap)
print(smallest_two_numbers) # Output: [2, 3]
heapq.heappushpop(heap, 6) # Push the new element and pop the smallest element
print(heap) # Output: [3, 4, 6, 5, 9, 7]


