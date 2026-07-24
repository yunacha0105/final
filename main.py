from test import test

attendance = input('''리눅스 시험을 시작합니다.
참가하시겠습니까? y / n : ''')

if attendance == 'y':
    test()
else:
    print('시험을 종료합니다.')