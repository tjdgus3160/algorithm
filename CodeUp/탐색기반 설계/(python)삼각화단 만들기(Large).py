import itertools
import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for i in range(n//3,(n-1)//2+1):
    for j in range(1,i+1):
        if i>=j and i>=n-j-i and j<=n-j-i:
            cnt+=1
print(cnt)
