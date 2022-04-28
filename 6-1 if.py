# if = 분기점
# if 조건 : 
#        실행 명령문
# if + 조건 명시 + :으로 문장 마무리 + 뒤에 실행 명령문 작성
# 조건에 해당하면 명령이 실행됨

weather = "비"
if weather == "비" :
    print("우산을 챙기세요")  # 출력됨


weather = "맑음"
if weather == "비" :
    print("우산을 챙기세요")  # 출력 안됨


# elif : 처음 조건이 아닐 경우 다음 조건(두번째 조건). 맞으면 출력, 틀리면 출력 안됨
# else : 위에 있는 모든 조건이 아닐 경우 명시된 조건 이외의 나머지 조건의 경우에 출력됨
# else가 없다면 위에 있는 모든 조건이 아닐 경우 아무것도 출력 안됨


weather = "미세먼지"
if weather == "비" :
    print("우산을 챙기세요")  # 비만 있는 경우 출력
elif weather == "미세먼지" :
    print("마스크를 챙기세요")  # 미세먼지만 있는 경우 출력
else:
    print("준비물이 필요 없어요")  # 비도 없고 미세먼지도 없는 경우


weather = "맑음"
if weather == "비" :
    print("우산을 챙기세요")  # 비만 있는 경우 출력
elif weather == "미세먼지" :
    print("마스크를 챙기세요")  # 미세먼지만 있는 경우 출력
else:
    print("준비물이 필요 없어요")  # 비도 없고 미세먼지도 없는 경우


# input : 사용자의 입력을 받는 문장


weather = input("오늘 날씨는 어때요? ")  # 출력문 ㅁ 에 조건을 작성하여 결과값 출력
if weather == "비" :
    print("우산을 챙기세요")  
elif weather == "미세먼지" :
    print("마스크를 챙기세요")  
else:
    print("준비물이 필요 없어요")


weather = input("오늘 날씨는 어때요? ")  # 출력문 ㅁ 에 조건을 작성하여 결과값 출력
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")  
elif weather == "미세먼지" :
    print("마스크를 챙기세요")  
else:
    print("준비물이 필요 없어요")


# ㅇㅇㅇ or ㅇㅇㅇ : 앞조건 혹은 뒷조건이 맞을 때
# ㅇㅇㅇ and ㅇㅇㅇ : 앞조건과 뒷조건이 모두 성립할 때


temp = int(input("기온은 어때요? "))  # 기온은 숫자이기 때문에 앞에 int() 입력하기
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")  # 기온이 30도 일 때
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")  # 기온이 10도 이상 30도 미만 일 때
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")  # 기온이 0도 이상 10도 이하 일 때 # elif 0 <= temp < 10: 도 가능(and생략)
else:
    print("너무 추워요. 외출을 자제하세요")