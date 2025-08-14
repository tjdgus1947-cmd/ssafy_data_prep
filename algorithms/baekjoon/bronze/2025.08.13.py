- PB_2753 윤년 
year = int(input())
if (year%4 == 0) and ((year%100 !=0) | (year%400 ==0)):
  print(1)
else: print(0)

- PB_10869 사칙연산 
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
  - map(함수, 반복가능한객체)
  - map() 함수는 여러 데이터를 한 번에 변환하거나 함수를 각 원소에 적용

- PB_2741 N 찍기 
N = int(input())
for i in range(1,N+1):
  print(i)

- PB_2562 최댓값 
numbers = [int(input()) for _ in range(9)]
n_max = max(numbers)
index_max = numbers.index(n_max) + 1
print(n_max)
print(index_max)
