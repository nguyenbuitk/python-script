def maxProfit(prices):
  minPrice = float('inf')
  maxProfit = 0
  for price in prices:
    minPrice = min(price,minPrice)
    maxProfit = max(maxProfit, price - minPrice)

  return maxProfit
