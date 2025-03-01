def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row < rows and col >= 0:
        print(matrix[row][col])
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            col += 1
        else: row -= 1
    return False

print(searchMatrix([[7,11,15],[8,12,19],[9,16,22]], 15))