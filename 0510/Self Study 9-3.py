#함수 선언
def para_func(*arg):
    result = 0
    for i in arg:
        result += i
    return result

#전역변수
hap = 0

#메인
hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para_func(10,20,30,40,50,60,70,80,90,100)
print("매개변수가 10개인 함수를 호출한 결과 ==> %d" % hap)
