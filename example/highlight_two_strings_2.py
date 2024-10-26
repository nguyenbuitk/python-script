import difflib
import re

def tokenize(s):
    return re.split('\s+', s)
def untokenize(ts):
    return ' '.join(ts)

def equalize(s1, s2):
    
    l1 = tokenize(s1)
    l1_highlight = l1
    l2 = tokenize(s2)
    l2_highlight = l2 
    print("l1: ", l1)
    print("l2: ", l2)
    res1 = []
    res2 = []
    prev = difflib.Match(0,0,0)
    for match in difflib.SequenceMatcher(a=l1, b=l2).get_matching_blocks():
        if (prev.a + prev.size != match.a):
            for i in range(prev.a + prev.size, match.a):
                l1_highlight[i] = "\033[92m" + l1[i] +  "\033[0m"
                # ele = ["\033[91m" + '_' * len(l1[i]) + "\033[0m"]
                # ele = ['_' * len(l1[i])]

                # res2 += ele
            res1 += l1_highlight[prev.a + prev.size:match.a]
        if (prev.b + prev.size != match.b):
            for i in range(prev.b + prev.size, match.b):
                l2_highlight[i] = "\033[91m" + l2[i] +  "\033[0m"
                # ele = ['_' * len(l2[i])]
                # res1 += ele
            res2 += l2[prev.b + prev.size:match.b]
        res1 += l1[match.a:match.a+match.size]
        res2 += l2[match.b:match.b+match.size]
        prev = match

    return untokenize(res1), untokenize(res2)


def show_comparison(s1, s2, width=40, margin=10, sidebyside=True, compact=False):
    s1, s2 = equalize(s1,s2)

    print(s1)
    print(s2)


s3 = "she hung her clothes on wire hangers"
s4 = "she hanged her cloth on the metal "
print(s3)
print(s4)
print('Above-below comparison')
print('-------------------------------------------------------------------------------------')
show_comparison(s3, s4, sidebyside=False)
