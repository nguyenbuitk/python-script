from typing import List

def isLanPerimeter(grid: List[List[int]]):
    rows, cols, perimeter = len(grid), len(grid[0]), 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i + 1 < rows and grid[i+1][j] == 1:
                    perimeter -= 2
                if j + 1 < cols and grid[i][j+1] == 1:
                    perimeter -= 2
    return perimeter