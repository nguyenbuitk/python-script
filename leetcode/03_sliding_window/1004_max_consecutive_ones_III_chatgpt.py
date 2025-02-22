# beat 40%

class Solution:
    def longestOnes(self, nums, k):
        # count_zeros: number of zeros in window
        left, count_zeros, res = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
                            
            # if 0 exceed k, shrink the window
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            
        return res


solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))