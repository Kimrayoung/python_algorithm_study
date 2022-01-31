#-*- coding: utf-8 -*-
#기본 숫자함수

print(abs(-5)) #5 (절대값)
print(pow(4,2)) #4^2 = 16 (제곱)
print(max(5,2,3,4,1)) #5(최대값)
print(min(3,4,1,43)) #1(최소값)
print(round(3.14)) #반올림

from math import *
print(floor(4.9)) #내림
print(ceil(4.14)) #올림
print(sqrt(16)) #제곱근(4)

#랜덤함수
from random import *
print(random()) #0.0이상 1.0미만의 임의의 값을 생성
print(random() * 10) #0.0이상 10.0미만의 임의의 값을 생성
print(int(random() * 10)) #0부터 10미만의 임의의 값을 생성
print(int(random() * 10) + 1) #1부터 10이하의 임의의 값을 생성
print(int(random() * 45) + 1) #1부터 45이하의 임의의 값을 생성
print(randrange(1, 46)) #1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) #1 ~ 45이하의 임의의 값을 생성(두 숫자를 모두 포함)

#연산자 퀴즈
from random import *
day = int((random() * 24) + 4)
# day = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ' +str(day) + '로 선정되었습니다')


#문자열
from calendar import c
from re import M


sentance = '나는 소년입니다.'
print(sentance)
sentance2 = "파이썬은 쉬워요"
print(sentance2)
sentance3 = '''
나는 소년이고
파이썬은 쉬워요
'''
print(sentance3)


#문자열 슬라이싱(필요한 정보만 잘라서 사용하는 것을 의미함)
jumin = "990103-1234566"

print("성별: " + jumin[7])
print('연 : ' + jumin[0:2]) #0부터 2직전까지(0,1번째 값만 가지고 옴)
print("월 : " + jumin[2:4]) #2부터 4직전까지 
print("일 : " + jumin[4:6])
print("생년월일: " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리: " + jumin[7:]) #7부터 마지막까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨뒤 7번째 부터 끝까지

#문자열 처리함수
python =  "Python is Amazing"
print(python.lower()) #전부다 소문자로 출력
print(python.upper()) #전부다 대문자
print(python[0].isupper()) #python이라는 문자열의 첫번째 문자가 대문자인지
print(len(python)) #파이썬의 전체 길이
print(python.replace("Python","Java")) #python이라는 문자열에서 python이라는 단어를 찾아서 java로 바꿔줌
index = python.index("n") #python이라는 단어안에서 n이라는 단어가 몇번째에 위치하는지 알려줌
print(index) #5
index = python.index("n", index + 1) #5에서 부터 다음 n이 몇번째에 있는지
print(python.find("n")) #5, python이라는 단어안에서 n이라는 단어가 몇번째에 있는지
print(python.find("java")) #-1 출력(원하는 값이 없으면 -1출력)
print(python.index("java")) # 에러 발생 (원하는 값이 없으면 오류가 나오고 프로그램 종류)
print(python.count("n")) #python이라는 단어에서 n이 몇번 나오는지

#문자열 포맷
#방법1
#%d에는 항상 숫자만 들어감 -> 정수
print("나는 %d살 입니다." % 20) #%d자리에 20이라는 숫자를 대입

#%s에는 문자열이 들어감 -> 문자열
print("나는 %s을 좋아합니다" % "파이썬")
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

#%c는 한 글자만 받겠다(char) -> 한글자
print("apple은 %c로 시작해요" % "a")

#방법2
print("나는 {}살입니다" .format(20)) #format의 ()에 있는 단어를 {}에 넣게됨
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
#순번에 맞게 출력하기
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))  #{1}에는 첫번쨰를 인자를 넣겠다 {0}에는 두번째 인자를 넣겠다

#방법3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color= "빨간"))

#방법4(v.3.6 ~)
age = 20
color = "빨강색"
print(f"나는 {age}살이며, {color}색을 좋아해요" )


#탈출문자
#\n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

#\"  혹은 \' : 문장내에서 따옴표처럼 사용
print("저는 '나도 코딩'입니다.")
print("저는 \'나도코딩\'입니다") 

#\\ : 문장내에서 \
#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

#\b : 백스페이스(한글자 삭제)
print("Redd\bApple") #RedApple

