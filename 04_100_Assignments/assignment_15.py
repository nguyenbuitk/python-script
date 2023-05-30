"""
Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất
    cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy,
    trên một dòng.
"""

res = []
for i in range(1000, 3001):
    s = str(i)
    flag = 0
    for j in s:
        if int(j) % 2:
            flag = 1
    if not flag:
        res.append(s)

print(','.join(res))

# Sample code
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)
# Bài tập Python 15, Code by Quantrimang.com
print(",".join(values))
