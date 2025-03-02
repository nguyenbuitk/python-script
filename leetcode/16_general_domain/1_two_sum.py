class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hm = {}
    for i, value in enumerate(nums):
      print("value, i", value, i)
      print(hm)
      complement = target - value
      print("complement: ",complement)
      if complement in hm:
        return [hm[complement], i]
      else: 
        hm[value] = i

solution = Solution()
solution.twoSum([2,7,11,15], 9)
