from typing import List

class Solution:
    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("")
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            for di, dj in [(0,1), (0, -1), (1,0), (-1,0)]:
                dfs(i + di, j + dj)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
                    self.print_matrix(grid)
        return res

solution = Solution()
print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
        