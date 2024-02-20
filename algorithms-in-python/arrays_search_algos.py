# 1. Linear Search: O(n)
def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

# 2. Binary Search: O(log n) - Only for sorted lists - Also know as Divide and Conquer Technique
def binary_search(my_list, target):
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 3. Sliding Window Technique: O(n) - Only for positive numbers
# This technique is used to find a subarray that sums up to a given target.
def sliding_window(my_list, target):
    left = 0
    right = 0
    sum = 0
    while right < len(my_list):
        sum += my_list[right]
        while sum > target:
            sum -= my_list[left]
            left += 1
        if sum == target:
            return True
        right += 1
    return False


# 4. Two Pointer Technique: O(n) - Only for sorted lists
# This technique is used to find a pair in a sorted array that sums up to a given target.
def two_pointer(my_list, target):
    left = 0
    right = len(my_list) - 1
    while left < right:
        sum = my_list[left] + my_list[right]
        if sum == target:
            return True
        
        if sum < target:
            left += 1
        else:
            right -= 1
    return False
