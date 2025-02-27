from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose_matrix = []
        for _ in range(cols):
            transpose_matrix.append([0]*rows)
            
        
        for i in range(rows):
            for j in range(cols):
                transpose_matrix[j][i] = matrix[i][j]
                
solution = Solution()
solution.transpose([[1,2,3],[4,5,6]])