import json
with open('questions.json', 'r') as file:
    content = file.read()
    data = json.loads(content)
print(type(content))
print(type(data))

score = 0
for question in content:
    print(question['question_text'])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    
    user_choice = int(input("Enter your answer: "))
    if user_choice == question['correct_answer']:
        score += 1
        
# Print final score
print(f"Score: {score}/{len(data)}")