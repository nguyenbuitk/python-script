class Solution:
    def lengthOfLongestSubstring(self, str):
        max_res = 0
        res = 0
        left = 0
        current_window = set()
        for i in str:
            while i in current_window:
                current_window.remove(str[left])
                res -= 1
                left += 1
            current_window.add(i)
            res += 1
            max_res = max(res, max_res) 
        return max_res