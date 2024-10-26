import difflib

l1 = ["she", "hung", "her", "clothes"]
l2 = ["she", "hunged", "her", "cloth"]

matcher = difflib.SequenceMatcher(a=l1, b=l2)
matching_blocks = matcher.get_matching_blocks()

for match in matching_blocks:
    print("type of match", type(match))
    print(f"Matching block: start in l1: {match.a}, start in l2: {match.b}, size {match.size}")


print(matching_blocks)