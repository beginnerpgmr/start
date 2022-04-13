print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # **은 제곱한다는 뜻의 연산자. 2의 3제곱(2^3)
print(5%3) # %는 나머지값 구하는 연산자. 5 나누기 3의 나머지값 구하는 공식
print(5//3) # //는 나눴을 때의 몫을 구하는 연산자 5 나누기 3의 몫은 1

print(10 > 3) #True
print(4 >= 7) # >= 크거나 같다 False
print(4 <= 7) # <= 작거나 같다 False

print(3 == 3) # ==는 앞, 뒤 숫자가 같다는 연산자. True
print(3+4 == 7) # True
print(3+2 == 7) # False

print(1 != 3) # !=는 앞, 뒤 숫자가 같지 않다는 연산자. True
print(not(1 != 3)) #1과 3은 같지않다를 not으로 부정함(1과 3이 같다는 해석). False 

print((3 >0) and (3 < 5)) #앞, 뒤 항 모두 참이어야 True 출력. True
print((3 >0) & (3 < 5)) #and와 같은 의미로 사용. True

print((3 >0) or (3 > 5)) # 앞, 뒤 중 하나만 맞아도 True 출력. True
print((3 >0) | (3 > 5)) # or과 같은 의미로 사용. True

print(5>4>3) # 연속된 값도 계산 가능. True
print(5>4>7) # 4는 7보다 작음. False