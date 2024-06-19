# Allow class attributes to be access as if they were public attributes while using getter and setter method internally
# Define using `@property` decorator.

class Dog:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self): # Getter
        return self._name
    
    @name.setter
    def name(self, name): # Setter
        self._name = name
        
dog = Dog("Buddy")
print(dog.name) 
dog.name = "Max"
print(dog.name)