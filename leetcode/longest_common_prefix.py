class Solution(object):
    def longestCommonPrefix(self, strs):
        # (n) is number of strings in the list
        # (m) is length of shortest string.
        # Complexity: O(n * m*m) or O(n * m)
        if not strs: 
            return ""
        
        m = {}
        # O(n) times, where n is the number of strings in the list
        for s in strs:
            if s == "":
                return ""
            # O(m) times for each string, where m is the length of the string.
            for index in range(1, len(s) + 1):
                # Dictionary lookups in Python are considered to have an average time complexity of O(1).
                # Creating the substring s[0:index] takes O(index) time, which in the worst case is O(m).
                if s[0:index] not in m.keys():
                    m[s[0:index]] = 1
                else:
                    m[s[0:index]] += 1
                    
        result = strs[0][0]
        if m[result] < len(strs): 
            return ""
        # O(k) complexity
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
