# Three Number Sum
# Write a function that takes in a non-empty array of distinct integers 
# and an integer representing a target sum. 
# The function should find all triplets in the array that sum up to the target sum 
# and return a two-dimensional array of all these triplets. 
# The numbers in each triplet should be ordered in ascending order, 
# and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.

# First Attempt using sorted array and two sum function
# O(N^2) time | O(N) space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets


