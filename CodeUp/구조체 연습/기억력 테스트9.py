import sys
import operator
input=sys.stdin.readline

n,m=map(int,input().split())
tmp={}
test=[]
for i in range(n):
    t=input().split()
    tmp.setdefault(t[0],0)
    tmp[t[0]]+=int(t[1])
for i in range(m):
    test.append(input()[:-1])
for i in test:
    tmp.setdefault(i,0)
    print(tmp[i])
