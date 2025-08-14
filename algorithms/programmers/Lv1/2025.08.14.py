## 📝 프로그래머스 Lv1 

# 각도 합치기
angle1 = int(input())
angle2 = int(input())
sum_angle = (angle1 + angle2)%360

print(sum_angle)

# 수 나누기
number = int(input())
answer = 0
for _ in range(int(len(str(number))/2)):
    answer += number % 100
    number //= 100

print(answer)

# 병과 분류
code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infl":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")

# 심폐소생술
def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer
