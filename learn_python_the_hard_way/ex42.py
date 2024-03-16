"""
Bạn sử dụng cụm từ 'is-a' khi bạn nói về những đối tượng và lớp được tham chiếu tới nhau
bằng mối quan hệ lớp. Bạn sử dụng has-a khi bạn nói về những đối tượng và lớp được chỉ liên quan bởi
vì chúng chỉ tham chiếu tới nhau.

Tóm lại:is-a tham chiếu bằng quan hệ lớp
        has-a chỉ tham chiếu tới nhau
"""

# Animal is-a object        (class Animal và object object tham chiếu bằng mối quan hệ lớp)


class Animal(object):
    pass


# Dog is-a Animal        (class Dog và object Animal tham chiếu bằng mối quan hệ lớp (class Dog và class Animal))


class Dog(Animal):
    def __init__(self, name):             # self giống this trong C++ ?
        # Dog has name       (class Dog và object name tham chiếu tới nhau)
        self.name = name    
        
# Cat is-a Animal


class Cat(Animal):
    def __init__(self, name):
        # Cat has name
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has name
        self.name = name
        # Person has pet of some kind
        self.pet = None

# Employee is-a object
class Employee(Person):
    def __init__(self, name, salary):
        # What is this strange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass
 
# Salmon is-a Fish
class Salmon(Fish):
    pass
 
# Halibut is-a object
class Halibut(Fish):
    pass

# Đặt rover là một thể hiện của class Dog, thứ mà has-a thuộc tính tên đặt là Rover.
# class Dog được gọi với các tham số "self" và Rover
# rover has-a tên thuộc tính đặt là Rover
rover = Dog("Rover")

# satan has-a tên thuộc tính đặt là Satan
satan = Cat("Satan")

# mary has-a tên thuộc tính đặt là Person
mary = Person("Mary")

# từ mary, lấy thuộc tính pet và đặt là satan
mary.pet = satan

# frank is-a Emplopyee has-a thuộc tính tên là Frank và lương là 120000
frank = Employee("Frank", 120000)

# thuộc tính pet của frank is-a rover
frank.pet = rover

# flipper is-a thể hiện của Fish
flipper = Fish()

# crouse is-a thể hiện của Salmon
crouse = Salmon()

# harry is-a thể hiện của Halibut
harry = Halibut()