# Solving the "Kth Largest Element in a Stream" Challenge
# Challenge Description:
# Design a class to efficiently find the kth largest element in a stream of numbers. 

# The class should have:
# A constructor which accepts an integer k and an array of integers nums, which might not be sorted.
# A method add(val) which adds an element val to the stream and returns the element representing the kth largest element in the stream.
# Approach:
# Use a min-heap to keep track of the top k largest elements. The kth largest element will always be at the root of the min-heap.

# Big O:
# Time Complexity: O(nlogk) | Space Complexity: O(k)

import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # Heapify the initial array, which sorts it in O(n) time complexity
        # Ensure the heap size is no more than k by popping the smallest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)  # Add the new value to the heap
        # If the heap size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  # The root element is the kth largest

# Test Cases
def test_kth_largest():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4  # returns 4
    assert kthLargest.add(5) == 5  # returns 5
    assert kthLargest.add(10) == 5  # returns 5
    assert kthLargest.add(9) == 8  # returns 8
    assert kthLargest.add(4) == 8  # returns 8

test_kth_largest()