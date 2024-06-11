from typing import List

class Solution:
    # (n) is number of the strings in the list
    # Complexity: O[n log(n)] = O[n log(n)] + O(m)
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        # O[n log(n)]
        v=sorted(v)
        first=v[0]
        last=v[-1]
        # O(m)
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

def test_longestCommonPrefix():
    solution = Solution()
    solution.longestCommonPrefix()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    assert solution.longestCommonPrefix([""]) == ""

    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

    assert solution.longestCommonPrefix(["apple", "app", "appril"]) == "app"

    print("All test cases pass")

test_longestCommonPrefix()