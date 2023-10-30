vocabulary = []

with open('Voca_01.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # Loại bỏ khoảng trắng dư thừa từ đầu và cuối dòng
        if not line:
          
            continue  # Bỏ qua dòng trống

        # Tách thông tin từ dòng sử dụng dấu ngoặc đơn (') và dấu ngoặc kép (")
        parts = line.split("(")
        if len(parts) < 2:
            print("not enough infor")
            continue  # Bỏ qua dòng không đủ thông tin
        else: 
            english = parts[0].strip()
            phonetic = parts[1].split(')')[0].strip()
            vietnamese = parts[1].split(')')[1].strip()
            if vietnamese == "":
              continue
            else:
              vocabulary.append((english, phonetic, vietnamese))

# In ra kết quả
for entry in vocabulary:
    print("English:", entry[0])
    print("Phonetic:", entry[1])
    print("Translation:", entry[2])
    print()

