class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
          return 0
        for index, num in enumerate(nums):
            if target == num:
                return index
            elif index == len(nums) - 1 or (target > num and target < nums[index + 1]):
                return index + 1
            print(f"{index} : {num}")
        return index

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
