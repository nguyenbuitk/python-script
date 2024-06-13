"""
Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ
    giao diện điều khiển. Định dạng nhật ký được hiển thị như sau:
D 100
W 200
(D là tiền gửi, W là tiền rút ra).
Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100
Thì đầu ra sẽ là:
500
"""
import sys


res = 0
while 1:
    s = input("Nhap thong tin: ")
    if s == "":
        break
    each_round = s.split(' ')
    if each_round[0] == 'D':
        res += int(each_round[1])
    else:
        res -= int(each_round[1])

print(res)

