// Solving the "Set Matrix Zeros" Challenge
// Problem Statement
// Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

// Implementation
// A straightforward approach involves first identifying the rows and columns that need to be set to zeros, 
// then updating the matrix. However, to achieve better space complexity,
// we use the first row and column of the matrix itself to track this information.

// Big O Analysis:
// Time Complexity: O(m * n) | Space Complexity: O(1), where m and n are the number of rows and columns in the matrix.

pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
    let mut first_column_has_zero = false;
    
    // Use first Row and Column as markers
    for i in 0..matrix.len() {
        if matrix[i][0] == 0 {
            first_column_has_zero = true;
        }
        for j in 1..matrix[0].len() {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Set zeros based on markers
    for i in (0..matrix.len()).rev() { // Reverse to avoid overwriting the markers
        for j in (1..matrix[0].len()).rev() {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0;
            }
        }
        if first_column_has_zero {
            matrix[i][0] = 0;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_set_zeroes() {
        let mut matrix = vec![
            vec![1, 1, 1],
            vec![1, 0, 1],
            vec![1, 1, 1]
        ];

        set_zeroes(&mut matrix);
        assert_eq!(matrix, vec![
            vec![1, 0, 1],
            vec![0, 0, 0],
            vec![1, 0, 1]
        ]);
        

        let mut matrix = vec![
            vec![0,1,2,0],
            vec![3,4,5,2],
            vec![1,3,1,5]
        ];
        set_zeroes(&mut matrix);
        assert_eq!(matrix, vec![
            vec![0,0,0,0],
            vec![0,4,5,0],
            vec![0,3,1,0]
        ]);
    }
}