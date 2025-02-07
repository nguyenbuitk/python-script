class Solution(object):
  def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # slow, fast is value, not index, next pointer is nums[value]
    # slow = slow.next
    slow = nums[0]
    # fast = fast.next.next
    fast = nums[nums[0]]
    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    slow2 = nums[0]
    slow = nums[slow]
    while slow != slow2:
      slow = nums[slow]
      slow2 = nums[slow2]

    return slow2
    
solution = Solution()
print(solution.findDuplicate([3,1,3,4,2]))
