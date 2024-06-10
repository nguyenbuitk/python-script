animals = ['cat', 'dog', 'rabbit', 'dog']

# Basic usage
print(animals.index('dog'))

try: 
    print(animals.index('elephant'))
except ValueError:
    print("Values not found in the list")

print(animals)