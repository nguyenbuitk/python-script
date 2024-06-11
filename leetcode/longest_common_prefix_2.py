class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        
        m = {}
        for s in strs:
            if s == "":
                return ""
            for index in range(1, len(s) + 1):
                if s[0:index] not in m.keys():
                    m[s[0:index]] = 1
                else:
                    m[s[0:index]] += 1
                    
        result = strs[0][0]
        if m[result] < len(strs): 
            return ""
        for key, value in m.items():    
            if len(key) > len(result) and value == m[result]:
                result = key
        print(result)
        
        return result


def test_longestCommonPrefix():
    solution = Solution()
    
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    print("case 1 pass")
    
    assert solution.longestCommonPrefix([""]) == ""
    print("case 2 pass")
    
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    print("case 3 pass")
    
    assert solution.longestCommonPrefix(["apple", "app", "appril"]) == "app"
    print("case 4 pass")
    
    assert solution.longestCommonPrefix(["flower","flower","flower","flower"]) == "flower"
    print("All test cases pass")

test_longestCommonPrefix()
