# copy data from file to another file!

name_file_read = input("File read name: ")
name_file_write = input("File write name: ")

file_read = open(name_file_read)
file_write = open(name_file_write, 'w')

file_write.write(file_read.read())

file_read.close()
file_write.close()