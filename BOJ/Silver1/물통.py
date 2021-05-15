# 2251번
from collections import deque
import sys
input=sys.stdin.readline

A,B,C=map(int,input().split())
tmp=deque([[0,0,C]])
dq=deque([[0,0,C]])
while dq:
    a,b,c=dq.popleft()
    if a:
        if B-b>=a and [0,a+b,c] not in tmp:
            tmp.append([0,a+b,c])
            dq.append([0,a+b,c])
        elif B-b<a and [a-(B-b),B,c] not in tmp:
            tmp.append([a-(B-b),B,c])
            dq.append([a-(B-b),B,c])
        if C-c>=a and [0,b,a+c] not in tmp:
            tmp.append([0,b,a+c])
            dq.append([0,b,a+c])
        elif C-c<a and [a-(C-c),b,C] not in tmp:
            tmp.append([a-(C-c),b,C])
            dq.append([a-(C-c),b,C])
    if b:
        if A-a>=b and [a+b,0,c] not in tmp:
            tmp.append([a+b,0,c])
            dq.append([a+b,0,c])
        elif A-a<b and [A,b-(A-a),c] not in tmp:
            tmp.append([A, b - (A - a), c])
            dq.append([A,b-(A-a),c])
        if C-c>=b and [a,0,c+b] not in tmp:
            tmp.append([a, 0, c + b])
            dq.append([a,0,c+b])
        elif C-c<b and [a,b-(C-c),C] not in tmp:
            tmp.append([a, b - (C - c), C])
            dq.append([a,b-(C-c),C])
    if c:
        if A-a>=c and [a+c,b,0] not in tmp:
            tmp.append([a + c, b, 0])
            dq.append([a+c,b,0])
        elif A-a<c and [A,b,c-(A-a)] not in tmp:
            tmp.append([A, b, c - (A - a)])
            dq.append([A,b,c-(A-a)])
        if B-b>=c and [a,b+c,0] not in tmp:
            tmp.append([a, b + c, 0])
            dq.append([a,b+c,0])
        elif B-b<c and [a,B,c-(B-b)] not in tmp:
            tmp.append([a, B, c - (B - b)])
            dq.append([a,B,c-(B-b)])
res=list(set([c for a,b,c in tmp if a==0]))
res.sort()
print(*res)