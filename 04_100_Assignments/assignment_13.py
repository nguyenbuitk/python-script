"""
Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng,
    loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
Giả sử đầu vào là: hello world and practice makes perfect and hello world again
Thì đầu ra là: again and hello makes perfect practice world
"""

s = input("Nhap chuoi: ")
element = s.split(' ')
res = []
for word in element:
    flag = 0
    for k in res:
        if word == k:
            flag = 1

    if flag == 0:
        res.append(word)

res.sort()
print(' '.join(res))

# Sample code
s = input("Nhập chuỗi của bạn: ")

# words = [word for word in s.split(" ")
# <=> words = s.split(" ") :D
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
