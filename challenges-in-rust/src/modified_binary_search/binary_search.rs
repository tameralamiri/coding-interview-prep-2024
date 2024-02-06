// Solving the "Binary Search" Challenge
// Problem Statement
// Given a sorted array of integers nums and an integer target, 
// write a function to search target in nums. If target exists, 
// then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.
pub fn binary_search(nums: Vec<i32>, target: i32) -> i32 {
    let mut left = 0;
    let mut right = nums.len() - 1;

    while left <= right {
        let mid = left + (right - left) / 2;
        if nums[mid] == target {
            return mid.try_into().unwrap(); // return the index of the target as i32 instead of usize
        } else if nums[mid] < target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    -1 // return -1 if target is not found
}


// Test Cases
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_binary_search() {
        assert_eq!(binary_search(vec![-1, 0, 3, 5, 9, 12], 9), 4);
        assert_eq!(binary_search(vec![-1, 0, 3, 5, 9, 12], 2), -1);
    }
}