class Solution():
    def findMaxAverage(self, nums, k):
        res = sum(nums[:k])/k
        current_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            res = max(res, current_sum/k)
        return res
