import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
b=[i for i in a if i%2==1]
if len(b)==0:
    print(-1)
else:
    print(sum(b))
