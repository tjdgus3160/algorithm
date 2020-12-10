tmp=[]
for i in range(int(input())):
    tmp.append([*map(int,input().split())])
tmp.sort(key=lambda x:-x[2])
res=[]
for i in tmp:
    if len(res)==3:
        break
    if len(res)==2:
        if res[0][0]!=res[1][0]:
            res.append(i[:2])
        else:
            if res[0][0]!=i[0]:
                res.append(i[:2])
    else:
        res.append(i[:2])
for i in res:
    print(*i)
