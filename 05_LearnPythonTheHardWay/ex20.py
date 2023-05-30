# in_file_name là chuỗi, là tên file, không liên quan gì đến file
# in_file mới là file
def create_file(in_file_name):
    in_file = open(in_file_name, 'w+')
    in_file.write("Hello, my name is Nguyen\n")
    in_file.write("I'm 20 years old\n")
    in_file.write("I'm learning python for 2 days\n")
    return in_file


def print_all(in_file):
    print(in_file.read())


def rewind(f):
    f.seek(0)
    

def print_line(linecount, f):
    print(f"Line {linecount}: {f.readline()}",end = '')


name_file = input("Input file name: ")

file = create_file(name_file)

print("Data in file: ")
print_all(file)

rewind(file)
print_line(1, file)
print_line(2, file)
print_line(3, file)
