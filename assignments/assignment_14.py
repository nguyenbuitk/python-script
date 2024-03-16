"""
Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy,
    kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách
    bởi dấu phẩy.
Ví dụ đầu vào là: 0100,0011,1010,1001
Đầu ra sẽ là: 1010
"""

# s = input("Nhap vao chuoi: ")
s = "0100,0011,1010,1001"
res = []
elements = s.split(',')
for i in elements:
    dec = 0
    for j in range(0, len(i)):
        dec += int(i[j])*(2**((len(i)-1) - int(j)))
    if not dec % 5:
        print(dec)
        res.append(i)

print(res)

# Sample code
value = []
items = [x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)
# Bài tập Python 14, viết bởi Quantrimang.com
print(','.join(value))
