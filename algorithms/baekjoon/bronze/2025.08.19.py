# PB_2739 구구단
N = int(input())

for i in range(1, 10):
  print(f"{N} * {i} = {N*i}")

# PB_10950 A+B-3
T = int(input())

for _ in range(T):
  a, b = map(int, input().split())
  print(a+b)

# PB_8393 합
n = int(input())
total = 0

for i in range(n+1):
  total = total+i
print(total)

# PB_25304 영수증
X = int(input())
N = int(input())
total = 0

for _ in range(N):
  a, b = map(int, input().split())
  total = total + (a*b)

if (total == X):
  print("Yes")
else:
  print("No")

# PB_25314 코딩은 체육과목 입니다
N = int(input())
a = N//4
result = ""

for i in range(a):
  result = result + "long "

result = result + "int"
print(result)

# PB_15552 빠른 A+B
# sys.sydin.readline() 은 코랩이나 쥬피터에서는 오류 생김 -> input()사용
# vs code(터미널)같은 표준 입력이 연결된 환경에서는 잘 작동함
import sys

T = int(sys.stdin.readline())

for _ in range(T):
  a,b = map(int, sys.stdin.readline().split())
  print(a+b)

# PB_11021 A+B-7
T = int(input())

for i in range(1,T+1):
  a,b = map(int, input().split())
  print(f"Case #{i}: {a+b}")

# PB_11022 A+B-8
T = int(input())

for i in range(1,T+1):
  a,b = map(int, input().split())
  print(f"Case #{i}: {a} + {b} = {a+b}")

# PB_2438 별 찍기-1
N = int(input())

for i in range(1,N+1):
  print('*' * i)

# PB_2438 별 찍기-1
N = int(input())
result = ''

for i in range(1,N+1):
  result = result +'*'
  print(result)

# PB_2439 별 찍기-2
N = int(input())

for i in range(1, N+1):
    print(" " * (N - i) + "*" * i)

# PB_10950 A+B-5
while True:
  a,b = map(int, input().split())
  if (a==0) and (b==0):
    break
  print(a+b)

# PB_10950 A+B-4
while True:
  try:
    a,b = map(int, input().split())
    print(a+b)
  except EOFError:
    break

# 명시적 종료 조건이 있는 문제 → while True + if 조건: break
# 입력이 언제 끝날지 모르는 문제 → try-except or sys.stdin
# 백준에서 많이 쓰는 방식 → sys.stdin
# input() : 입력이 언제 끝날지 알 수 없으니, 보통 EOFError 처리나 종료 조건(0 0 같은 값)을 따로 줘야 함.
# for line in sys.stdin : 입력 스트림 전체를 파일처럼 한 줄씩 차례대로 읽으며 더 이상 읽을 게 없으면 자동 종료.

# PB_10950 A+B-4
import sys
for line in sys.stdin:
  a,b = map(int, input().split())
  print(a+b)

# sys.stdin : 스트림 자체 (파일 같은 객체)
# for line in sys.stdin: : EOF까지 한 줄씩 반복
# sys.stdin.readline() : 한 줄만 읽기 (기능 input과 거의 유사하지만 속도가 훨씬 빠름)
# sys.stdin.readlines() : 전체 데이터를 리스트로 한 번에 읽기
