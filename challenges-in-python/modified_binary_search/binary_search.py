# Solving the "Binary Search" Challenge
# Challenge Description:
# Implement the binary search algorithm to find the position of a target value within a sorted array. 
# If the target is not found, return -1.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test Cases
def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([2], 2) == 0

test_binary_search()