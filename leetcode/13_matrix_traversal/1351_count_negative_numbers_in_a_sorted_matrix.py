from typing import List

class Solution:
    def findFirstNegative(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] >= 0:
                l += 1
            else: r -= 1
        if l < len(nums):
            return l
        return len(nums)
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            new_col = self.findFirstNegative(grid[i][:cols])
            res += (rows - i) * (cols - new_col)
            cols = new_col
        return res
solution = Solution()
print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))