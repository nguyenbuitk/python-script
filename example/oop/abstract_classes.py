# An abstract class can be considered a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.

from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triagle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
        
# Driver code
R = Triagle()
R.noofsides()
K = Pentagon()
K.noofsides()