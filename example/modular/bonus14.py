from modular.parser import parse
from modular.converter import convert

user_input = input("Enter feet and inches: ")
parsed = parse(user_input)
result = convert(parsed["feet"], parsed["inches"])
print(result)

