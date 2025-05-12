#별 마름모
i,k = 0,0
while i<9:
    #윗줄
    if i<5:
        #공백
        k=0
        while k<(4-i):
            print(" ",end="")
            k += 1
        #별
        k=0
        while k<i*2+1:
            print("*",end="")
            k += 1
    #아래줄 i=5부터 시작
    else:
        #공백
        k=0
        while k<i-4 :
            print(" ",end="")
            k += 1
        #별
        k=0
        while k<(8-i)*2+1:
            print("*",end="")
            k += 1
    i += 1
    print()
        