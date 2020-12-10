import itertools
import sys
input=sys.stdin.readline

n=int(input())
s=input()
res=[]
c=n%3
for i in s:
    if c==0:
        if len(res)>0:
            res.append(",")
        c=3
    res.append(i)
    c-=1

print("".join(res))


