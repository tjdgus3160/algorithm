# 1068번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
dic={}
for i in range(n):
    dic.setdefault(i,[])
arr=[*map(int,input().split())]
root=0
for i in range(len(arr)):
    if arr[i]==-1:
        root=i
    else:
        dic[arr[i]].append(i)
x=int(input())
res=0
dq=deque([root])
if x!=root:
    while dq:
        k=dq.pop()
        if not dic[k]:
            res+=1
            continue
        flag=False
        for i in dic[k]:
            if i !=x:
                dq.append(i)
                flag=True
        if not flag:
            res+=1
print(res)