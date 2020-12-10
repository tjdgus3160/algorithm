# 16282번
import sys
input=sys.stdin.readline

n=int(input())
t=1
while True:
    if n<=2**(t+1)*(t+1)-1:
        break
    t+=1
print(t)