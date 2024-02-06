// Solving the "Jump Game I" Challenge
// Problem Statement
// Given an array of non-negative integers nums, where each element represents your maximum jump length
// at that position, determine if you can reach the last index.

// Example 1:
// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// Big O:
// Time complexity: O(n) | Space complexity: O(1)
pub fn can_jump(nums: Vec<i32>) -> bool {
    let mut max_reach = 0;
    for (i, &num) in nums.iter().enumerate() { 
        if i > max_reach { // if we can't reach the current index
            return false;
        }
        max_reach = max_reach.max(i + num as usize); // update the max_reach 
        if max_reach >= nums.len() - 1 { // if we can reach the last index
            return true;
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_can_jump() {
        assert_eq!(can_jump(vec![2,3,1,1,4]), true);
        assert_eq!(can_jump(vec![2,2,1,1,4]), true);
        assert_eq!(can_jump(vec![3,2,1,0,4]), false);
        assert_eq!(can_jump(vec![0]), true);
    }
}