#변수선언부분
answer, num1, num2, add = 0,0,0,0

#메인코드
num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
add = int(input(" *** 더할 숫자를 입력하세요 : "))
for i in range(num1, num2+1, add) :
    answer = answer+i
print("%d+%d+...+%d는 %d입니다. "%(num1, num1+add, num2, answer))