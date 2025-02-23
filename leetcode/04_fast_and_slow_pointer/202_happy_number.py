class Solution:
  def isHappy(self, n: int) -> bool:
    res = 0
    seen = set()
    
    while res != 1:
      terms = []
      s = str(n)
      res = 0
      for char in s:
        terms.append(f"{char}^2")
        res += int(char) ** 2
      n = res
      if n in seen:
        return False
      seen.add(n)
      print(" + ".join(terms) + f"= {res}")
    
    return True
      
solution = Solution()
print(solution.isHappy(19))


