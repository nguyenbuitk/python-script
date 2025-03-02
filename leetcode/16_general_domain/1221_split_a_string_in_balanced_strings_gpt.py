class Solution:
  def balancedStringSplit(self, s: str) -> int:
    balance = 0
    res = 0
    for char in s:
      balance += 1  if char == "L" else  -1
      
      if balance == 0:
        res += 1
    return res

solution = Solution()
# print("res: ", solution.balancedStringSplit("RLRRL"))
print("res: ", solution.balancedStringSplit("RLRRLLRLRL"))

