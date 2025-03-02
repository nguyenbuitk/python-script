def plusOne(digits):
    n = len(digits) - 1
    while n >= 0:
        val = digits[n] + 1
        if val < 10:
            digits[n] = val
            return digits
        elif val == 10:
            if n == 0:
                res = [1] + [0]*len(digits)
                return res
            else:
                digits[n] = 0
                n -= 1

print(plusOne([9,8,9]))
        