#팩토리얼 값을 구하는 함수
def factorial(num):
    if num <= 1:
        return num
    else:
        return num*factorial(num-1)
print(factorial(4))
print(factorial(10))