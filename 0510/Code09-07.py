#함수
def func1():
    global a
    a = 10
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)

#함수 변수선언
a = 10

#메인
func1()
func2()