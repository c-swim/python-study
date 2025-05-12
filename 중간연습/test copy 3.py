#rectangle
# 사각형 A 좌표 입력
A=[]
#A의 xy쌍
for i in range(2):
    xy=[]
    #A의 x,y
    for j in range(2):
        n = int(input())
        xy.append(n)
    A.append(xy)
B=[]
#B의 xy쌍
for i in range(2):
    xy=[]
    #B의 x,y
    for j in range(2):
        n = int(input())
        xy.append(n)
    B.append(xy)

if (A[0][0] >= B[0][0] and A[0][0] <= B[1][0]) or (A[1][0] >= B[0][0] and A[1][0] <= B[1][0]):
    if (A[0][1] >= B[0][1] and A[0][1] <= B[1][1]) or (A[1][1] >= B[0][1] and A[1][1] <= B[1][1]):
        print(True)
    else:
        print(False)
else: print(False)