"""Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng,
phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320."""

x = input()
if x != 0:
    j = 1
    for i in range(1, int(x)):
        j = i * j
    print(str(j))

# origin
x = int(input("Nhập số cần tính giai thừa:"))


def fact(k):
    if k == 0:
        return 1
    return k * fact(k - 1)


print(fact(x))
