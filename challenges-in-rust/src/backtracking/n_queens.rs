// Solving the "N-Queens" Challenge
// Problem Statement
// The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
// such that no two queens attack each other. 
// Given an integer n, return all distinct solutions to the n-queens puzzle.

// Big O:
// Time complexity: O(n!) | Space complexity: O(n^2)
pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
    let mut board = vec![vec!['.'; n as usize]; n as usize];
    let mut solutions = Vec::new();
    solve(&mut board, 0, &mut solutions);
    solutions
}

// Check if a queen can be placed on board[row][col]
// This function is called when "col" queens are already placed in columns from 0 to col -1.
// So we need to check only left side for attacking queens
fn solve(board: &mut Vec<Vec<char>>, col: usize, solutions: &mut Vec<Vec<String>>) {
    if col == board.len() { 
        solutions.push(board.iter().map(|row| row.iter().collect()).collect());
        return;
    }
    for row in 0..board.len() {
        if is_safe(board, row, col) {
            board[row][col] = 'Q';
            solve(board, col + 1, solutions);
            board[row][col] = '.';
        }
    }
}

fn is_safe(board: &Vec<Vec<char>>, row: usize, col: usize) -> bool {
    for i in 0..col {
        for j in 0..board.len() {
            if board[j][i] == 'Q' && (row == j || row as i32 - col as i32 == j as i32 - i as i32 || row as i32 + col as i32 == j as i32 + i as i32) {
                return false;
            }
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_4_queens() {
        let solutions = solve_n_queens(4);
        assert_eq!(solutions.len(), 2); // There are 2 distinct solutions for 4-queens puzzle
    }

    #[test]
    fn test_1_queens() {
        let solutions = solve_n_queens(1);
        assert_eq!(solutions.len(), 1); // There is 1 distinct solution for 1-queens puzzle
    }
}