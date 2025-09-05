## 단계9 : 약수, 배수와 소수1 (6문제)

# PB_5086 배수와 약수
while True:
  a,b = map(int, input().split())
  if (a == 0) and (b == 0):
      break
  if a % b == 0:
      print("multiple")
  elif b % a == 0:
      print("factor")
  else: print("neither")

# PB_2501 약수 구하기
N, K = map(int, input().split())
lst = []
for i in range(1,N+1):
  if (N % i) == 0:
    lst.append(i)

if len(lst) < K:
  print(0)
else: print(lst[K-1])

# PB_9506 약수들의 합
while True:
    n = int(input())
    if n == -1:
        break
    
    factor = []
    for i in range(1, n):
        if n % i == 0:
            factor.append(i)
    
    if sum(factor) == n:
        print(f"{n} =", " + ".join(map(str, factor)))
    else:
        print(f"{n} is NOT perfect.")

# PB_1978 소수 찾기
N = int(input())
lst = list(map(int, input().split()))
result = 0
for num in lst:
  factor = []
  for i in range(1, num+1):
    if (num % i) == 0:
      factor.append(i)

  if len(factor) == 2:
    result = result+1
print(result)

# PB_2581 소수
M = int(input())
N = int(input())
result = []

for num in range(M,N+1):
  factor = []
  for i in range(1, num+1):
    if (num % i) == 0:
      factor.append(i)

  if len(factor) == 2:
    result.append(num)

if result:  
    print(sum(result))
    print(result[0])
else:
    print(-1)

# PB_11653 소인수분해
N = int(input())
i = 2
while N > 1:
  if (N % i) == 0:
    print(i)
    N = N // i
  else: i = i+1
