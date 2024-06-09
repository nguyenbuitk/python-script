class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the shortest string in the list
        min_str = min(strs, key=len)

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
