# defined using `def` keyword
# can access and modify by both instance and class variable

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self): # instance method
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.bark())