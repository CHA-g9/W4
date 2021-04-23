#문자열 내장함수
'''
#덧셈
str = "멋쟁이사자처럼"
str2 = "은 좋은 동아리입니다"
print(str + str2)
#곱셈
print(str*3)
#인덱스 : 문자 하나하나에 번호를 단 것
print(str[0])
print(str[3])
print(str[4])
#슬라이싱 : 일부에 범위로 접근
#[x:y] = x번째 인덱스부터 y번째 인덱스 전까지
print(str[0:4])
print(str[1:4])
#내장함수
#길이 구하기 len 함수 : len(문자열변수)
print(len(str))
#특정 문자의 등장 횟수를 반환하는 함수 : str.count('특정문자')
print(str.count("사"))
#문자열을 특정 기준으로 나누는 함수 : str.split("특정문자")
print(str.split()) #공백을 기준으로 나누겠다 #결과는 리스트로 반환
print(str.split(','))
print(str.split("'"))
#특정문자의 인덱스 찾는 함수 : str.find() / str.index()
print(str.index('사')) #찾고자 하는 문자가 없을 때 오류
print(str.find('사')) #찾고자 하는 문자가 없을 때 -1 반환

#리스트 실습
li = [3,1,'배가',4,'고파요',5,1]
#인덱싱/슬라이싱
print(li[1])
print(li[2])
print(li[0:2])
print(li[0:3])
#리스트의 길이 구하기 : len(리스트변수)
print(len(li))
#리스트 변수 오름차순 정렬 : sort()
li2 = [3,1,4,5,1]
print(li2)
# print(li2.sort()) : 오류, 정렬된 리스트를 반환하지 않으므로 None 반환
li2.sort() #이렇게 쓰면 알아서 정렬
print(li2)
#리스트 내 특정원소의 인덱스 반환 : index()
li3 = [3,1,'움칫',4,'둠칫', 5,2,2,2,2]
print(li3.index("움칫"))
#리스트 내의 특정 원소 개수 세기 : count()
print(li3.count(2))

# 딕셔너리 실습
pairs = {"잔나비":"뜨거운 여름밤은 가고 남은 건 볼품없지만", "이무진":"산책", "홍크":"어쩌면"}
# 하나의 키와 벨류 쌍을 추가하는 방법 : 딕셔너리형 변수[키] = value
print(pairs)
pairs["스탠딩 에그"] = "오래된 노래"
print(pairs)
# 특정 키와 벨류 삭제하는 법 : del(변수[키])
del pairs["홍크"] # tuple에서도 쓰임
print(pairs)
# 키로 Value 얻기 : 변수.get(key) Django에서도 쓰인대영
jannabi = pairs.get("잔나비")
print(jannabi)
honk = pairs.get('홍크')
print(honk)
'''

#제어문(1) - 분기문
'''
제어문 : 코드의 흐름을 제어하는 코드.
이전까지는 무조건 순차적 실행만 했기 때문에 문제가 복잡했음
이에 조건에 따라 다른 문장을 수행하거나 반복하도록 지정하기로 함.

# if문 : 컴퓨터에게 선택의 여지와 조건을 부여하는 문장
예) 뭐먹지? -> 돈을 확인하자!
돈이 5000원 이상 -> 아웃백
3000원 이상 5000원 미만 -> 학식
3000원 미만 -> 편의점...

if () : 조건에 따라 실행할 문장
들여쓰기랑 :에 주의
'''
# 예제 1 : 85점 이상은 합격, 이하는 낙제
score = int(input("당신의 점수는 몇 점입니까? : "))
if(score >= 85):
    print("PASS")
else:
    print("FAIL")

# 예제 2
activity = input("당신의 동아리는 무엇입니까? : ")
if(activity == "멋쟁이사자처럼"):
    print("당신도 멋사?")
else :
    print("앟,,,")

# 예제 3 : 비교기준이 3개 이상인 경우(비효율ver.)
money = int(input("자, 얼마 있으세요? : "))
if (money >= 5000) :
    print("아웃백 가세이")
else:
    if(money >= 3000) : 
        print("학식 가세이")
    else :
        if(money >= 1000):
            print("편의점 가세이")
        else:
            print("굶자.")

