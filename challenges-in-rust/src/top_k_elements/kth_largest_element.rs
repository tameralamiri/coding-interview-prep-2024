// Solving the "Kth Largest Element in a Stream" Challenge
// Problem Statement
// Design a class to find the kth largest element in a stream. 
// The class needs to support two operations: 
// adding a number to the stream and finding the kth largest element at any point.

// Implementation Strategy
// Use a min-heap to keep track of the top k largest elements. 
// The heap size is maintained at k, ensuring that the kth largest element can be found at the heap's root.

// The KthLargest struct has two fields: k and min_heap.
// The add method takes a number as an argument and adds it to the min-heap.
// The find_kth_largest method returns the kth largest element from the min-heap.

// Big O Analysis
// time complexity: O(log k) for add and O(1) for find_kth_largest | space complexity: O(k)

use std::collections::BinaryHeap;
use std::cmp::Reverse;

pub struct KthLargest {
    k: i32,
    min_heap: BinaryHeap<Reverse<i32>>,
}

impl KthLargest {
    pub fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut kth_largest = KthLargest {
            k,
            min_heap: BinaryHeap::new(),
        };
        for num in nums {
            kth_largest.add(num);
        }
        kth_largest
    }

    pub fn add(&mut self, val: i32) -> i32 {
        if self.min_heap.len() < self.k as usize {
            self.min_heap.push(Reverse(val));
        } else if self.min_heap.peek().unwrap().0 < val {
            self.min_heap.pop();
            self.min_heap.push(Reverse(val));
        }

        
        self.min_heap.peek().unwrap().0
    }
}


// Testing the function
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_kth_largest() {
        let mut kth_largest: KthLargest = KthLargest::new(3, vec![4, 5, 8, 2]);
        assert_eq!(kth_largest.add(3), 4);
        assert_eq!(kth_largest.add(5), 5);
        assert_eq!(kth_largest.add(10), 5);
        assert_eq!(kth_largest.add(9), 8);
        assert_eq!(kth_largest.add(4), 8);
    }
}