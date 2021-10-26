p,q,l,r= map(int,input().split())
l1=[]
lis=[]
c1=0
for i in range(p):
    a,b= map(int,input().split())
    l1+= [x for x in range(a,b+1)]
for i in range(q):
    c,d= map(int,input().split())
    lis+=[x for x in range(c,d+1)]
t=l
while r>=t:
    for h in lis:
        if (h+t) in l1:
            c1+=1
            break
    t+=1
print(c1)
