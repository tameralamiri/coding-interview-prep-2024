# Solving the "Subsets" Challenge
# Challenge Description:
# Given an integer array nums, return all possible subsets (the power set). 
# The solution set must not contain duplicate subsets.

# A subset is a set that contains all elements of another set, including the empty set.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# implementing the function using recursive approach
# Big O:
# Time complexity: O(n * 2^n) | Space complexity: O(n * 2^n)
def subsets(nums):
    def backtrack(start, path):
        res.append(path[:]) # Add the subset to the result
        for i in range(start, len(nums)):
            path.append(nums[i]) # Add the number into the subset
            backtrack(i+1, path) # Move to the next number
            path.pop() # Backtrack the subset by removing the number from the subset

    res = []
    backtrack(0, [])
    return res

# implementing the function using iterative approach
# Big O:
# Time complexity: O(n * 2^n) | Space complexity: O(n * 2^n)
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [item + [num] for item in res] # Add the number into the subset
    return res

# Test the function
def test_subsets():
    assert subsets([1,2,3]) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
    assert subsets([0]) == [[]]