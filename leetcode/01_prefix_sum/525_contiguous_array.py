class Solution:
    def findMaxLength(sef, nums):
        # d[prefix_sum] = index
        d = {0: -1}
        prefix_sum = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else: prefix_sum += 1
            if prefix_sum in d:
               res = max(res, i - d[prefix_sum]) 
            else: d[prefix_sum] = i
        return res
solution = Solution()
print(solution.findMaxLength([0,0,1,0,0,0,1,1]))