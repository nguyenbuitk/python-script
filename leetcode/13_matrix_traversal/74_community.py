def searchMatrix(matrix, target: int):
    rows = len(matrix)
    cols = len(matrix[0])
    l, r = 0, rows*cols - 1
    while l <= r:
        mid = (l+r)//2
        if matrix[mid//cols][mid%cols] == target:
            return True
        if matrix[mid//cols][mid%cols] < target:
            l = mid + 1
        else: r = mid - 1
    return False