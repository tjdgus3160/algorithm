# 17176번
from collections import defaultdict
import sys
input=sys.stdin.readline

input()
dic=defaultdict(int)
for i in [*map(int,input().split())]:
    if i==0:
        dic[' ']+=1
    elif i<=26:
        dic[chr(64+i)]+=1
    else:
        dic[chr(97-27+i)]+=1
s=input().rstrip()
flag=True
for i in s:
    if i in dic and dic[i]:
        dic[i]-=1
    else:
        flag=False
        break
print('y' if flag else 'n')
