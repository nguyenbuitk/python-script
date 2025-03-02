class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    dP = []
    for i in range(m):
      row = []
      for j in range(n):
        row.append(float('inf'))
      dP.append(row)
    dP[0][0] = grid[0][0]
    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          continue
        if i == 0:
          dP[i][j] = grid[i][j] + dP[i][j-1]
        if j == 0:
          dP[i][j] = grid[i][j] + dP[i-1][j]
        else:
          dP[i][j] = grid[i][j] + min(dP[i][j-1], dP[i-1][j])
        print(f"d[{i}][{j}]: ", dP[i][j])
    print("dP", dP)
    return dP[m-1][n-1]

solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
