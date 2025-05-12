#Self Study 6-7
#전역변수선언
i, k = 0, 0

#메인 코드
i=0
for i in range(9):
    if i<5:
        k=0
        for k in range(4-i):
            print('  ', end='')
        k=0
        for k in range(i*2+1):
            print('\u2605', end='')
    else:
        k=0
        for k in range(i-4) :
            print('  ', end='')
        k=0
        for k in range((9-i)*2-1) :
            print('\u2605', end='')
    print()
