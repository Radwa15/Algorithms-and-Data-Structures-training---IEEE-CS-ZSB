n,d=map(int,input().split())
l=sorted(list(map(int,input().split())) for _ in range(n))
j=0
ff=0
m=0
for i in range(n):
    ff+=l[i][1]
    while (l[i][0]-l[j][0])>=d:
        ff-=l[j][1]
        j+=1
    m=max(m,ff)
print(m)
