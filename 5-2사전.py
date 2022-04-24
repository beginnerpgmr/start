cabinet = {3:"유재석", 100:"보필PD"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 대괄호 값을 가져올 경우 값이 없어서 오류나면 프로그램 종료됨
# print(cabinet.get(5)) # 오류를 None로 표현

# in 을 이용하여 값이 있는지 확인 가능
print(3 in cabinet) # in # 3이라는 키가 캐비넷에 있다면 True 출력
print(5 in cabinet) # 5라는 키가 캐비넷에 없다면 False 출력


cabinet = {"A-3":"유재석", "B-100":"보필PD"}
print(cabinet["A-3"]) # 숫자 뿐만 아니라 글자도 가능
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "전소민" # 유재석 -> 전소민 바꾸기 가능
cabinet["C-20"] = "송지효" # 추가 가능
print(cabinet)

# 간 손님
del cabinet["A-3"] # del 로 삭제 가능
print(cabinet)

# key 들만 출력
print(cabinet.keys()) # .keys # 키 번호만 출력

# value 들만 출력
print(cabinet.values()) # .values # 키 값(이름)만 출력

# key, value 둘 다 출력
print(cabinet.items()) # .items # 값 모두 출력

# 목욕탕 폐점
cabinet.clear() # .clear # 값 모두 삭제
print(cabinet) # 공백 출력