# Defined using `@staticmethod` decorator
# Do not take `self` or `cls` as first parameter.
# Can not access or modify instance or class variables.
# Typicall used to  utility functions

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3,5))