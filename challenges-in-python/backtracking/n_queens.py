# Solving the "N-Queens" Challenge
# Challenge Description:
# The N-Queens puzzle is the problem of placing N chess queens on an N×N chessboard 
# so that no two queens threaten each other. Given an integer N, 
# return all distinct solutions to the N-queens puzzle. 
# Each solution contains a distinct board configuration of the queen's placement, 
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Approach:
# Use backtracking to explore all possible positions for placing queens one row at a time, 
# applying constraints to ensure no two queens can attack each other.

def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(row - i) == abs(col - board[i]): # Check if queens are in the same column or diagonal
                return False
        return True

    def place_queens(board, row):
        if row == n:
            result.append([''.join('Q' if i == col else '.' for i in range(n)) for col in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col # Place queen
                place_queens(board, row + 1) # Explore next row

    result = []
    place_queens([0] * n, 0)
    return result

# Example Usage
def test_solve_n_queens():
    results = solve_n_queens(4)
    expected = [
        [".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]
    ]
    assert len(results) == 2
    assert sorted(results) == sorted(expected)
