# 2865번
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=[]
for _ in range(m):
    s=input().split()
    for i in range(n):
        arr.append([int(s[2*i]),float(s[2*i+1])])
arr.sort(key=lambda x:-x[1])
v=[]
res=0
for a,b in arr:
    if a not in v:
        v.append(a)
        res+=b
    if len(v)==k:
        break
print("%.1f"%(res))