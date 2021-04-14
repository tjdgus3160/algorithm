# 5525번
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
s=input().rstrip('\n')
res=0
cur=-1
p=2*n
for i in range(m):
    if s[i]=='I':
        if cur==-1:
            cur=i
            continue
        if i-cur==p:
            res+=1
            cur+=2
        elif s[i-1]=='I':
            cur = i
    else:
        if i==0:
            continue
        if s[i-1]=='O':
            cur=-1
print(res)