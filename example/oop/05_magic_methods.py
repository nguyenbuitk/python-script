# Special methods with double underscores at the beginning and end (e.g., `__init__`, `__str__`, `__repr`__)
# Allow customization of class behavior (e.g., initialization, string representation, operator overloading)

class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self): # Magic method for string representation
        return f"Dog(name={self.name})"

dog = Dog("Buddy")
print(dog)