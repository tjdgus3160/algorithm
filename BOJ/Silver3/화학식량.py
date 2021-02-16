# 2257번
import sys
input=sys.stdin.readline

stack=[]
s=input().rstrip('\n')
for i in s:
    if i=='H':
        stack.append(1)
    elif i=='C':
        stack.append(12)
    elif i=='O':
        stack.append(16)
    elif i=='(':
        stack.append(i)
    elif i==')':
        k=0
        while stack[-1]!='(':
            k+=stack.pop()
        stack.pop()
        stack.append(k)
    elif i.isdigit():
        stack.append(stack.pop()*int(i))

print(sum(stack))