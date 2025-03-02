#####################
# Dictionary python #
#####################

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

## Access dictionary elements
print(person["name"])
print(person["age"])

## Adding dictionary elements
person["job"] = "Engineer"
person[0] = "abc"
print(person)

## Remove key-value pair
del person["city"]
print(person) # Output: {'name': 'John', 'age': 30, 'job': 'Engineer'}

## Terating over a dicrionary
for key, value in person.items():
    print("{}: {}".format(key, value))
