class Solution(object):
  def longestPalindrome(self,s):
    """
    :type s: str
    :rtype: int
    """
    hm = {}
    for i in range(len(s)):
      if s[i] in hm:
        hm[s[i]] += 1

      else: hm[s[i]] = 1

    res = 0
    for key, value in hm.items():
      print("{}: {}".format(key, value))
      if value % 2 == 0:
        res += value
    
    return res + 1

solution = Solution()
print(solution.longestPalindrome("abccccdd"))
