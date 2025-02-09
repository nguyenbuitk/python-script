def validPalin(s):
  print("s: ", s)
  l, r = 0, len(s) - 1
  while (l < len(s) / 2):
    if s[l] == s[r]:
      l += 1
      r -= 1
    else: return False
  return True

class Solution(object):
  def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(len(s)):
      if validPalin(s[:i] + s[i+1:]) == True:
        return True
    return False

solution = Solution()
print(solution.validPalindrome("abca"))
