class Solution:
    def minSubArrayLen(self, target, nums):
        left, res = 0, float('inf')
        if nums[left] >= target:
            return 1
        sum = nums[left]
        for right in range(1, len(nums)):
            sum += nums[right]
            while sum >= target:
                res = min(right-left + 1, res)
                sum -= nums[left]
                left += 1
                
        if res == float('inf'):
            return 0
        return res
solution = Solution()
print(solution.minSubArrayLen(4, [1,4,4]))