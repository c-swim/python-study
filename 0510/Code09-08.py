#함수
def func1():
    result = 100
    return result

def func2():
    print("반환값이 없는 함수 실행")

#전역변수
hap = 0

#메인
hap = func1()
print("func1()에서 돌려준 값 ==> %d" %hap)
func2()