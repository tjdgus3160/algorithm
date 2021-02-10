# 5534번
import sys
input=sys.stdin.readline

n=int(input())
name=input().rstrip('\n')
m=len(name)
res=0
for _ in range(n):
    s=input().rstrip('\n')
    k=1
    flag=False
    while len(name)+(len(name)-1)*(k-1)<=len(s):
        for i in range(len(s)-m*k+k):
            if name == s[i:i+m*k:k]:
                flag=True
                k+=1000000
                break
        k+=1
    if flag:
        res+=1
print(res)