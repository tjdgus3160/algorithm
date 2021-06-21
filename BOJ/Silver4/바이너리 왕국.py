# 16567번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0]+[*map(int,input().split())]+[0]
res=0
flag=False
for i in arr:
    if i:
        if not flag:
            flag=True
            res+=1
    else:
        if flag:
            flag=False
for _ in range(m):
    s=[*map(int,input().split())]
    if s[0]==0:
        print(res)
    else:
        i=s[1]
        if not arr[i]:
            if not arr[i-1] and not arr[i+1]:
                res+=1
            elif arr[i-1] and arr[i+1]:
                res-=1
            arr[i]=1
