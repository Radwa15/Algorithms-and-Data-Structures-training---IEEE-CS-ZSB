def f(i, t, Y, c):
    arr, res = [(t,t)], 0
    for x, y, r in c:
        d = r - (y-Y)**2
        if d < 0: 
            continue
        d = int(d**.5)
        arr.append((x-d, x+d+1))
    for a, b in sorted(arr):
        if i < a and i < t: 
            res += a - i
        if i < b: 
            i = b
    return res
 
xa, ya, xb, yb = map(int, input().split())
if xa > xb: 
    xa, xb = xb, xa
if ya > yb: 
    ya, yb = yb, ya
n = int(input())
arr = [map(int, input().split()) for _ in range(n)]
arr1 = [(x, y, r*r) for x, y, r in arr]
arr2 = [(y, x, r) for x, y, r in arr1]
res1 = f(xa, xb+1, ya, arr1)
res2 = f(xa, xb+1, yb, arr1)
res3 = f(ya+1, yb, xa, arr2)
res4 = f(ya+1, yb, xb, arr2)
print(res1 + res2 + res3 + res4)
