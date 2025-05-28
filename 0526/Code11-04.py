inFp = None
inList, inStr = [],""

inFp = open("C:/temp/data1.txt", "r")

inList = inFp.readlines()
for i in inList :
    print(inStr, end = '')

inFp.close()