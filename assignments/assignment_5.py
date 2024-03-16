"""
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM
"""

class InChuoi:
    chuoi_nhap = ""
    def __init__(self):
        # self.chuoi_nhap = chuoi_nhap
        pass

    def get_string(self):
        self.chuoi_nhap = input("Nhap mot chuoi: ")

    def print_string(self):
        print(self.chuoi_nhap.upper())

def kiem_tra():
    a = InChuoi()
    a.get_string()
    a.print_string()

kiem_tra()

# Sample Code
class OutString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Please input string: ")

    def print_string(self):
        print(self.s.upper())

t = OutString()
t.get_string()
t.print_string()
