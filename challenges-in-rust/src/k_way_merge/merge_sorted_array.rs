// Solving the "Merge Sorted Array" Challenge
// Problem Statement
// Given two sorted arrays nums1 and nums2, 
// merge nums2 into nums1 in-place, maintaining the sorted order. 
// Assume that nums1 has enough space to hold additional elements from nums2.

// Implementation
// This problem can be solved efficiently by using a two-pointer approach starting from the end of both arrays, 
// which aligns with the K-way merge pattern when K=2.

// The merge function takes two mutable references to the input arrays nums1 and nums2,
// and the lengths of the two arrays as arguments.

// Big O Analysis:
// time complexity: O(m + n) | space complexity: O(1)
pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let (mut p1, mut p2, mut p) = (m - 1, n - 1, (m + n - 1) as usize);
    while p2 >= 0 {
        if p1 >= 0 && nums1[p1 as usize] > nums2[p2 as usize] {
            nums1[p] = nums1[p1 as usize];
            p1 -= 1;
        } else {
            nums1[p] = nums2[p2 as usize];
            p2 -= 1;
        }
        if p >= 1 { // to avoid overflow
            p -= 1;
        }
    }
}

// Let's test the merge function with a few test cases:
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_merge() {
        let mut nums1 = vec![1, 2, 3, 0, 0, 0];
        let m = 3;
        let mut nums2 = vec![2, 5, 6];
        let n = 3;
        merge(&mut nums1, m, &mut nums2, n);
        assert_eq!(nums1, vec![1, 2, 2, 3, 5, 6]);

        let mut nums1 = vec![1];
        let m = 1;
        let mut nums2 = vec![];
        let n = 0;
        merge(&mut nums1, m, &mut nums2, n);
        assert_eq!(nums1, vec![1]);
        
        let mut nums1 = vec![0, 0, 0];
        let m = 0;  
        let mut nums2 = vec![1, 2, 3];
        let n = 3;
        merge(&mut nums1, m, &mut nums2, n);
        assert_eq!(nums1, vec![1, 2, 3]);
    }
}