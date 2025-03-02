class Solution(object):
    # Complexity O(n) Where n is the length of the input string s.
    def romanToInt(self, s):
        romant_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        next = 0
        prev = 0
        for char in reversed(s):
            next = romant_to_int[char]
            if next < prev:
                result -= next
            else:
                result += next
            prev = next
        return result

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
