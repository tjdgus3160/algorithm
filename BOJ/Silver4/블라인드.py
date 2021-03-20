# 2799번
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
input()
res=[0]*5
for _ in range(m):
    tmp=[0]*n
    for _ in range(4):
        s=input().rstrip('\n').split('#')
        for i in range(n):
            if s[i+1]=='****':
                tmp[i]+=1
    for i in tmp:
        res[i]+=1
    input()
print(*res)
