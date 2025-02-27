class Solution:
    def setZeroes(self, matrix):
        col = set()
        row = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for r in row:
            for j in range(cols):
                matrix[r][j] = 0
        for i in range(rows):
            for c in col:
                matrix[i][c] = 0
        print(matrix)

solution = Solution()
solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])