# 5567번
from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())
dic=defaultdict(list)
for _ in range(int(input())):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
tmp=set(dic[1]+[1])
res=set(dic[1]+[1])

for i in tmp:
    res=res.union(set(dic[i]))
print(len(res)-1)