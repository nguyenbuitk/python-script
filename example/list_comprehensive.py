#  List comprehensions in Python provide a concise way to create lists. They can be used to apply an expression to each item in an iterable, potentially filtering items based on a conditio

# Ex 1: Basic
squares = [x**2 for x in range(10)]
print(squares)

# Ex 2: Using with condition
test2 = [x for x in range(20) if x % 20 == 0 and x % 3 == 0]
print(test2)
test3 = []
for x in range(20):
    if x % 20 == 0 and x % 3 == 0:
        test3.append(x)
print(test3)
# Ex 3: Using list comprehensive for replace
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
l = ['Shardul' if name == 'Hardik' else name for name in l]
print(l)

# Ex 4: Using in matrix
board = [[]]
path = [board[i][j] for i in range(1,3) for j in range(1,3)]
## Equal to
path = []
for i in range(1,3):
    for j in range(1,3):
        path.append(board[i][j])
        
        