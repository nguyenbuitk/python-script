class Solution(object):
  def canPlaceFlowers(self, flowerbed, n):
    res = 0
    if len(flowerbed) == 1:
      if flowerbed[0] == 1:
        res = 1
      return res >= n
    for i in range(len(flowerbed)):
      if i == 0:
        if flowerbed[i] == 0 and flowerbed[i+1] == 0:
          res += 1
          flowerbed[i] = 1
      elif i == len(flowerbed) - 1:
        if flowerbed[i] == 0 and flowerbed[i-1] == 0:
          res += 1
          flowerbed[i] = 1
      else:
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
          res += 1
          flowerbed[i] = 1
    return res >= n


solution = Solution()
print(solution.canPlaceFlowers([1], 1))

