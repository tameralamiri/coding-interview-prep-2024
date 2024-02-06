# Solving the "Missing Number" Challenge
# Challenge Description:
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Approach 1:
# Use the Cyclic Sort pattern to place each number in its correct position, 
# and then iterate through the sorted array to find the missing number.

# Big O:
# O(n) Time | O(1) Space
def find_missing_number_1(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1

    # After sorting, the first index where the number is not equal to the index is the missing number
    for i in range(n):
        if nums[i] != i:
            return i
    return n

# Approach 2:
# Use the XOR operation to find the missing number.

# Big O:
# O(n) Time | O(1) Space
def find_missing_number_2(nums):
    n = len(nums)
    x1, x2 = 0, 0
    for i in range(n):
        x1 ^= i # XOR operation
        x2 ^= nums[i] # XOR operation
    return x1 ^ x2 ^ n # XOR operation

# Approach 3:
# Use the Gauss' Formula to find the missing number.

# Big O:
# O(n) Time | O(1) Space
def find_missing_number_3(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# if the missing numbers range is [n, m], then the expected sum is:
# expected_sum = ((m - n + 1) * (n + m)) // 2


# Test Cases
def test_find_missing_number():
    assert find_missing_number_1([3, 0, 1]) == 2
    assert find_missing_number_2([0, 1]) == 2
    assert find_missing_number_3([9,6,4,2,3,5,7,0,1]) == 8
    assert find_missing_number_3([0]) == 1

test_find_missing_number()