# '&'.join(list): add '&' between two elements of list.
# list.pop(): get last element of list.

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait, not enough ten things")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Friss", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    stuff.append(more_stuff.pop())
    
print("stuff after append: ")
print(stuff)

new_stuff_1 = ' '.join(stuff)
print(new_stuff_1)

new_stuff_2 = '#%'.join(stuff)
print(new_stuff_2)