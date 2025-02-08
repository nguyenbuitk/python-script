class Solution(object):
  def jump(self, nums):
    farthest = 0 
    end = 0
    jump = 0 
    for i in range(len(nums) - 1):
      farthest = max(farthest, nums[i] + i)
      if i == end:
        jump += 1
        end = farthest
    return jump
solution = Solution()
print(solution.jump([2,3,1,1,4]))
