class Solution(object):
  def canJump(self, nums):
    jump = [0] * len(nums)
    jump[0] = 1
    for i in range(len(nums)):
      if jump[i]:
        for j in range(1, nums[i] + 1):
          if i + j < len(nums):
            jump[i + j] = 1
    return jump[len(nums)-1] == 1
        

solution = Solution()
print(solution.canJump([2,3,1,1,4]))
