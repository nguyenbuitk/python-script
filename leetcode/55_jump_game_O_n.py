class Solution(object):
  def canJump(self, nums):
    # jump[i] = maximum distance from i
    max_distance = 0
    i = 0
    while(i < len(nums) - 1):
      if max_distance < i:
        return False
      else:
        max_from_current = nums[i] + i
        max_distance = max(max_distance, max_from_current) 
      i += 1
    return max_distance >= len(nums) - 1
        

solution = Solution()
print(solution.canJump([2,3,1,1,4]))
