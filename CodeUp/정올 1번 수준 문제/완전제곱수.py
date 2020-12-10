from collections import Counter
import operator
import sys
input=sys.stdin.readline

a=int(input())
b=int(input())
res=[]
for i in range(a,b+1):
    if int(i**0.5)**2==i:
        res.append(i)
print(sum(res))
print(res[0])
