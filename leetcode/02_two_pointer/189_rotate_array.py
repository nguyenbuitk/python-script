class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead
    """
    
    padding = [1] * k
    new_nums = padding + nums
    print(new_nums)

    l, r = k - 1, len(new_nums) - 1
    for i in range(k):
      new_nums[l], new_nums[r] = new_nums[r], new_nums[l]
      r -= 1
      l -= 1

    new_nums = new_nums[0:-k]
    print("new_nums ", new_nums)
    for i in range(len(nums)):
      nums[i] = new_nums[i]


solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums,3)
print(nums)
#solution.rotate([99,-1,-100,3],3)

