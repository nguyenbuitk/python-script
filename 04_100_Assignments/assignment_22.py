"""
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string
    , age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.

Nếu đầu vào là:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Thì đầu ra sẽ là:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

def swap(a, b):
    temp = a
    a = b
    b = temp


res = []
while 1:
    s = input("Nhap thong tin: ")
    if not s:
        break
    res.append(s)

for i in range(0, len(res)):
    res[i] = res[i].split(',')

for i in range(0, len(res) - 1):
    for j in range(i + 1, len(res)):
        if res[i][0] > res[j][0]:
            res[i], res[j] = res[j], res[i]
        elif res[i][0] == res[j][0]:
            if int(res[i][1]) > int(res[j][1]):
                res[i], res[j] = res[j], res[i]
            elif int(res[i][1]) == int(res[j][1]):
                if int(res[i][2]) > int(res[j][2]):
                    res[i], res[j] = res[j], res[i]

for i in range(0, len(res)):
    res[i] = tuple(res[i])
print(res)

# Sample code
from operator import itemgetter, attrgetter
# Bài tập Python 22 Code by Quantrimang.com
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))