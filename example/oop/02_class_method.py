# Defined using `@classmethod` decorator
# The first parameter is alwasy 'cls', which refers to the class itself
# Can access and modify class variables.

class Dog:
    species = "Canine"
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

Dog.change_species("Canidae")
print(Dog.species)