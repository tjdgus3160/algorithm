# 1895번
import sys
input=sys.stdin.readline

r,c=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(r)]
t=int(input())
res=0
for x in range(r-2):
    for y in range(c-2):
        tmp=sorted([arr[x+i][y+j] for i in range(3) for j in range(3)])
        if tmp[4]>=t:
            res+=1
print(res)