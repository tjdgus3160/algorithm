# 14425번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    s=input().rstrip('\n')
    arr.append(s)
res=0
for _ in range(m):
    s = input().rstrip('\n')
    if s in arr:
        res+=1
print(res)