## 단계4 : 1차원 배열 (10문제)

# PB_10807 개수 세기
N = int(input())
# nums = [int(input()) for _ in range(N)]
nums = list(map(int, input().split()))
v = int(input())
result = 0

for i in range(N):
  if nums[i] == v:
    result = result+1
print(result)

# PB_10807 개수 세기(gpt)

N = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(nums.count(v))

# PB_10871 X보다 작은 수 
N, X = map(int, input().split())
nums = list(map(int, input().split()))
lst = []
for i in range(N):
  if nums[i] < X:
    lst.append(nums[i])
print(*lst) # 리스트를 풀어서 공백으로 구분하여 출력

# PB_10871 X보다 작은 수(gpt)
N, X = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    if num < X:
        print(num, end=" ")   # 공백 구분 출력

# PB_10818 최소, 최대
N = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# PB_10810 공 넣기
N, M = map(int, input().split())
basket = [0] * (N)

for _ in range(M):
  i, j, k = map(int, input().split())
  for x in range(i, j+1):
    basket[x-1] = k

print(*basket[0:N+1])

# PB_10813 공 바꾸기
N, M = map(int, input().split())
basket = list(range(1,N+1))

for _ in range(M):
  i, j = map(int, input().split())
  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)

# PB_5597 과제 안 내신 분..?
all = set(range(1,31))
for _ in range(28):
  x = int(input())
  all.remove(x)

a,b = sorted(all)
print(a)
print(b)

# PB_5597 과제 안 내신 분..?(gpt)
lst = list(range(1,31))
for _ in range(28):
  n = int(input())
  lst.remove(n)

lst.sort()
print(lst[0])
print(lst[1])

# PB_3052 나머지
lst = []
for _ in range(10):
  n = int(input()) % 42
  lst.append(n)
set_unique = set(lst) 
print(len(set_unique))

# 리스트에 중복 값이 있을때 중복값을 제거한 원소 개수 구하기
# 1. set() 활용 : set_unique = set(lst)
# 2. 직접 중복 제거 
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []
# for x in lst:
    # if x not in unique_list:
        # unique_list.append(x)

# PB_10811 바구니 뒤집기
N, M = map(int, input().split())
lst = list(range(1,N+1))
for _ in range(M):
  i, j = map(int, input().split())
  lst[i-1:j] = lst[i-1:j][::-1]
print(*lst)

# 리스트 역순으로 출력하기
# 1. reversed(lst) : 원본 안 바뀜 (반복자로 꺼냄)
# 2. lst[::-1] : 새 리스트를 반환
# 3. lst.reverse() : 원본 자체를 바꿈

# PB_1546 평균
N = int(input())
lst = list(map(int, input().split()))
lst_max = max(lst)
lst1 = []
for i in range(N):
  lst1.append((lst[i]/lst_max)*100)
lst1_mean = sum(lst1) / len(lst1)
print(lst1_mean)

# PB_1546 평균(gpt)
N = int(input())
lst = list(map(int, input().split()))

lst_max = max(lst)
new_avg = sum([(x / lst_max) * 100 for x in lst]) / N
print(new_avg)
