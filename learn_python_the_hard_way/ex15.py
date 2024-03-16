# open file:    txt = open(filename)    (auto mode = 'r' (only read))
# read file:    read_txt = txt.read()
from sys import argv

script, filename = argv
txt = open(filename)
print(f"Here's you file {filename}")
print(txt.read())

print("Type the file again")
file_again = input("> ")
txt_again = open(file_again)

print (txt_again.read())