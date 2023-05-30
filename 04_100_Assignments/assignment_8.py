"""
Định nghĩa một lớp gồm có thuộc tính của lớp cùng tên với biến của instance
"""

# name ở (1) là Person.name, name ở (2) là instance.name.
# 2 biến name không liên quan đến nhau !
class Person:

    # Định nghĩa lớp "name"
    name = "Person"     # (1)
    def __init__(self, name=None):

        # self.name là biến của instance
        self.name = name    # (2)

john = Person()
john.name = "john"
print(f"{Person.name} name is {john.name}")

white = Person("white")
print(f"{Person.name} name is {white.name}")
