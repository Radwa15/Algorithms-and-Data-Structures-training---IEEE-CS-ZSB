n=int(input())
a=[int(i) for i in input().split()]
d=sorted(set(a))
if len(d)<=2 or len(d)==3 and d[0]+d[2]==2*d[1]:
    print('YES')
else:
    print('NO')
