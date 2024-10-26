import difflib

def compare_strings(s1, s2):
    s1_words = s1.split()
    s2_words = s2.split()

    # So sánh từng từ trong s1 và s2
    diff = difflib.ndiff(s1_words, s2_words)
    
    result_s1 = []
    result_s2 = []

    for word in diff:
        if word.startswith(" "):  # Không có sự thay đổi
            result_s1.append(word[2])
            result_s2.append(word[2])
        elif word.startswith("-"):  # Từ xuất hiện trong s1 nhưng không có trong s2
            result_s1.append(word[2])
            result_s2.append("_" * len(word[2]))
        elif word.startswith("+"):  # Từ xuất hiện trong s2 nhưng không có trong s1
            result_s1.append("_" * len(word[2]))
            result_s2.append(word[2])

    # Tạo lại chuỗi sau khi so sánh
    final_s1 = " ".join(result_s1)
    final_s2 = " ".join(result_s2)

    print(final_s1)
    print(final_s2)

# Ví dụ sử dụng
s1 = "she hung her clothes on wire hangers"
s2 = "she hunged her cloth on the metal"

compare_strings(s1, s2)

