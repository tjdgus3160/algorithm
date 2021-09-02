# 4358번
from collections import defaultdict
import sys
input=sys.stdin.readline

dic=defaultdict(int)
n=0
while True:
    s=input().rstrip()
    if not s:
        break
    dic[s]+=1
    n+=1
for i in sorted(dic):
    print("%s %.4f"%(i,round(dic[i]*100/n,4)))
