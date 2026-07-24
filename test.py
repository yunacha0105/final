import random
from questions import q, questions
from result import result

def play_round(question_list):
    wrong = []
    score = 0

    for question, answer in question_list:
        if q(question, answer):
            score += 1
        else:
            wrong.append((question, answer))

    return score, wrong


# 첫 도전
remaining = random.sample(questions, 3)
total_count = len(remaining)
total_score = 0

score, wrong = play_round(remaining)
total_score += score
result(total_score, total_count)   # ← 여기서 "맞춘 개수 + 등급" 둘 다 출력됨

# 재도전 (틀린 문제만)
while wrong:
    retry = input('\n틀린 문제 다시 풀어보시겠습니까? (y/n): ')
    if retry.strip().lower() != 'y':
        break

    print(f'\n틀린 {len(wrong)}문제 재도전합니다.\n')
    score, wrong = play_round(wrong)
    total_score += score
    result(total_score, total_count)

print('\n게임을 종료합니다.')