def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    
    if haystack == needle:
        return 0
    for i in range(1, len(haystack) - len(needle) + 1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1