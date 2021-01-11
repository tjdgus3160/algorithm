# 10773번
import sys
input=sys.stdin.readline

res=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:
        if res:
            res.pop()
        else:
            res.append(n)
    else:
        res.append(n)
print(sum(res))