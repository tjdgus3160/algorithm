# 2812번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
stack=[]
for i in input():
    while stack and stack[-1]<i and k>0:
        stack.pop()
        k-=1
    stack+=[i]
print(''.join(stack[:n-k]))