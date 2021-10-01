# 9324번
from collections import defaultdict
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s=input().rstrip()
    idx=0
    dic=defaultdict(int)
    flag=True
    while idx<len(s):
        dic[s[idx]]+=1
        if dic[s[idx]]==3:
            idx+=1
            if idx==len(s) or s[idx]!=s[idx-1]:
                flag=False
                break
            dic[s[idx]]=0
        idx+=1
    print('OK' if flag else 'FAKE')
