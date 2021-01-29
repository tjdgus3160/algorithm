# 1327번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dq=deque([[*map(str,input().split())]])
res=0
flag=True
dic={}
dic["".join(dq[0])]=1
while True:
    cnt=len(dq)
    before=len(dic)
    f=False
    for _ in range(cnt):
        arr=dq.popleft()
        if arr==sorted(arr):
            f=True
            break
        for i in range(n-k+1):
            tmp=arr[i:i+k]
            tmp.reverse()
            tmp=arr[:i]+tmp+arr[i+k:]
            kk="".join(tmp)
            if kk not in dic:
                dq.append(tmp)
                dic[kk]=1
    if f:
        break
    if before==len(dic):
        flag=False
        break
    res+=1
print(res if flag else -1)

