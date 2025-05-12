Ax1 = int(input())
Ay1 = int(input())
Ax2 = int(input())
Ay2 = int(input())
Bx1 = int(input())
By1 = int(input())
Bx2 = int(input())
By2 = int(input())

if (Ax1 <= Bx1 and Bx1 <= Ax2) or (Ax1 <= Bx2 and Bx2 <= Ax2) :
    if (Ay1 <= By1 and By1 <= Ay2) or (Ay1 <= By2 and By2 <= Ay2) :
        print(True)
    else : print(False)
else: print(False)