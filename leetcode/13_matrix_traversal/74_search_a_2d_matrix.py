def searchMatrix(matrix, target):
    for row in matrix:
        l, r = 0, len(row) - 1
        # binary search on each row
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target: 
                return True
            if row[mid] < target:
                l = mid + 1
            else: r = mid - 1
        
        # if target is larger than the last element in the row, skip this row
        if row[-1] > target:
            return False
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34))