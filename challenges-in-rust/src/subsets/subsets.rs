// Solving the "Subsets" Challenge
// Problem Statement
// Given an integer array nums, return all possible subsets (the power set). 
// The solution set must not contain duplicate subsets.

// Big O:
// Time Complexity: O(N * 2^N) | Space Complexity: O(N * 2^N)
pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut result = vec![vec![]]; // initialize the result with an empty vector
    for &num in &nums { // iterate through the input vector
        let mut new_subsets = result.clone(); // clone the result
        for subset in &mut new_subsets { // &mut is used to make the subset mutable so that we can append to it
            subset.push(num); // append the current number to the subset
        }
        result.append(&mut new_subsets); 
    }
    result // return the result
}

// The subsets function takes a vector of integers as input and returns a vector of vectors of integers.
// The result vector is initialized with an empty vector.
// We then iterate through the input vector and clone the result vector.
// We then iterate through the cloned result vector and append the current number to each subset.
// Finally, we append the new subsets to the result vector and return the result.

// Let's test the subsets function with a few test cases:
#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashSet;

    fn as_set(vv: Vec<Vec<i32>>) -> HashSet<Vec<i32>> {
        vv.into_iter().collect()
    }

    #[test]
    fn test_subsets() {
        let input = vec![1, 2, 5];
        let result = subsets(input);
        let expected = vec![
            vec![],
            vec![1],
            vec![2],
            vec![1, 2],
            vec![5],
            vec![1, 5],
            vec![2, 5],
            vec![1, 2, 5],
        ];
        assert_eq!(as_set(result), as_set(expected));
    }

}