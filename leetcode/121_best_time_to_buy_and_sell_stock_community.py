class Solution(object):
  def maxProfit(self, prices):
    maxProfit = 0
    indexMinPrice = 0
    for i in range (1, len(prices)):
      print("i: ", i )
      maxProfit = max(maxProfit, prices[i] - prices[indexMinPrice])
      indexMinPrice = min(prices[indexMinPrice], prices[i])

    return maxProfit
solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))
