from typing import List

class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        rows, cols = len(board), len(board[0])
        def dfs(i, j, k, visited):
            visited.add((i,j))
            if k == len(word) - 1:
                return True
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == word[k+1] and (ni, nj) not in visited:
                    if dfs(ni, nj, k+1, visited):
                        return True
            visited.remove((i,j))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False
solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))