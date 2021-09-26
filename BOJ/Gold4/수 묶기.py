# 1744번
import sys
input=sys.stdin.readline

plus=[]
minus=[]
for _ in range(int(input())):
    n=int(input())
    if n>0:
        plus.append(n)
    else:
        minus.append(n)
plus.sort(reverse=True)
minus.sort()
res=0
for i in range(0,len(plus),2):
    if i+1<len(plus):
        if plus[i+1]!=1:
            res+=plus[i]*plus[i+1]
        else:
            res+=plus[i]+plus[i+1]
    else:
        res+=plus[i]
for i in range(0,len(minus),2):
    if i+1<len(minus):
        res+=minus[i]*minus[i+1]
    else:
        res+=minus[i]
print(res)
