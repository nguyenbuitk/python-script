import random
import re
import unicodedata

def read_vocabulary(filename):
  vocabulary = []
  with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
      line = line.strip()
      if line:
        parts = line.split('(')
        if len(parts) < 2 :
          # print("not enough infor")
          continue
        else:
          english = parts[0].strip()
          phonetic = parts[1].split(')')[0].strip()
          vietnamese = parts[1].split(')')[1].strip()
          vocabulary.append((english,phonetic,vietnamese))
  return vocabulary

def check_answer(question, answer, is_english):
    # print(f"{answer}, {question[2]}" if is_english else "{answer}, {question[0]}")
    if is_english:
        return answer == question[2]
    else:
        return answer == question[0]

def print_vocabulary_list(vocabulary):
  print("English\tPornunciation\tTranslation")
  for word in vocabulary:
    print(f"{word[0]}\t{word[1]}\t{word[2]}")

def vocabulary_quiz(files):
  while True:
    print("Choose a file to practice vocabulary: ")
    for i, file in enumerate(files):
      print(f"{i + 1}. {file}")
    file_choice = int(input("Enter the number of file: ")) - 1
    if 0 <= file_choice < len(files):
      selected_file = files[file_choice]
    else:
      print("Invalid file choice. Please choose a valid file.")
      continue
    
    vocabulary = read_vocabulary(selected_file)
    
    # print_vocabulary_list(vocabulary)
    is_english = input("Choose the language (English or Vietnamese): ").strip().lower() == 'english'
    
    print("Dịch từ tiếng Anh sang tiếng Việt:" if is_english else "Translate from English to Vietnamese:")
    while vocabulary:
      question = random.choice(vocabulary)
      print(question[0] if is_english else question[2], end=": ")

      user_answer = input()
      # print("user input ", user_answer)
      if check_answer(question, user_answer, is_english):
          # print("Correct! Next question.\n")
          vocabulary.remove(question)
      else:
          print(f"Wrong! The correct answer is: {question[2] if is_english else question[0]}\n")

    continue_quiz = input("Do you want to continue (yes/no)? ")
    if continue_quiz.lower() != 'yes':
        break

if __name__ == '__main__':
    files = ['Voca_01.txt', 'Voca_02.txt']  # Thay thế danh sách tệp của bạn tại đây
    vocabulary_quiz(files)
