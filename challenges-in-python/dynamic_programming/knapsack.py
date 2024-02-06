# Solving the "0/1 Knapsack" Challenge
# Challenge Description:
# Given two integer arrays vals (representing the values of the items) 
# and weights (representing the weights of the items), 
# along with an integer W representing the maximum weight capacity of the knapsack, 
# determine the maximum value you can achieve by choosing items such that 
# their total weight is less than or equal to W. 
# Each item can only be selected once (0/1 property).

# Approach:
# A dynamic programming solution involves creating a 2D DP table 
# where dp[i][w] represents the maximum value that can be achieved with the first i items 
# and a maximum weight limit of w.

# The base case is when i = 0 or w = 0,
# where the maximum value that can be achieved is 0.

# The recursive case is when the weight of the current item is less than or equal to w.
# In this case, we have two choices:
# 1. We can include the current item in the knapsack,
#    in which case the maximum value that can be achieved is dp[i-1][w-weights[i]] + vals[i].
# 2. We can exclude the current item from the knapsack,
#    in which case the maximum value that can be achieved is dp[i-1][w].

# The maximum value that can be achieved is the maximum of the two choices.

# If the weight of the current item is greater than w,
# we can only exclude the current item from the knapsack,
# in which case the maximum value that can be achieved is dp[i-1][w].

# The final answer is stored in dp[n][W], where n is the number of items.

# Big O:
# Time complexity: O(nW) | Space complexity: O(nW)
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w-weights[i-1]] + values[i-1], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Test cases
def test_knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    assert knapsack(values, weights, W) == 220

test_knapsack()