class Solution:
  def balancedStringSplit(self, s: str) -> int:
    count_r = 0
    count_l = 0
    res = 0
    for char in s:
      if char == "L":
        count_l += 1
      elif char == "R":
        count_r += 1
      
      if count_r == count_l and count_r != 0:
        count_r = 0
        count_l = 0
        res += 1
    return res

solution = Solution()
# print("res: ", solution.balancedStringSplit("RLRRL"))
print("res: ", solution.balancedStringSplit("RLRRLLRLRL"))

