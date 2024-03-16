"""
Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để
    kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
Các tiêu chí kiểm tra mật khẩu bao gồm:

1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12

Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng
    có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau
    bởi dấu phẩy.

Ví dụ mậ khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345
Thì đầu ra sẽ là: ABd1234@1
"""

s = input("Nhap ten nguoi dung: ")
elements = s.split(',')
res = []
for each_user in elements:
    flag = 0
    for j in each_user:
        if 'a' <= j <= 'z':
            flag += 1
            break

    for j in each_user:
        if '0' <= j <= '9':
            flag += 1
            break

    for j in each_user:
        if 'A' <= j <= 'Z':
            flag += 1
            break

    for j in each_user:
        if j == '$' or j == '#' or j == '@':
            flag += 1
            break

    if 6 <= len(each_user) <= 12:
        flag += 1
    if flag == 5:
        res.append(each_user)

print(','.join(res))

# Sample code
import re
value = []
items=[x for x in input("Nhập mật khẩu: ").split(',')]
# Bài tập Python 21, Code by Quantrimang.com
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))
