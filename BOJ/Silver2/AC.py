# 5430번
from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    p=input().rstrip('\n')
    n=input()
    a=input().rstrip('\n')
    dq=deque(a[1:-1].split(','))
    k=True # True 앞 False 뒤
    flag=True
    for c in p:
        if c=='R':
            k= not k
        else:
            if len(dq) == 0 or (len(dq)==1 and dq[0]==''):
                print('error')
                flag=False
                break
            if k:
                dq.popleft()
            else:
                dq.pop()
    if not k:
        dq.reverse()
    if flag:
        print('['+','.join(dq)+']')