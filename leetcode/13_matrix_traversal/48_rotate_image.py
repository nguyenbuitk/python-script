from typing import List

class Solution:
    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("")
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        self.print(matrix)
        converted = list(zip(*matrix))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = converted[i][n - j - 1]

    def rotate2(self, matrix):
        matrix.reverse()
        self.print_matrix(matrix)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                self.print_matrix(matrix)
        
    def print(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=',')
            print("")
solution = Solution()
solution.rotate2([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])