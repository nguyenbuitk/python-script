class Solution(object):
  def jump(self, nums):
    # jump[i] = số bước nhỏ nhất để nhảy từ i đến cuối cùng
    min_jump = [float('inf')]*len(nums)
    min_jump[len(nums) - 1] = 0
    for i in range(len(nums) - 2, -1 , -1):
      print("i: ", i)
      sub_problems = []
      for k in range(i + 1, i + 1+ nums[i] ):
        print("k: ", k)
        if k < len(nums):
          sub_problems.append(min_jump[k])
      print(sub_problems)
      min_jump[i] = 1 + min(sub_problems)
    return min_jump[0]
solution = Solution()
print(solution.jump([2,3,0,1,4]))
