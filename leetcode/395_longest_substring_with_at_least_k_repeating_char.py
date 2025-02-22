class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dict = {}
        for right in s:
            dict[right] = dict.get(right, 0) + 1
        
        for right in s:
            if dict[right] < k:
                res_end = []
                for sub in s.split(right):
                    res_end.append(self.longestSubstring(sub, k))
                return max(res_end)
        return len(s)
            
            
        
solution = Solution()
print(solution.longestSubstring("ababbc", 2))