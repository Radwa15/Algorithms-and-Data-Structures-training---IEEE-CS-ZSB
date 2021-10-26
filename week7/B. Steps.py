n, m = map(int, input().split())
x, y = map(int, input().split())
e = 0
 
 
for i in range(int(input())):
    dx, dy = map(int, input().split())
    a, b = n, m
    op1=(m - y)
    op2=(y - 1)
    op3=(n - x)
    op4=(x - 1)
    if dy > 0: 
      a = op1 // dy
    elif dy < 0: 
      a = op2 // (- dy)
    if dx > 0: 
      b = op3 // dx
    elif dx < 0: 
      b = op4 // (- dx)
    result = min(a, b)
    x += result * dx
    y += result * dy
    e += result
print(e)
