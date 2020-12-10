import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
a=[i*i for i in a]
print(sum(a)%10)
