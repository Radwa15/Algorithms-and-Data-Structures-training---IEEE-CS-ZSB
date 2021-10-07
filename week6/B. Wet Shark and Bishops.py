a = [0]*3000
m = [0]*3000
res = 0
for i in range(int(input())):
    x , y = map(int,input().split())
    res += a[x+y] + m[x-y]
    a[x+y] += 1
    m[x-y] += 1
    
print(res)
