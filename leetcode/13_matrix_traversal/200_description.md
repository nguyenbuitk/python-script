# Medium
## 200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

# Key Idea
** Similar to problem 130 surrounded regions **
## Approach DFS
1. Start DFS from `"1"` cell and mark them as `"X"`
2. End of DFS count += 1 and return count

## Approach BFS
