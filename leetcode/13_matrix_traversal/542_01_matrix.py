from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[float('inf')]*cols for _ in range(rows)]
        dq = deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    dq.append((i,j))
        print(dq)
        while dq:
            i, j = dq.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = di +i , dj + j
                if 0 <= ni < rows and 0 <= nj < cols and res[ni][nj] > res[i][j] + 1:
                    res[ni][nj] = res[i][j] + 1
                    dq.append((ni,nj))
        return res

solution = Solution()
print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))