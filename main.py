print('Welcome to Computer Quiz!')

playing = input('Do you want to play? [y/n] ')

if not(playing.lower() == 'y' or playing.lower() == 'yes'):
  print('Okay, come back later!')
  quit()
else:
  print("Okay, let's move then!")

score = 0

questions = [
  {
    "question": "1. What does CPU stand for? ",
    "answer": "central processing unit"
  },
  {
    "question": "2. What does GPU stand for? ",
    "answer": "graphics processing unit"
  },
  {
    "question": "3. What does RAM stand for? ",
    "answer": "random access memory"
  },
  {
    "question": "4. What does PSU stand for? ",
    "answer": "power supply"
  },
]

for element in questions:
  answer = input(element["question"])
  if answer.lower() == element["answer"]:
    print('Correct!')
    score += 1
  else:
    print('Wrong!')

print(f'You got correct {score} out of {len(questions)} questions')
print(f'You got {score / len(questions) * 100}%')