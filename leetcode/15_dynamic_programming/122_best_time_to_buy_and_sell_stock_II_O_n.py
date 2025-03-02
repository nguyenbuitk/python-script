class Solution(object):
  def maxProfit(self, prices):
    mP = [0] * len(prices)
    # notSellP = [0] * len(prices)
    # sellP = [0] * len(prices)

    for i in range(1, len(prices)):
      hold_profit = mP[i-1]
      mP[i] = max(hold_profit, hold_profit + prices[i] - prices[i-1])
    return max(mP)
solution = Solution()
print(solution.maxProfit([7,1,5,1,5,3,6,4]))
