def compare_unicode_strings(input_string, compare_string):
    return input_string.lower() == compare_string.lower()

# Nhập dữ liệu từ người dùng
user_input = input("Nhập một chuỗi: ")
print("user input: ", user_input.encode("utf-8"))

# Chuỗi để so sánh
compare_string = "đoạn văn"

# So sánh và in kết quả
result = compare_unicode_strings(user_input, compare_string)
if result:
    print("Chuỗi bạn nhập giống với 'đoạn văn'.")
else:
    print("Chuỗi bạn nhập không giống với 'đoạn văn'.")

