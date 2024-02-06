# Solving the "Merge Sorted Array" Challenge
# Challenge Description:
# Given two sorted arrays nums1 and nums2, merge nums2 into nums1 in a sorted manner. 
# Assume that nums1 has enough space to hold additional elements from nums2.

# Approach:
# A straightforward approach would involve inserting all elements from nums2 into nums1 and then sorting, 
# but this wouldn't be efficient. A better approach is to fill nums1 from the end, 
# comparing elements from nums1 and nums2 and placing the larger ones first. 
# This way, we avoid overwriting elements in nums1 that haven't been checked yet.

def merge(nums1, m, nums2, n):
    # Set pointers to the end of each array
    p1 = m - 1
    p2 = n - 1
    # Set pointer for the end of the merged array
    p = m + n - 1

    # While there are elements in nums1 and nums2
    while p2 >=0 :
        # If there are elements in nums1 and nums2, compare them
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

# Test cases
def test_merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert nums1 == [1]


test_merge()