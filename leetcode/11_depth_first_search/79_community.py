from typing import List

class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i, j, k):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
 
            board[i][j] = "#"
            res = dfs(i + 1, j, k+1) or dfs(i -1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            board[i][j] = word[k]
            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
