'''
The @staticmethod decorator in Python is used to declare a method within a class as a static method, which means that it can be called without creating an instance of the class. Static methods do not receive the special first argument self, which is a reference to the instance. They behave like regular functions but belong to the class's namespace
'''

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

result = MathOperations.add(5, 3)
print(result) # Output: 8