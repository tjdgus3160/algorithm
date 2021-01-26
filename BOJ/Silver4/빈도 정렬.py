# 2910번
import sys
input=sys.stdin.readline

n,c=map(int,input().split())
arr=[*map(int,input().split())]
tmp={}
for i,v in enumerate(arr):
    if v not in tmp:
        tmp[v]=[1,i]
    else:
        tmp[v][0]+=1
res=[]
for sub in sorted(tmp.items(),key=lambda x:(-x[1][0],x[1][1])):
    res+=[sub[0]]*sub[1][0]
print(*res)