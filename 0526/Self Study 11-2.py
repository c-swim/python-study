inFp = None
inList, inStr = [],""
num = 1

with open("C:/temp/data1.txt", "r", encoding="utf-8") as inFp:
    inList = inFp.readlines()
    for inStr in inList :
        print("%d: %s" %(num,inStr), end= "")
        num += 1
        