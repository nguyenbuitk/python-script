def remove_non_alphabet(s):
  # chỉ giữ lại chữ cái và số
  l = [ char.lower() for char in s if char.isalnum() ]
  return ''.join(l)

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = remove_non_alphabet(s)
    print(s)
    l, r = 0, len(s) - 1
    while (l < len(s)/2):
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))
