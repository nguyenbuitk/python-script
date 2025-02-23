import collections

def removeDuplicateLetters(s):
    stack = []
    dict = collections.Counter(s)
    
    for char in s:
        dict[char] -= 1
        if char in stack:
            continue
        while stack and char < stack[-1] and dict[stack[-1]] > 0:
            stack.pop()
            
        stack.append(char)
    return "".join(stack)

print(removeDuplicateLetters("cbacdcbc"))
