#Code05-07.py
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("B")
        else:
            if score >= 60:
                print("C")
            else:
                print("F")
print("학점입니다. ^^")
