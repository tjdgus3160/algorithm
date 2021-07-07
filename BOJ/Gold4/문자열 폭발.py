# 9935번
import sys
input=sys.stdin.readline

s=input().rstrip()
k=input().rstrip()
stack=[]

for i in s:
    stack.append(i)
    if ''.join(stack[-len(k):])==k:
        for _ in range(len(k)):
            stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))