# 예제 4 : 비교기준이 3개 이상인 경우(효율ver. feat.elif)
money = int(input("자, 얼마 있으세요? : "))
if (money >= 5000) :
    print("아웃백 가세이")
elif(money >= 3000) : 
    print("학식 가세이")
elif(money >= 1000):
    print("편의점 가세이")
else:
    print("굶자.")

# 제어문(2) - 반복문
'''
반복문의 종류 : for, while
# for 반복제어변수 in 반복대상 : 
#                   반복실행할 코드
반복대상 : 리스트, 튜플, 문자열 등 반복해서 연산할 어떤 대상
반복제어변수 : 하나하나 발로 뛰며 반복대상을 가져와 계산하는 변수

for number in [1,2,3,4,5,6,7,8,9,10]:
    sum+=number
    print(sum)
number -> 반복제어변수
리스트 -> 반복대상

반복대상으로 자주 쓰이는 함수 : range(x,y)
: x부터 y이전까지의 범위를 리스트로 반복하는 함수

# while (조건) : 
#        조건이 참일 동안 수행할 명령문

while(num>0):
    print("반복문 수행중!")
    num--
위 코드에서 num = 10일 경우 반복문 10번 반복 됨
조건이 참이면 무한 루프가 되는 것.
이에 억지로 중지시키기 위해서 사용하는 명령어가 바로 break.

while(condition1):
    code1
    if(condition2):
        break

컴퓨터에게 죽어라 반복하되, 여기서만 멈추는거야 ㅇㅋ? 형태로 이 조합을 자주 씀.
'''
# 함수
'''
프로그래밍 상에서 함수의 정의 : 코드를 기능으로 묶은 단위, 즉 코드의 기능 단위
정의 형태 : 
def func_nm(factor):
    code1
    code2
    return value

[함수가 필요한 이유 : Divide & Conquer]

인스타그램을 만든다고 생각해보자. 댓글, 좋아요, 사진 등의 무수한 기능을 하나의 코드로
쭉 짠다면 무수히 긴 코드가 생성될 것이고 에러 디버깅도 어려울 것이다.
이에 기능별로 함수로 묶어서 실행하면 쉬워질 것이다.
따라서 함수란, 엄청나게 길고 복잡한 코드를 기능별로 나누어서 
간단하고 짧고 단순하게 만들어주는 문법

함수를 많이 안 쓸 수록 바보 소리를 듣게 된다구.
되도록 함수 호출로만 이루어진 코드가 좋은 코드다. 
대신에 하나의 함수에 기능 몰빵할 생각은 하지 않는게 좋다.

[함수의 입구와 출구]

함수는 일종의 박스. 원인이 입력되면 결과가 나오는 구조.
원인이 되는 데이터를 인자, 결과로 나오는 데이터를 리턴 값이라고 함.
인자는 함수 호출, 정의 시 괄호 안에 들어감. 인자 개수는 개인의 자유. 없어도 무방.
리턴값은 함수가 제 기능을 다한 결과. 리턴 값은 언제나 하나! -> why?
함수의 존재 목적이 코드를 기능적으로 구분하는 것인데, 
결과가 이거일수도 있고, 저거일수도 있어요.
하면 안되기 때문!
리턴 값은 없을 수도 있음. 
예를 들면 종료함수의 경우나 단순 출력함수의 경우 그 역할만 하면 되므로
리턴 값이 있을 필요가 없음.

[함수의 안과 밖 : 변수의 범위]

함수 내부는 함수만의 세상. 
따라서 함수 안에서 변수를 정의하면 그 함수 안에서는 무한 사용 가능.
이것을 <지역변수>라고 함. 함수 바깥에서는 아무런 영향을 주지도 받지도 않음.

<지역변수>를 여러 함수에서 쓰고 싶다면?
안됨. 대신에 <전역변수>를 사용하면 됨. 
전역변수는 코드 전체의 영역에서 영향력을 갖는 함수이기 때문.

그러나, 전역변수는 웬만하면 쓰지 않는 게 좋음.
실제로 코딩할 때는 지역변수를 압도적으로 많이 사용하게 됨.
함수 선언은 코드로 영역구분 하는 것과 똑같음.
그런데 전역변수가 나타나서 설치면 함수의 존재 목적이 흐려지게 되므로!!!!
지역변수를 주로 사용하되, 전역변수가 있음을 알아두기만,,하자..

'''