#\t : tab
print("Red\tApple") #Red    Apple

#문자열 퀴즈(내 풀이)
url_string = 'http://naver.com'
findhttp = url_string.find("//")
findfinal = url_string.find(".")
finalstring = url_string[findhttp+2:findfinal]
first_three_string = finalstring[0:3]

count_e = url_string.count("e")
length = len(finalstring)

print(findhttp,first_three_string, count_e, length)
print(first_three_string+str(length)+str(count_e)+'!')

#문자열 퀴즈(강사님 풀이)
# url = 'http://naver.com'
url = "http://youtube.com"
my_str = url.replace('http://','') #http://을 찾아서 ''(빈 문자열)로 변경하겠다
my_str = my_str[:my_str.index(".")] #문자열을 자를건데 처음부터 my_str에서 처음으로 .이 나오는 위치까지
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"

print("{0}의 비밀번호는 {1}입니다." .format(url,password))
# print(f"{url}의 비밀번호는 {password}입니다.")


#리스트(순서가 있는 객체의 집합) []

subway = ['yoo','jo','park']
print(subway)
print(subway.index('park'))
#리스트 맨 끝에 추가
subway.append('haha')
print(subway)
#리스트에 삽입
subway.insert(1,'jeng')
print(subway)

#리스트 마지막에서 빼기
subway.pop()

num_list = [5,2,3,1]

#리스트 정렬
num_list.sort()
print(num_list)

#리스트 뒤집기
num_list.reverse()

#리스트 모두 지우기
#num_list.clear()

#f리스트 확장
num_list = [1,2,3,4]
mix_list = ['jo',20,False]
num_list.extend(mix_list)

#딕셔너리(dict) key와 value로 이루어짐
#key은 중첩이 불가능함
cabinet = {3: 'yoo', 100: 'kim'}

print(cabinet[3])

print(cabinet.get(3))
# print(cabinet[5]) #없는 key이기 때문에 프로그램이 종료
print(cabinet.get(5)) #없는 key이지만 None이 종료

#dict 안에 값이 있는지 확인
print(3 in cabinet) #true
print(5 in cabinet) #false

#새로운 key를 만들고 value를 추가 만약에 원래 존재하는 key라면 value를 변경
cabinet["c-20"] = 'jo'
cabinet[3] = 'haha'

print(cabinet[3])
print(cabinet["c-20"])

#value 삭제
del cabinet[3]
print(cabinet)

#총 사용하고 있는 key만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key와 value를 모두 출력
print(cabinet.items()) #[(100, 'kim'), ('c-20', 'jo')]

#전체 삭제
# cabinet.clear()

#tuple -> 리스트와는 다르게 변경이나 추가를 할 수 없음(불변 객체)
#장점 -> 속도가 리스트보다 빠름

#tuple 선언
menu = ("kimchi", "pizza")
print(menu[0])
print(menu[1])

#menu.add("hambuger") 오류발생

(name, age, hobby) = ("KIM", 20, "coding")

print(name,age,hobby)

# 집합 set --> 중복이 안되고, 순서가 없음
my_set = {1,2,3,4,5.3,3,3}
print(my_set) #{1,2,3,4,5}만 출력

java = {"yoo","kim","yang"}
python = set(["yoo", "park"])

#교집합
print(java & python) #yoo출력
print(java.intersection(python)) #print yoo

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#추가
python.add("KIM")

#삭제
java.remove('kim')

#자료구조 변경
menu = {"coffe","milk","juice"}
print(menu, type(menu)) #<type 'set'> {"coffe","milk","juice"}

menu = list(menu)
print(menu, type(menu)) #<type 'list'> ["coffe","milk","juice"]

menu = tuple(menu)
print(menu,type(menu)) # <type 'tuple'> ("coffe","milk","juice")

#자료구조 퀴즈
users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

from random import * 
chicken = sample(users,1)

coffee = set(sample(users,3))
print(chicken,coffee)

#강사님 코드
from random import *
users = range(1, 21) #1부터 20까지 숫자를 생성
#print(type(users)) #range라는 타입으로 리스트에 해당하는 함수들을 사용할 수가 없음

users = list(users)
shuffle(users)

winners = sample(users, 4)

print("chicken : {0}" .format(winners[0]))
print("coffe: {0}" .format(winners[1:]))