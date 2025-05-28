outFp = None
fName, outStr = "",""

fName = input("파일경로 입력 : ")
outFp = open(fName, "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + '\n')
    else:
        break;
outFp.close()
print("--- 정상적으로 파일에 씀 ---")