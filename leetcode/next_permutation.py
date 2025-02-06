# Most people look from front to back, but looking in the opposite direction can provide useful solutions.


class Solution(object):
  def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead
    """
    k = -1
    for i in range(len(nums) - 2, -1, -1):
      if nums[i] < nums[i+1]:
        k = i
        break
    
    if k == -1:
      nums.reverse()
    print("k: ", k)
    min_index = k + 1
    for i in range(k + 2, len(nums)):
      if nums[i] < nums[min_index] and nums[i] > nums[k]:
        min_index = i
    print("min_index: ", min_index) 
    nums[k] , nums[min_index] = nums[min_index] ,nums[k]
    res_arr = nums[k+1:]
    res_arr.sort()
    for i in range(len(res_arr)):
      nums[k+i+1] = res_arr[i]
    print("nums: ", nums)
    print("res_arr: ", res_arr)

solution = Solution()
nums = [1,5, 1]
solution.nextPermutation(nums)
