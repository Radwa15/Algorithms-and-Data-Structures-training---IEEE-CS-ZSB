a,b=[],[]
for i in range(int(input())):
    x=list(map(int,input().split()))
    a.append(x[0])
    b.append(x[1])
if a!=b:
    print("rated")
elif sorted(a,reverse=True)==b:
    print("maybe")
else:
    print("unrated")
