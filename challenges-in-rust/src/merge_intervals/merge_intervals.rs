// Solving the "Merge Intervals" Challenge
// Problem Statement
// Given an array of intervals where intervals[i] = [start_i, end_i], 
// merge all overlapping intervals and return an array of the non-overlapping intervals 
// that cover all the intervals in the input.

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]

// Implementation:
// Time Complexity: O(n log n) 
// Space Complexity: O(n) 
pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    // Check if the intervals are empty
    if intervals.is_empty() {
        return intervals;
    }
    // Sort the intervals by the start time
    intervals.sort_by(|a, b| a[0].cmp(&b[0]));
    let mut result: Vec<Vec<i32>> = Vec::new();
    let mut current_interval = intervals[0].clone(); // Clone the first interval
    for interval in intervals {
        if interval[0] <= current_interval[1] { // Check if the interval overlaps
            current_interval[1] = current_interval[1].max(interval[1]); // Merge the interval
        } else {
            result.push(current_interval.clone());
            current_interval = interval;
        }
    }
    result.push(current_interval);
    result
}

// Test Cases:
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_merge_no_overlap() {
        let intervals = vec![vec![1, 3], vec![4, 6], vec![8, 10]];
        let expected = vec![vec![1, 3], vec![4, 6], vec![8, 10]];
        assert_eq!(merge(intervals), expected);
    }

    #[test]
    fn test_merge_with_overlap() {
        let intervals = vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]];
        let expected = vec![vec![1, 6], vec![8, 10], vec![15, 18]];
        assert_eq!(merge(intervals), expected);
    }

    #[test]
    fn test_merge_subinterval() {
        let intervals = vec![vec![1, 4], vec![2, 3]];
        let expected = vec![vec![1, 4]];
        assert_eq!(merge(intervals), expected);
    }

    #[test]
    fn test_merge_single_interval() {
        let intervals = vec![vec![5, 7]];
        let expected = vec![vec![5, 7]];
        assert_eq!(merge(intervals), expected);
    }

    #[test]
    fn test_merge_empty() {
        let intervals: Vec<Vec<i32>> = Vec::new();
        let expected: Vec<Vec<i32>> = Vec::new();
        assert_eq!(merge(intervals), expected);
    }
}