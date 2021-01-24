# 6219번
import sys
input=sys.stdin.readline

a,b,d=map(int,input().split())
n=b
l=[True for _ in range(n+1)]
l[1]=False
for i in range(2,int(n**0.5)+1):
    if l[i]:
        j=i+i
        while j<=n:
            l[j]=False
            j+=i
res=0
for i in range(a,b+1):
    if l[i] and str(d) in str(i):
        res+=1
print(res)
