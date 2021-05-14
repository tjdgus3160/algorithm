# 5883번
import sys
input=sys.stdin.readline

arr=[int(input()) for _ in range(int(input()))]
s=set(arr)
res=0
for i in s:
    cnt=0
    loc=-1
    for j in arr:
        if j==i:
            continue
        if loc==j:
            cnt+=1
        else:
            res=max(res,cnt)
            loc = j
            cnt = 1
    res = max(res, cnt)
if len(s)==1:
    print(len(arr))
else:
    print(res)