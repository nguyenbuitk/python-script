class Solution:
    def removeDuplicates(self, nums):
        min_pos = 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[min_pos]:
                nums[i], nums[min_pos+1] = nums[min_pos+1], nums[i]
                k += 1
                min_pos += 1
                
        return k
    def removeDuplicates_chatgpt(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[k - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k
solution = Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])