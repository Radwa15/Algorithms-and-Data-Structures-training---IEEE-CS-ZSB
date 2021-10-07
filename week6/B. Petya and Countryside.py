n = int(input())
h = list(map(int, input().split()))
 
a , b = [0]*n , [0]*n

for i in range(1, n):
    if h[i] >= h[i - 1]: 
        a[i] = a[i - 1] + 1
    if h[- i] <= h[- 1 - i]: 
        b[- i - 1] = b[- i] + 1

res=0
for i in range(n):
    res = max(a[i] + b[i] , res)
print(res + 1)
