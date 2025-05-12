#shift 연산자
    # a*-1/2
    a>>1
    # a*2
    a<<1

#bin,oct,hex
bin(), oct(), hex()
a=int(a,2)
b=int(b,8)
c=int(c,16)

#삼항연산자
"true" if a>0 else "false"

#eval?
eval(str) #문자열 그대로 실행

#list 값 변경
list=[10,20,30]
list[1:2] = [200,201]
# 결과: [10,200,201,30]
list[1:2] = []
# 결과: [10,201,30]

#list
del(list[1])
del(list)
list.append()
list.pop()
list.sort()
list.reverse()
list.index()
list.insert()
list.remove()
list.extend()
list.count()
list.clear()
del(list)
len(list)
list.copy()
sorted(list)

#tuple
tuple=(10,)
tuple=10,

#dictionary
dict={key:value}
dict={'학번','이름','학과'} #키값만 설정
dict['학번']="20240877" #값 넣어주기
dict.get('학번') #키 값 찾기 가능 (**없을지도 모르는 키 찾을 때 사용)
dict.keys() #모든 키 반환, value도 동일 .values()
list(dict.keys()) #키 값만 출력
dict.items() #튜플형태로 출력
'학번' in dict #T/F 값

#import operator 의 경우
sorted(list,key = operator.itemgetter(0 or 1))

#set
set={1,2,2,3,4,5,1} #교집합, 차집합, 합집합, 대칭 차집합(^)가능.

#컴프리헨션
A = [num for num in range(5) if num > 0]

#zip() 두리스트를 묶음
for i,j in zip(ii,jj):
    print(i,'>',j)
list(zip(i,j)) #리스트안에 (튜플)
dict(zip(i,j)) #딕셔너리 {i:j}

#문자열
a.upper()
a.lower()
a.swapcase()
a.title()

a.count()
a.find() #r 있음
a.index() #r 있음
a.startswith()
a.endswith()

a.strip() #r,l 옵션 있음. 없으면 기본 공백 양쪽 제거.