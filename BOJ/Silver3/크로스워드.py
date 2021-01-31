# 1706번
import sys
input=sys.stdin.readline

r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input().rstrip('\n')))
res=[]
tmp=""
for i in range(r):
    for j in range(c):
        if arr[i][j]=='#':
            if len(tmp)>1:
                res.append(tmp)
            tmp=""
        else:
            tmp+=arr[i][j]
    if len(tmp)>1:
        res.append(tmp)
    tmp=""
tmp=""
for i in range(c):
    for j in range(r):
        if arr[j][i]=='#':
            if len(tmp)>1:
                res.append(tmp)
            tmp=""
        else:
            tmp+=arr[j][i]
    if len(tmp)>1:
        res.append(tmp)
    tmp=""
res.sort()
print(res[0])