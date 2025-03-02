class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # Chỉ sử dụng một mảng 1 chiều để lưu trữ trạng thái
        dP = [float('inf')] * n
        
        dP[0] = grid[0][0]  # Khởi tạo giá trị đầu tiên

        for i in range(m):
          for j in range(n):
            if i == 0 and j == 0:
              continue
            if j == 0:
              dP[j] = dP[j] + grid[i][j]
            else: 
              dP[j] = grid[i][j] + min(dP[j], dP[j-1])


        
        
        return dP[-1]  # Giá trị cuối cùng là đáp án

solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
