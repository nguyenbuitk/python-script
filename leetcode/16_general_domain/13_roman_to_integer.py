class Solution(object):
    # Complexity O(n) Where n is the length of the input string s.
    def romanToInt(self, s):
        """_summary_
            :type s: str
            :rtype: int
        """
        result = 0
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for index, char in enumerate(s):
            current_int = roman_to_int[s[index]]

            if (index > 0 and current_int > roman_to_int[s[index-1]]):
                continue
            
            if index < len(s) - 1 and current_int < roman_to_int[s[index + 1]]:
                result = result + (roman_to_int[s[index + 1]] - roman_to_int[s[index]])
            else:
                result += roman_to_int[char]
        
        return result

sol = Solution()
print(sol.romanToInt("III"))    # Output: 3
print(sol.romanToInt("IV"))     # Output: 4
print(sol.romanToInt("IX"))     # Output: 9
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV")) # Output: 1994