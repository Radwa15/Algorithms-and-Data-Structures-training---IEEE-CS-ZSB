n, p = map(int,input().split())
p -= 1
c = list(map(int,input().split()))
 
res = 0
for i in range(n):
    if c[i]:
        x = 2 * p - i
        if x < 0 or x >= n or c[x]:
            res += 1
print(res)
