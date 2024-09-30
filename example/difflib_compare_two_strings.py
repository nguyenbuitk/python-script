from difflib import SequenceMatcher

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

print(similar('tackoverflow', 'stackoverflow'))
print(similar('h0t', 'hot'))
print(similar('The wall have an insulated layer for keep the house warm', 'The walls have an insulated layer to keep the house warm'))

