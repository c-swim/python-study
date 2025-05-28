#2행과 3행을 합친 코드
list1 = [1,2,3,4]
list2 = [10,20,30,40]
hapList = list(map(lambda n1,n2 : n1+ n2, list1, list2))
print(hapList)