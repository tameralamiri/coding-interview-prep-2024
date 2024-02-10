# Solving the "Set Matrix Zeros" Challenge
# Challenge Description:
# Given an m x n matrix, if an element is 0, set its entire row and column to 0. You must do it in-place.

# Approach:
# A straightforward approach might involve using additional matrices, 
# but to do it in-place, we can use the first row and column of the matrix itself 
# to keep track of which rows and columns need to be zeroed.


def set_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # use first row and first column as flags
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0 # set flags

    # zero out cells based on flags
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # zero out first row and column if needed
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix


# Test cases
# Test 1
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# After calling the function
# [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(set_zeros(matrix))

# Test 2
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# After calling the function
# [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
print(set_zeros(matrix))
