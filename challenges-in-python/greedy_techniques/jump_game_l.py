# Solving the "Jump Game I" Challenge
# Challenge Description:
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array. 
# Each element in the array represents your maximum jump length at that position. 
# Determine if you can reach the last index.

# Approach:
# The greedy approach for this problem involves iterating from the start to the end of the array, 
# at each step updating the furthest index that can be reached (furthestReachSoFar). 
# If at any point the furthestReachSoFar becomes less than the current index, 
# it means there is no way to move forward, and the answer is false. Otherwise, 
# continue updating the furthestReachSoFar and check if it reaches or surpasses the last index.

# Time complexity: O(n) | Space complexity: O(1)
def can_jump(nums):
    furthest_reach_so_far = 0
    target = len(nums) - 1
    for i in range(len(nums)):
        if i > furthest_reach_so_far:
            return False
        furthest_reach_so_far = max(furthest_reach_so_far, i + nums[i])
        if furthest_reach_so_far >= target:
            break
    return True


# Testing the solution
def test_can_jump():
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    assert can_jump([0]) == True
    assert can_jump([2, 0]) == True
    assert can_jump([2, 5, 0, 0]) == True
    assert can_jump([2, 0, 0]) == True
    assert can_jump([1, 0, 1, 0]) == False
    print("All test cases passed!")

test_can_jump()