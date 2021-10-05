# 11509번
from collections import defaultdict
import sys
input=sys.stdin.readline

input()
dic=defaultdict(int)
res=0
for i in map(int,input().split()):
    if not dic[i]:
        dic[i-1]+=1
        res+=1
    else:
        dic[i]-=1
        dic[i-1]+=1
print(res)