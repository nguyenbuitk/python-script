class Solution(object):
  def canPlaceFlowers(self, flowerbed, n):
    res = 0
    start = -1
    fl = [1,0]
    fl.extend(flowerbed)
    fl.extend([0,1])
    print(fl)
    for i in range(len(fl)):
      if fl[i] == 1:
        distance = i - start - 1
        print("distance, i: ", distance, i)
        start = i
        if distance % 2 == 0:
          if int(distance/2 - 1)<0:
            continue
          res += int(distance/2 - 1)
        else:
          if int(distance/2-1)<0:
            continue
          res += int(distance/2)
        print("res: ", res)
        print("\n")



    return res >= n


solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1],1 ))

