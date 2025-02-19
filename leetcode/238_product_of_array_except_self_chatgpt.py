class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        for i in range(1, n):
            res[i] = res[i-1]* nums[i-1]
        
        subfix_product = nums[n-1]
        for i in range(n - 2, -1, -1):
            res[i] = res[i] * subfix_product
            subfix_product *= nums[i]
        
    
        return res
        

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))