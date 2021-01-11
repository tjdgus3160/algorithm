# 10815번
import sys
input=sys.stdin.readline

dic={}
n=int(input())
arr=[*map(int,input().split())]
for i in range(n):
    dic[arr[i]]=1
m=int(input())
tmp=[*map(int,input().split())]
res=[]
for i in range(m):
    if tmp[i] in dic:
        res.append(1)
    else:
        res.append(0)
print(*res)