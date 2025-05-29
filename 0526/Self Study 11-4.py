inFp, outFp = None, None
s_fName, t_fName = "", "" 
inStr = ""

s_fName = input("소스 파일명을 입력하세요: ")
t_fName = input("타깃 파일명을 입력하세요: ")

inFp = open(s_fName, "r")
outFp = open(t_fName, "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("--- %s 파일이 %s 파일로 복사되었음 ---" %(s_fName, t_fName))