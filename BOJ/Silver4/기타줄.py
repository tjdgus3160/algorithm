# 1049번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
six=1001
one=1001
for _ in range(m):
    a,b=map(int,input().split())
    six=min(six,a)
    one=min(one,b)
if one*6>six:
    print(min((n//6)*six+(n%6)*one,six*((n//6)+1)))
else:
    print(min(one*n,(n//6)*six+(n%6)*one))