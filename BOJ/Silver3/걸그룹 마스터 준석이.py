# 16165번
from collections import defaultdict
import sys
input=sys.stdin.readline

dic=defaultdict(list)
n,m=map(int,input().split())

for _ in range(n):
    team=input().rstrip()
    for _ in range(int(input())):
        dic[team].append(input().rstrip())
for _ in range(m):
    name=input().rstrip()
    x=int(input())
    if x==0:
        for i in sorted(dic[name]):
            print(i)
    else:
        for i,arr in dic.items():
            if name in arr:
                print(i)
                break