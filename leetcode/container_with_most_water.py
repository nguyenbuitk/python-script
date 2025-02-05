class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    max = 0 
    for i, value_i  in enumerate(height[:-1]):
      for j, value_j in enumerate(height[i+1:], start=i+1):
        # print(i, value_i, j, value_j)
        if (j-i)*min(value_i,value_j) > max:
          max = (j-i)*min(value_i,value_j) 
    return max
solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
