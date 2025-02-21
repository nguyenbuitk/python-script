class Solution:
    def minSubArrayLen(self, target, nums):
        dict = {}
        for i in range(len(nums)):
            if i != len(nums) - 1:
                nums[i+1] += nums[i]
            res = float('inf')
            
            compen = nums[i] - target
            if compen == 0:
                res = min(res, i)
            
            if compen in dict:
                res = min(res, i - max(dict[compen]))
                

            if nums[i] in dict:
                dict[nums[i]].append(i)
            else: dict[nums[i]] = [i]
        
        if res == float('inf'): res = 0 
        return res

solution = Solution()
print(solution.minSubArrayLen(4, [1,4,4]))