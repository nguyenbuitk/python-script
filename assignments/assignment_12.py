"""
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng
này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:
Hello world
Practice makes perfect
Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

sentences = []
print("Nhap vao cac dong: ")
while 1:
    s = input()
    if s:
        sentences.append(s)
    else:
        break

for x in sentences:
    print(x.upper())

