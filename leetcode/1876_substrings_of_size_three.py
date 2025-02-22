class Solution:
    def countGoodSubstrings(self, s):
        dict = {}
        res = 0
        left, right = 0, 0
        while right < len(s):
            while right - left  < 3 and right < len(s):
                dict[s[right]] = dict.get(s[right], 0) + 1
                right += 1
            if max(dict.values()) == 1 and right - left > 2:
                res += 1
            dict[s[left]] -= 1
            left += 1
        return res