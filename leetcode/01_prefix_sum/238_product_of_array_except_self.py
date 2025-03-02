class Solution:
    def productExceptSelf(self, nums):
        product_left = [nums[0]]
        product_right = [1] * len(nums)
        product_right[len(nums) - 1] = nums[len(nums) - 1]
        res = []
        for i in range(1,len(nums)):
            product_left.append(product_left[i-1]*nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            product_right[i] = product_right[i+1]*nums[i]
        
        for i in range(len(nums)):
            if not i: res.append(product_right[i+1])
            elif i == len(nums) - 1: res.append(product_left[len(nums) - 2])
            else: res.append(product_left[i-1]*product_right[i+1])
        return res
        

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))