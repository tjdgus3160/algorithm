# 20006번
import sys
input=sys.stdin.readline

p,m=map(int,input().split())
dic={}
for _ in range(p):
    i,n=input().split()
    i=int(i)
    if not dic:
        dic[n]={'max':i+10,'min':i-10,'user':[(i,n)]}
        continue
    for room in dic.values():
        if room['min']<=i<=room['max'] and len(room['user'])<m:
            room['user'].append((i,n))
            break
    else:
        dic[n]={'max': i + 10, 'min': i - 10, 'user': [(i, n)]}
for room in dic.values():
    if len(room['user'])==m:
        print('Started!')
    else:
        print('Waiting!')
    for user in sorted(room['user'],key=lambda x:x[1]):
        print(*user)