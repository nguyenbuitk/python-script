#  List comprehensions in Python provide a concise way to create lists. They can be used to apply an expression to each item in an iterable, potentially filtering items based on a conditio

# Ex 1: Basic
squares = [x**2 for x in range(10)]
print(squares)

# Ex 2: Using with condition
test2 = [x for x in range(20) if x % 20 == 0 and x % 3 == 0]
print(test2)
