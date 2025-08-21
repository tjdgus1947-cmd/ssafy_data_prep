- PB_1000 A+B
A, B = map(int, input().split())
print(A+B)
  
- PB_1002 터렛  
N = int(input())

for _ in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dx = x1-x2
  dy = y1-y2
  d2 = dx*dx + dy*dy
  rp = r1+r2
  rm = abs(r1-r2)
  rp2 = rp*rp
  rm2 = rm*rm

  if d2 == 0:
    if r1 == r2:
      print(-1)
    else : print(0)

  else:
    if (d2>rp2) or (d2<rm2): 
      print(0)
    elif (d2==rp2) or (d2==rm2):
      print(1)
    else : print(2)
    
