#################
# Set in Python #
#################

# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5} (Order may vary)

# Create empty set
num = set()

# Adding elements to a set
numbers.add(6)
numbers.add(3)  # Duplicate value will be ignored
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
numbers.remove(2)  # Removes '2' from set
print(numbers)  # Output: {1, 3, 4, 5, 6}

# Checking if an element exists
print(4 in numbers)  # Output: True
print(10 in numbers) # Output: False

# Iterating over a set
for num in numbers:
    print(num)

# Set Operations
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}

union_set = evens.union(odds)  # Combines both sets
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = numbers.intersection(evens)
print("Intersection:", intersection_set)  # Output: {4, 6}

difference_set = numbers.difference(evens)
print("Difference:", difference_set)  # Output: {1, 3, 5}

