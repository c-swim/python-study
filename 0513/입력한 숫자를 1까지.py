#입력한 숫자를 1까지...
def count(num):
    if num >= 1 :
        print(num, end=' ')
        count(num-1)
    else:
        return
count(10)
count(20)