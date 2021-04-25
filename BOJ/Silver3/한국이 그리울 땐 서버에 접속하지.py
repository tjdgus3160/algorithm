# 9996번
import sys
input=sys.stdin.readline

n=int(input())
s,e=input().rstrip().split('*')
e=e[::-1]
for _ in range(n):
    i=input().rstrip()
    flag=True
    for idx,v in enumerate(s):
        if v!=i[idx]:
            flag=False
            break
    if flag:
        i=i[::-1]
        for idx,v in enumerate(e):
            if v!=i[idx]:
                flag=False
                break
    if len(i)<len(s)+len(e):
        flag=False
    print('DA' if flag else 'NE')