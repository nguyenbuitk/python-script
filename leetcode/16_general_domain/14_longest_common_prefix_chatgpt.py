
class Solution(object):
    # (n) is number of strings in the list
    # (m) is length of shortest string.
    # Complexity: O(n * m) = O(n * m) + O(n)
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""

        # O(n) Find the shortest string in the list
        min_str = min(strs, key=len)

        # O(n * m) Comparing character
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]

        return min_str

def test_longestCommonPrefix():
    solution = Solution()
    
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    assert solution.longestCommonPrefix([""]) == ""

    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

    assert solution.longestCommonPrefix(["apple", "app", "appril"]) == "app"

    print("All test cases pass")

test_longestCommonPrefix()
