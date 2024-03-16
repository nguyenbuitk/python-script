print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehen passion from intuition
and requirs an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates


start_point = 1000 
beans, jars, crates = secret_formula(start_point)
print(f"With a starting point of: {start_point}")
print(f"We'd have {beans} beans, {jars} jars, {crates} crates")

