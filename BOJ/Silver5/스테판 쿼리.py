# 14654번
import sys
input=sys.stdin.readline

n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
res=1
aw,bw=0,0
for i in range(n):
    if a[i]==b[i]:
        if aw:
            aw=0
            bw=1
        else:
            aw=1
            bw=0
    elif (a[i]==1 and b[i]==3) or (a[i]==2 and b[i]==1) or (a[i]==3 and b[i]==2):
        if i==0:
            aw+=1
            continue
        if aw:
            aw+=1
            res=max(res,aw)
        else:
            aw=1
            bw=0
    else:
        if i==0:
            bw+=1
            continue
        if bw:
            bw+=1
            res=max(res,bw)
        else:
            bw=1
            aw=0
print(res)