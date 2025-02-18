class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        while p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                p2 -= 1
            else: 
                p1 -= 1
                p2 -= 1
        return p1 == -1

solution = Solution()

print(solution.isSubsequence("aaaaaa", "bbaaaa"))
