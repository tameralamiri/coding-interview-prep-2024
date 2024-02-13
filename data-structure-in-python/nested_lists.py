# Nested lists
# They are used to represent different data types:
# Graphs: Nested lists are used to represent graphs as a collection of edges and vertices
# Trees: Nested lists are used to represent trees as a collection of nodes
# Matrices: Nested lists are used to represent matrices as a collection of rows and columns

# Defining Nested Arrays:
###################
nested_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3x3 matrix , 2D array
three_d_array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] # 2x2x2 matrix, 3D array

# Accessing Elements:
####################
# 1. Using Indexing:
print(nested_array[0][0]) # 1
print(three_d_array[1][1][1]) # 8

# Arrays Operations:
# They are the same as the operations on 1D arrays, referenced in lists.py.
####################

# Traversing Nested Arrays:
# This is an interesting topic and common in programming interviews.
###########################
# 1. Using for loop:
# 2D Array
for row in nested_array:
    for element in row:
        print(element, end=" ") # 1 2 3 4 5 6 7 8 9
    print() # New line

# 3D Array
for matrix in three_d_array:
    for row in matrix:
        for element in row:
            print(element, end=" ") # 1 2 3 4 5 6 7 8
        print() # New line

# 2. Using List Comprehension:
# 2D Array
elements = [element for row in nested_array for element in row] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(elements)

# 3D Array
elements = [element for matrix in three_d_array for row in matrix for element in row] # [1, 2, 3, 4, 5, 6, 7, 8]
print(elements)

## Famous Traversals:
# 1. Row-wise Traversal
nested_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in nested_array:
    for item in row:
        print(item, end=" ")
    print() # New line

# 2. Column-wise Traversal
for i in range(len(nested_array[0])): # Assuming all rows have the same columns length
    for j in range(len(nested_array)):
        print(nested_array[j][i], end=" ") 
    print() # New line
# 3. Diagonal Traversal
for i in range(len(nested_array)): # Assuming it's a square matrix
    print(nested_array[i][i], end=" ") # 1 5 9

# Anti-Diagonal Traversal
n = len(nested_array)
for i in range(n): # Assuming it's a square matrix
    print(nested_array[i][n - 1 - i], end=" ") # 3 5 7
# 4. Zig-Zag Traversal
print("Zig-Zag Traversal")
def zig_zag_traveral(matrix: list[list[int]]) -> list[int]:
    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(zig_zag_traveral(matrix)) # [1, 2, 3, 6, 5, 4, 7, 8, 9]

# 5. Zig-Zag Vertical Traversal
print("Zig-Zag Vertical Traversal")
for i in range(len(nested_array[0])):
    if i % 2 == 0:
        for j in range(len(nested_array)):
            print(nested_array[j][i], end=" ")
    else:
        for j in range(len(nested_array) - 1, -1, -1):
            print(nested_array[j][i], end=" ")
    print() # New line

# 6. Spiral Traversal
print("Spiral Traversal")
def spirtal_traversal(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        result += matrix.pop(0) # Top Row
        if matrix and matrix[0]:
            for row in matrix: # Right Column
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1] # Bottom Row in reverse
        if matrix and matrix[0]: # Left Column
            for row in matrix:
                result.append(row.pop(0)) 
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spirtal_traversal(matrix)) # [1, 2, 3, 6, 9, 8, 7, 4, 5]


# 7. Boundary Traversal
print("Boundary Traversal")
def boundary_traversal(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    result = []
    rows, cols = len(matrix), len(matrix[0])
    # Top Row
    result.extend(matrix[0])
    # Right Column
    for i in range(1, rows - 1):
        result.append(matrix[i][cols - 1])
    # Bottom Row
    if rows > 1:
        result.extend(matrix[rows - 1][::-1])
    # Left Column
    for i in range(rows - 2, 0, -1):
        result.append(matrix[i][0])
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(boundary_traversal(matrix)) # [1, 2, 3, 6, 9, 8, 7, 4]

# 8. Transpose of a Matrix
print("Transpose of a Matrix")
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    # Using zip() and map() functions to transpose the matrix, *matrix is used to unpack the matrix, 
    # and zip() function is used to group the elements of the same index, 
    # and map() function is used to convert the tuples to lists.
    return list(map(list, zip(*matrix))) 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix)) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 10. Rotate a Matrix
print("Rotate a Matrix")
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    return list(map(list, zip(*matrix[::-1]))) # Rotate 90 degrees, clockwise, 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix)) # [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

# 11. Flatten a Matrix
print("Flatten a Matrix")
def flatten(matrix: list[list[int]]) -> list[int]:
    return [element for row in matrix for element in row]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(matrix)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 12. Unflatten a Matrix
print("Unflatten a Matrix")
def unflatten(matrix: list[int], rows: int, cols: int) -> list[list[int]]:
    return [matrix[i * cols:(i + 1) * cols] for i in range(rows)] # Using list comprehension, 
matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows, cols = 3, 3
print(unflatten(matrix, rows, cols)) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 13. "S" Shape Traversal
print("S Shape Traversal")
def s_shape_traversal(matrix: list[list[int]]) -> list[int]:
    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s_shape_traversal(matrix)) # [1, 2, 3, 6, 5, 4, 7, 8, 9]

# 14. Checkerboard Traversal
print("Checkerboard Traversal")
def checkerboard_traversal(matrix: list[list[int]]) -> list[int]:
    result = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if (i + j) % 2 == 0: # check for black cells in the checkerboard
                result.append(element)
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(checkerboard_traversal(matrix)) # [1, 3, 5, 7, 9]

# 15. Random Traversal
print("Random Walk Traversal")
import random
def random_walk_traversal(matrix: list[list[int]]) -> list[int]:
    visited = set()
    result = []
    rows, cols = len(matrix), len(matrix[0])
    current = (0, 0) # starting point
    while len(visited) < rows * cols:
        result.append(matrix[current[0]][current[1]])
        visited.add(current)
        # Generate a list of all possible next moves
        next_moves = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]
        # Filter invalid next moves
        next_moves = [move for move in next_moves if 0 <= move[0] < rows and 0 <= move[1] < cols and move not in visited]
        # Choose a random next move
        if next_moves:
            current = random.choice(next_moves)
        else:
            break
    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(random_walk_traversal(matrix)) # random output
