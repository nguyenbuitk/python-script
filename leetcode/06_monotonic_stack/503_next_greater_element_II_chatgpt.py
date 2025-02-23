# Beat 20%

class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)*2 -1, -1, -1):
            # Remove all the element < tempratures[i]
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
                
            # If stack is not empty, calculate the waiting day
            if stack:
                res[i%len(nums)] = stack[-1]
            
            # Push current temperature and its index to the stack
            stack.append(nums[i%len(nums)])
        return res