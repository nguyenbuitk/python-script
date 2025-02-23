class Solution:
  def calSquare(self, n: int) -> int:
    res = 0
    while n > 0:
      digit = n % 10
      res += digit ** 2
      n = n//10
    return res
  def isHappy(self, n: int) -> bool:
    slow = fast = n
    while True:
      slow = self.calSquare(slow)
      fast = self.calSquare(fast)
      fast = self.calSquare(fast)
      if slow == fast:
        break
    if slow == 1:
      return True
    return False
      
solution = Solution()
print(solution.isHappy(19))


