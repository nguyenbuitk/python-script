"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""

s = input("Nhap chuoi: ")
so_chu_cai, so_chu_so = 0, 0
for i in range(0,len(s)):
    if '0' <= s[i] <= '9':
        so_chu_so += 1
    elif 'a' <= s[i].lower() <= 'z':
        so_chu_cai += 1
    else:
        pass
print("Số chữ cái là: ", so_chu_cai)
print("Số chữ số là: ", so_chu_so)

# Sample code
s = input("Nhập câu của bạn: ")
# Bài tập Python 16, Code by Quantrimang.com
d = {"DIGITS": 0, "LETTERS": 0}
for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("Số chữ cái là:", d["LETTERS"])
print("Số chữ số là:", d["DIGITS"])
