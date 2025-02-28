matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Remove last 2 columns using slicing
matrix = [row[:-2] for row in matrix]

# Print result
for row in matrix:
    print(row)
