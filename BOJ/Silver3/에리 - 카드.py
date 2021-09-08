# 15728번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
arr=[(i,j) for i in a for j in b]
s=set()
for i,j in sorted(arr,key=lambda x:(x[0]*x[1]),reverse=True):
    if j in s:
        continue
    if len(s)<k:
        s.add(j)
    else:
        print(i*j)
        break
