# Medium
## 130. Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:
Input: 
["X","X","X","X"]
["X","O","O","X"]
["X","X","O","X"]
["X","O","X","X"]

Output: 
["X","X","X","X"]
["X","X","X","X"]
["X","X","X","X"]
["X","O","X","X"]

# Key Idea
## Approach 1 (self)
1. Use DFS to find all connected regions of `'O'`
    - Iterate over the board, when encoutering `'O'`, check if it already belongs to an existing region
    - If not, perform DFS to find all `'O'` cells connected to it
    - Store connected component (set of coordinates) in a dictionary
2. Check if a region is surrounded
    - After identifying all regions, check if a region is completely enclosed
    - If completely enclosed, flip all `'O'` in that region

## Approach 2 (chatgpt - using DFS or BFS)
1. Identify `'O'` regions connected to the border:
    - Any `'O'` that is connected to the border must not be flipped to `'X'`
    - Start DFS/BFS from all `'O'` cells on the first and last rows and first and last column
2. Mark safe `'O'` regions:
    - Perform DFS/BFS from border `'O'` and temporarily mark them as `'#'`
    - This prevents them from being converted to `'X'`
3. Flip the board:
    - Convert all remaining `'O'` to `'X'` since they are surrounded
    - Convert all `'#'` back to `'O'`