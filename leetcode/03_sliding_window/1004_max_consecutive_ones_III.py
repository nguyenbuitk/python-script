# beats 72.32 %

from collections import deque
class Solution:
    def longestOnes(self, nums, k):
        zero_count, res, current_res  = 0, 0, 0
        
        # deque to store indices of zeros for efficient removeal
        dq = deque([])
        
        for i in range(len(nums)):
            if nums[i] == 0 and zero_count < k:
                # if the current number is 0 and we still have flips available
                zero_count += 1
                current_res += 1
                dq.append(i)
                
            elif nums[i] == 1:
                current_res += 1
                
            else: # nums[i] == 0 and zero_count >= k
                if dq:
                    # If the deque is not empty, remove the leftmost zero
                    current_res = i - dq.popleft()
                    dq.append(i)
                else:
                    # If there are no zeros to remove, reset current_res
                    current_res = 0 
            res = max(current_res, res)
        return res

solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1], 0))