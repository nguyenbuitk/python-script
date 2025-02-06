class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = set()
    nums.sort()
    for start in range(len(nums) - 2):
      l, r = start + 1, len(nums) - 1
      print("l, r", l,r)
      target = -nums[start]
      while l < r:
        print(f"travers: {nums[start]}, {nums[l]}, {nums[r]}")
        if nums[l] + nums[r] == target:
          arr = (nums[start], nums[l], nums[r])
          res.add(arr)

          l +=1 
        elif nums[l] + nums[r] < target:
          l += 1
        else: r -= 1
    return [list(triple) for triple in res]
def check_duplicate(arr1, arr2):
  return set(arr1) == set(arr2)


solution = Solution()
#print(solution.threeSum([0,0,0]))
print(solution.threeSum([-1,0,1]))
