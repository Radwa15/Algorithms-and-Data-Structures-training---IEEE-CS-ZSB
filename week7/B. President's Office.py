n,m, b_color = input().split()
office = []
for _ in range(int(n)):
    office.append(list(input()))
x,y = [-1,1,0,0], [0,0,1,-1]
lis=  []
for i in range(int(n)):
    for j in range(int(m)):
        if office[i][j] == b_color:
            for k in range(4):
                if i+x[k] not in [-1,int(n)] and j+y[k] not in [-1,int(m)] and office[i+x[k]][j+y[k]] not in [b_color,'.'] and (office[i+x[k]][j+y[k]] not in lis):
                    lis.append(office[i+x[k]][j+y[k]])
print(len(lis))
