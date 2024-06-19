# Instance variable: each object of the class has its own copy

class Dog:
    species = "Cannie" # Class variable
    def __init__(self, name):
        self.name = name # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.name) # Output: Buddy
print(dog2.name) # Output: Max
print(dog1.species) # Output: Cannie
print(dog2.species) # Output: Cannie