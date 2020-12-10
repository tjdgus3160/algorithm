import copy
import sys
input=sys.stdin.readline

a=[]
for i in range(int(input())):
    t=input().split()
    a.append([t[0]]+list(map(int,t[1:])))
a.sort(key=lambda x:(x[1],x[2],x[3],x[0]))
for i in a:
    print(i[0])
