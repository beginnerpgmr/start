# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"김나경", "마서현", "배유진"}
python = set(["김나경", "박소현"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)              # & 사용
print(java.intersection(python))  # .intersection() 사용

# 합집합 (java 나 python을 할 수 있는 개발자)
print(java | python)       # | 사용
print(java.union(python))  # .union() 사용

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)            # - 사용
print(java.difference(python))  # .difference() 사용

# python 할 줄 아는 사람이 늘어남
python.add("베유정") # .add() : 값 추가
print(python)

# java를 까먹음
java.remove("배유진") # .remove() : 값 삭제
print(java)
