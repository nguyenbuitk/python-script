"""
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó
thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
"""

s = input("input string: ")
res = s.split(',')
res.sort()
print(f"After sort: {','.join(res)}")

# Sample code
items = [x for x in input("Nhập một chuỗi: ").split(',')]
print(items)
items.sort()
print(','.join(items))
