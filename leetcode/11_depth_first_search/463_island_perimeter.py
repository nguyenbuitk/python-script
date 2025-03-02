from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    res = []
    def dfs(grid, i, j):
        print("dfs ", i, j)
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
            return
        
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        print("visited: ", visited)
        visited.add((i,j))
        grid[i][j] = "#"
        dup = 0
        for di, dj in direction:
            ni, nj = i +di, j + dj
            if 0 <= ni < rows and 0 <= j < cols and (ni, nj) in visited:
                dup += 1
        
        if dup == 0:
            res.append(4)
        elif dup == 1:
            res.append(2)
        elif dup == 2:
            res.append(0)
        elif dup == 3:
            res.append(-2)
        elif dup == 4:
            res.append(-4)
        
        for di, dj in direction:
            ni, nj = i +di, j + dj
            dfs(grid, ni, nj)
        
    found = False
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dfs(i, j)
                break
        else:
            continue
        break
                
    return sum(res)
        
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))