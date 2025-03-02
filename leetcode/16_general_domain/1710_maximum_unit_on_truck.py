class Solution(object):
  def maximumUnits(self, boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """

    # boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4 
    """
    boxTypes = [[5,3], [2,2], [3,1]]:
    Loại thùng 1: Có 5 thùng, mỗi thùng chứa 3 đơn vị.
    Loại thùng 2: Có 2 thùng, mỗi thùng chứa 2 đơn vị.
    Loại thùng 3: Có 3 thùng, mỗi thùng chứa 1 đơn vị.
    truckSize = 4: Xe tải có thể chứa tối đa 4 thùng.
    """

    # sort 2D array
    res = 0
    sorted_array = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    print(sorted_array)
    for i in range(len(sorted_array)):
      if truckSize <= 0:
        return res
      
      if truckSize <= sorted_array[i][0]:
        res += truckSize * sorted_array[i][1]
        return res

      truckSize = truckSize - sorted_array[i][0]
      res += sorted_array[i][0] * sorted_array[i][1]

    return res

    
solution = Solution()
#print(solution.maximumUnits([[1,3],[2,2],[3,1]], 4))
print(solution.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))    
