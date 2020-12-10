# 1380번
import sys
input=sys.stdin.readline

res=[]
cnt=1
while(1):
    n=int(input())
    if n==0:
        break
    arr=[]
    for i in range(n):
        name=input()[:-1]
        arr.append(name)
    v=[]
    for _ in range(2*n-1):
        a,b=input().split()
        if a not in v:
            v.append(a)
        else:
            v.remove(a)
    res.append([cnt,arr[int(v[0])-1]])
    cnt+=1
for i in res:
    print(*i)