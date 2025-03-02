class Solution:
    # Complexity O(n) Where n is the length of the input string s.
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                result -= m[s[i]]
            else:
                result += m[s[i]]
        return result

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
