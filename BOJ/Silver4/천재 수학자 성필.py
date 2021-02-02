# 15815번
from collections import deque
import sys
input=sys.stdin.readline

dq=deque()
s=list(input().rstrip('\n'))
for i in s:
    if i in '+-*/':
        a=dq.pop()
        b=dq.pop()
        if i =='/':
            i+='/'
        dq.append(str(eval(b+i+a)))
    else:
        dq.append(i)
print(dq[0])