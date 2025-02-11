class Solution(object):
  def largestPerimeter(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort(reverse=True)

    res = 0 
    # i: 0, 1
    for i in range(len(nums)-2):
      # j: 1, 2
      for j in range(i+1, len(nums)-1):
        # k: 2, 3
        for k in range(j+1, len(nums)):
          if nums[i] - nums[j] < nums[k] < nums[i] + nums[j]:
            return nums[i] + nums[j] + nums[k]
            
solution = Solution()
print(solution.largestPerimeter([1,2,1,10]))
