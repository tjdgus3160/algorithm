# 1543번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
k=input().rstrip('\n')
res=0
idx=0
while True:
    if idx>(len(s)-len(k)):
        break
    if s[idx:idx+len(k)]==k:
        res+=1
        idx+=len(k)
    else:
        idx+=1
print(res)