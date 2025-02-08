class Solution(object):
  def jump(self, nums):
    # jump[i] = số bước nhỏ nhất để đến index i 
    min_jump = [float('inf')]*len(nums)
    min_jump[0] = 0
    for i in range(1, len(nums)):
      sub_problems = []
      for k in range(i):
        if nums[k] + k >= i:
          sub_problems.append(min_jump[k])
      min_jump[i] = 1 + min(sub_problems)
    print(min_jump)
    return min_jump[len(nums) - 1]
solution = Solution()
print(solution.jump([2,3,1,1,4]))
