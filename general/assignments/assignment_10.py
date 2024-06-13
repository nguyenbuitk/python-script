"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
"""

# x là số dòng, y là số cột

x = int(input("Nhap X (dòng): "))
y = int(input("Nhap y (cột): "))

res = []

for i in range(x):
    element = []
    for j in range(y):
        element.append(i*j)
    res.append(element)

print(res)

# sample code
multilist = [[0 for col in range(y)] for row in range(x)]
# for row in range(x)
#   for col in range(y)
#       multilist[row][col] = 0

for row in range(x):
    for col in range(y):
        multilist[row][col] = row*col
print(multilist)




