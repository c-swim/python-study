#각 자리 수의 합 출력
sum = 0
a=int(input())

while a>0:
    sum += a%10
    a = a//10

print(sum)