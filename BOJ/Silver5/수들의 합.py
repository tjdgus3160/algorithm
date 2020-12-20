# 1789번
import sys
input=sys.stdin.readline

s=int(input())
res=1
while True:
    if res*(res+1)//2>s:
        break
    res+=1
print(res-1)