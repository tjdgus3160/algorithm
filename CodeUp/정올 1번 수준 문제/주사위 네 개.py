import sys
input=sys.stdin.readline

tmp=[]
for i in range(int(input())):
    tmp.append([*map(int,input().split())])

res=[]
for i in tmp:
    if len(set(i))==1:
        res.append(50000+i[0]*5000)
    elif len(set(i))==2:
        i.sort()
        if i[1]==i[2]:
            res.append(10000+i[2]*1000)
        else:
            res.append(2000+i[0]*500+i[2]*500)
    elif len(set(i))==3:
        k=0
        for j in i:
            if i.count(j)==2:
                k=j
                break
        res.append(1000+k*100)
    else:
        res.append(max(i)*100)

print(max(res))

