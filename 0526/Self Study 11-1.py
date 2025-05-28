inFp = None
inStr = ""
num = 1
inFp = open("C:/Temp/data1.txt", "r", encoding='UTF8')

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d: %s" %(num,inStr), end= "")
    num += 1
    
inFp.close()