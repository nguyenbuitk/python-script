# one element in dics (called hashs in some language) is tuple (keys: value)
# dics don't have order like list and this is the difference
from textwrap import dedent
from random import randint
from textwrap import dedent
stuff = {'Name': 'Nguyen', 'Age': '18', 'Height': '175'}
stuff[1] = '34'
stuff[2] = 'Hello'          # insert in last dics
stuff[2] = 'Hellsdso'       # dict can't have two keys, so it del the key before and add new key
print(stuff)
del stuff[1]
print(f"stuff after delele {stuff}")

print(dedent("""
    sdaflkdsjaf
    sladkfjasdlkf
    """))
