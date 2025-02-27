# zip() in python is used to combine multiple iterables (list, tuples, etc) together in to an iterator containing tuples corresponding to the position.
# How zip() works
#  - Concetenate elements by postion from different iterables
#  - Stop when the shortest iterable runs out of element

# Example
a = [1, 2, 3]
b = [10, 20, 30]
x = zip(a, b)

print(list(x))
# [(1, 10), (2, 20), (3, 30)]

# Using zip to get column in 2D matrix
matrix = [
    [1,2,3,4],
    [4,5,6,8],
    [7,8,9,10]
]

columns = list(zip(*matrix))
print("==== column ====")
print(columns)

print("==== matrix_2 ====")
matrix_2= [[0]*len(columns[0]) for _ in range(len(columns))]

for i in range(len(columns)):
    for j in range(len(columns[0])):
        pass
print(matrix_2)
# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# Why zip(*matrix) can get the column?
#  - *matrix (unpacking) will unzip the matrix into indivdual rows as parameters to zip()
#  - zip() then groups elements that have the same position in each row -> which are the columns of the matrix