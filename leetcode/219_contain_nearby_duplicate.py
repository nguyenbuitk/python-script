class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        left, right = 0, 0
        while right < len(nums):
            if nums[right] in dict:
                return True
            dict[nums[right]] = right

            if right >= k:
                del dict[nums[right - k]]
        return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
            
            
