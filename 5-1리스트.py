# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
from re import sub

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "이미주", "전소민"]
print(subway)

# 이미주씨가 몇 번째 칸에 타고 있는가? / .index
print(subway.index("이미주"))

# 송지효씨가 다음 정류장에서 다음 칸에 탐 / .append
subway.append("송지효") # 제일 뒷자리에 추가
print(subway)

# 제시를 유재석 / 이미주 사이에 태워봄 / .insert
subway.insert(1, "제시") # 어디 다음에 삽입할 지 부터 적고 개체 적음
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 (뒤에서부터 순서대로 삭제함) / .pop
print(subway.pop())
print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인 / .count
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 순서 정렬도 가능 / .sort 
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능 / .reverse
num_list.reverse()
print(num_list)

# 모두 지우기 / .clear
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 / mix_list
num_list = [5,2,4,3,1]
mix_list = ["은하", 22, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)