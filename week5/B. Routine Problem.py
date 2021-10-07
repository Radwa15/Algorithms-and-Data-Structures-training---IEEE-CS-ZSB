from math import gcd
l = list(map(int,input().split()))
l[1] = l[1]*l[2]
l[3] = l[3]*l[0]
p = abs(l[1] - l[3])
q = max(l[1] , l[3])
x = gcd(p , q)
p //= x
q //= x
print(p , "/", q , sep="")
