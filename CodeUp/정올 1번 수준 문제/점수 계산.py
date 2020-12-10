import sys
input=sys.stdin.readline

input()
a=[*map(int,input().split())]
res=[]
for i in a:
    if i==1:
        if len(res)>0:
            res.append(res[-1]+1)
        else:
            res.append(1)
    else:
        res.append(0)
print(sum(res))

