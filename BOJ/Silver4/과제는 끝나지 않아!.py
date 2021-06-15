# 17952번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
res=0
for _ in range(n):
    s=input().rstrip()
    if s=='0':
        if arr:
            if arr[-1][1]==1:
                res+=arr[-1][0]
                arr.pop()
            else:
                arr[-1][1]-=1
    else:
        _,a,t=map(int,s.split())
        if t==1:
            res+=a
        else:
            arr.append([a,t-1])
print(res)