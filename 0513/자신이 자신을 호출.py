#자신이 자신을 호출
def selfCall():
    print('하',end='')
    selfCall()
selfCall()