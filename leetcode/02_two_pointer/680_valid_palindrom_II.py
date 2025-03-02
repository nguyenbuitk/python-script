def validPalin(s):
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
    mid = len(s) / 2
    l, r = 0, len(s) - 1
    deleted = 0
    while (l < mid):
      if s[l] == s[r]:
        l += 1
        r -= 1
      # return l+1 -> r (delete l)  or l -> r-1 (delete r)
      else: return validPalin(s[l+1:r+1]) or validPalin(s[l:r])
    return True
