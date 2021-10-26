s=set()
n,m=input().split(" ")
n=int(n)
m=int(m)
for i in range(n):
    test=input()
    if(test.find("S")-test.find("G")<0):
        print(-1)
        exit(0)
        break
    else:
        s.add(int(test.find('S')-test.find("G")))
print(len(s))
