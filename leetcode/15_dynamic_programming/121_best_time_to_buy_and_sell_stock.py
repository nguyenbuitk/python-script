class Solution(object):
  def maxProfit(self, prices):
    profit = [0] * len(prices)
    minPrice=[]
    minPrice.append(prices[0])
    for i in range (1, len(prices)):
      minPrice.append(min(minPrice[i-1], prices[i]))
    print(minPrice)
    for i in range(1, len(prices)):
      profit[i] = prices[i] - minPrice[i]
    return max(profit)

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
