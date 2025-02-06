class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead
    """
    
    padding = [1] * k
    nums = padding + nums

    l, r = k - 1, len(nums) - 1
    for i in range(k):
      nums[l], nums[r] = nums[r], nums[l]
      r -= 1
      l -= 1

    nums = nums[0:-k]
    print(nums)


solution = Solution()
solution.rotate([1,2,3,4,5,6,7],3)
#solution.rotate([99,-1,-100,3],3)

