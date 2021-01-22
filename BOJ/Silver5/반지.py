# 5555번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
res=0
for _ in range(int(input())):
    ss=input().rstrip('\n')
    ss*=2
    if s in ss:
        res+=1
print(res)