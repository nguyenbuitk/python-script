from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        def dfs(i, j):
            board[i][j] = '#'
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) and board[ni][nj] == 'O':
                    board[ni][nj] = '#'
                    dfs(ni, nj)
        
        def dfs_method2(i, j):
            if i < 0 or i>= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = '#'
            for dr, dc in [(1,0), (-1,0), (0, -1), (0, 1)]:
                dfs_method2(i+dr, j + dc)
        
        # Step 1: Convert all `'O'` regions that connected to the border to "#"
        for i in range(rows):
            if board[i][0] == "O":
               dfs(i,0)
            if board[i][cols-1] == "O":
               dfs(i, cols-1) 
               
        for j in range(cols):
            if board[0][j] == "O":
               dfs(0, j)
            if board[rows-1][j] == "O":
               dfs(rows -1, j) 
        
        # Step 2: Convert all remaining 'O' to 'X' since they are surrounded
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    
        # Convert all "#" back to "O"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "#":
                    board[i][j] = "O"
        print(board)
                
solution = Solution()
solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])                        