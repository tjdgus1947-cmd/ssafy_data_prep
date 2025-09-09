## 단계10. 기하1: 직사각형과 삼각형 8문제

# PB_27323 직사각형
length = int(input())
width = int(input())
area = length * width
print(area)

# PB_1085 직사각형에서 탈출
x, y, w, h = map(int, input().split())
distance_length = h-y
distance_width = w-x
result = min(x, y, distance_length, distance_width)
print(result)

# PB_3009 네 번째 점
x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for x in x_list:
    if x_list.count(x) == 1:
        ans_x = x

for y in y_list:
    if y_list.count(y) == 1:
        ans_y = y

print(ans_x, ans_y)

# PB_15894 수학은 체육과목 입니다
n = int(input())
result = 4*n
print(result)

# PB_9063 대지
x_list = []
y_list = []
N = int(input())

for _ in range(N):
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)

x_max = max(x_list)
y_max = max(y_list)
x_min = min(x_list)
y_min = min(y_list)
result = (x_max-x_min) * (y_max-y_min)

print(result)

# PB_10101 삼각형 외우기
a, b, c = [int(input()) for _ in range(3)]

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# PB_5073 삼격형과 세 변
while True:
  a, b, c = map(int, input().split())
  if a==b==c==0:
    break

  elif a+b<=c or a+c<=b or b+c<=a:
    print("Invalid")

  elif a==b==c!=0:
    print("Equilateral")

  elif a==b or a==c or b==c:
    print("Isosceles")

  else:
    print("Scalene")

# PB_14125 세 막대
a, b, c = map(int, input().split())
lst = [a,b,c]
lst.sort()
if lst[0] + lst[1] > lst[2]:
  lst[2] = lst[2]
else: lst[2] = lst[0] + lst[1] - 1 
print(sum(lst))
