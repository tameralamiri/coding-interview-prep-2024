// Solving the "Missing Number" Challenge
// Problem Statement
// Given an array nums containing n distinct numbers in the range [0, n], 
// return the only number in the range that is missing from the array.

// Approach 1:
// We will iterate through the array and place the numbers at their correct index.
// After sorting the array, we will iterate through the array and check if the number is at its correct index.
// If the number is not at its correct index, we will return the number.
// If all the numbers are at their correct index, we will return the length of the array.

// Big O:
// Time Complexity: O(n) | Space Complexity: O(1).
pub fn missing_number(nums: Vec<i32>) -> i32 {
    let mut nums = nums;
    let n = nums.len();
    let mut i = 0;
    while i < n {
        let j = nums[i] as usize;
        if j < n && nums[i] != nums[j] {
            nums.swap(i, j);
        } else {
            i += 1;
        }
    }
    for i in 0..n {
        if nums[i] != i as i32 {
            return i as i32;
        }
    }
    n as i32
}

// Approach 2:
// The problem can also be solved using the sum of the first n natural numbers.
// We will calculate the sum of the first n natural numbers.
// We will iterate through the array and calculate the sum of the given array.
// We will subtract the sum of the given array from the sum of the first n natural numbers.
// The result will be the missing number from the given array.

// Big O:
// Time Complexity: O(n) | Space Complexity: O(1).
pub fn missing_number_2(nums: Vec<i32>) -> i32 {
    let n = nums.len() as i32;
    let mut sum = n * (n + 1) / 2; // sum of the first n natural numbers
    for num in nums {
        sum -= num;
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_missing_number() {
        assert_eq!(missing_number(vec![3, 0, 1]), 2);
        assert_eq!(missing_number(vec![0, 1]), 2);
    }

    #[test]
    fn test_missing_number_2() {
        assert_eq!(missing_number_2(vec![3, 0, 1]), 2);
        assert_eq!(missing_number_2(vec![0, 1]), 2);
    }
}


