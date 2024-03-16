# Begin function with "def"
# The difference from C++ is ":" character instead of "{}"
# Remember indenting all line in function

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("arg1:", arg1, ", arg2: ", arg2)


print_two("hello", "nguyen")
