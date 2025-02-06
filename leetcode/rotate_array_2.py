"""
nums = "----->-->"; k =3
result = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"
this visualization help me figure it out :)
"""
def reverse(nums, start, end):
  l, r = start ,end
  while(l < r):
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
  

class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead
    """
    if len(nums) == 1 or k == 1 or k == len(nums):
      return
    k = k % len(nums)
    reverse(nums, 0, len(nums) -1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) -1)
    print(nums)
    

solution = Solution()
solution.rotate([1,2,3,4,5,6,7],3)

#solution.rotate([99,-1,-100,3],3)

nums = [1 ,2 , 3, 4]
reverse(nums, 1, 3)
print(nums)
