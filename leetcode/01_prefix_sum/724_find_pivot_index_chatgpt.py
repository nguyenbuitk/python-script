class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum, right_sum = 0, sum(nums) # right_sum = total sum
        for i in range(len(nums)):
            right_sum -= nums[i]        # calculate the right sum
            
            if left_sum == right_sum:   # return if pivot
                return i
            left_sum += nums[i]         # calculate the left sum before traver
        return -1

solution = Solution()
solution.pivotIndex([1,7,3,5,6])