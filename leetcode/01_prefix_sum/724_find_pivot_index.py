class Solution:
    def pivotIndex(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else: left_sum = nums[i-1]
            if i == len(nums) - 1:
                right_sum = 0
            else: right_sum = nums[len(nums)-1] - nums[i+1]
            if left_sum == right_sum:
                return i
        return -1

solution = Solution()
solution.pivotIndex([1,7,3,5,6])