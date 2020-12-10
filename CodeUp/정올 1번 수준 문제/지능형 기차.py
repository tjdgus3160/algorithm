from math import gcd
import sys
input=sys.stdin.readline

tmp=[]
for i in range(4):
    tmp.append([*map(int,input().split())])
res=0
cur=0
for i in tmp:
    cur=cur-i[0]+i[1]
    if cur > 10000:
        cur = 10000
    if res<cur:
        res=cur
print(res)
