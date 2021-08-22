from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
if n==1:
    print(0)
    exit()
s=set()
s.add(n)
dq=deque([[n,0]])
while dq:
    n,c=dq.popleft()
    if n-1==1:
        print(c+1)
        exit()
    elif n-1 not in s:
        s.add(n-1)
        dq.append([n-1,c+1])
    if n+1==1:
        print(c+1)
        exit()
    elif n+1 not in s:
        s.add(n+1)
        dq.append([n+1,c+1])
    if n%2==0:
        if n//2==1:
            print(c+1)
            exit()
        elif n//2 not in s:
            s.add(n//2)
            dq.append([n//2,c+1])
    if n%3==0:
        if n//3==1:
            print(c+1)
            exit()
        elif n//3 not in s:
            s.add(n//3)
            dq.append([n//3,c+1])