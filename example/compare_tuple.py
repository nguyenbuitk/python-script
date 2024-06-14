################
# Tuple Python #
################

# Define a tuple
person = ("John", 30, "New York")

# Access tuple elements
print(person[0])
print(person[1])

# Since tuples are immutable, we can't add or remove elements directly
# Instead, we can create a new tuple with the additional information
person_with_job = person + ("Engineer", )
print(person_with_job)

# We can remove an element by creating new tuple excluding the element
# Here, we remove the city by slicing the tuple
person_without_city = (person[0], person[1]) + person_with_job[3:]
print(person_without_city)

for item in person_with_job:
    print(item)