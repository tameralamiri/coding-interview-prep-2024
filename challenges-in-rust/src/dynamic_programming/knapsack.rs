// Solving the "0/1 Knapsack" Challenge
// Problem Statement
// Given two integer arrays vals (representing the values of items) and weights (representing the weights of items), 
// along with an integer W representing the maximum capacity of a knapsack, 
// find the maximum value you can achieve by choosing items such that the total weight does not exceed W. 
// Each item can either be included or excluded (hence 0/1 Knapsack).

// Example
// vals = [60, 100, 120]
// weights = [10, 20, 30]
// W = 50
// Output: 220

// Big O:
// Time cmp: O(n * W) | Space cmp: O(n * W)
pub fn knapsack(vals: Vec<i32>, weights: Vec<i32>, maximum_capacity: i32) -> i32 {
    let n = vals.len();
    // dp[i][w] is the maximum value that can be attained with weight less than or equal to w using the first i items
    // vec![0; (w + 1) as usize]: This part creates a vector of integers initialized with zeros. The size of this vector is w + 1
    // vec![vec![0; (w + 1) as usize]; n + 1]: This part creates a vector of vectors of integers. The size of the outer vector is n + 1. The size of the inner vector is w + 1
    let mut dp = vec![vec![0; maximum_capacity as usize + 1]; n + 1];
    for i in 0..=n {
        for w in 0..=maximum_capacity as usize {
            if i == 0 || w == 0 {
                dp[i][w] = 0;
            } else if weights[i - 1] <= w as i32 {
                dp[i][w] = std::cmp::max(
                    vals[i - 1] + dp[i - 1][w - weights[i - 1] as usize], //
                    dp[i - 1][w],
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    dp[n][maximum_capacity as usize]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_knapsack() {
        assert_eq!(knapsack(vec![60, 100, 120], vec![10, 20, 30], 50), 220);
        assert_eq!(knapsack(vec![60, 100, 120], vec![10, 20, 30], 0), 0);
    }
}
