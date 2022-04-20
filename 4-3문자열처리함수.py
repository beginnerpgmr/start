python = "Python is Amazing"
print(python.lower()) # lower : 전부 소문자로 출력
print(python.upper()) # upper : 전부 대문자로 출력
print(python[0].isupper()) # isupper : 문장 에서 첫번째 글자가 대문자인지 알려줌
print(len(python)) # len : 문장의 길이를 변환해줌
print(python.replace("Python", "Java")) # replace : 앞 단어를 뒤 단어로 변환해줌

index = python.index("n") # index : 문장에서 특정단어가 몇번째에 위치해있는지 알려줌
print(index)
index = python.index("n", index + 1) # 앞의 n이 나온 위치 + 1 부터 다시 n의 위치를 찾음
print(index)

print(python.find("n"))
print(python.find("Java"))
# print(python.index("Java"))
# find : index와 비슷하지만, 문장에 없는 단어를 찾을 때 -1 로 표시함.
# index는 오류로 처리하고 프로그램을 종료함
print("hi") # 프로그램이 종료되어 출력 안됨/find로 쓰면 정상 출력 됨

print(python.count("n")) # python 이라는 변수에서 n이 총 몇번 등장하는지 계산