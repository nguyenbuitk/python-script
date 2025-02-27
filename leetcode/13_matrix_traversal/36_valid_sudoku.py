from typing import List
from collections import Counter

class Solution:
    def isValidUnit(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check is row and col valid
        for i in range(9):
            row = []
            col = []
            path = []
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    # check subbox 3x3 is valid
                    path = [board[p][k] for p in range(i, i+3) for k in range(j, j+3)]
                    if not self.isValidUnit(path):
                        return False
                    
                row.append(board[i][j])
                col.append(board[j][i])
                
            if not self.isValidUnit(row) or not self.isValidUnit(col):
                return False

        return True
    
solution = Solution()
print(solution.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(solution.isValidSudoku(
[[".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]
))