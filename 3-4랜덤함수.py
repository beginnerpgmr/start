from random import *

print(random()) # random : 0.0 이상 1.0 미만의 랜덤한 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 랜덤한 값 생성

print(int(random) * 10) # 0 이상 10 미만의 랜덤한 값 생성(소숫점X)

print(int(random() * 10) + 1) # 1 이상 10 이하의 랜덤한 값 생성

# 로또 값 만들어보기
print(int(random() * 45) + 1) # 1 이상 45 이하의 랜덤한 값 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # randrange : 1 이상 46 미만의 임의의 값 생성
print(randrange(1, 46)) # (int(random() * 45) + 1) 간편 버전
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45)) # randint : 1 이상 45 이하의 임의의 값 생성
print(randint(1, 45)) # (int(random() * 45) + 1) 간편 버전
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))