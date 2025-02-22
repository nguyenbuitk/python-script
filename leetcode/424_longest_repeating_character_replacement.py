# idea
# iterate through each element in nums with the left and right pointer
# maintain the frequency of each number with a counter
# if the window has too many different numbers that cann't be transformed with just k, shrink the window from the left

class Solution:
    def characterReplacement(self, s, k):
        left, right = 0, 0
        res = 0
        dict = {}
        
        # expand the window by moving 'right' pointer
        for right in range(len(s)):
            
            if s[right] not in dict:
                dict[s[right]] = 1
            else: dict[s[right]] += 1
            
            # compute the current window length
            length = right - left + 1
            
            # find the max frequencey of character in the window
            max_freq = max(dict.values())
            
            # shrink the windows if the number of replacement needed is grater 
            if length - max_freq > k :
                dict[s[left]] -= 1
                left += 1
                
                length -= 1
            res = max(res, length)
        return res

solution = Solution()
print(solution.characterReplacement("ABAB", 0))