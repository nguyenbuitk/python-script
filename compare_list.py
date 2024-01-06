###############
# List python #
###############

fruits = ["apple", "banana", "cherry", "orange", 20, [30,70]]





## Access list elements
print(fruits[0]) # output: apple
print(fruits[2]) # output: cherry

## Adding list item
fruits.append("mango")
print(fruits)

## Remove list item
fruits.remove("banana")
print(fruits)

# Iterating over a list
for fruit in fruits:
    print(fruit)

## Characteritics of list
### - Ordered: maintain the order of the data insertion
### - Changealbe: list is mutable and we can modify
### - Heterogeneous: list can container of different types