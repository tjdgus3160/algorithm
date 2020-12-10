from math import gcd
import sys
input=sys.stdin.readline

tmp=[]
for i in range(7):
    tmp.append(int(input()))
a=[i for i in tmp if i%2==1]
if len(a)==0:
    print(-1)
else:
    print(sum(a))
    print(min(a))
