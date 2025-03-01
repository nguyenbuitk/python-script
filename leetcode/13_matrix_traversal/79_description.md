# Medium
## 79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

# Key Idea
1. DFS with backtracking:
    - Start searching from each cell `(i, j)`
    - If the character at `board[i][j]` matches the first letter of `word`, initiate a DFS to explore all possible paths
2. Valide moves:
    - Move in four directions: right left down up
    - Ensure the next cell is within bounds, not already visited, and matches the next letter
3. Backtracking:
    - If a valid path is found, return `true`
    - If a path fails, backtrack by restoring the previous state
