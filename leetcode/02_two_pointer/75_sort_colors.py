def swap(a, b):
  return b, a
class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead
    """
    l, r = -1 , len(nums)
    while l < r - 1:
      print(f"l, r: {l}, {r}")
      m = l + 1
      
      while m < r:
        if nums[m] == 1:
          m += 1
          if m == r:
            return nums 
          continue
        if nums[m] == 2:
          nums[r - 1], nums[m] = swap(nums[r - 1], nums[m])
          r -= 1
          break
        if nums[m] == 0:
          nums[l + 1], nums[m] = swap(nums[l+1], nums[m])
          l += 1
          break

      
    return nums
solution = Solution()
print(solution.sortColors([2, 0, 2,1,1,0]))
print(solution.sortColors([0,0]))
