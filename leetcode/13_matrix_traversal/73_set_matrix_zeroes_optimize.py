class Solution:
    def printMatrix(self, matrix):
        for row in matrix:
            print(row)
        print("")
    def setZeroes(self, matrix):
        self.printMatrix(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        first_col_has_zeros = False
        first_row_has_zeros = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_zeros = True
                    if j == 0:
                        first_col_has_zeros = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        self.printMatrix(matrix)
        
        for i in range(1, cols):
            if matrix[0][i] == 0:
                for j in range(rows):
                    matrix[j][i] = 0
                
        self.printMatrix(matrix)
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] =0 
        print(first_col_has_zeros)
        if first_col_has_zeros:
            for i in range(rows):
                matrix[i][0] = 0
        if first_row_has_zeros:
            for i in range(cols):
                matrix[0][i] = 0
        self.printMatrix(matrix)


solution = Solution()
solution.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])