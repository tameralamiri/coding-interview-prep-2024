# Solving the "Maximize Capital" Challenge
# Challenge Description:
# Given two arrays: Capital and Profits of equal length, and an integer k. 
# Each ith element of Capital denotes the capital you need to start the ith project, 
# and each ith element of Profits denotes the profit you can earn from completing the ith project. 
# Starting with 0 capital, you can only start a project if you have the required capital. 
# Find the maximum capital you can accumulate after finishing at most k projects. 
# You can only work on one project at a time.

# Approach:
# Use a min-heap to keep track of available projects based on capital requirements.
# Use a max-heap to keep track of profitable projects that can be started with the available capital.

import heapq

def find_maximum_capital(capital, profits, k, initial_capital):
    min_capital_heap = [(capital[i], profits[i]) for i in range(len(capital))]
    max_profit_heap = []
    
    # Build the min-heap based on capital requirements
    heapq.heapify(min_capital_heap)

    for _ in range(k):
        #  Move all projects that can be started with the aviailable capital to the max-heap
        while min_capital_heap and min_capital_heap[0][0] <= initial_capital:
            capital, profit = heapq.heappop(min_capital_heap)
            heapq.heappush(max_profit_heap, (-profit, capital)) # Use -profit to make it a max-heap, the negative sign is removed when the profit is popped
        
        # Break if no project can be started
        if not max_profit_heap:
            break
        # Start the most profitable project
        initial_capital += -heapq.heappop(max_profit_heap)[0] # Remove the negative sign to get the profit

    return initial_capital

# Test
def test_find_maximum_capital():
    capital = [0, 1, 2]
    profits = [1, 2, 3]
    k = 2
    initial_capital = 1
    assert find_maximum_capital(capital, profits, k, initial_capital) == 6
    print("All test cases passed")

test_find_maximum_capital()
