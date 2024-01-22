# Four Number Sum
# Write a function that takes in a non-empty array of distinct integers
# and an integer representing a target sum.
# The function should find all quadruplets in the array that sum up to the target sum
# and return a two-dimensional array of all these quadruplets in no particular order.

# If no four numbers sum up to the target sum, the function should return an empty array.


# Sample input: [7, 6, 4, -1, 1, 2], 16
# Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
# O(N^2) time | O(N^2) space
def four_number_sums(array, targetSum):
    pair_sums = {}
    quadruplets = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in pair_sums:
                for pair in pair_sums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in pair_sums:
                pair_sums[currentSum] = [[array[k], array[i]]]
            else:
                pair_sums[currentSum].append([array[k], array[i]])
    return quadruplets


array = [7, 6, 4, -1, 1, 2]
target_sum = 16
print(four_number_sums(array, target_sum))
