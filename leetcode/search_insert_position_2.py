class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1 
        while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
            return mid
          elif nums[mid] < target:
            left = mid + 1
          elif nums[mid] > target: 
            right = mid - 1
        return left


def test_searchInsert():
    solution = Solution()
    nums1 = [1,3,5,6]
    target1 = 5
    expected1 = 2
    assert solution.searchInsert(nums1, target1) == expected1, f"Test case 1 failed: {nums1}, {target1}"

    nums2 = [1, 3,5,6]
    target2 = 2
    expected2 = 1
    assert solution.searchInsert(nums2, target2) == expected2, f"Test case 2 failed {nums2}, {target2}"

    nums3 = [1, 3, 5, 6]
    target3 = 7
    expected3 = 4
    assert solution.searchInsert(nums3, target3) == expected3, f"Test case 3 failed {nums3}, {target3}"

    nums4 = [1 ,3, 5, 6]
    target4 = 0
    expected4 = 0
    assert solution.searchInsert(nums4, target4) == expected4, f"Test case 4 failed {nums4}, {target4}"
    print("All test cases passed!")
# solution = Solution()
# solution.searchInsert([1, 3, 5,6], 2)
test_searchInsert()
