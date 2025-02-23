# Beat 97%

class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            
            # We iterate the array in reverse order to correctly process the last element first
            if i == len(nums) - 1:
                for j in range(len(nums) - 2, -1, -1):
                    
                    # get all element greater than nums[len - 1]
                    if nums[j] > nums[i]:
                        stack.append(nums[j])
            
            # Remove all element <= nums[i] of the stack
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]
                
            stack.append(nums[i])
        return res