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


def test():
    total_score = 0
    total_count = 0
    wrong = []

    while True:
        if wrong:
            print(f'\n틀린 {len(wrong)}문제 재도전합니다.\n')
            round_questions = wrong
        else:
            print('\n새 문제 3개를 출제합니다.\n')
            round_questions = random.sample(questions, 3)

        round_score, wrong = play_round(round_questions)
        total_score += round_score
        total_count += len(round_questions)

        result(total_score, total_count)

        retry = input('\n다시 풀어보시겠습니까? (y/n): ')
        if retry.strip().lower() != 'y':
            break

    print('\n게임을 종료합니다.')