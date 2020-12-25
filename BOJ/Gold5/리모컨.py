# 1107번
import sys
input=sys.stdin.readline

def check(n):
    for i in err:
        if i in str(n):
            return False
    return True

n=int(input())
m=int(input())
err={*map(str,input().split())}
res=abs(n-100)
for i in range(1000001):
    if check(i):
        res=min(res,len(str(i))+abs(n-i))
print(res)