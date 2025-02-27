from typing import List
def initial_matrix():
    # Initialize 2D matrix
    ## Method 1: Using nested list
    matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print(matrix1)

    ## Method 2: Create 2D matrix m x n with default value
    rows, cols = 3, 4
    matrix = [[0] * cols for _ in range(rows)]

    matrix = []
    for _ in range(rows):
        matrix.append([0]*cols)
    print(matrix)

    # Traversal through matrix
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            print(f"matrix[{i}][{j}] = {matrix1[i][j]}")
            
    # Print matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Duyệt ma trận theo hướng


def test():
    rows, cols = 4, 4

    directions = [(-1,0), (1,0), (0, -1), (0, 1)]
    for row in range(rows):
        for col in range(cols):
            print(f"current postition of matrix: matrix[{row}][{col}] = {matrix3[row][col]}")
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    print(f"  -> Có thể đi đến: matrix[{new_row}][{new_col}] = {matrix3[new_row][new_col]}")



# Duyệt ma trận theo DFS
def dfs(matrix, row, col, visited):
    rows, cols = len(matrix), len(matrix[0])
    if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
        return
    
    visited.add((row,col))
    print(f"Visiting: matrix[{row}][{col}] = {matrix[row][col]}")
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        dfs(matrix, row + dr, col + dc, visited)
matrix3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
def spiral_dfs(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    res = []
    visited.add((row, col))
    res.append(matrix[row][col])
    while len(visited) < rows * cols:
        print(visited)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < rows and 0 <= new_col < cols and (new_row,new_col) not in visited:
                visited.add((new_row, new_col))
                res.append(matrix[new_row][new_col])
                print(res)
                new_row, new_col = new_row + dr, new_col + dc
            print('Test')
            row, col = new_row - dr, new_col - dc
    return res

print(spiral_dfs(matrix3))
