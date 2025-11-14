'''
The @staticmethod decorator in Python is used to declare a method within a class as a static method, which means that it can be called without creating an instance of the class. Static methods do not receive the special first argument self, which is a reference to the instance. They behave like regular functions but belong to the class's namespace

Using when not dependent on class or instance
'''

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

result = MathOperations.add(5, 3)
print(result) # Output: 8


# example_2
class Person:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    # age needs access self.year_of_birth -> can't be static
    def age(self, current_year):
        return current_year - self.year_of_birth

    # is_adult only need input -> does not using self -> static_method is reasonable
    @static_method
    def is_adult(age):
        return age >= 18
