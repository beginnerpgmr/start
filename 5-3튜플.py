# 리스트와 다르게 내용변경 / 추가 불가능
# 리스트보다 처리속도 빠름
# 하지만 할 수 있는 것이 많지 않음
# 변경되지 않는 목록을 사용할 때 활용 가능

menu = ("돈가스", "생선가스")
print(menu[0])
print(menu[1])

# menu.add("생선가스") # 튜플은 .add 사용 불가능

# 리스트로 작성
name = "김나경"
age = 26
hobby = "눕방"
print(name, age, hobby)

# 튜플로 작성
(name, age, hobby) = ("김나경", 26, "눕방")
print(name, age, hobby)