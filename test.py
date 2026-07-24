import random
from questions import q, questions

selected = random.sample(questions, 3)

score = 0
for question, answer in selected:
    if q(question, answer):
        score += 1

print(f'\n총 {len(selected)}문제 중 {score}문제 맞췄습니다.')