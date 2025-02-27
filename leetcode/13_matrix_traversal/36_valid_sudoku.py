from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count_row = Counter(board[i])
            del count_row['.']
            if count_row and (max(count_row.values()) > 1):
                return False
            print(count_row)
            col = []
            for j in range(9):
                col.append(board[j][i])
            count_col = Counter(col)
            del count_col['.']
            if count_row and (max(count_row.values()) > 1):
                return False
            print()
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                path = []
                path = [board[p][k] for p in range(i, i+3) for k in range(j, j+3)]
                count_sq = Counter(path)
                del count_sq['.']
                print(count_sq)
                if count_sq and (max(count_sq.values()) > 1):
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