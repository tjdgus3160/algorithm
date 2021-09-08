# 1747번
import sys
input=sys.stdin.readline

n=1004000
l=[True for _ in range(n+1)]
l[1]=False
for i in range(2,int(n**0.5)+1):
    if l[i]:
        j=i+i
        while j<=n:
            l[j]=False
            j+=i
n=int(input())
while True:
    if l[n] and str(n)==str(n)[::-1]:
        print(n)
        break
    n+=1