"""Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và
một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""


def split_string():
    result = []
    str_split = input("input a string: ")
    l = len(str_split)
    print(l)
    j = 0
    element = ''
    for i in range(0, l):
        if str_split[i] != ',':
            element += str_split[i]
        else:
            result.append(element)
            element = ''
    result.append(element)
    return result


res = split_string()
print(res)
print(tuple(res))

# Sample code
values = input("Nhập vào các giá trị:")
l = values.split(",")   # l là list
t = tuple(l)            # chuyển từ list sang tuple
print(l)
print(t)


