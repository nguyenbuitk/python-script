def spiral_dfs(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0 # start position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited, res = set(), []
    visited.add((row, col))
    res.append(matrix[row][col])
    
    while len(visited) < rows * cols:
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < rows and 0 <= new_col < cols and (new_row,new_col) not in visited:
                visited.add((new_row, new_col))
                res.append(matrix[new_row][new_col])
                new_row, new_col = new_row + dr, new_col + dc

            # chagne direction
            row, col = new_row - dr, new_col - dc
    return res
