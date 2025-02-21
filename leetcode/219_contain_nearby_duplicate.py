class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        left, right = 0, 0
        for i in range(k + 1):
            if i < len(nums):
                if nums[i] in dict:
                    return True
                dict[nums[i]] = i
        right = k + 1
        while right < len(nums):
            del dict[nums[left]]
            if nums[right] in dict:
                return True
            dict[nums[right]] = right
            right += 1
            left += 1
        return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
            
            