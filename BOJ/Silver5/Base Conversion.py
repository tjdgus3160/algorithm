# 11576번
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
m=int(input())
arr=[*map(int,input().split())]
k=0
for i in arr:
    k+=i*(a**(m-1))
    m-=1
res=[]
while k:
    res.append(k%b)
    k//=b
res.reverse()
print(*res)