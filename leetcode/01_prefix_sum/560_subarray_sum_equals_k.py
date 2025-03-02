class Solution:
    def subarraySum(self, nums, k):
        dt = {}     # dictionary for save the index of prefix sum
        res = 0     # biến đếm số lượng subarray có tổng bằng k
        
        for i in range(len(nums)):
            if i < len(nums) - 1:
                nums[i+1] += nums[i]        # calcualte prefix sum (sum from start to nums[i])
            target = nums[i] - k
            if target == 0:
                res += 1
            if target in dt:
                res += len(dt[target])
            if nums[i] in dt:
                dt[nums[i]].append(i)
            else: dt[nums[i]] = [i]
        return res
            

solution = Solution()
print(solution.subarraySum([1,-1,0], 0))