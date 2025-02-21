class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        left, current_window = 0, 1
        for right in range(len(nums)):
            current_window *= nums[right]
            print(f"current_window start at {left} -> {right}")
            # find longest sliding windows end at index right
            while current_window >= k and left <= right:
                current_window //= nums[left]
                left +=1
                print(f"current_window start at {left} -> {right}")
            # total number of combinations end at index right
            res += right - left + 1
            
        return res

solution = Solution()
print(solution.numSubarrayProductLessThanK([10,5,2,6], 100 ))