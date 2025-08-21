# PB_14681 사분면 고르기
x = int(input())
y = int(input())
if (x>0) and (y>0):
  print("1")
if (x<0) and (y>0):
  print("2")
if (x<0) and (y<0):
  print("3")
if (x>0) and (y<0):
  print("4")

# PB_2884 알람 시계
H, M = map(int, input().split())
if (M>=45) :
  print(f"{H} {M-45}")
elif (M<45) and (H==0) :
  print(f"23 {M+15}")
elif (M<45) and (H!=0) :
  print(f"{H-1} {M+15}")

# PB_2525 오븐 시계
A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C
hour = (total // 60) % 24
minute = total % 60
print(hour, minute)

# PB_2480 주사위 세개
a, b, c = map(int, input().split())
lst = [a,b,c]
if (a==b==c) :
  print(f"{10000+a*1000}")
elif (a==b!=c) :
  print(f"{1000+a*100}")
elif (a!=b==c):
  print(f"{1000+b*100}")
elif (a==c!=b):
  print(f"{1000+c*100}")
else :
  print(max(lst)*100)
