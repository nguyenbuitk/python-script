def addBinary(a, b):
    if len(a) > len(b):
        b = "0"*(len(a) - len(b)) + b
    else:
        a = "0"*(len(b) - len(a)) + a
        
    carry = 0
    n = len(a) - 1
    res = [0] * len(a)
    while n >= 0:
        val = int(a[n]) + int(b[n]) + carry
        if val < 2:
            res[n] = val
            carry = 0
        elif val == 2:
            res[n] = 0
            carry = 1
        elif val == 3:
            res[n] = 1
            carry = 1
        if n == 0 and carry:
            res = [1] + res
        n -= 1
    
    return str("".join(map(str, res)))

print(addBinary("101", "11"))