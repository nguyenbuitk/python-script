# beat 40%

# this solution is more clear
# 1.  using two pointer left and right to create sliding window
# - right traverse through each element
# - left change to ensure the window have at most k number of zeros
# 2. calculate the number of zeros in window, if it exceed k, move left to remove 0
class Solution:
    def longestOnes(self, nums, k):
        # count_zeros: number of zeros in window
        left, count_zeros, res =0, 0, 0
        
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