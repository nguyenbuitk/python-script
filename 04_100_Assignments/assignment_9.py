"""
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ:
Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 50, H là 30.
D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân
cách bằng dấu phẩy.

Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
"""

import math

def calculate():
    res = []
    c, h = 50, 30
    s = input("Nhap vao mot chuoi so: ")
    list_ele = s.split(",")
    for i in list_ele:
        res.append(str(int((math.sqrt((2*c*(int(i)))/h)))))
    return res

res = calculate()

print(",,".join(res))



