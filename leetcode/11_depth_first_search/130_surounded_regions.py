from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        # Dictionary to store identified regions of 'O' cells
        visitedLand = {}
        
        k = 0   # Region index
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # DFS to find all connected 'O' cells
        def dfs(i, j, k, visitedLand):
            visitedLand[k].add((i,j))   # Mark the cell as visited in the current region
            for dr, dc in directions:
                ni, nj = i+dr, j + dc
                # Ensure within bounds, not visited, and is 'O'
                if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visitedLand[k] and board[ni][nj] == "O":
                    dfs(ni, nj, k, visitedLand)     # Recursive DFS call
        
        # Step 1: Identify all 'O' regions using DFS
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    isDuplicated = False # Flag to check if cell is already visited
                    
                    # Check if this 'O' already belongs to an identified region
                    for _, val in visitedLand.items():
                        # print("visitedLand val: ", val)
                        if (i,j) in val:
                            isDuplicated = True
                            break
                    if isDuplicated:    # Skip if already visited
                        continue
                    visitedLand[k] = set()  # Create a new region
                    dfs(i, j, k, visitedLand)   # Perform DFS to explore the region
                    k += 1                  # Increment region index
        
        # Step 2: Check which 'O' regions should be converted to 'X'
        for k, val in visitedLand.items():
            # print("=================")
            # print(val)
            min_x = min(x for x, _ in visitedLand[k])
            max_x = max(x for x, _ in visitedLand[k])
            min_y = min(y for _, y in visitedLand[k])
            max_y = max(y for _, y in visitedLand[k])
            # print(min_x, max_x, min_x, max_y)
            if 0 < min_x and max_x < rows - 1 and 0 < min_y and max_y < cols - 1:
                for i,j in val:
                    board[i][j] = 'X'
        # print(board)
solution = Solution()
solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])    