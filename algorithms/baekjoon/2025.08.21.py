## 단계5 : 문자열 (11문제)

# PB_27866 문자와 문자열
word = input()
i = int(input())
print(word[i-1])

# PB_2743 단어 길이 재기
word1 = input()
print(len(word1))

# PB_9086 문자열
T = int(input())

for _ in range(T):
  word2 = input()
  result = word2[0] + word2[-1]
  print(result)

# 떨어져 있는 두 글자 추출하는 방법
# 1. 인덱스로 하나씩 이어붙이기 : result = word[0] + word[-1]
# 2. join 사용하기

# PB_9086 문자열(gpt) - join
# T = int(input())
word = input()
index = [0,3]
result = "".join(word[i] for i in index)
print(result)

# PB_11720 숫자의 합
N = int(input())
nums = map(int, input())
print(sum(nums))

# PB_10809 알파벳 찾기
word3 = input()
lower_alphabet = [chr(i) for i in range(97, 123)]
lst = [-1]*26

for i in range(len(word3)):
  for j in range(len(lower_alphabet)):
    if word3[i] == lower_alphabet[j]:
      if lst[j] == -1:
        lst[j] = i
print(*lst)

# PB_10809 알파벳 찾기(gpt)
word3 = input().strip()
lst = [-1] * 26

for i, ch in enumerate(word3):
    idx = ord(ch) - ord('a')   # 'a' → 0, 'b' → 1, ...
    if lst[idx] == -1:         # 첫 등장만 기록
        lst[idx] = i

print(*lst)

# enumerate : 리스트 같은 걸 반복문으로 돌릴 때, 인덱스(번호)와 값을 동시에 꺼내주는 함수
# ord :문자를 유니코드(정수 코드값) 로 바꿔주는 함수

# 문자 -> 숫자 
print(ord('a'))  # 97
print(ord('b'))  # 98
print(ord('z'))  # 122

# 숫자 -> 문자

print(chr(97))   # a
print(chr(122))  # z

# PB_2675 문자열 반복
T = int(input())

for _ in range(T):
  R, S = input().split()
  R = int(R)
  result = ""
  for i in range(len(S)):
    result = result + S[i]*R
  print(result)

# PB_1152 단어의 개수
sentence = input().strip()      # 앞뒤 공백 제거 / lstrip() : 왼쪽(앞쪽) 공백만 제거 / rstrip() : 오른쪽(뒤쪽) 공백만 제거 
words = sentence.split()        # 공백 기준 분리
print(len(words))               # 단어 개수 출력

# PB_2908 상수
num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])
if num1 > num2 : 
  print(num1)
else : print(num2)

# print(max(num1, num2))

# PB_5622 다이얼
word = input()
dial = {
    'ABC' : 2, 'DEF' : 3, 'GHI' :4, 'JKL' : 5,
    'MNO' : 6, 'PQRS' : 7, 'TUV' : 8, 'WXYZ' : 9
}
lst = []

for i in range(len(word)):
  values = [v for k, v in dial.items() if word[i] in k ]
  lst.append(values[0])

result = sum(lst) + len(word) 
print(result)

# PB_5622 다이얼(gpt)
word = input()
dial = {
    'ABC' : 2, 'DEF' : 3, 'GHI' :4, 'JKL' : 5,
    'MNO' : 6, 'PQRS' : 7, 'TUV' : 8, 'WXYZ' : 9
}
result = 0

for ch in word:
    for k, v in dial.items():
        if ch in k:
            result += v + 1
            break
print(result)

# 리스트를 모았다가 sum하는 방법 대신 바로 누적하여 출력하기

# PB_11718 그대로 출력하기
while True:
  try:
    print(input())
  except EOFError:
    break

# PB_11718 그대로 출력하기(gpt)
import sys
for line in sys.stdin:
  print(line, end='')
