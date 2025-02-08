class Solution(object):
  def maxProfit(self, prices):
    mP = [0] * len(prices)
    # notSellP = [0] * len(prices)
    # sellP = [0] * len(prices)

    for i in range(1, len(prices)):
      # sub_problem is profit if sell at day i
      sub_problem = []
      for k in range(i):
        if prices[k] < prices[i]:
          sub_problem.append(prices[i]-prices[k] + mP[k])
      # if hold at day i, mP[i] = mP[i-1]
      sub_problem.append(mP[i-1])
      mP[i] = max(sub_problem) if sub_problem else 0
    return max(mP)
solution = Solution()
print(solution.maxProfit([7,1,5,1,5,3,6,4]))
