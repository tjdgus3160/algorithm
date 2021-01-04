# 2693번
import sys
input=sys.stdin.readline

res=[]
for _ in range(int(input())):
    tmp=[*map(int,input().split())]
    tmp.sort(reverse=True)
    res.append(tmp[2])
for i in res:
    print(i)