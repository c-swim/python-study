#Self Study 6-5
hap = 0
a,b = 0,0

while True:
    a = input("더할 첫 번째 수를 입력하세요 : ")
    if a == '$' :
        break
    a=int(a)
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a+b
    print("%d + %d = %d" %(a,b,hap))
    
print("$을 입력해 반복문을 탈출했습니다.")

#질문필요 > 언제든지 $를 입력하는 것인가 a에 $를 입력해야하는 것인가
